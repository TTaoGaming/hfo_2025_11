---
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 1c125cca-6b39-4a5f-a34d-2ac28b8c34b9
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:07.001552+00:00'
  topos:
    address: memory/episodic/gen_50_archive/obsidian_hourglass.md
    links: []
  telos:
    viral_factor: 0.0
    meme: obsidian_hourglass.md
---

# ⏳ The Obsidian Hourglass: Temporal Traversal Strategy

> **Status**: Draft
> **Type**: Algorithm / Strategy

## Executive Summary
The **Obsidian Hourglass** is the core spatial traversal strategy for Hive Fleet Obsidian. It represents the flow of information through time:
1.  **PAST (Karmic Web)**: Retrieval of precedents and case-based reasoning.
2.  **PRESENT (Neck)**: Real-time orchestration and execution.
3.  **FUTURE (Simulation Web)**: Monte Carlo simulations and predictive modeling.

It is an **Anytime Algorithm**, meaning it can be stopped at any moment to yield the best current path distribution.

## Visualization

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
