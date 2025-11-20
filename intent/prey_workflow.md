# PREY Loop Visualization

**Lineage**:
*   **OODA Loop** (Boyd): Observe → Orient → Decide → Act
*   **MAPE-K** (IBM): Monitor → Analyze → Plan → Execute (+ Knowledge)
*   **JADC2** (DoD): Sense → Make Sense → Act

```mermaid
stateDiagram-v2
    [*] --> Perceive: Intent Received

    state Perceive {
        [*] --> GatherContext
        GatherContext --> ToolUse: Search/Read
        ToolUse --> ContextObject: Raw Data
    }
    note right of Perceive
        **Sense / Monitor / Observe**
        Gather raw signals from environment
    end note

    Perceive --> React: Context Object

    state React {
        [*] --> AnalyzeContext
        AnalyzeContext --> CynefinSort: Simple/Complicated/Complex/Chaotic
        CynefinSort --> CBR: Retrieve Precedents
        CBR --> GeneratePlan: Todo List
    }
    note right of React
        **Make Sense / Analyze / Orient**
        Filter signal from noise
    end note

    React --> Execute: Plan

    state Execute {
        [*] --> Step1
        Step1 --> Step2
        Step2 --> StepN
        StepN --> ExecutionResult
    }
    note right of Execute
        **Act / Plan+Execute / Decide+Act**
        Change the state of the world
    end note

    Execute --> Yield: Execution Result

    state Yield {
        [*] --> SelfAudit
        SelfAudit --> CheckIntent: Did it work?
        CheckIntent --> Retry: No (Feedback Loop)
        CheckIntent --> Commit: Yes
    }
    note right of Yield
        **Feedback / Knowledge / Loop**
        Update model & memory
    end note

    Retry --> Perceive: Updated Constraints
    Commit --> [*]: Mission Complete
```