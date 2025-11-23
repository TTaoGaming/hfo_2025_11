---
hexagon:
  ontos:
    id: ff7ab93b-2e59-468f-bde5-67dae051c7bb
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.888305Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_23/research_swarmlord_of_webs_T-gamma_hex_ssot_2025-11-05.md
    links: []
  telos:
    viral_factor: 0.0
    meme: research_swarmlord_of_webs_T-gamma_hex_ssot_2025-11-05.md
---
# Research — Swarmlord of Webs (Gen23 SSOT, T‑Gamma Hex) — 2025‑11‑05

BLUF
- The Swarmlord of Webs is your always‑on alter ego (navigator), running 24/7 with durable state and memory. You speak only to Swarmlord; it orchestrates squads and swarms.
- Hard gate: Mission Intent is created only after ≥3 separate Clarification Passes for the same timeframe. One active Mission Intent per timeframe (hour/day/week/month/year/decade); extras are archived.
- Hexagonal, vendor‑neutral SSOT: Temporal is used now for always‑on workflows, but the model treats the scheduler as an abstract hex‑port (swappable). Obsidian Horizon Hourglass is a first‑class tool the Swarmlord may use anytime to explore near/next/later futures.

What this page is
- A research specification for the T‑Gamma variant: hexagonal architecture + MBSE single source of truth.
- It explains responsibilities, guardrails, and artifacts in plain language and includes a YAML SSOT slice preview. Diagrams and SysML v2 will be generated from the YAML model (not hand‑drawn here).

## Core responsibilities (plain language)
- Always‑on navigator
  - Run continuously; maintain durable state (recent chats, receipts, run pointers, stigmergy signals, active timeframes).
  - Receive signals (chat/Telegram) and CP files; do not create a Mission Intent until ≥3 Clarification Passes exist for that timeframe.
- Mission Intent governance
  - Exactly one active Mission Intent per timeframe bucket (hour/day/week/month/year/decade). New intents for the same timeframe archive the prior one or are rejected while the current is active.
- Orchestrate squads and lanes
  - Group work by topic (hex‑cell) and time horizon (near/next/later). Squads contain multiple PREY lanes (Crew roles: Observer→Bridger→Shaper→Assimilator). Post‑lane: Immunizer/Disruptor validators feed Quorum.
- Hourglass tool
  - Use the Obsidian Horizon Hourglass to propose scenarios and explore futures across horizons. Not mandatory; used when it increases confidence.
- Evidence and digest
  - Append receipts to the blackboard JSONL for every material action. After Verify/Quorum PASS, produce a single Swarmlord Digest and notify the operator.

## Hard guardrails (enforced)
- CP≥3 gate: No Mission Intent unless ≥3 dated Clarification Pass docs exist for the same timeframe. Violations are archived with a hallucination flag.
- Single active Mission Intent per timeframe: hour/day/week/month/year/decade. All others go to archive; no concurrency within the same bucket.
- Safety envelope: ≤200 lines per write; no placeholders; receipts must include evidence paths and timestamps.
- Model allowlist + bounded tokens; reasoning flags per policy; retries on empty when applicable.
- Verify/Quorum is independent. No “done” claims before PASS.

## Hexagonal (ports/adapters) — vendor neutral
- Ports (hex‑edges)
  - consult_api (chat/Telegram), cp_gate, scenarios (Hourglass), run_queue (scheduler), run_state_events, blackboard_io, artifacts_io.
- Adapters (today)
  - Temporal for always‑on Swarmlord workflow and durable signals/state; local file/JSONL stores for blackboard and chat mirrors; Crew AI runners for lanes and validators.
- Swap‑ability
  - The model binds to abstract ports; implementations (Temporal/Prefect/other) can change without altering the model.

## Timeframes and intent lifecycle
- Buckets: hour, day, week, month, year, decade (extendable).
- Lifecycle per bucket
  1) Collect CP1..CPn (≥3 required) → gate opens.
  2) Create Mission Intent (becomes the single active Intent for the bucket).
  3) Run squads/lanes under safety; append receipts and spans.
  4) Verify/Quorum → PASS → compile digest; else remediate and repeat.
  5) On new intent for the same bucket, archive previous; maintain clean lineage (no duplicates active).

## SSOT YAML slice (T‑Gamma preview; not persisted)
```yaml
model:
  id: hfo.gen23
  name: Hive Fleet Obsidian
  version: 0.1.0
  doctrine_tags: [PREY, CP>=3, HOURGLASS, TEMPORAL, HEXAGONAL, SINGLE_INTENT_PER_TIMEFRAME]
  provenance:
    sources: [AGENTS.md, hfo_gem/gen_23/HFOMBSE_Gen23_Roadmap_2025-11-05T00:00:00Z.md]

blocks:
  - id: swarmlord
    title: Swarmlord of Webs (Always‑On)
    kind: service
    tags: [alter_ego, navigator, always_on]
    provides: [consult_api, squad_allocation, orchestration_api]
    consumes: [cp_gate, mission_intent, blackboard_jsonl, stigmergy_field, state_store]

  - id: scheduler
    title: Orchestration Engine (abstract)
    kind: infra
    tags: [temporal_now, pluggable_later]
    provides: [run_queue, run_state_events]
    consumes: [scenarios]

  - id: hourglass
    title: Obsidian Horizon Hourglass
    kind: planner
    provides: [scenarios]
    consumes: [mission_intent, stigmergy_field, prior_runs]

  - id: squad_manager
    title: Squad Manager
    kind: controller
    provides: [squad_plan]
    consumes: [stigmergy_field, scenarios, mission_intent]

  - id: squad
    title: Holonic Squad (hex_cell × horizon)
    kind: composite
    tags: [hex_cell, horizon]
    provides: [squad_artifacts]
    consumes: [mission_intent]
    parts:
      - id: laneN
        ref: prey_lane
        multiplicity: "N>=1"

  - id: prey_lane
    title: PREY Lane (Crew roles)
    kind: worker
    tags: [Observer,Bridger,Shaper,Assimilator]
    provides: [lane_artifacts]
    consumes: [mission_intent]

  - id: quorum
    title: Verify Quorum
    kind: validator
    provides: [quorum_report]
    consumes: [lane_artifacts]

  - id: digest
    title: Swarmlord Digest Compiler
    kind: reporter
    provides: [operator_digest]
    consumes: [quorum_report, lane_artifacts, spans]

  - id: blackboard
    title: Blackboard (JSONL)
    kind: datastore
    paths: [hfo_blackboard/obsidian_synapse_blackboard.jsonl]
    provides: [blackboard_jsonl]

  - id: clarification_manager
    title: Clarification Gate (≥3)
    kind: policy
    provides: [cp_gate]

  - id: state_store
    title: Durable State Store
    kind: datastore
    provides: [state_store]

interfaces:
  - id: consult_api        ; from: chat_gateway ; to: swarmlord
  - id: cp_gate            ; from: clarification_manager ; to: swarmlord
  - id: horizon_planning   ; from: swarmlord ; to: hourglass
  - id: enqueue_runs       ; from: swarmlord ; to: scheduler
  - id: dispatch_to_lanes  ; from: scheduler ; to: prey_lane
  - id: allocate_squads    ; from: swarmlord ; to: squad_manager
  - id: spawn_squad        ; from: squad_manager ; to: squad
  - id: squad_to_quorum    ; from: squad ; to: quorum
  - id: digest_out         ; from: digest ; to: chat_gateway

relationships:
  - type: composes ; from: squad ; to: prey_lane
  - type: writes   ; from: swarmlord ; to: blackboard
  - type: reads    ; from: swarmlord ; to: state_store
  - type: reads    ; from: swarmlord ; to: run_state_events

allocations:
  - block: prey_lane      ; paths: [scripts/crew_ai/runner_unified.py, scripts/crew_ai/analyze_traces.py]
  - block: quorum         ; paths: [scripts/crew_ai/validate_run.py]
  - block: digest         ; paths: [scripts/crew_ai/build_research_digest.py]
  - block: chat_gateway   ; paths: [scripts/swarmlord/telegram_bot.py, scripts/swarmlord/repo_consult.py]
  - block: state_store    ; paths: [swarmlord_chat/chat.jsonl, SWARMLORD_CHATLOG.md]
  # scheduler is abstract; Temporal is the current adapter; swapping requires no model change
```

## Acceptance (what “working” looks like)
- CP≥3 enforced per timeframe (hour/day/week/…): only then a Mission Intent is created; no duplicates active in the same bucket.
- Receipts appended for clarify→intent→plan→execute→verify→digest; no placeholders; ≤200 lines per write.
- Lanes and squads tagged with {hex_cell, horizon}; spans show parallelism; Quorum PASS recorded; single digest produced and sent to you.
- Hourglass scenarios visible in receipts/digest when used; okay to skip when not needed.

## Next steps (low risk)
- Confirm T‑Gamma as the SSOT direction.
- I’ll mirror this slice into `models/hfo.yml` (≤200 lines), then we’ll generate the diagrams and a SysML v2 mirror.
- Implement the timeframe gate in the runner (reject or archive duplicate intents); keep Swarmlord always‑on via the Temporal (or abstract) adapter.
