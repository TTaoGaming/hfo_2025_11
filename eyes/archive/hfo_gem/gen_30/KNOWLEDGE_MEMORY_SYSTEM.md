---
hexagon:
  ontos:
    id: 2aec74a4-1e47-4db5-a1ae-a39adb70280b
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.689775Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/KNOWLEDGE_MEMORY_SYSTEM.md
    links: []
  telos:
    viral_factor: 0.0
    meme: KNOWLEDGE_MEMORY_SYSTEM.md
---
# Knowledge Memory System - Gen 30

**Created**: 2025-11-12
**Problem**: AGENTS.md is 3000 lines, context limits hit, lossy summarization, no semantic search
**Solution**: Structured knowledge graph + pgvector semantic memory

---

## Current Problem Analysis

### AGENTS.md Issues
- **Size**: 2931 lines, 124KB (too large for context)
- **Structure**: Append-only log (incidents stacked chronologically)
- **Retrieval**: No search except grep (no semantic queries)
- **Relationships**: Manual cross-references (no graph structure)
- **Context Loss**: Summaries lose interconnections
- **Scalability**: Will hit 10K+ lines by Gen 35

### What We're Losing
- **Causal chains**: "Artifact brittleness CAUSED BY hardcoded directories, REQUIRES factory pattern"
- **Temporal patterns**: "Timeout issues recurring across 3 incidents"
- **Concept evolution**: "PREY loop definition changed 5 times across generations"
- **Cross-generation learnings**: "Gen 29 solved X, Gen 30 forgot and re-encountered same issue"

---

## Proposed Solution: Hybrid Knowledge System

### 3-Layer Architecture

```
┌─────────────────────────────────────────────────────────────┐
│ Layer 3: AGENTS.md (Human-Readable Narrative)              │
│ - Weekly summaries only                                    │
│ - Current mission status                                   │
│ - Critical incidents (300 lines max)                       │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 2: PostgreSQL Knowledge Graph                        │
│ - Incidents (id, timestamp, severity, status)             │
│ - Concepts (name, definition, generation_introduced)      │
│ - Relationships (incident → caused_by → incident)         │
│ - Evolutions (concept → evolved_to → concept)             │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Layer 1: pgvector Semantic Memory                         │
│ - Embeddings of all incidents, docs, code comments        │
│ - Similarity search: "Find similar bugs to timeout X"     │
│ - Concept retrieval: "What is PREY loop across all gens?" │
│ - Citation grounding: "Which file defined artifact factory?"│
└─────────────────────────────────────────────────────────────┘
```

### Database Schema

```sql
-- Layer 2: Structured Knowledge Graph

CREATE TABLE hfo_incidents (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    generation INTEGER NOT NULL,
    title TEXT NOT NULL,
    severity TEXT CHECK (severity IN ('CRITICAL', 'HIGH', 'MEDIUM', 'LOW')),
    status TEXT CHECK (status IN ('ACTIVE', 'RESOLVED', 'BLOCKED', 'MONITORING')),
    symptom TEXT,
    root_cause TEXT,
    solution TEXT,
    impact TEXT,
    evidence_paths TEXT[],  -- File citations
    related_concepts TEXT[], -- Link to hfo_concepts
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE hfo_concepts (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    category TEXT,  -- 'architecture', 'pattern', 'algorithm', 'role', etc.
    definition TEXT NOT NULL,
    generation_introduced INTEGER,
    generation_last_modified INTEGER,
    aliases TEXT[],
    related_concepts TEXT[],
    implementation_files TEXT[],
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE hfo_concept_evolution (
    id SERIAL PRIMARY KEY,
    concept_id INTEGER REFERENCES hfo_concepts(id),
    generation INTEGER NOT NULL,
    change_type TEXT CHECK (change_type IN ('CREATED', 'REFINED', 'RENAMED', 'DEPRECATED', 'MERGED')),
    old_definition TEXT,
    new_definition TEXT,
    reason TEXT,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE hfo_relationships (
    id SERIAL PRIMARY KEY,
    source_type TEXT CHECK (source_type IN ('incident', 'concept')),
    source_id INTEGER NOT NULL,
    relationship_type TEXT,  -- 'CAUSED_BY', 'REQUIRES', 'BLOCKS', 'RELATED_TO', 'EVOLVED_TO'
    target_type TEXT CHECK (target_type IN ('incident', 'concept')),
    target_id INTEGER NOT NULL,
    strength FLOAT,  -- 0.0-1.0 confidence
    evidence TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Layer 1: Semantic Memory (pgvector)

CREATE TABLE hfo_semantic_memory (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    content_type TEXT,  -- 'incident', 'concept', 'code', 'doc', 'comment'
    source_table TEXT,  -- 'hfo_incidents', 'hfo_concepts', etc.
    source_id INTEGER,
    metadata JSONB,  -- Flexible metadata
    embedding vector(1536),  -- OpenAI embeddings
    created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX ON hfo_semantic_memory USING ivfflat (embedding vector_cosine_ops);
```

---

## Migration Strategy

### Phase 1: Extract Current AGENTS.md (1-2 hours)

**Goal**: Parse AGENTS.md into structured data

**Script**: `scripts/knowledge/migrate_agents_to_db.py`

```python
import re
from datetime import datetime
import psycopg2
from openai import OpenAI

# 1. Parse AGENTS.md sections
incidents = []
current_incident = None

with open('AGENTS.md') as f:
    for line in f:
        # Detect incident headers: "## 🚨 CRITICAL INCIDENT – 2025-11-12"
        if match := re.match(r'## 🚨 (.*) INCIDENT – ([\d-]+)', line):
            if current_incident:
                incidents.append(current_incident)
            current_incident = {
                'severity': match.group(1),
                'timestamp': datetime.fromisoformat(match.group(2)),
                'lines': []
            }
        elif current_incident:
            current_incident['lines'].append(line)

# 2. Insert into PostgreSQL
conn = psycopg2.connect(os.getenv('DATABASE_URL'))
cursor = conn.cursor()

for inc in incidents:
    content = ''.join(inc['lines'])

    # Extract structured fields
    symptom = extract_section(content, 'Symptom')
    root_cause = extract_section(content, 'Root Cause')
    solution = extract_section(content, 'Solution')

    cursor.execute("""
        INSERT INTO hfo_incidents
        (timestamp, severity, symptom, root_cause, solution, generation)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
    """, (inc['timestamp'], inc['severity'], symptom, root_cause, solution, 30))

    incident_id = cursor.fetchone()[0]

    # 3. Generate embedding for semantic search
    client = OpenAI()
    embedding = client.embeddings.create(
        input=content,
        model="text-embedding-3-small"
    ).data[0].embedding

    cursor.execute("""
        INSERT INTO hfo_semantic_memory
        (content, content_type, source_table, source_id, embedding)
        VALUES (%s, 'incident', 'hfo_incidents', %s, %s)
    """, (content, incident_id, embedding))

conn.commit()
```

**Actions**:
1. ⏳ Create schema: `psql $DATABASE_URL -f hfo_gem/gen_30/schema/knowledge_graph.sql`
2. ⏳ Run migration: `python scripts/knowledge/migrate_agents_to_db.py`
3. ⏳ Validate: `psql $DATABASE_URL -c "SELECT COUNT(*) FROM hfo_incidents"`

---

### Phase 2: Semantic Query Interface (2-3 hours)

**Goal**: Natural language queries against knowledge graph

**Script**: `scripts/knowledge/query_memory.py`

```python
from openai import OpenAI
import psycopg2
import numpy as np

class HFOMemory:
    def __init__(self, db_url):
        self.conn = psycopg2.connect(db_url)
        self.client = OpenAI()

    def semantic_search(self, query: str, top_k: int = 5):
        """Find similar incidents/concepts via semantic search."""
        # Generate query embedding
        embedding = self.client.embeddings.create(
            input=query,
            model="text-embedding-3-small"
        ).data[0].embedding

        # Cosine similarity search
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT
                content,
                content_type,
                source_table,
                source_id,
                1 - (embedding <=> %s::vector) as similarity
            FROM hfo_semantic_memory
            ORDER BY embedding <=> %s::vector
            LIMIT %s
        """, (embedding, embedding, top_k))

        return cursor.fetchall()

    def find_related_incidents(self, incident_id: int):
        """Find incidents causally related to this one."""
        cursor = self.conn.cursor()
        cursor.execute("""
            WITH RECURSIVE related AS (
                SELECT target_id, relationship_type, 1 as depth
                FROM hfo_relationships
                WHERE source_type = 'incident'
                  AND source_id = %s
                UNION
                SELECT r.target_id, r.relationship_type, rel.depth + 1
                FROM hfo_relationships r
                JOIN related rel ON r.source_id = rel.target_id
                WHERE rel.depth < 3  -- Max 3 levels deep
            )
            SELECT DISTINCT i.*, r.relationship_type, r.depth
            FROM related r
            JOIN hfo_incidents i ON i.id = r.target_id
            ORDER BY r.depth, i.timestamp DESC
        """, (incident_id,))

        return cursor.fetchall()

    def concept_evolution(self, concept_name: str):
        """Track how concept definition evolved across generations."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT
                ce.generation,
                ce.change_type,
                ce.old_definition,
                ce.new_definition,
                ce.reason,
                ce.timestamp
            FROM hfo_concepts c
            JOIN hfo_concept_evolution ce ON ce.concept_id = c.id
            WHERE c.name = %s
            ORDER BY ce.generation ASC
        """, (concept_name,))

        return cursor.fetchall()

# Usage
memory = HFOMemory(os.getenv('DATABASE_URL'))

# Query 1: Find similar bugs
results = memory.semantic_search("artifact collision at L2 scale")
for content, ctype, table, id, sim in results:
    print(f"{ctype} (similarity: {sim:.2f}): {content[:200]}...")

# Query 2: Trace incident causality
related = memory.find_related_incidents(incident_id=5)
for incident, rel_type, depth in related:
    print(f"  {'  ' * depth}→ {rel_type}: {incident['title']}")

# Query 3: Track concept evolution
evolution = memory.concept_evolution("PREY loop")
for gen, change, old, new, reason, ts in evolution:
    print(f"Gen {gen} ({change}): {reason}")
    print(f"  Old: {old}")
    print(f"  New: {new}")
```

---

### Phase 3: Auto-Update from Swarm Runs (2-3 hours)

**Goal**: Swarm missions automatically populate knowledge graph

**Integration**: Modify `SimpleOrchestrator` to log learnings

```python
class SimpleOrchestrator:
    def execute_mission(self, intent, constraints, ...):
        # ... existing code ...

        # After mission completes
        result = {
            'executive_summary': summary,
            'consensus_level': consensus,
            'artifacts_dir': artifacts_dir,
            'mission_id': mission_id
        }

        # NEW: Auto-extract concepts and incidents
        self._update_knowledge_graph(result, intent, constraints)

        return result

    def _update_knowledge_graph(self, result, intent, constraints):
        """Extract learnings and update knowledge graph."""
        memory = HFOMemory(self.db_url)

        # 1. Analyze mission for new concepts
        new_concepts = self._extract_concepts(result['executive_summary'])
        for concept in new_concepts:
            memory.add_concept(
                name=concept['name'],
                definition=concept['definition'],
                generation=30,
                evidence_path=result['artifacts_dir']
            )

        # 2. Detect incidents from hallucination/quorum analysis
        if result.get('hallucinations_detected'):
            memory.add_incident(
                severity='MEDIUM',
                title=f"Hallucination detected in mission {result['mission_id']}",
                symptom=result['hallucination_details'],
                generation=30,
                evidence_paths=[result['artifacts_dir'] + '/03_validation/hallucinations.md']
            )

        # 3. Create embeddings for semantic search
        memory.embed_document(
            content=result['executive_summary'],
            content_type='mission_digest',
            metadata={'mission_id': result['mission_id']}
        )
```

---

## Usage Patterns

### For Researchers (Tool Access)

**Before** (read entire AGENTS.md, 3000 lines):
```python
researcher_prompt = f"""
Read AGENTS.md to understand HFO history.
{open('AGENTS.md').read()}  # 124KB in context
"""
```

**After** (semantic query, 5 results):
```python
memory = HFOMemory(db_url)
relevant = memory.semantic_search(intent, top_k=5)
researcher_prompt = f"""
Relevant HFO context for '{intent}':
{format_context(relevant)}  # 5KB in context
"""
```

### For Validation (Hallucination Detection)

**Query**: "Has this claim appeared before?"
```python
claim = "L2 artifact collision caused by hardcoded directory names"
matches = memory.semantic_search(claim, top_k=3)
if matches[0]['similarity'] > 0.95:
    print(f"✅ Known incident: {matches[0]['source_id']}")
else:
    print(f"⚠️ New claim, needs validation")
```

### For Strategic Planning

**Query**: "What were the critical incidents in Gen 29-30?"
```sql
SELECT title, severity, status, root_cause
FROM hfo_incidents
WHERE generation BETWEEN 29 AND 30
  AND severity IN ('CRITICAL', 'HIGH')
ORDER BY timestamp DESC;
```

**Query**: "What concepts evolved between Gen 29-30?"
```sql
SELECT c.name, ce.change_type, ce.reason
FROM hfo_concepts c
JOIN hfo_concept_evolution ce ON ce.concept_id = c.id
WHERE ce.generation BETWEEN 29 AND 30
ORDER BY ce.timestamp;
```

---

## Benefits

### 1. Context Efficiency
- **Before**: 3000 lines (124KB) → context limit hit
- **After**: 5 relevant results (5KB) → 96% reduction

### 2. Semantic Queries
- **Before**: grep "artifact brittleness" (exact match only)
- **After**: "Find similar bugs to L2 scaling issues" (semantic)

### 3. Causal Reasoning
- **Before**: Manual reading of incidents
- **After**: Graph traversal shows "Incident A CAUSED_BY Incident B REQUIRES Solution C"

### 4. Cross-Generation Learning
- **Before**: "What changed between Gen 29-30?" → read all docs
- **After**: SQL query returns concept evolution table

### 5. Auto-Documentation
- **Before**: Human writes incident reports
- **After**: Swarm missions auto-populate knowledge graph

### 6. Tool Access Grounding
- **Before**: Researchers fabricate citations (no file access)
- **After**: Researchers query knowledge graph for real precedents

---

## Implementation Timeline

**Week 1: Foundation**
- Day 1-2: Create schema, migrate AGENTS.md → PostgreSQL
- Day 3-4: Build semantic query interface
- Day 5: Test semantic search accuracy

**Week 2: Integration**
- Day 1-2: Integrate with SimpleOrchestrator
- Day 3-4: Auto-extraction from swarm runs
- Day 5: Validate with live missions

**Week 3: Refinement**
- Day 1-2: Tune embedding model (try text-embedding-3-large)
- Day 3-4: Build visualization (NetworkX graph of relationships)
- Day 5: Document usage patterns

---

## Cost Analysis

**Storage**:
- PostgreSQL: ~10MB per 1000 incidents (negligible)
- pgvector: 1536 floats × 1000 embeddings = ~6MB (negligible)

**Embeddings**:
- OpenAI text-embedding-3-small: $0.02/1M tokens
- 1000 incidents × 500 tokens avg = 500K tokens = $0.01
- Total migration cost: < $0.05

**Ongoing**:
- 1 mission = 1 digest embedding = ~500 tokens = $0.00001
- 100 missions/week = $0.001/week (negligible)

---

## Migration from AGENTS.md

**Step 1**: Extract incidents (automated)
```bash
python scripts/knowledge/migrate_agents_to_db.py
```

**Step 2**: Slim down AGENTS.md to 300 lines
- Keep: Current mission status, last 3 critical incidents, weekly summary
- Move to DB: All historical incidents, concept definitions, long analyses

**Step 3**: Add header to AGENTS.md
```markdown
# Agents & Active Mission Status

**See**: `HFOMemory` in PostgreSQL for full incident history and semantic search.

This file contains:
- Current active mission (updated real-time)
- Last 3 critical incidents (rolling window)
- Weekly summary (updated Sundays)

For historical queries, use:
- `python scripts/knowledge/query_memory.py "search query"`
- `psql $DATABASE_URL -c "SELECT * FROM hfo_incidents WHERE ..."`
```

---

## Example Queries

### Find Root Cause of Current Bug
```python
memory = HFOMemory(db_url)
results = memory.semantic_search(
    "tool-enabled researchers return 0 characters",
    top_k=5
)
# Returns: Similar timeout incidents, context explosion cases
```

### Trace Concept Evolution
```python
evolution = memory.concept_evolution("PREY loop")
# Returns: Gen 1 (created), Gen 5 (refined), Gen 12 (renamed), Gen 30 (formalized)
```

### Find Blocking Dependencies
```python
blockers = memory.find_related_incidents(incident_id=42)
# Returns: Graph showing "Tool access BLOCKS L1 production REQUIRES Hypothesis testing"
```

### Cross-Generation Pattern Detection
```sql
SELECT
    i1.title as incident_1,
    i2.title as incident_2,
    i1.generation - i2.generation as gen_gap
FROM hfo_incidents i1
JOIN hfo_incidents i2 ON
    i1.symptom ILIKE '%timeout%' AND
    i2.symptom ILIKE '%timeout%' AND
    i1.id != i2.id
WHERE i1.generation != i2.generation
ORDER BY gen_gap DESC;
-- Find: "We've hit timeout issues 5 times across 10 generations"
```

---

## Next Steps

**Immediate** (Today):
1. ⏳ Create schema: `hfo_gem/gen_30/schema/knowledge_graph.sql`
2. ⏳ Write migration script: `scripts/knowledge/migrate_agents_to_db.py`
3. ⏳ Test semantic search with 10 sample incidents

**This Week**:
1. ⏳ Migrate full AGENTS.md → PostgreSQL
2. ⏳ Build query interface: `scripts/knowledge/query_memory.py`
3. ⏳ Integrate with SimpleOrchestrator for auto-updates

**Next Week**:
1. ⏳ Slim AGENTS.md to 300 lines (current mission + recent incidents)
2. ⏳ Add tool access to researchers: `read_memory(query)` function
3. ⏳ Test with phased architecture consensus mission

---

**Status**: Design complete, ready for implementation
**Priority**: HIGH - Blocks effective tool access for researchers
**Estimated Effort**: 3 weeks (foundation + integration + refinement)
**User Vision**: "These pieces are all interconnected" → Knowledge graph captures those connections
