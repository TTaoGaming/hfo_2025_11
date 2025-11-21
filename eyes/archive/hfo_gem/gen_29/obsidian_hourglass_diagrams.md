# Obsidian Hourglass Visual Models

**Date**: 2025-11-11
**Generation**: 29
**Purpose**: Visual representation of state-action space web model
**Updated**: 2025-11-11 - Added geometric hourglass structure

---

## Geometric Structure: Literal Hourglass in State-Action Space

```mermaid
graph TB
    subgraph PAST["PAST CONE (Expanding Backwards)"]
        P_TOP[/"Search Depth = ∞<br/>Radius = MAX"/]
        P1[Research Papers<br/>Decades of Info]
        P2[Open Source Code<br/>GitHub/GitLab]
        P3[Training Data<br/>Billions of Docs]
        P4[Internet Knowledge<br/>Web Search]
        P5[Local Archives<br/>pgvector]
        P_TOP -.->|expanding| P1
        P_TOP -.->|expanding| P2
        P_TOP -.->|expanding| P3
        P_TOP -.->|expanding| P4
        P_TOP -.->|expanding| P5
        P1 --> P_NARROW
        P2 --> P_NARROW
        P3 --> P_NARROW
        P4 --> P_NARROW
        P5 --> P_NARROW
    end

    P_NARROW["⧖ PRESENT DIAMETER ⧖<br/>───────────────<br/>Radius = f(budget, time, energy, agents)<br/>CONSTRAINED WAIST<br/>───────────────"]

    subgraph FUTURE["FUTURE CONE (Expanding Forward)"]
        P_NARROW --> F1
        P_NARROW --> F2
        P_NARROW --> F3
        P_NARROW --> F4
        P_NARROW --> F5
        F1[Monte Carlo Sim 1<br/>Success: 70%]
        F2[Monte Carlo Sim 2<br/>Success: 60%]
        F3[VM Probe A<br/>Real Experiment]
        F4[A* Path 1<br/>High Risk]
        F5[Thompson Sample<br/>Explore]
        F1 -.->|expanding| F_BOTTOM
        F2 -.->|expanding| F_BOTTOM
        F3 -.->|expanding| F_BOTTOM
        F4 -.->|expanding| F_BOTTOM
        F5 -.->|expanding| F_BOTTOM
        F_BOTTOM[\"Projection Horizon = Days<br/>Radius = MAX"\]
    end

    style PAST fill:#2a1a4d,stroke:#7c3aed,stroke-width:3px
    style P_NARROW fill:#dc2626,stroke:#fca5a5,stroke-width:4px
    style FUTURE fill:#1a2d1a,stroke:#22c55e,stroke-width:3px
    style P_TOP fill:#7c3aed,stroke:#a78bfa,stroke-width:2px
    style F_BOTTOM fill:#22c55e,stroke:#86efac,stroke-width:2px
```

---

## Three Horizons as State-Action Spaces

```mermaid
graph TB
    subgraph PAST["PAST HORIZON: Karmic Web (Indra's Net)"]
        P1[Historical Mission A]
        P2[Historical Mission B]
        P3[Codebase State T-1]
        P4[Research Archive]
        P5[Precedent Database]

        P1 -->|led to| P3
        P2 -->|failed, learned| P5
        P3 -->|evolved into| P5
        P4 -->|referenced in| P1
    end

    subgraph PRESENT["PRESENT HORIZON: Swarm Web"]
        S1[Swarm Config A<br/>10 agents, temp=0.7]
        S2[Swarm Config B<br/>5 agents, temp=0.3]
        S3[Execution State<br/>partial results]
        S4[Quorum Achieved<br/>consensus=85%]

        S1 -->|dispatch| S3
        S2 -->|dispatch| S3
        S3 -->|validate| S4
    end

    subgraph FUTURE["FUTURE HORIZON: Simulation Web"]
        F1[Simulation A<br/>success 70%]
        F2[Simulation B<br/>success 40%]
        F3[Simulation C<br/>failure 90%]
        F4[Projected Outcome]

        F1 -->|likely| F4
        F2 -->|possible| F4
        F3 -->|avoid| F4
    end

    P5 -.->|retrieve precedents| S1
    P5 -.->|retrieve precedents| S2
    S4 -.->|simulate outcomes| F1
    S4 -.->|simulate outcomes| F2
    F1 -.->|learn as if past<br/>FLIP| P5
    F2 -.->|learn as if past<br/>FLIP| P5

    style PAST fill:#2a1a4d,stroke:#7c3aed,stroke-width:2px
    style PRESENT fill:#1a2d1a,stroke:#22c55e,stroke-width:2px
    style FUTURE fill:#2d1a1a,stroke:#ef4444,stroke-width:2px
    style P5 fill:#7c3aed,stroke:#a78bfa,stroke-width:2px
    style S4 fill:#22c55e,stroke:#86efac,stroke-width:2px
    style F4 fill:#ef4444,stroke:#fca5a5,stroke-width:2px
```

---

## The Flip Operation (Geometric Swap)

```mermaid
stateDiagram-v2
    direction LR

    state "Normal Orientation" as Normal {
        [*] --> PastOnTop
        PastOnTop: PAST CONE (Top)<br/>Hunt Information
        PastOnTop --> PresentMiddle
        PresentMiddle: PRESENT DIAMETER<br/>Execute Swarm
        PresentMiddle --> FutureBottom
        FutureBottom: FUTURE CONE (Bottom)<br/>Simulate Outcomes
        FutureBottom --> [*]
    }

    Normal --> Flipped: 🔄 FLIP HOURGLASS

    state "Flipped Orientation" as Flipped {
        [*] --> FutureOnTop
        FutureOnTop: FUTURE CONE (Top)<br/>Retroflip Analysis
        FutureOnTop --> PresentMiddle2
        PresentMiddle2: PRESENT DIAMETER<br/>Postmortem
        PresentMiddle2 --> PastBottom
        PastBottom: PAST CONE (Bottom)<br/>Archive Learnings
        PastBottom --> [*]
    }

    Flipped --> Normal: 🔄 FLIP AGAIN

    note right of Normal
        Forward Flip:
        Past info → Present execution → Future sims
    end note

    note right of Flipped
        Reverse Flip:
        Future sims → Present analysis → Past archive
        (Learn from simulations as if they already happened)
    end note
```

---

## Diameter Equations (Resource Constraints)

```mermaid
graph LR
    subgraph Inputs["Resource Inputs"]
        B[Budget: $100]
        T[Time: 24 hours]
        E[Energy: 80%]
        A[Agents: 10]
        C[Compute: 4 CPUs]
    end

    subgraph Calculation["Diameter Calculation"]
        F1["d₁ = budget / cost_per_agent"]
        F2["d₂ = time * throughput"]
        F3["d₃ = √(energy × compute)"]
        MIN["d_present = min(d₁, d₂, d₃)"]
    end

    subgraph Output["Present Diameter"]
        D["Diameter = 8 agents<br/>───────────<br/>Can explore 8 parallel<br/>configurations"]
    end

    B --> F1
    T --> F2
    E --> F3
    C --> F3
    A --> F1

    F1 --> MIN
    F2 --> MIN
    F3 --> MIN

    MIN --> D

    style Inputs fill:#3b82f6,stroke:#60a5fa,stroke-width:2px
    style Calculation fill:#f59e0b,stroke:#fcd34d,stroke-width:2px
    style Output fill:#dc2626,stroke:#fca5a5,stroke-width:3px
    style D fill:#ef4444,stroke:#fca5a5,stroke-width:4px
```

---

## Recursive Flipping Loop (Convergence)

```mermaid
stateDiagram-v2
    [*] --> MissionIntent

    MissionIntent --> HuntPrecedents: Flip to PAST
    HuntPrecedents --> SimulateFutures: Flip to FUTURE
    SimulateFutures --> Postmortem: Analyze outcomes
    Postmortem --> LearnAsPast: Flip FUTURE→PAST
    LearnAsPast --> HuntPrecedents: Refined search

    HuntPrecedents --> ExecuteSwarm: Flip to PRESENT
    ExecuteSwarm --> ValidateResults: Check quorum
    ValidateResults --> ExecuteSwarm: Failed consensus
    ValidateResults --> SimulateFutures: Flip to FUTURE

    ValidateResults --> PublishArtifact: Convergence ✓
    PublishArtifact --> [*]

    SimulateFutures --> PublishArtifact: Anytime stop
    ExecuteSwarm --> PublishArtifact: Anytime stop
    HuntPrecedents --> PublishArtifact: Anytime stop

    note right of HuntPrecedents
        PAST Horizon
        - CYNEFIN, CBR
        - pgvector search
        - Pattern matching
    end note

    note right of ExecuteSwarm
        PRESENT Horizon
        - Swarm dispatch
        - Quorum voting
        - Hallucination detect
    end note

    note right of SimulateFutures
        FUTURE Horizon
        - Monte Carlo tree
        - A* search
        - VM experiments
    end note
```

---

## Constrained State-Action Web (Graph Structure)

```mermaid
graph LR
    subgraph States["State Space (Nodes)"]
        S0[Mission Config:<br/>intent, constraints,<br/>time_horizon]
        S1[Swarm Config A:<br/>10 agents,<br/>temp=0.7]
        S2[Swarm Config B:<br/>5 agents,<br/>temp=0.3]
        S3[Execution State:<br/>partial results,<br/>cost=$50]
        S4[Terminal:<br/>success prob=85%]
    end

    subgraph Actions["Action Space (Edges)"]
        S0 -->|hunt_precedents<br/>P=0.9| S1
        S0 -->|hunt_precedents<br/>P=0.1| S2
        S1 -->|execute_swarm<br/>cost=$30| S3
        S2 -->|execute_swarm<br/>cost=$15| S3
        S3 -->|validate_quorum<br/>P=0.7| S4
        S3 -->|flip_to_future<br/>P=0.3| S1
        S1 -->|simulate<br/>P=0.5| S4
    end

    subgraph Constraints["Constraint Boundaries"]
        C1[Budget: cost ≤ $100]
        C2[Time: duration ≤ 1 hour]
        C3[Quality: quorum ≥ 70%]
        C4[Safety: hallucinations ≤ 5%]
    end

    S0 -.->|enforces| C1
    S3 -.->|monitors| C1
    S3 -.->|monitors| C2
    S4 -.->|validates| C3
    S4 -.->|validates| C4

    style S0 fill:#3b82f6,stroke:#60a5fa,stroke-width:2px
    style S4 fill:#22c55e,stroke:#86efac,stroke-width:2px
    style C1 fill:#ef4444,stroke:#fca5a5,stroke-width:2px
    style C2 fill:#ef4444,stroke:#fca5a5,stroke-width:2px
    style C3 fill:#f59e0b,stroke:#fcd34d,stroke-width:2px
    style C4 fill:#f59e0b,stroke:#fcd34d,stroke-width:2px
```

---

## Integration with PREY Loop (Nested Execution)

```mermaid
sequenceDiagram
    participant O as Overmind
    participant N as Navigator<br/>(Orchestrator)
    participant P as PrecedentHunter<br/>(PAST)
    participant S as SwarmExecutor<br/>(PRESENT)
    participant F as SimulationEngine<br/>(FUTURE)
    participant V as Validator<br/>(Immunizer)

    O->>N: Mission Intent + Constraints

    Note over N: PREY: Perceive<br/>(Sense mission)
    N->>N: Parse intent, constraints

    Note over N: PREY: React<br/>(Decide flip strategy)
    N->>P: Flip to PAST (hunt precedents)

    Note over P: PREY: Execute<br/>(Retrieve precedents)
    P->>P: CYNEFIN, CBR, pgvector
    P->>N: Precedents found

    Note over N: PREY: Yield<br/>(Log precedents)
    N->>N: Store to knowledge base

    N->>S: Flip to PRESENT (execute swarm)

    Note over S: PREY: Execute<br/>(Dispatch N researchers)
    S->>S: Fan-out to 10 agents
    S->>V: Partial results

    Note over V: PREY: Yield<br/>(Validate quorum)
    V->>V: Quorum check, hallucinations
    V->>N: Consensus=85%, valid ✓

    N->>F: Flip to FUTURE (simulate)

    Note over F: PREY: Execute<br/>(Monte Carlo tree)
    F->>F: Run 100 simulations
    F->>N: Probability distribution

    Note over N: PREY: Yield<br/>(Publish artifact)
    N->>O: DIGEST.md with recommendations

    Note over O,N: Anytime stop:<br/>Can exit at any flip
```

---

## Probability Distribution Output (Artifact Format)

```mermaid
graph TD
    subgraph Input["Input: Mission Intent"]
        I1[Goal: Improve math benchmark]
        I2[Constraint: Budget $100]
        I3[Horizon: 1 day]
    end

    subgraph Flips["Hourglass Flips Executed"]
        F1[Flip 1: PAST→FUTURE<br/>5 precedents, 10 sims]
        F2[Flip 2: FUTURE→PAST<br/>Learn from sims]
        F3[Flip 3: PAST→PRESENT<br/>Execute swarm]
        F4[Flip 4: PRESENT→FUTURE<br/>Validate outcomes]
    end

    subgraph Output["Output: Probability Distribution"]
        O1[Best Path:<br/>Use GPT-4 + CoT prompts]
        O2[Confidence: 75%<br/>Expected: +30% score]
        O3[Alternatives:<br/>3 backup plans]
        O4[Tail Risks:<br/>5% catastrophic failure]
        O5[Evidence:<br/>12 precedents,<br/>3 swarm runs,<br/>50 simulations]
    end

    I1 --> F1
    I2 --> F1
    I3 --> F1

    F1 --> F2
    F2 --> F3
    F3 --> F4

    F4 --> O1
    F4 --> O2
    F4 --> O3
    F4 --> O4
    F4 --> O5

    style Input fill:#3b82f6,stroke:#60a5fa,stroke-width:2px
    style Flips fill:#f59e0b,stroke:#fcd34d,stroke-width:2px
    style Output fill:#22c55e,stroke:#86efac,stroke-width:2px
    style O1 fill:#10b981,stroke:#34d399,stroke-width:3px
```

---

## Comparison: Gen 28 (Temporal) vs Gen 29 (State-Action Web)

```mermaid
graph TB
    subgraph Gen28["Gen 28: Temporal Workflow"]
        G28_1[IntakeMissionIntent]
        G28_2[HuntPrecedents]
        G28_3[ConfigureSimulations]
        G28_4[RunSimulations]
        G28_5[RetroflipPrecedents]
        G28_6[PublishArtifact]

        G28_1 --> G28_2
        G28_2 --> G28_3
        G28_3 --> G28_4
        G28_4 --> G28_5
        G28_5 --> G28_6

        Note28[Linear sequence<br/>One-directional<br/>Fixed pipeline<br/>Single artifact]
    end

    subgraph Gen29["Gen 29: State-Action Web"]
        G29_0[Mission Config]
        G29_P[PAST States<br/>precedents]
        G29_S[PRESENT States<br/>swarm configs]
        G29_F[FUTURE States<br/>simulations]
        G29_T[Terminal State<br/>prob distribution]

        G29_0 -.->|hunt| G29_P
        G29_0 -.->|execute| G29_S
        G29_P -.->|flip| G29_F
        G29_F -.->|flip| G29_P
        G29_S -.->|flip| G29_F
        G29_P -.->|flip| G29_S
        G29_S -.->|converge| G29_T
        G29_F -.->|converge| G29_T
        G29_P -.->|anytime| G29_T

        Note29[Recursive graph<br/>Bidirectional flips<br/>Adaptive algorithms<br/>Probability distributions]
    end

    style Gen28 fill:#2a1a4d,stroke:#7c3aed,stroke-width:2px
    style Gen29 fill:#1a2d1a,stroke:#22c55e,stroke-width:2px
    style Note28 fill:#ef4444,stroke:#fca5a5,stroke-width:2px
    style Note29 fill:#10b981,stroke:#34d399,stroke-width:2px
```

---

## SysML v2 Model Preview (Conceptual)

```sysml
package ObsidianHourglass {

    // State space definition
    attribute def MissionConfig {
        attribute intent: String;
        attribute constraints: ConstraintSet;
        attribute timeHorizon: Duration;
    }

    attribute def SwarmConfig {
        attribute numAgents: Integer;
        attribute roles: String[*];
        attribute temperatures: Real[*];
        attribute models: String[*];
    }

    attribute def ExecutionState {
        attribute partialResults: String[*];
        attribute quorumStatus: Real;
        attribute costSpent: Real;
        attribute timeElapsed: Duration;
    }

    // Action space definition
    enum def HourglassAction {
        huntPrecedents;
        executeSwarm;
        simulateFutures;
        flipHourglass;
        publishArtifact;
    }

    // Constraint definitions
    attribute def ConstraintSet {
        attribute maxBudget: Real;
        attribute maxTime: Duration;
        attribute minQuality: Real;
        attribute maxRisk: Real;
    }

    // Value function outputs
    attribute def ProbabilityDistribution {
        attribute outcomes: Outcome[*];
        attribute bestPath: String;
        attribute confidence: Real;
        attribute evidence: EvidenceSummary;
    }

    attribute def Outcome {
        attribute description: String;
        attribute probability: Real;
        attribute expectedValue: Real;
        attribute risk: String;
    }

    // Flip algorithm interface
    abstract part def FlipAlgorithm {
        in attribute currentState: ExecutionState;
        in attribute horizon: String;  // PAST, PRESENT, FUTURE
        out attribute nextAction: HourglassAction;
        out attribute nextState: ExecutionState;
    }

    part def ThompsonSampling :> FlipAlgorithm {
        // Bayesian multi-armed bandit
    }

    part def MonteCarloTree :> FlipAlgorithm {
        // Tree search with rollouts
    }

    part def AStar :> FlipAlgorithm {
        // Goal-directed heuristic search
    }

    // Main orchestrator
    part def HourglassOrchestrator {
        part precedentHunter: PrecedentHunter;
        part swarmExecutor: SwarmExecutor;
        part simulationEngine: SimulationEngine;
        part validator: Validator;
        part flipAlgorithm: FlipAlgorithm;

        in attribute missionConfig: MissionConfig;
        out attribute artifact: ProbabilityDistribution;

        action flip(state: ExecutionState, horizon: String) : ExecutionState;
        action anytimeStop() : ProbabilityDistribution;
    }
}
```

---

## Next Steps for SysML v2 Implementation

1. **Define complete state space blocks** in `Obsidian_Hourglass_StateActionWeb.sysml`
2. **Model transition probabilities** as part/connector attributes
3. **Encode constraint boundaries** as requirement elements
4. **Define flip algorithm interfaces** with inputs/outputs
5. **Connect to PREY orchestrator** via composition relationships
6. **Map to OBSIDIAN roles** (Navigator, Observer, Shaper, etc.)
7. **Generate diagrams automatically** using updated `export_ssot_diagrams.py`

---

**Status**: Visual models complete. Ready for SysML v2 encoding and orchestrator implementation.
