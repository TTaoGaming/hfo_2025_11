---
title: Pheromones & Composability
status: Draft
domain: Biology
owners:
- Swarmlord
- Immunizer
type: Conceptual Architecture

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 6718f2e1-29b1-48c2-960a-f298eda48613
    type: doc
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T06:32:09.820405Z'
  topos:
    address: 1.0.0
    links: []
  telos:
    viral_factor: 0.0
    meme: Pheromones & Composability
---


# 🧪 Pheromones & Composability: The Antifragile Stigmergy

## ⚡ BLUF (Bottom Line Up Front)
True Stigmergy in Hive Fleet Obsidian is not just NATS messages. It is a **Tri-Layered Pheromone System** that ensures **Antifragility**. By composing signals from **Static Headers** (YAML), **Hot Streams** (NATS), and **Cold Memory** (Vector), the Hive creates a "Scent Landscape" that allows complex, self-organizing behaviors to emerge. Stress on the system (high signal density) triggers hardening (Immunizer activation), making the Hive stronger.

## 📊 The Pheromone Matrix

| Layer | Type | Implementation | Time Horizon | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Static** | **Scent Mark** | YAML Header (File) | Infinite | Machine-parsable governance, indexing, and "Slop" detection. |
| **Hot** | **Alarm/Food** | NATS JetStream | Seconds/Minutes | Real-time coordination, triggers, and immediate reaction. |
| **Cold** | **Ancestral** | Vector/Graph DB | Generations | Deep wisdom, pattern recognition, and long-term strategy. |
| **Composite**| **Complex** | Overlapping Signals | Variable | Emergent behavior (e.g., "Danger" + "Food" = "Caution"). |

## 🧠 Concept Visualization

### View 1: The Tri-Layered Stigmergy Stack
*How the three layers interact to form a complete signal.*

```mermaid
graph TD
    Agent[Agent Action] -->|Writes| File[File Artifact]
    Agent -->|Emits| NATS[NATS Signal]

    subgraph Static Layer
        File -->|Contains| YAML[YAML Header]
        YAML -->|Read by| Guard[Hive Guard]
    end

    subgraph Hot Layer
        NATS -->|Trigger| React[Reactive Agent]
    end

    subgraph Cold Layer
        File -->|Ingested by| Assimilator
        Assimilator -->|Embeds| Vector[Vector DB]
    end

    Guard -.->|Validates| NATS
    React -.->|Queries| Vector
```

### View 2: Antifragile Stress Response
*How the system gets stronger when stressed (High Pheromone Density).*

```mermaid
stateDiagram-v2
    State Normal
    State Stressed
    State Hardened

    Normal --> Stressed : High Signal Density / Attack
    Stressed --> Hardened : Immunizer Activation
    Hardened --> Normal : Decay / Relaxation

    note right of Stressed
        - Pheromones > Threshold
        - Disruptors Active
    end note

    note right of Hardened
        - Validation Strictness: HIGH
        - Stem Cells: SPAWNED
        - System is Stronger
    end note
```

### View 3: Pheromone Composability
*Complex behavior from simple signals.*

```mermaid
graph LR
    SignalA(Food Pheromone)
    SignalB(Danger Pheromone)

    SignalA -->|Combine| Composite{Composite Signal}
    SignalB -->|Combine| Composite

    Composite -->|Result| Action[Cautious Harvesting]

    style SignalA fill:#9f9,stroke:#333
    style SignalB fill:#f99,stroke:#333
    style Composite fill:#ff9,stroke:#333
```
