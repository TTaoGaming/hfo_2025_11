---
title: Memory GraphRAG Architecture (The Karmic Web)
summary: A self-reproducing 'Quine Loop' memory system using GraphRAG with PostgreSQL/pgvector
  and NetworkX for capture, structure, reuse, and improvement flows.
domain: Memory
concepts:
- GraphRAG
- Quine Loop
- Stigmergy
- Knowledge Graph
- RAG Retrieval
owner: Architect
actionable: false
related_files: []
type: crystallized_memory
status: active
last_verified: '2025-11-21'

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 6ff08772-2b50-418f-8df1-ee37ceac942c
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:10.318555+00:00'
  topos:
    address: memory/semantic/library/memory/memory_architecture.md
    links: []
  telos:
    viral_factor: 0.0
    meme: memory_architecture.md

---

# 🧠 Memory GraphRAG Architecture (The Karmic Web)

> **Status**: Active (Gen 50)
> **Storage**: PostgreSQL (pgvector) + NetworkX (Graph)
> **Flow**: Capture → Structure → Reuse → Improve

## 🧬 Concept: The Quine Loop
The system is a "Quine" (Self-Reproducing Automaton).
1.  **Stigmergy (Short-Term)**: The "Stream of Consciousness" (NATS).
2.  **Memory (Long-Term)**: The "Crystallized Wisdom" (GraphRAG).
3.  **Evolution**: The Graph updates the Agents, who then update the Graph.

## 📊 Data Flow Diagram (Mermaid)

```mermaid
graph TD
    subgraph Stigmergy [Bus Layer - Short Term]
        Signal[Result Signal]
        Vote[Consensus Vote]
    end

    subgraph Assimilation [The Scribe]
        Assimilator[Assimilator Agent]
        Embedder[Vector Embedder]
        Indexer[Graph Indexer]
    end

    subgraph Storage [The Brain - Long Term]
        PG[(Postgres / pgvector)]
        KG((Knowledge Graph))
        Archive[Cold Storage]
    end

    subgraph Retrieval [The Recall]
        Navigator[Navigator Agent]
        Query[Semantic Query]
        Context[RAG Context]
    end

    %% Capture Flow
    Signal -->|Consumes| Assimilator
    Vote -->|Validates| Assimilator
    Assimilator -->|Extracts| Embedder

    %% Structure Flow
    Embedder -->|Writes Vector| PG
    Assimilator -->|Creates Node| KG
    Indexer -->|Links Concepts| KG

    %% Reuse Flow
    Navigator -->|Asks| Query
    Query -->|Hybrid Search| PG
    Query -->|Traverse| KG
    PG -->|Raw Data| Context
    KG -->|Relationships| Context
    Context -->|Informs| Navigator

    %% Improve Flow
    Assimilator -->|Updates| KG
    KG -->|Prunes| Archive
```


---
**Grafted by Gardener**: [[gen_50_README|Gen 50 Hub]]
