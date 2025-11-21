# The SWARM Loop: Fractal Coordination Holon

> **Status**: Active
> **Type**: Level 1+ (Recursive Coordination)

The **SWARM Loop** is the coordination pattern for Hive Fleet Obsidian. It is **Fractal**, meaning a SWARM can coordinate other SWARMs or atomic PREY Agents.

## 🧜‍♀️ State Diagram (Mermaid)

```mermaid
stateDiagram-v2
    [*] --> SET

    state SET {
        [*] --> AnalyzeMission
        AnalyzeMission --> DecomposeTasks
        DecomposeTasks --> SelectChildren
        SelectChildren --> [*]
    }

    SET --> WATCH: Children Spawned

    state WATCH {
        [*] --> DispatchTasks
        DispatchTasks --> MonitorSignals
        MonitorSignals --> [*]
    }

    WATCH --> ACT: Signals Received

    state ACT {
        [*] --> CollectOutputs
        CollectOutputs --> SynthesizeResults
        SynthesizeResults --> ResolveConflicts
        ResolveConflicts --> [*]
    }

    ACT --> REVIEW: Results Ready

    state REVIEW {
        [*] --> EvaluateSuccess
        EvaluateSuccess --> UpdateArchive
        UpdateArchive --> [*]
    }

    REVIEW --> MUTATE: Always (QD Loop)
    REVIEW --> YIELD: Stop Condition (Max Gen/Confidence)

    state MUTATE {
        [*] --> AdjustStrategy
        AdjustStrategy --> RespawnChildren
        RespawnChildren --> [*]
    }

    MUTATE --> WATCH: Next Generation

    state YIELD {
        [*] --> PackageArtifact
        PackageArtifact --> EmitSignal
        EmitSignal --> [*]
    }

    YIELD --> [*]: Mission Complete
```

## 🌌 Fractal Holarchy Structure

The system scales by nesting these loops:

*   **Level 3 (HIVE)**: Strategic SWARM. Decomposes "War" into "Battles".
    *   *Children*: Level 2 SWARMs.
*   **Level 2 (GROWTH)**: Operational SWARM. Decomposes "Battle" into "Missions".
    *   *Children*: Level 1 SWARMs.
*   **Level 1 (SWARM)**: Tactical SWARM. Decomposes "Mission" into "Tasks".
    *   *Children*: Level 0 PREY Agents.
*   **Level 0 (PREY)**: Atomic Agent. Executes "Task".
    *   *Children*: None (Tools).

```mermaid
graph TD
    H[L3: HIVE Holon] -->|Orchestrates| G1[L2: GROWTH Holon A]
    H -->|Orchestrates| G2[L2: GROWTH Holon B]

    G1 -->|Orchestrates| S1[L1: SWARM Holon X]
    G1 -->|Orchestrates| S2[L1: SWARM Holon Y]

    S1 -->|Manages| P1[L0: PREY Agent 1]
    S1 -->|Manages| P2[L0: PREY Agent 2]
    S1 -->|Manages| P3[L0: PREY Agent 3]

    subgraph "Atomic Execution"
    P1
    P2
    P3
    end

    subgraph "Tactical Coordination"
    S1
    S2
    end

    subgraph "Strategic Coordination"
    G1
    G2
    H
    end
```
