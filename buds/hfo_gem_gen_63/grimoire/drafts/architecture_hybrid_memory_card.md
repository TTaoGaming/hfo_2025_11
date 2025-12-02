---
card:
  id: hybrid-stigmergic-graphrag-memory
  source: architecture_hybrid_memory.md
  type: Concept
---

# 🃏 Hybrid Stigmergic GraphRAG Memory

> **Intuition**: Emulating biological memory consolidation, this hybrid system transforms ephemeral "hot" real-time signals into enduring "cold" semantic wisdom via stigmergic crystallization.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hybrid Stigmergic GraphRAG Memory Management

  Scenario: Crystallizing Hot Episodic Signals into Cold Semantic Knowledge
    Given a stream of real-time events in NATS JetStream "Hot" memory
    When the Crystal Spinner agent ingests and processes the stream
    Then facts and relationships are extracted and stored in Postgres Graph + pgvector "Cold" memory
    And agents can query the Knowledge Graph for precedents and semantic search via vectors
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Crystal Spinner - Bridge from Hot to Cold Memory
import nats
from sqlalchemy import create_engine
from neo4j import GraphDatabase  # Or pg_graphql for Postgres graph

async def crystal_spinner():
    # Connect to Hot Memory (NATS JetStream)
    nc = await nats.connect("nats://localhost:4222")
    jsm = nc.jetstream()
    
    # Connect to Cold Memory (Postgres Graph + Vector)
    engine = create_engine("postgresql://user:pass@localhost/brain")
    graph_driver = GraphDatabase.driver("bolt://localhost:7687")  # Hybrid Postgres/Neo4j option
    
    async for msg in jsm.consume("agent-signals", durable_name="spinner"):
        event = msg.data.decode()
        facts, relations, vectors = extract_knowledge(event)  # LLM-powered extraction
        
        # Crystallize into Cold Memory
        with engine.connect() as conn:
            for fact in facts:
                conn.execute("INSERT INTO node (id, label, properties, embedding) VALUES (%s, %s, %s, %s)", fact)
            for rel in relations:
                conn.execute("INSERT INTO edge (source, target, relation, weight) VALUES (%s, %s, %s, %s)", rel)
        
        await msg.ack()
```

## ⚔️ Synergies
*   **Agents & Signaling**: Agents emit real-time "hot" events to NATS for coordination, ingested by Crystal Spinner.
*   **Warm Tier**: Redis/Plasma extends session context, buffering between hot and cold loops.
*   **Cold Tier**: Postgres GraphRAG enables semantic querying/precedents for agent decision-making.
*   **Frozen Tier**: Markdown docs provide immutable architecture/intent, linking back to ontos/chronos metadata.
*   **Crystal Spinner Agent**: Central orchestrator, leveraging LLM for knowledge extraction from streams.