---
title: The Three Webs Architecture
status: Active
type: Architecture
tags:
- karmic-web
- present-web
- simulation-web
hexagon:
  ontos:
    id: 118b92c6-187b-4d70-9381-1a756f37012f
    type: doc
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T06:32:09.812322Z'
    generation: 51
  topos:
    address: brain/architecture_three_webs.md
    links: []
  telos:
    viral_factor: 0.0
    meme: The Three Webs Architecture
---



# 🕸️ The Three Webs Architecture

## ⚡ BLUF (Bottom Line Up Front)
The **Three Webs** architecture is the cognitive framework of Hive Fleet Obsidian. It divides the system's operation into three distinct temporal domains: **The Karmic Web** (Past/Memory), **The Present Web** (Action/Execution), and **The Simulation Web** (Future/Planning). This separation allows the swarm to balance "Fast" reactive behaviors with "Slow" deliberative planning and "Deep" historical wisdom.

---

## 1. The Tri-Web Topology

The spatial relationship between the three domains.

```mermaid
graph TD
    subgraph "Past (Z < 0)"
        K[Karmic Web]
        K_Desc[GraphRAG + VectorDB]
    end

    subgraph "Present (Z = 0)"
        P[Present Web]
        P_Desc[NATS + Temporal + Ray]
    end

    subgraph "Future (Z > 0)"
        S[Simulation Web]
        S_Desc[DSPy + MAP-Elites]
    end

    K -->|Context| P
    P -->|Uncertainty| S
    S -->|Golden Path| P
    P -->|Experience| K

    style K fill:#f9f,stroke:#333
    style P fill:#bfb,stroke:#333
    style S fill:#bbf,stroke:#333
```

## 2. Data Flow & Transformation

How information mutates as it crosses the boundaries.

```mermaid
sequenceDiagram
    participant K as Karmic Web
    participant P as Present Web
    participant S as Simulation Web

    Note over K: Stigmergic Graph
    K->>P: Retrieval (Context)
    Note over P: Active Swarm
    P->>P: Execute Action
    alt Failure / Uncertainty
        P->>S: Request Simulation
        Note over S: Evolutionary Forge
        S->>S: Mutate & Test
        S->>P: Optimized Plan
    end
    P->>K: Commit Result (Memory)
```

## 3. Technology Stack Mapping

The concrete technologies powering each Web.

```mermaid
classDiagram
    class KarmicWeb {
        +Postgres
        +pgvector
        +NetworkX
        +AssimilatorAgent
    }
    class PresentWeb {
        +NATS JetStream
        +Temporal.io
        +Ray Core
        +SwarmController
    }
    class SimulationWeb {
        +DSPy
        +PyRibs (MAP-Elites)
        +OpenELM
        +DisruptorAgent
    }

    KarmicWeb <.. PresentWeb : Queries
    PresentWeb ..> SimulationWeb : Spawns
```

**The Obsidian Hex-Hive**
*   *Why*: Hexagonal architecture (Ports & Adapters) meets Hive mind.

**Hyper-Heuristic Horizon (H3)**
*   *Why*: Emphasizes the "Hyper-Heuristic" nature of evolving the algorithms themselves.

**The Panarchic Loop**
*   *Why*: In ecology, "Panarchy" describes the interplay between change and persistence (Adaptive Cycles).
