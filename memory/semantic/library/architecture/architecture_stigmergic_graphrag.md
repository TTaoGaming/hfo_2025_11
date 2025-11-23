---
title: Stigmergic GraphRAG Architecture
summary: Hybrid memory architecture for Hive Fleet Obsidian combining fast stigmergic
  coordination via NATS with deep semantic reasoning via GraphRAG in Postgres.
domain: Architecture
concepts:
- Stigmergy
- GraphRAG
- NATS JetStream
- Postgres
- Hybrid Memory
owner: Architect
actionable: false
related_files: []
type: crystallized_memory
status: active
last_verified: '2025-11-21'
hexagon:
  ontos:
    id: f18ce356-f00e-48eb-9f7e-2d8f91ba15a8
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:10.172162+00:00'
    generation: 51
  topos:
    address: memory/semantic/library/architecture/architecture_stigmergic_graphrag.md
    links: []
  telos:
    viral_factor: 0.0
    meme: architecture_stigmergic_graphrag.md
---


# Stigmergic GraphRAG Architecture

This diagram formalizes the **Hybrid Memory Architecture** for Hive Fleet Obsidian (Gen 50).
It combines the speed of **Stigmergy (NATS)** for coordination with the depth of **GraphRAG (Postgres)** for reasoning.

```mermaid
graph TD
    subgraph "Fast Loop (Episodic / Stigmergy)"
        A[Agent Swarm] -- "1. Emits Signal (Pheromone)" --> NATS[NATS JetStream]
        NATS -- "2. Triggers Reaction" --> A
        NATS -- "3. Publishes Event" --> Stream[Event Stream]
    end

    subgraph "Slow Loop (Semantic / GraphRAG)"
        Stream -- "4. Consumed By" --> Assim[Assimilator Agent]
        Assim -- "5. Extracts Entities" --> LLM[Instructor / LLM]
        LLM -- "6. Structured Data" --> Assim
        Assim -- "7. Writes Node/Edge" --> PG_Graph[Postgres (NetworkX/Graph)]
        Assim -- "8. Writes Embedding" --> PG_Vector[Postgres (pgvector)]
    end

    subgraph "Retrieval (The Wisdom)"
        NewTask[New Mission] --> Nav[Navigator Agent]
        Nav -- "9. Hybrid Search" --> PG_Vector
        Nav -- "10. Graph Traversal" --> PG_Graph
        PG_Vector & PG_Graph -- "11. Context Context" --> Nav
    end

    style NATS fill:#f9f,stroke:#333,stroke-width:2px
    style PG_Graph fill:#9cf,stroke:#333,stroke-width:2px
    style PG_Vector fill:#9cf,stroke:#333,stroke-width:2px
    style Assim fill:#ff9,stroke:#333,stroke-width:2px
```

## Core Principles

1.  **Decoupling**: Agents never write directly to the Database. They only write to NATS.
2.  **Asynchrony**: The "Assimilator" runs at its own pace. If the swarm generates 1000 events/sec, the Assimilator can batch process them without slowing down the swarm.
3.  **Dual-State**:
    *   **Hot State**: In NATS (Last 5 minutes, ephemeral, fast).
    *   **Cold State**: In Postgres (Permanent, structured, queryable).


---
**Grafted by Gardener**: [[gen_50_README|Gen 50 Hub]]
