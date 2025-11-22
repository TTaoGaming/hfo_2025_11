---
title: Obsidian Hourglass Strategy
status: Active (Gen 51)
domain: Strategy
owners: [Swarmlord]
type: Temporal Algorithm
---

# ⏳ Obsidian Hourglass Strategy

## ⚡ BLUF (Bottom Line Up Front)
The **Obsidian Hourglass** is the core temporal traversal algorithm of Hive Fleet Obsidian. It allows the Swarm to act as an **Anytime Algorithm**, instantly querying the **Past (Karmic Web)** for precedents, executing in the **Present (Neck)**, and simulating the **Future (Simulation Web)** to minimize tail risk. It is the "Ship" that navigates the State-Action space.

## 📊 Temporal Domain Matrix

| Domain | Component | Function | Technology |
| :--- | :--- | :--- | :--- |
| **Past** | Karmic Web | Retrieval & Case-Based Reasoning | GraphRAG (Postgres) |
| **Present** | The Neck | Real-time Orchestration | Ray / Temporal |
| **Future** | Simulation Web | Monte Carlo & Predictive Modeling | DSPy / Simulation |

## 🧠 Concept Visualization

### View 1: The Hourglass Shape (Conceptual)
*The flow of information through time.*

```mermaid
graph TD
    subgraph PAST [The Karmic Web]
        History[Historical Data]
        Patterns[Learned Patterns]
    end

    subgraph NECK [The Present]
        Action[Current Action]
    end

    subgraph FUTURE [The Simulation Web]
        Sim1[Scenario A]
        Sim2[Scenario B]
        Risk[Tail Risk Analysis]
    end

    PAST -->|Informs| NECK
    NECK -->|Simulates| FUTURE
    FUTURE -->|Refines| NECK
    NECK -->|Writes to| PAST
```

### View 2: The Anytime Algorithm (Logical)
*How the algorithm yields results at any moment.*

```mermaid
stateDiagram-v2
    direction TB

    state "PAST: Karmic Web" as Past {
        [*] --> Retrieval
        Retrieval --> Cynefin_Sort
        Cynefin_Sort --> CaseBasedReasoning
    }

    state "NECK: Present Web" as Present {
        Orchestrate --> Swarm_Execution
        Swarm_Execution --> Stigmergy_Check
    }

    state "FUTURE: Simulation Web" as Future {
        MonteCarloTree --> ThompsonSampling
        ThompsonSampling --> Simulated_Outcome
    }

    %% The Flip Logic
    Past --> Present : Precedents (Karma)
    Present --> Future : Simulation Request
    Future --> Present : Probabilities & Tail Risk
    Present --> Past : Post-Mortem (Learning)

    note right of Present
        ANYTIME ALGORITHM:
        Stop at any moment to get
        Best_Path_Distribution.
    end note
```

### View 3: Data Flow Architecture (Physical)
*The movement of data between storage and compute.*

```mermaid
sequenceDiagram
    participant DB as Postgres (Karma)
    participant Ray as Ray Cluster (Neck)
    participant Sim as Sim Engine (Future)

    Ray->>DB: Query Precedents
    DB-->>Ray: Return Case History
    Ray->>Ray: Formulate Plan
    Ray->>Sim: Request Monte Carlo (N=1000)
    Sim-->>Ray: Return Success Probabilities
    Ray->>Ray: Execute Best Path
    Ray->>DB: Log Outcome
```

## 🦅 Executive Summary
The **Obsidian Hourglass** is the core spatial traversal strategy for Hive Fleet Obsidian. It represents the flow of information through time:
1.  **PAST (Karmic Web)**: Retrieval of precedents and case-based reasoning.
2.  **PRESENT (Neck)**: Real-time orchestration and execution.
3.  **FUTURE (Simulation Web)**: Monte Carlo simulations and predictive modeling.

It is an **Anytime Algorithm**, meaning it can be stopped at any moment to yield the best current path distribution.
