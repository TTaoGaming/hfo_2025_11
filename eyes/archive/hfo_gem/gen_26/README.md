# Gen26 — SSOT + SysML v2 mirror (HFO)

This document is the single write-surface for the Gen26 system model of Hive Fleet Obsidian (HFO). It follows the constrained Markdown schema expected by `scripts/mbse/md_to_sysml.py` and is mirrored to a textual SysML v2 file under `sysml/hfo_gen26.sysml`.

Keep edits ≤200 lines per write; no placeholders; treat the SysML file as generated/read‑only once produced.

## MBSE Migration To‑Do & Question Backlog (Gen26)

Goal (confirmed): Establish ONE authoritative architecture source (SysML v2 mirror) eliminating drift; current Markdown is a transitional surface until we optionally flip to editing SysML directly.

Status Levels (scaling horizon):
- Level0 = 1 concurrent agent (canary / solo lane)
- Level1 = 10 concurrent agents (current stable target)
- Level2 = 100 concurrent agents (in progress / optimization needed)

Active To‑Dos (plain language)
1. List and freeze the names of the brain / facade pieces (control layer).
2. List and freeze the names of the worker / service pieces (doing the work).
3. Confirm where each kind of data actually lives (receipts, spans, knowledge, chat memory, mission intents) and if any need a new store.
4. Decide how scaling from 1→10→100 changes architecture (thread pool size only, or add message bus, queue, etc.).
5. Tag each block with status: active vs planned; and level relevance (L0/L1/L2).
6. Add relationships for control flow and data flow (keep them human readable first).
7. Generate first SysML text mirror and verify we can round‑trip without drift.
8. Add an automated check: regenerate diagrams + mirror and diff → no unexpected changes.

Question Sets (we advance a few each iteration)
- Set A (Core Blocks) — IN PROGRESS
- Set B (External Actors) — PENDING
- Set C (Critical Flows) — PENDING
- Set D (Constraints & Guardrails) — PENDING
- Set E (Viewpoints Priority) — PENDING
- Set F (Allocations & Code Paths) — PENDING
- Set G (Scaling Semantics L0/L1/L2) — PENDING
- Set H (States & Modes) — PENDING
- Set I (Performance & Capacity Targets) — PENDING
- Set J (Feature Flags & Evolution) — PENDING
- Set K (Validation & Drift Enforcement) — PENDING

Answered (foundation):
• Purpose: Single source of truth for architecture (not docs prose).
• Authoritative surface: SysML v2 mirror (Markdown transitional).
• Horizon: Multi‑level scaling (L0, L1, L2) captured directly in the model.

Next Plain‑Language Questions (please answer; short bullet answers fine):
Q1. Which components are the "brain" (the ones that coordinate others)? List their exact canonical names (e.g., SwarmlordFacade, CrewAIRunner, QuorumEngine). If a name here differs from the current list below, note the correction.
Q2. For each data type, confirm or adjust the storage path / mechanism:
	- Receipts (blackboard JSONL)
	- Telemetry spans
	- Knowledge vectors + provenance
	- Chat / conversational memory
	- Mission intents
	- Stigmergy signals
	- Digest / consensus artifacts
	If any needs a redesign (e.g., move stigmergy to a structured DB), call it out.
Q3. When scaling from 1 to 10 to 100 agents, what is the first architectural addition beyond just a larger thread pool (e.g., message bus activation, distributed queue, sharded knowledge queries, separate write‑ahead logging)? Provide the order you expect these to appear.

After your answers I'll: (a) freeze canonical block names, (b) add status + level tags, (c) produce the first SysML block skeleton, and (d) propose the next 3 questions.

---

Decision under consideration — Orchestration decomposition (choose one)
- O1 Orchestrated (simple conductor): ObsidianIntentGateway → OrchestratorService → LaneExecutionScheduler; QuorumConsensusEngine + DigestSynthesizer at end; PolicyEnforcementService at stage gates.
	• Pros: Lowest complexity, fast to stabilize for Level0/Level1; easy to reason about.
	• Cons: Tight coupling; scaling to Level2 (100 agents) may require later refactor to bus/Temporal.
	• Pick when: You want a clean baseline now and rapid iterative validation.
- O2 Event‑driven (message bus): Intent publishes to CommandBus (NATS); Lane workers consume; Orchestrator tracks saga; Quorum listens to lane.completed; Digest on quorum.pass.
	• Pros: Elasticity, natural backpressure, idempotency, replay; strong for Level2.
	• Cons: More infra and ops; higher cognitive load.
	• Pick when: You’re prioritizing 100‑lane reliability and elasticity soon.
- O3 Workflow‑centric (Temporal): Gateway starts workflow; PREY phases and Quorum/Digest are activities; Scheduler as child workflow; policies as interceptors.
	• Pros: Built‑in retries, visibility, failure semantics; fewer bespoke pipes.
	• Cons: New runtime to operate; SDK learning curve.
	• Pick when: You want reliability semantics now, with a paved path to Level2.

	### Orchestration layering (composition, not either/or)
	These options are not mutually exclusive. Treat them as layers that can be combined and enabled per level:

	- Process semantics (always on)
		- OrchestratorService defines the PREY flow and when to call Quorum/Digest/Policy. This is the “what.”
	- Execution drivers (choose one default; others can be added as adapters)
		- InProcessDriver (threads/pool) — simplest; great for Level0–Level1.
		- EventBusDriver (NATS) — queues, backpressure, idempotency; useful as Level2 fan‑out.
		- WorkflowDriver (Temporal) — durable retries/state/visibility; strong reliability for Level1→Level2.
	- Coordination/events (optional, additive)
		- Even with Temporal, NATS can carry domain events (lane.completed, quorum.pass) for decoupled consumers.

	Recommended staged composition
	- Level0 (single agent): OrchestratorService + InProcessDriver.
	- Level1 (≈10 agents): Same, plus optional NATS for long/slow tasks; begin emitting domain events.
	- Level2 (≈100 agents): Temporal as primary WorkflowDriver; NATS for high‑fan‑out signals; InProcessDriver remains for trivial/local steps.

	SysML representation (preview)
	- «block» OrchestratorService composes «interface» ExecutionDriver.
	- Realizations: InProcessDriver, EventBusDriver(NATS), WorkflowDriver(Temporal).
	- Level tags: {L0: InProcess}, {L1: InProcess [+EventBus optional]}, {L2: Workflow [+EventBus]}. Feature flags: HFO_ENABLE_TEMPORAL, HFO_ENABLE_NATS.


## Context
Hive Fleet Obsidian orchestrates multi‑agent AI swarms (Crew AI PREY lanes) with Temporal‑style activities, a durable knowledge base (PostgreSQL + pgvector), and an event spine (NATS JetStream). Operator input flows via a Telegram gateway to the Swarmlord facade. Safety and auditability are enforced with receipts (blackboard JSONL), parser‑safe diagrams, and a SysML v2 mirror. Observability uses OpenTelemetry; feature rollout via OpenFeature. Security posture includes SLSA provenance and an SBOM. FinOps tracks LLM token cost, storage, and messaging throughput.

## Blocks
Swarmlord, service, [facade, PREY]
CrewAI_Runner, worker, [parallel, PREY]
Telegram_Gateway, gateway, [chat]
Temporal_Workflow, orchestrator, [activities, retries]
Knowledge_Ingest, worker, [pgvector, provenance]
Knowledge_Query, worker, [hybrid, vector, bm25]
PostgreSQL_pgvector, datastore, [vector, sql]
NATS_JetStream, messaging, [events, durable]
OpenTelemetry_Collector, telemetry, [spans, otlp]
OpenFeature_Service, feature-flags, [flags]
FinOps_Meter, validator, [cost]
Security_Guard, validator, [slsa, sbom]
Blackboard, datastore, [receipts]
Diagrams_Generator, generator, [mermaid]
SysML_Generator, generator, [sysml]
Receipts_Validator, validator, [jsonl]
ARC_Swarm_Runner, worker, [benchmark]
OpenRouter_Client, client, [allowlist, reasoning]
OTEL_Traces, telemetry-store, [jsonl]

## Interfaces
Telegram_Gateway -> Swarmlord, human intents, Telegram Bot API
Swarmlord -> CrewAI_Runner, launch PREY lanes, Python API
Swarmlord -> Temporal_Workflow, start workflows, Python API
Temporal_Workflow -> Knowledge_Ingest, ingest_delta activity, Temporal gRPC
Temporal_Workflow -> Knowledge_Query, healthcheck/query activity, Temporal gRPC
CrewAI_Runner -> OpenRouter_Client, bounded LLM calls, HTTPS
CrewAI_Runner -> OTEL_Traces, emit engage_llm spans, file/jsonl
CrewAI_Runner -> Blackboard, append engage receipts, JSONL
Knowledge_Ingest -> PostgreSQL_pgvector, upsert vectors+meta, SQL
Knowledge_Query -> PostgreSQL_pgvector, hybrid retrieval, SQL
Swarmlord -> NATS_JetStream, publish agent events, NATS
Workers -> NATS_JetStream, consume events, NATS
All -> OpenTelemetry_Collector, OTLP spans export, OTLP
All -> OpenFeature_Service, fetch flags, HTTP
Generators -> SysML_Generator, produce mirror, CLI
Generators -> Diagrams_Generator, produce Mermaid, CLI
Security_Guard -> FinOps_Meter, attest + cost gate, Python API

## Relationships
Swarmlord uses CrewAI_Runner
Swarmlord uses Temporal_Workflow
Swarmlord uses OpenRouter_Client
Swarmlord writes Blackboard
CrewAI_Runner uses OpenRouter_Client
CrewAI_Runner writes OTEL_Traces
Knowledge_Ingest writes PostgreSQL_pgvector
Knowledge_Query reads PostgreSQL_pgvector
Temporal_Workflow uses Knowledge_Ingest
Temporal_Workflow uses Knowledge_Query
Swarmlord uses NATS_JetStream
Workers reads NATS_JetStream
OpenTelemetry_Collector reads OTEL_Traces
Receipts_Validator reads Blackboard
SysML_Generator reads Diagrams_Generator
Security_Guard uses FinOps_Meter

## Allocations
Swarmlord -> scripts/swarmlord/repo_consult.py
CrewAI_Runner -> scripts/crew_ai/runner_unified.py
ARC_Swarm_Runner -> scripts/crew_ai/arc_swarm_runner.py
Telegram_Gateway -> scripts/swarmlord_chat/telegram_swarmlord.py
OpenRouter_Client -> scripts/crew_ai/llm_client.py
Knowledge_Ingest -> scripts/knowledge/ingest_repo.py
Knowledge_Query -> scripts/knowledge/client.py
PostgreSQL_pgvector -> ops/vectordb/pgvector/docker-compose.yml
Blackboard -> hfo_blackboard/obsidian_synapse_blackboard.jsonl
OTEL_Traces -> temp/otel/
OpenTelemetry_Collector -> scripts/crew_ai/analyze_traces.py
OpenFeature_Service -> (env) OPENFEATURE_* / feature flags in mission intent
Temporal_Workflow -> scripts/orchestration/temporal_activities.py
NATS_JetStream -> (planned) ops/nats/
SysML_Generator -> scripts/mbse/md_to_sysml.py
Diagrams_Generator -> hfo_gem/gen_23/diagrams_swarmlord_of_webs_2025-11-05.md
Receipts_Validator -> scripts/ci/validate_blackboard.py
FinOps_Meter -> scripts/crew_ai/engage_costs.py
Security_Guard -> scripts/ci/generate_sbom.py

## Tags
ssot_version: gen26
allowlisted_models: openai/gpt-oss-120b, openai/gpt-oss-20b, x-ai/grok-4-fast, deepseek/deepseek-v3.2-exp, minimax/minimax-m2, qwen/qwen3-235b-a22b-2507
reasoning_default: high
chunk_limit_lines: 200
receipts_path: hfo_blackboard/obsidian_synapse_blackboard.jsonl
spans_path: temp/otel/
feature_flags: OPENROUTER_MAX_TOKENS, OPENROUTER_REASONING, HFO_KNOWLEDGE_USE_BM25, HFO_ENABLE_TEMPORAL
security: SLSA provenance, SBOM (CycloneDX)
finops: tokens_per_1k_usd=OPENROUTER_PRICE_DEFAULT_PER_1K, vector_dims=256, nats_streams=agent.events

## Provenance
- Based on Gen23 YAML model guidance and Gen25 MD→SysML pipeline (`scripts/mbse/md_to_sysml.py`).
- Paths verified from repo structure on 2025-11-07; some items are planned and marked accordingly (e.g., NATS ops path). Update these paths when the components land.
- This file is the single write-surface for Gen26; the SysML mirror is generated and read-only.

## Mirror generation (local)
- Generate SysML v2 mirror (textual):
	- `python3 scripts/mbse/md_to_sysml.py hfo_gem/gen_26/README.md > sysml/hfo_gen26.sysml`
- Treat `sysml/hfo_gen26.sysml` as read-only in source control; edit this SSOT file instead.
