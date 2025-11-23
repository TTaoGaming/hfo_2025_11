---
hexagon:
  ontos:
    id: df57134e-af44-4d30-9e0c-bfed1ffb6c84
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:07.006057+00:00'
    generation: 51
  topos:
    address: memory/episodic/gen_50_archive/prey_workflow.md
    links: []
  telos:
    viral_factor: 0.0
    meme: prey_workflow.md
---


# The PREY Loop: Atomic Cognitive Holon

> **Status**: Active
> **Type**: Level 0 (Atomic Execution)

The **PREY Loop** is the fundamental state machine for all agents in Hive Fleet Obsidian. It represents the smallest unit of "Cognitive Work".

## 🧜‍♀️ State Diagram (Mermaid)

```mermaid
stateDiagram-v2
    [*] --> PERCEIVE

    state PERCEIVE {
        [*] --> GatherContext
        GatherContext --> ReadMemory
        ReadMemory --> [*]
    }

    PERCEIVE --> REACT: Context Acquired

    state REACT {
        [*] --> Synthesize
        Synthesize --> PlanActions
        PlanActions --> ValidateSafety
        ValidateSafety --> [*]
    }

    REACT --> EXECUTE: Plan Approved
    REACT --> YIELD: Plan Rejected (Error)

    state EXECUTE {
        [*] --> InvokeTools
        InvokeTools --> CaptureOutput
        CaptureOutput --> [*]
    }

    EXECUTE --> YIELD: Action Complete

    state YIELD {
        [*] --> Reflect
        Reflect --> CalculateReward
        CalculateReward --> UpdateMemory
        UpdateMemory --> EmitSignal
        EmitSignal --> [*]
    }

    YIELD --> PERCEIVE: Feedback Loop (RL)
    YIELD --> [*]: Task Done (State Saved)
```

## 🧠 Cognitive Chunking
*   **Perceive**: "What is happening?" (Input)
*   **React**: "What should I do?" (Logic)
*   **Execute**: "Do it." (Action)
*   **Yield**: "What did I learn?" (Reinforcement/Stigmergy)
