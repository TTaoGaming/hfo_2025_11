---
title: Karmic Web Workflow
status: Active
type: Workflow
tags:
- stigmergy
- graphrag
- memory
hexagon:
  ontos:
    id: 8a17b157-325d-4295-b14f-377e71aa375a
    type: doc
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T06:32:09.814743Z'
    generation: 51
  topos:
    address: brain/workflow_karmic_web.md
    links: []
  telos:
    viral_factor: 0.0
    meme: Karmic Web Workflow
---



# 🕸️ Karmic Web Workflow

## ⚡ BLUF (Bottom Line Up Front)
The **Karmic Web** is the "Deep Memory" system of Hive Fleet Obsidian. Unlike the "Hot State" (NATS), which is ephemeral, the Karmic Web persists knowledge into a **Stigmergic Graph** (Postgres + NetworkX + pgvector). This workflow defines how the **Assimilator** agent consumes ephemeral signals, crystallizes them into nodes/edges, and allows other agents to query this "Ancestral Wisdom" for long-horizon planning. It is the bridge between *doing* (Action) and *knowing* (Wisdom).

---

## 1. Context & Architecture

The Karmic Web sits at the center of the **Tri-Brain Architecture**, mediating between the fast-twitch "Reflex" brain and the slow-twitch "Reasoning" brain.

```mermaid
graph TD
    subgraph "Hot State (NATS)"
        A[Agent Action] -->|Signal| B(NATS Stream)
    end

    subgraph "The Karmic Web (Postgres)"
        B -->|Consume| C{Assimilator}
        C -->|Extract| D[Entities]
        C -->|Extract| E[Relations]
        D --> F[(Node Store)]
        E --> G[(Edge Store)]
        C -->|Embed| H[(Vector Store)]
    end

    subgraph "Cold State (Query)"
        I[Planner Agent] -->|Query| H
        I -->|Traverse| F
        H -->|Context| I
    end

    style C fill:#f9f,stroke:#333,stroke-width:4px
    style F fill:#bbf,stroke:#333,stroke-width:2px
    style G fill:#bbf,stroke:#333,stroke-width:2px
```

## 2. The Assimilation Process

How raw signals become crystallized wisdom.

```mermaid
sequenceDiagram
    participant Agent
    participant NATS
    participant Assimilator
    participant GraphDB
    participant VectorDB

    Agent->>NATS: Publish Signal (Action/Result)
    NATS->>Assimilator: Push Message
    Assimilator->>Assimilator: Parse & Validate (Pydantic)
    Assimilator->>GraphDB: Merge Node (Entity)
    Assimilator->>GraphDB: Merge Edge (Relation)
    Assimilator->>VectorDB: Upsert Embedding (Semantic)
    GraphDB-->>Assimilator: Ack
    Assimilator-->>NATS: Ack Message
```

## 3. State Transitions

The lifecycle of a piece of information within the Karmic Web.

```mermaid
stateDiagram-v2
    [*] --> Ephemeral
    Ephemeral --> Ingesting: Assimilator Pick-up
    Ingesting --> Crystallized: Graph Merge Success
    Ingesting --> Rejected: Validation Fail
    Crystallized --> Embedded: Vectorization
    Embedded --> Reinforced: Cited by Agent
    Reinforced --> Decaying: No Citations (Time)
    Decaying --> Pruned: Garbage Collection
    Pruned --> [*]
```
