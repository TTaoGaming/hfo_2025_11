---
hexagon:
  ontos:
    id: 3b317733-9620-46c5-89ef-d325f16be4e7
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:06.996111+00:00'
    generation: 51
  topos:
    address: memory/episodic/gen_50_archive/memory_architecture.md
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
