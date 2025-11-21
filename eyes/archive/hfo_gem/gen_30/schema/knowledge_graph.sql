-- HFO Knowledge Graph Schema
-- Purpose: Structured memory system to replace append-only AGENTS.md
-- Enables: Semantic search, causal reasoning, concept evolution tracking
-- Created: 2025-11-12

-- Extension for vector similarity search
CREATE EXTENSION IF NOT EXISTS vector;

-- ==============================================================================
-- LAYER 2: Structured Knowledge Graph
-- ==============================================================================

-- Incidents: Critical events, bugs, discoveries
CREATE TABLE IF NOT EXISTS hfo_incidents (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    generation INTEGER NOT NULL,
    title TEXT NOT NULL,
    severity TEXT CHECK (severity IN ('CRITICAL', 'HIGH', 'MEDIUM', 'LOW', 'INFO')),
    status TEXT CHECK (status IN ('ACTIVE', 'RESOLVED', 'BLOCKED', 'MONITORING', 'ARCHIVED')),

    -- Structured incident fields
    symptom TEXT,           -- What we observed
    root_cause TEXT,        -- Why it happened
    solution TEXT,          -- How we fixed it
    impact TEXT,            -- What was affected

    -- Evidence and context
    evidence_paths TEXT[],  -- File citations ["hfo_swarm/orchestrator.py:123"]
    related_concepts TEXT[], -- Links to hfo_concepts.name

    -- Metadata
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_incidents_generation ON hfo_incidents(generation);
CREATE INDEX idx_incidents_severity ON hfo_incidents(severity);
CREATE INDEX idx_incidents_status ON hfo_incidents(status);
CREATE INDEX idx_incidents_timestamp ON hfo_incidents(timestamp DESC);

-- Concepts: Core ideas, patterns, algorithms, roles
CREATE TABLE IF NOT EXISTS hfo_concepts (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    category TEXT,  -- 'architecture', 'pattern', 'algorithm', 'role', 'tool', 'infrastructure'
    definition TEXT NOT NULL,

    -- Temporal tracking
    generation_introduced INTEGER,
    generation_last_modified INTEGER,

    -- Cross-references
    aliases TEXT[],           -- ["PREY", "Perceive-React-Execute-Yield"]
    related_concepts TEXT[],  -- Names of related concepts
    implementation_files TEXT[], -- Where it's coded

    -- Metadata
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_concepts_name ON hfo_concepts(name);
CREATE INDEX idx_concepts_category ON hfo_concepts(category);
CREATE INDEX idx_concepts_generation ON hfo_concepts(generation_introduced);

-- Concept Evolution: Track how definitions change across generations
CREATE TABLE IF NOT EXISTS hfo_concept_evolution (
    id SERIAL PRIMARY KEY,
    concept_id INTEGER REFERENCES hfo_concepts(id) ON DELETE CASCADE,
    generation INTEGER NOT NULL,
    change_type TEXT CHECK (change_type IN ('CREATED', 'REFINED', 'RENAMED', 'DEPRECATED', 'MERGED', 'SPLIT')),

    old_definition TEXT,
    new_definition TEXT,
    reason TEXT,

    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_evolution_concept ON hfo_concept_evolution(concept_id);
CREATE INDEX idx_evolution_generation ON hfo_concept_evolution(generation);

-- Relationships: Causal links, dependencies, associations
CREATE TABLE IF NOT EXISTS hfo_relationships (
    id SERIAL PRIMARY KEY,

    -- Source and target (polymorphic)
    source_type TEXT CHECK (source_type IN ('incident', 'concept', 'mission')),
    source_id INTEGER NOT NULL,

    relationship_type TEXT,  -- 'CAUSED_BY', 'REQUIRES', 'BLOCKS', 'RELATED_TO', 'EVOLVED_TO', 'IMPLEMENTS'

    target_type TEXT CHECK (target_type IN ('incident', 'concept', 'mission')),
    target_id INTEGER NOT NULL,

    -- Metadata
    strength FLOAT DEFAULT 1.0,  -- 0.0-1.0 confidence
    evidence TEXT,               -- Why we think this relationship exists

    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_relationships_source ON hfo_relationships(source_type, source_id);
CREATE INDEX idx_relationships_target ON hfo_relationships(target_type, target_id);
CREATE INDEX idx_relationships_type ON hfo_relationships(relationship_type);

-- ==============================================================================
-- LAYER 1: Semantic Memory (pgvector)
-- ==============================================================================

-- Semantic Memory: Vector embeddings for similarity search
CREATE TABLE IF NOT EXISTS hfo_semantic_memory (
    id SERIAL PRIMARY KEY,

    -- Content
    content TEXT NOT NULL,
    content_type TEXT,  -- 'incident', 'concept', 'code', 'doc', 'comment', 'mission_digest'

    -- Source tracking
    source_table TEXT,  -- 'hfo_incidents', 'hfo_concepts', etc.
    source_id INTEGER,

    -- Flexible metadata
    metadata JSONB,

    -- Vector embedding (OpenAI text-embedding-3-small = 1536 dimensions)
    embedding vector(1536),

    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Vector similarity index (IVFFlat for approximate nearest neighbor)
CREATE INDEX IF NOT EXISTS idx_semantic_embedding
    ON hfo_semantic_memory
    USING ivfflat (embedding vector_cosine_ops)
    WITH (lists = 100);

CREATE INDEX idx_semantic_type ON hfo_semantic_memory(content_type);
CREATE INDEX idx_semantic_source ON hfo_semantic_memory(source_table, source_id);

-- ==============================================================================
-- LAYER 3: Mission Tracking
-- ==============================================================================

-- Missions: Swarm execution history
CREATE TABLE IF NOT EXISTS hfo_missions (
    id SERIAL PRIMARY KEY,
    mission_id INTEGER UNIQUE,  -- From simple_missions table
    intent TEXT NOT NULL,
    constraints TEXT,

    -- Execution details
    num_researchers INTEGER,
    consensus_level TEXT,

    -- Results
    executive_summary TEXT,
    artifacts_dir TEXT,

    -- Findings
    concepts_discovered TEXT[],
    incidents_detected INTEGER[],  -- Links to hfo_incidents.id
    hallucinations_found BOOLEAN DEFAULT FALSE,

    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX idx_missions_timestamp ON hfo_missions(timestamp DESC);
CREATE INDEX idx_missions_consensus ON hfo_missions(consensus_level);

-- ==============================================================================
-- HELPER VIEWS
-- ==============================================================================

-- Recent critical incidents
CREATE OR REPLACE VIEW recent_critical_incidents AS
SELECT
    id,
    timestamp,
    generation,
    title,
    severity,
    status,
    symptom,
    root_cause
FROM hfo_incidents
WHERE severity IN ('CRITICAL', 'HIGH')
  AND status != 'ARCHIVED'
ORDER BY timestamp DESC
LIMIT 10;

-- Concept evolution timeline
CREATE OR REPLACE VIEW concept_timeline AS
SELECT
    c.name,
    c.category,
    ce.generation,
    ce.change_type,
    ce.reason,
    ce.timestamp
FROM hfo_concepts c
JOIN hfo_concept_evolution ce ON ce.concept_id = c.id
ORDER BY c.name, ce.generation ASC;

-- Incident causality graph
CREATE OR REPLACE VIEW incident_causality AS
SELECT
    i1.id as source_id,
    i1.title as source_title,
    r.relationship_type,
    i2.id as target_id,
    i2.title as target_title,
    r.strength
FROM hfo_relationships r
JOIN hfo_incidents i1 ON r.source_type = 'incident' AND r.source_id = i1.id
JOIN hfo_incidents i2 ON r.target_type = 'incident' AND r.target_id = i2.id
WHERE r.relationship_type IN ('CAUSED_BY', 'REQUIRES', 'BLOCKS');

-- ==============================================================================
-- FUNCTIONS
-- ==============================================================================

-- Update timestamp on row modification
CREATE OR REPLACE FUNCTION update_modified_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers for auto-updating timestamps
CREATE TRIGGER update_incidents_timestamp
    BEFORE UPDATE ON hfo_incidents
    FOR EACH ROW EXECUTE FUNCTION update_modified_timestamp();

CREATE TRIGGER update_concepts_timestamp
    BEFORE UPDATE ON hfo_concepts
    FOR EACH ROW EXECUTE FUNCTION update_modified_timestamp();

-- ==============================================================================
-- SAMPLE DATA (For Testing)
-- ==============================================================================

-- Insert sample incident
INSERT INTO hfo_incidents (
    timestamp,
    generation,
    title,
    severity,
    status,
    symptom,
    root_cause,
    solution,
    evidence_paths
) VALUES (
    '2025-11-12 20:15:00-07'::timestamptz,
    30,
    'Artifact Structure Brittleness at L2',
    'HIGH',
    'RESOLVED',
    'L2 test completed but only 4 files visible instead of 111 (100 L0 + 10 L1 + 1 L2)',
    'SwarmRunArtifacts.__init__() hardcodes timestamped directory from intent, all L1 holons created same directory name',
    'Abstract Factory Pattern with HolonAddress for unique paths',
    ARRAY['hfo_swarm/artifact_manager.py', 'AGENTS.md:1-100']
) ON CONFLICT DO NOTHING;

-- Insert sample concept
INSERT INTO hfo_concepts (
    name,
    category,
    definition,
    generation_introduced,
    aliases,
    implementation_files
) VALUES (
    'PREY loop',
    'pattern',
    'Perceive → React → Execute → Yield feedback loop used at worker and orchestrator levels',
    1,
    ARRAY['PREY', 'Perceive-React-Execute-Yield'],
    ARRAY['hfo_swarm/simple_orchestrator.py', 'hfo_swarm/prey_orchestrator.py']
) ON CONFLICT (name) DO NOTHING;

-- Insert concept evolution
INSERT INTO hfo_concept_evolution (
    concept_id,
    generation,
    change_type,
    old_definition,
    new_definition,
    reason
) VALUES (
    (SELECT id FROM hfo_concepts WHERE name = 'PREY loop'),
    30,
    'REFINED',
    'Basic sense-act-feedback loop',
    'Perceive → React → Execute → Yield feedback loop used at worker and orchestrator levels',
    'Formalized as nested holonic pattern in V²C-SPIRAL-QUORUM'
) ON CONFLICT DO NOTHING;

-- Insert sample relationship
INSERT INTO hfo_relationships (
    source_type,
    source_id,
    relationship_type,
    target_type,
    target_id,
    strength,
    evidence
) VALUES (
    'incident',
    (SELECT id FROM hfo_incidents WHERE title LIKE '%Artifact Structure%'),
    'REQUIRES',
    'concept',
    (SELECT id FROM hfo_concepts WHERE name = 'PREY loop'),
    0.8,
    'Artifact factory pattern needs to compose with PREY loop semantics'
) ON CONFLICT DO NOTHING;

-- ==============================================================================
-- GRANT PERMISSIONS (if needed)
-- ==============================================================================

-- Grant access to application user (adjust as needed)
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO hfo_app;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO hfo_app;

-- ==============================================================================
-- NOTES
-- ==============================================================================

-- To load this schema:
-- psql $DATABASE_URL -f hfo_gem/gen_30/schema/knowledge_graph.sql

-- To query semantic memory (example):
-- SELECT content, 1 - (embedding <=> '[...]'::vector) as similarity
-- FROM hfo_semantic_memory
-- ORDER BY embedding <=> '[...]'::vector
-- LIMIT 5;

-- To find causal chain:
-- WITH RECURSIVE chain AS (
--     SELECT id, title, 1 as depth
--     FROM hfo_incidents WHERE id = 1
--     UNION
--     SELECT i.id, i.title, c.depth + 1
--     FROM hfo_relationships r
--     JOIN hfo_incidents i ON r.target_id = i.id AND r.target_type = 'incident'
--     JOIN chain c ON r.source_id = c.id AND r.source_type = 'incident'
--     WHERE c.depth < 5
-- )
-- SELECT * FROM chain ORDER BY depth;
