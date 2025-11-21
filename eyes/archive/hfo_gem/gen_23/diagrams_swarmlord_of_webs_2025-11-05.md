# Diagrams — Swarmlord of Webs (Gen23, T‑Gamma) — 2025‑11‑05

Note
- Research views for confirmation. SSOT remains the YAML model. Labels use plain language; diagrams are parser‑friendly.
- Assumptions: CP≥3 gate, one active Mission Intent per timeframe, squads (topic × horizon), Hourglass tool, Verify/Quorum, single Digest.

## 1) Context view (C4‑style)

```mermaid
graph LR
  OP[Operator] --> CG[Chat Gateway]
  CG --> SL[Swarmlord always on]
  SL --> HG[Hourglass]
  SL --> ST[State Store]
  SL --> SCH[Scheduler abstract]
  SL --> BB[Blackboard JSONL]
  SCH --> SQ[Squads]
  SQ --> PL[PREY Lanes]
  PL --> QV[Quorum]
  QV --> DG[Digest]
  DG --> OP
```

## 2) Swimlane flow (actors across steps)

```mermaid
graph TB
  subgraph Operator
    O1[Send chat]
    O2[Receive digest]
  end

  subgraph Swarmlord
    S1[Perceive]
    S2[Clarify Pass]
    S3[Gate CP>=3]
    S4[Create Mission Intent]
    S5[Plan Scenarios]
    S6[Allocate Squads]
    S7[Append Receipts]
  end

  subgraph Hourglass
    H1[Near]
    H2[Next]
    H3[Later]
  end

  subgraph Scheduler
    R1[Enqueue Runs]
    R2[Dispatch Lanes]
  end

  subgraph Squad
    Q1[Run Lanes]
    Q2[Collect Artifacts]
  end

  subgraph Quorum
    V1[Validate]
    V2[PASS]
    V3[FAIL]
  end

  O1 --> S1
  S1 --> S2
  S2 --> S3
  S3 --> OK
  OK --> S4
  S4 --> S5
  S5 --> H1
  S5 --> H2
  S5 --> H3
  S5 --> S6
  S6 --> R1
  R1 --> R2
  R2 --> Q1
  Q1 --> Q2
  Q2 --> V1
  V1 --> V2
  V1 --> V3
  V2 --> S7
  S7 --> O2
  V3 --> S5
```

## 3) Swarmlord state life‑cycle (graph fallback)

```mermaid
graph LR
  A[Always On] --> B[Clarify]
  B --> B
  B --> C[Gate CP>=3]
  C --> D[Plan]
  D --> E[Orchestrate]
  E --> F[Verify]
  F --> G[PASS]
  F --> H[FAIL]
  G --> I[Digest]
  I --> A
  H --> D
```

## 4) Timeframe gate (single active intent per bucket)

```mermaid
graph TB
  subgraph Hour
    HCP1[CP1] --> HGH[Gate]
    HCP2[CP2] --> HGH
    HCP3[CP3] --> HGH
    HGH --> HMI[Mission Intent Active]
    HMI --> HAR[Archive]
  end

  subgraph Day
    DCP1[CP1] --> DGH[Gate]
    DCP2[CP2] --> DGH
    DCP3[CP3] --> DGH
    DGH --> DMI[Mission Intent Active]
    DMI --> DAR[Archive]
  end

  subgraph Week
    WCP1[CP1] --> WGH[Gate]
    WCP2[CP2] --> WGH
    WCP3[CP3] --> WGH
    WGH --> WMI[Mission Intent Active]
    WMI --> WAR[Archive]
  end
```

## 5) Feedback mesh (memory, stigmergy, scenarios, results)

```mermaid
graph LR
  MEM[State Store] --> SL[Swarmlord]
  BB[Blackboard] --> SL
  STIG[Stigmergy] --> SL
  SL --> HG[Hourglass]
  HG --> SCN[Scenarios]
  SCN --> SQ[Squads]
  SQ --> LANES[PREY Lanes]
  LANES --> ART[Artifacts]
  ART --> QV[Quorum]
  QV --> PASS
  QV --> FAIL
  PASS --> DG[Digest]
  DG --> OP[Operator]
  ART --> MEM
  PASS --> MEM
  FAIL --> MEM
  STIG --> HG
  DG --> STIG
```

## 6) Artifact and evidence flow

```mermaid
graph LR
  MI[Mission Intent] --> PERC[Perception Snapshot]
  MI --> REACT[React Plan]
  MI --> ENG[Engage Report]
  MI --> YIELD[Yield Summary]
  PERC --> QV[Quorum]
  REACT --> QV
  ENG --> QV
  YIELD --> QV
  QV --> DG[Digest]
  DG --> BB[Blackboard]
  PERC --> BB
  REACT --> BB
  ENG --> BB
  YIELD --> BB
```

Acceptance
- Diagrams render; labels match: CP>=3 gate, single intent per timeframe, squads (topic × horizon), Hourglass, Quorum, Digest, blackboard receipts.
- If you want these committed as generated views later, we will mirror from the YAML SSOT rather than maintain them by hand.
