---
title: Stigmergy Layer (NATS JetStream)
status: Active (Gen 51)
domain: Infrastructure
owners:
- Swarmlord
type: Technical Specification
hexagon:
  ontos:
    id: e4731280-94bc-4fee-9aaa-4fa519444646
    type: doc
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T06:32:09.795198Z'
    generation: 51
  topos:
    address: brain/infrastructure_stigmergy.md
    links: []
  telos:
    viral_factor: 0.0
    meme: Stigmergy Layer (NATS JetStream)
---



# 📡 Stigmergy Layer: NATS JetStream

## ⚡ BLUF (Bottom Line Up Front)
**Stigmergy** is the principle of indirect coordination through the environment. In Hive Fleet Obsidian, we implement this using **NATS JetStream**. Agents do not talk to each other; they modify the environment (publish messages), and other agents react to those modifications. This decouples the Swarm and allows for massive scalability.

## 📊 Stigmergy Matrix

| Component | Concept | Implementation | Purpose |
| :--- | :--- | :--- | :--- |
| **Pheromone** | Signal | JSON Message (Subject) | Trigger Action |
| **Artifact** | Heavy Object | S3 / Postgres / File | Persist State |
| **Environment** | Medium | NATS JetStream | Transport Signals |
| **Decay** | Cleanup | Stream Retention Policy | Prevent Clutter |

## 🧠 Concept Visualization

### View 1: Indirect Coordination (Conceptual)
*Agents talk to the environment, not each other.*

```mermaid
graph TD
    AgentA[Agent A] -->|Modifies| Env[Environment]
    Env -->|Triggers| AgentB[Agent B]
    Env -->|Triggers| AgentC[Agent C]

    AgentB -.->|No Direct Link| AgentA
    AgentC -.->|No Direct Link| AgentA
```

### View 2: The Signal-Artifact Pattern (Logical)
*Lightweight signals carry pointers to heavy artifacts.*

```mermaid
graph LR
    AgentA[Agent A] -->|Publish Signal| NATS((NATS Stream))
    AgentA -->|Write Artifact| Memory[(Memory Store)]

    NATS -->|Push Signal| AgentB[Agent B]
    AgentB -->|Read Artifact| Memory

    subgraph Stigmergy Layer
        NATS
    end
```

### View 3: JetStream Architecture (Physical)
*Streams, Consumers, and Subjects.*

```mermaid
graph TD
    subgraph NATS Server
        Stream[Stream: HFO.>]
        Subject1[Subject: HFO.Task.Complete]
        Subject2[Subject: HFO.Task.Failed]

        Stream --> Subject1
        Stream --> Subject2
    end

    Pub[Publisher] -->|Msg| Stream
    Subject1 -->|Push| Sub1[Consumer A]
    Subject2 -->|Push| Sub2[Consumer B]
```

## 🦅 Executive Summary
**Stigmergy** is indirect coordination via the environment. In HFO, the "Environment" is the **NATS JetStream** message bus.
*   **Signals**: Lightweight JSON messages (Pheromones).
*   **Artifacts**: Heavy data stored in Memory/Object Store.
*   **Decoupling**: Agents do not know who consumes their output.
