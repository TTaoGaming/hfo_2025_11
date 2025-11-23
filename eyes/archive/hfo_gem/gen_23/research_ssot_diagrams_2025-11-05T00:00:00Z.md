---
hexagon:
  ontos:
    id: 9098a047-9bfc-4b33-b1f9-9a3e23721fbb
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.886778Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md
    links: []
  telos:
    viral_factor: 0.0
    meme: research_ssot_diagrams_2025-11-05T00:00:00Z.md
---
# Hive Fleet Obsidian — Gen23 SSOT Diagrams (single source of truth)

Date: 2025-11-05 (UTC)
Branch: feat/telegram-topic-research-digest

BLUF
- This file consolidates the architecture and workflow diagrams across gens 1–22 (favoring Gen21–Gen22) into one parser-safe source you can build from as code.
- Control path is invariant: Mission intent → Orchestrate → PREY lanes → Quorum Verify → Digest. Evidence is chained and observable.

References (upstream SSOTs)
- gen_22: `hfo_gem/gen_22/crew_ai_swarm_ssot_gen22.md`
- gen_21: `hfo_gem/gen_21/gpt5-attempt-3-gem.md`, `hfo_gem/gen_21/crew_ai_swarm_pilot_2025-10-30.md`
- repo SSOT: `AGENTS.md`

Notes
- Diagrams follow Mermaid parser-safe conventions (graph LR/TB; simple labels; one arrow per line).
- Names align with Gen21/22: HIVE/GROWTH/SWARM/PREY labels persist; “Swarmlord” is the sole operator facade.

---

## Diagram A — End-to-end orchestration
```mermaid
graph LR
  OP[Operator] --> SW[Swarmlord]
  SW --> MI[Mission intent]
  SW --> LN[Parallel lanes]
  LN --> YD[Yields]
  YD --> VQ[Verify quorum]
  VQ --> PASS[Pass]
  VQ --> FAIL[Fail]
  PASS --> DG[Digest]
  FAIL --> RR[Targeted re run]
  RR --> LN
  DG --> OP
```

Key points
- Single facade (Swarmlord) runs PREY across lanes, then Verify gates Digest.
- Retry is targeted and scoped; success requires quorum PASS.

---

## Diagram B — Lane lifecycle (Orchestrate + PREY + Verify)
```mermaid
graph TB
  O[Orchestrate] --> P[Perceive]
  P --> R[React]
  R --> E[Engage]
  E --> Y[Yield]
  Y --> V[Verify deterministic]
  V --> VPASS[Pass]
  V --> VFAIL[Fail]
  VFAIL --> R
  VPASS --> DONE[Lane done]
```

Key points
- LLM may be used at each phase (per Gen22 defaults: max_tokens≈1000; reasoning=high where supported).
- Failure loops back to React with a smaller chunk and tighter tripwires.

---

## Diagram C — Evidence chain and observability (per lane)
```mermaid
graph LR
  PS[perception_snapshot.yml] --> RP[react_plan.yml]
  RP --> ER[engage_report.yml]
  ER --> YS[yield_summary.yml]
  PS -.-> H1[sha256 parent]
  RP -.-> H2[sha256 parent]
  ER -.-> H3[sha256 parent]
  YS -.-> BB[Blackboard jsonl]
  ER -.-> SP[Spans jsonl]
```

Key points
- Each artifact includes trace_id, parent_refs, evidence_hashes, and context_notes (≥3 lines).
- Blackboard is append-only; spans live under `temp/otel/`.

---

## Diagram D — Lanes per model and concurrency
```mermaid
graph TB
  MI[Mission intent] --> SEL[Model selection]
  SEL --> L1[Lane 1]
  SEL --> L2[Lane 2]
  SEL --> L3[Lane 3]
  L1 --> Y1[Yield]
  L2 --> Y2[Yield]
  L3 --> Y3[Yield]
  Y1 --> VQ[Quorum]
  Y2 --> VQ
  Y3 --> VQ
```

Key points
- One lane per allowlisted model (or filtered set) is supported; env and mission can bias selection.
- Parallelism is validated by engage_llm span overlap (analyzer: “Parallel detected: True”).

---

## Diagram E — Telegram consult to digest (authoritative path)
```mermaid
graph TB
  TG[Telegram message obsidian …] --> BOT[Telegram bot]
  BOT --> SW[Swarmlord]
  SW --> RC[Repo consult]
  RC --> MI[Ephemeral mission or task]
  MI --> LN[PREY lanes]
  LN --> VQ[Verify quorum]
  VQ --> DG[Digest]
  DG --> TG_REPLY[Reply with link and BLUF]
```

Key points
- Bot is authoritative; watcher does not mirror when bot is active.
- One ack, then one digest reply with BLUF and next steps.

---

## Diagram F — HIVE → GROWTH → SWARM → PREY (label map)
```mermaid
graph LR
  H[HIVE] --> G[GROWTH]
  G --> S[SWARM]
  S --> P[PREY]
  P --> V[Verify]
  V --> D[Digest]
```

Key points
- Use these exact labels in code, docs, and receipts to stay aligned with Gen21/22.

---

## Minimal acceptance checklist (for builds from these diagrams)
- Mission intent loads; lanes planned; PREY runs; quorum PASS recorded; digest present.
- Per-lane artifacts exist and chain via parent hashes; blackboard receipts appended; spans present.
- Parser-safe diagrams render; no placeholders; ≤200 lines per write respected.

---

Provenance
- Consolidated from gens 1–22 with emphasis on Gen21–Gen22 diagrams and contracts.
- This file is normative for Gen23; refactor code to conform to these flows.
