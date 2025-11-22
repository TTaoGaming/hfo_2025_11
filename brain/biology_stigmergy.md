---
title: Evolutionary Pheromones
status: Active (Gen 51)
domain: Biology
owners: [Swarmlord]
type: Communication
---

# 🧪 Evolutionary Pheromones

## ⚡ BLUF (Bottom Line Up Front)
In a biological swarm, communication is chemical, not digital. **Pheromones** are signals deposited in the environment that have **Strength** (Priority) and **Decay** (Time-to-Live). This prevents information overload; old, irrelevant signals simply fade away, while important signals are reinforced by other agents.

## 📊 Pheromone Matrix

| Type | Analogue | Meaning | HFO Implementation |
| :--- | :--- | :--- | :--- |
| **Trail** | Ant | "Follow this path" | Success Trace (LangSmith) |
| **Alarm** | Bee | "Danger here" | Error Log / Exception |
| **Aggregation** | Cockroach | "Gather here" | Task Queue (NATS) |
| **Territory** | Wolf | "This is mine" | Lock File / Mutex |

## 🧠 Concept Visualization

### View 1: The Feedback Loop (Conceptual)
*Positive feedback amplifies success.*

```mermaid
graph TD
    AgentA[Agent A] -->|Finds Food| Pheromone[Deposit Pheromone]
    Pheromone -->|Attracts| AgentB[Agent B]
    AgentB -->|Finds Food| Reinforce[Reinforce Pheromone]
    Reinforce -->|Attracts| AgentC[Agent C]
```

### View 2: Signal Decay (Logical)
*Information has a half-life.*

```mermaid
graph LR
    Time[Time Passes] -->|Reduces| Strength[Signal Strength]
    Strength -->|Below Threshold| Death[Signal Death]
    Reinforcement[Agent Action] -->|Increases| Strength
```

### View 3: Digital Implementation (Physical)
*How we code chemistry.*

```mermaid
classDiagram
    class Pheromone {
        +subject: str
        +payload: dict
        +strength: float
        +timestamp: int
        +decay_rate: float
    }

    class Environment {
        +evaporate()
        +diffuse()
    }

    Environment "1" *-- "*" Pheromone
```

## 🦅 Executive Summary
**Pheromones** are the language of Stigmergy. They are not just data; they have **biological properties** like decay and strength.
*   **Ant Pheromone**: "Follow me." (Pathfinding)
*   **Termite Pheromone**: "Build here." (Construction)
*   **Slime Mold Pheromone**: "Explore there." (Search)
