---
octagon:
  ontos:
    id: design-hfo-level2-swarm-workflow-v1
    type: design
    owner: Swarmlord
  logos:
    protocol: HFO-L2-SWARM
    format: markdown
  techne:
    stack:
    - mermaid
    - markdown
    - dspy
    - map-reduce
    complexity: extreme
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T14:45:00Z'
  pathos:
    stress_level: 0.9
    validation: pending
  ethos:
    security_level: internal
    compliance:
    - hfo-evolutionary-pressure
  topos:
    address: brain/design_hfo_level2_swarm_workflow.md
    links:
    - brain/design_hfo_level2_architecture.md
    - brain/design_hfo_level2_fractal_disruption.md
  telos:
    viral_factor: 1.0
    meme: 1-8-64-8-1. The Pulse of Evolution.
hexagon:
  ontos:
    id: 50c95245-729c-47be-af49-9cd5fab0998d
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-24T14:30:05.833666Z'
    generation: 51
  topos:
    address: brain/archive/gen52_drafts/design_hfo_level2_swarm_workflow.md
    links: []
  telos:
    viral_factor: 0.0
    meme: design_hfo_level2_swarm_workflow.md
---


# 🐝 HFO Level 2: The SWARM Workflow (S-W-A-R-M)

> **Intent**: To define the **Level 2 Lifecycle** using the **SET-WATCH-ACT-REVIEW-MUTATE** protocol. This implements the "Diamond Pulse" scaling pattern ($1 \to 8 \to 64 \to 8 \to 1$).

## 1. The Pulse (1-8-64-8-1)
The workflow follows a specific expansion and contraction rhythm, breathing life into the static architecture.

*   **1 (SET)**: The Navigator & User (Intent).
*   **8 (WATCH)**: Async Background Watchers (Context).
*   **64 (ACT)**: The Octarchy Squads (Execution).
*   **8 (REVIEW)**: The Consensus Engines (Truth).
*   **1 (MUTATE)**: The Injector/Assimilator (Evolution).

```mermaid
graph TD
    subgraph The_Pulse [The 1-8-64-8-1 Expansion]
        direction TB
        L0[1: SET (Navigator)]
        L1[8: WATCH (Watchers)]
        L2[64: ACT (The Octarchy)]
        L3[8: REVIEW (Assimilators)]
        L4[1: MUTATE (Injector)]

        L0 -->|Intent| L1
        L1 -->|Context| L2
        L2 -->|Artifacts| L3
        L3 -->|Consensus| L4
        L4 -->|Evolution| L0
    end

    style L2 fill:#ffcccc,stroke:#f00,stroke-width:2px
```

## 2. The Workflow Stages

### Phase 1: SET (1 Agent)
*   **Actors**: User + Navigator (Swarmlord).
*   **Action**: Define the **Mission Intent** (Gherkin), Constraints, and Success Criteria.
*   **Output**: A `MissionManifest` (JSON).

### Phase 2: WATCH (8 Agents)
*   **Actors**: 8 Async Watchers (1 per Dimension: Ontos, Logos, etc.).
*   **Action**: Background scan of the environment.
    *   *Ontos Watcher*: Scans `AGENTS.md`, `README.md`.
    *   *Techne Watcher*: Scans `requirements.txt`, code.
    *   *Chronos Watcher*: Checks timestamps and git logs.
*   **Output**: 8 `ContextStreams` fed into the Squads.

### Phase 3: ACT (64 Agents)
*   **Actors**: 8 Squads of 8 Agents (The Octarchy).
*   **Action**: **PREY Loops** (Perceive-React-Execute-Yield).
    *   **Map**: Distribute tasks to 64 agents.
    *   **Filter**: Apply local constraints.
    *   **Reduce**: Generate raw artifacts.
*   **Disruption**: The "Hidden Disruptor" logic is active here (1 per Squad).

### Phase 4: REVIEW (8 Agents)
*   **Actors**: 8 Level 1 Assimilators (1 per Squad).
*   **Action**: **Byzantine Consensus & Reveal**.
    *   **The Reveal**: Hidden Disruptors show their hand.
    *   **The Vote**: 3 Immunizers + 4 Assimilators vote on the valid artifact.
    *   **The Verdict**: Pinpoint the disruption vector.
*   **Output**: 8 Validated Dimensional Facets.

### Phase 5: MUTATE (1 Agent)
*   **Actors**: 1 Level 2 Injector/Assimilator.
*   **Action**: **Meta-Evolution & QD Optimization**.
    *   **Synthesis**: Merge 8 Facets into 1 Holon.
    *   **DSPy Tuning**: Use the "Disruptor Success Rate" to mutate the System Prompts.
        *   *If Disruptor won*: Strengthen Immunizer prompts.
        *   *If Disruptor lost*: Evolve Disruptor tactics (make them smarter).
    *   **Role Mutation**: Evolve "Champion Personas" based on performance.
*   **Output**: 1 Final Artifact + Updated `dspy_state.json`.

## 3. The Evolutionary Loop (DSPy & QD)
The goal is not just a result, but **System Evolution**.

```mermaid
graph LR
    subgraph Mutation_Engine [Phase 5: The Mutate Engine]
        direction TB
        Input[8 Verified Facets]
        Data[Disruption Data]

        subgraph QD_Optimizer [Quality-Diversity (QD)]
            Metric1[Novelty Score]
            Metric2[Quality Score]
            Map[MAP-Elites Grid]
        end

        subgraph DSPy_Compiler [DSPy Teleprompter]
            P_Old[Current Prompts]
            Feedback[Success/Fail Signal]
            P_New[Mutated Prompts]
        end

        Input --> QD_Optimizer
        Data --> DSPy_Compiler

        QD_Optimizer -->|Select Champions| DSPy_Compiler
        DSPy_Compiler -->|Update| P_New
        P_New -->|Next Cycle| Next_Round[Next SET Phase]
    end
```

## 4. Summary
*   **1-8-64-8-1**: The breathing rhythm of the Hive.
*   **Fractal Friction**: The "Act" phase (64 agents) creates friction/heat.
*   **Cooling**: The "Review" phase (8 agents) condenses that heat into signal.
*   **Evolution**: The "Mutate" phase uses the signal to upgrade the DNA (Prompts).
