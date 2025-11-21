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
        [*] --> Scatter: Orchestrated Map-Reduce
        Scatter --> PREY_Loop_xN: Parallel Execution
        PREY_Loop_xN --> InjectDisruptor: 1+ Hidden Disruptors
        InjectDisruptor --> Gather: Collect Results
    }
    note right of Act
        **Deliver / Execute**
        Orchestrated Map-Reduce
        Scatter-Gather + Hidden Disruptors
    end note

    Act --> Review: Raw Results

    state Review {
        [*] --> Filter: Remove Noise
        Filter --> AdversarialQuorum: Confidence & Behavior
        AdversarialQuorum --> GenerateOutput: Readable & Usable
    }
    note right of Review
        **Assess / Validate**
        Filter -> Byzantine Quorum
        Output Generation
    end note

    Review --> Mutate: Feedback

    state Mutate {
        [*] --> TuneKnobs: Adjust Parameters
        note right of TuneKnobs
            **Knobs:**
            - Temperature
            - Model Selection
            - Prompt Strategy
            - Voting Threshold
            - Disruptor Count
            - Mutation Rate
        end note
        TuneKnobs --> UpdateArchive: MAP-Elites
        UpdateArchive --> EvolveStrategy: Next Gen
    }
    note right of Mutate
        **Evolve / Improve**
        Multi-Parameter Mutation
    end note

    Mutate --> Set: Next Generation (Loop)
    Mutate --> [*]: Success (Consensus Reached)
```
