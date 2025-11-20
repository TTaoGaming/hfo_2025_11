# SWARM Loop Visualization (Level 1)

**Lineage**:
*   **D3A** (Targeting): Decide → Detect → Deliver → Assess
*   **Byzantine Fault Tolerance**: 3f+1 Consensus
*   **Evolutionary Computation**: MAP-Elites / Quality-Diversity

```mermaid
stateDiagram-v2
    [*] --> Set: Mission Intent

    state Set {
        [*] --> DefineIntent
        DefineIntent --> SetConstraints
        SetConstraints --> InitEvolution: Search Space
    }
    note right of Set
        **Decide / Intent**
        User defines Goal & Constraints
    end note

    Set --> Watch: Config

    state Watch {
        [*] --> InitTelemetry
        InitTelemetry --> SubscribeStigmergy
    }
    note right of Watch
        **Detect / Observability**
        LangSmith Traces & NATS Signals
    end note

    Watch --> Act: Ready

    state Act {
        [*] --> Scatter
        Scatter --> PREY_Loop_x10: Parallel Execution
        PREY_Loop_x10 --> InjectDisruptor: 1-3 Adversaries
        InjectDisruptor --> Gather: Collect Results
    }
    note right of Act
        **Deliver / Execute**
        Scatter-Gather (10 Agents)
        Includes Disruptor Injection
    end note

    Act --> Review: 10 Results

    state Review {
        [*] --> RunImmunizers: Blue Team Check
        RunImmunizers --> CalculateQuorum: 3f+1 Vote
        CalculateQuorum --> CapConfidence: Max 90%
    }
    note right of Review
        **Assess / Validate**
        Byzantine Quorum & Red Teaming
    end note

    Review --> Mutate: Quorum Result

    state Mutate {
        [*] --> UpdateArchive: Quality-Diversity
        UpdateArchive --> OptimizeDSPy: Evolve Prompts
        OptimizeDSPy --> EvolveStrategy: Hyper-Heuristics
        EvolveStrategy --> CheckConvergence
    }
    note right of Mutate
        **Evolve / Improve**
        MAP-Elites & DSPy Optimization
    end note

    Mutate --> Set: Next Generation (Loop)
    Mutate --> [*]: Success (Consensus Reached)
```