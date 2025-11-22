---
title: Hybrid Stigmergic GraphRAG Memory
status: Active (Gen 51)
domain: Architecture
owners: [Swarmlord]
type: Memory System
---

# 🧠 Hybrid Stigmergic GraphRAG Memory

## ⚡ BLUF (Bottom Line Up Front)
The **Memory Organ** is a hybrid system designed to solve the "Goldfish Memory" problem of LLMs. It combines a **Fast Loop** (NATS JetStream) for real-time "Hot" episodic memory with a **Slow Loop** (Postgres GraphRAG) for "Cold" semantic wisdom. The **Crystal Spinner** agent acts as the bridge, crystallizing fleeting signals into permanent knowledge.

## 📊 Memory Tier Matrix

| Tier | Technology | Speed | Retention | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Hot** | NATS JetStream | <10ms | 1 Hour | Coordination & Signaling |
| **Warm** | Redis / Plasma | <1ms | Session | Context Window Extension |
| **Cold** | Postgres (Graph+Vector) | >100ms | Infinite | Wisdom & Precedents |
| **Frozen** | Markdown Files | N/A | Infinite | Documentation & Intent |

## 🧠 Concept Visualization

### View 1: The Crystallization Process (Conceptual)
*Turning noise into signal.*

```mermaid
graph TD
    Stream[Stream of Consciousness] -->|Filter| Spinner[Crystal Spinner]
    Spinner -->|Extract| Fact[Fact]
    Spinner -->|Extract| Relation[Relationship]

    Fact -->|Store| Graph[Knowledge Graph]
    Relation -->|Link| Graph
```

### View 2: The Hybrid Architecture (Logical)
*Hot and Cold loops working together.*

```mermaid
graph TD
    Agent[Agent] -->|Signal| NATS((NATS Stream))

    subgraph Hot Memory
        NATS
    end

    NATS -->|Ingest| Spinner[Crystal Spinner]

    subgraph Cold Memory
        Spinner -->|Nodes/Edges| Graph[(Postgres Graph)]
        Spinner -->|Vectors| Vector[(pgvector)]
    end

    Agent -.->|Query| Graph
    Agent -.->|Search| Vector
```

### View 3: Data Schema (Physical)
*How we store the graph.*

```mermaid
erDiagram
    NODE {
        uuid id
        string label
        json properties
        vector embedding
    }
    EDGE {
        uuid source
        uuid target
        string relation
        float weight
    }
    NODE ||--o{ EDGE : originates
    NODE ||--o{ EDGE : terminates
```

## 🦅 Executive Summary
The **Memory Organ** is a hybrid system:
1.  **Fast Loop (NATS)**: "Hot" Episodic memory. Real-time signals.
2.  **Slow Loop (Postgres)**: "Cold" Semantic memory. Knowledge Graph + Vectors.
