---
hexagon:
  ontos:
    id: a8d52e43-c5a2-4137-844b-88c4acaabb74
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.938508Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_26/gap_analysis_2025-11-07.md
    links: []
  telos:
    viral_factor: 0.0
    meme: gap_analysis_2025-11-07.md
---

# Gen26 — System Gap Analysis (2025-11-07T00:00:00Z)

BLUF
- You have working proofs (Crew AI lanes, knowledge module code, receipts, spans), and a fresh SSOT + SysML mirror. The vector DB isn’t running, NATS isn’t provisioned, and SBOM/SLSA are not wired. Temporal is scaffolded but not executing as a worker. This doc lists current state, evidence, and an actionable path to close gaps.

## Snapshot (2025-11-07)
- SSOT + SysML (Gen26)
  - Present: `hfo_gem/gen_26/README.md` (authoritative) → `sysml/hfo_gen26.sysml` (generated)
  - Diagram: `diagrams/gen26_context.md`
  - Official validation: MISSING — Java 17 is available but `SYSML_V2_PILOT_JAR` not set; current validation task exits 2. Action: download official SysML v2 Pilot JAR, export `SYSML_V2_PILOT_JAR`, rerun task for PASS/FAIL.
- Crew AI (parallel AI lanes)
  - Present: `scripts/crew_ai/runner_unified.py`, results under `hfo_crew_ai_swarm_results/` (2025-10-30…2025-11-07)
  - Observability: `scripts/crew_ai/analyze_traces.py` and spans at `temp/otel/trace-*.jsonl`
- Knowledge Base (pgvector)
  - Code present: `scripts/knowledge/{ingest_repo.py, client.py, healthcheck.py, query_cli.py}`
  - Healthcheck result: FAIL (Postgres not ready)
    - Command: `python3 scripts/knowledge/healthcheck_cli.py`
    - Output: `{ "status": "FAIL", "pg_isready": false, "row_count": 0, "vector_column_dims": 256 }`
  - Compose present: `ops/vectordb/pgvector/docker-compose.yml` (container likely not running)
- Temporal orchestration
  - Scaffold: `scripts/orchestration/temporal_activities.py` (stub activities + spans)
  - Worker/workflow not wired; no dependency in `requirements.txt` yet
- NATS JetStream (agent bus)
  - Not provisioned (`ops/nats/` missing); no `nats-py` dependency yet; stubs in activities
- OpenRouter (LLM)
  - Code path: `scripts/crew_ai/llm_client.py` (allowlist, reasoning controls). `.env` expected (not verified here)
- OpenTelemetry
  - Spans present: `temp/otel/trace-*.jsonl`; analyzers present
- OpenFeature
  - Mentioned/assumed via env flags; no central feature-service client yet
- FinOps
  - No `engage_costs.py` in repo; costs partly inferred from env; needs a minimal meter
- Security (SLSA + SBOM)
  - No SBOM generator script yet; no SLSA provenance emission

## Evidence refs
- SSOT: `hfo_gem/gen_26/README.md`, `sysml/hfo_gen26.sysml`, `diagrams/gen26_context.md`
- Official validation scaffold: `scripts/mbse/validate_sysml_official.sh`, `reports/sysml_v2_audit_2025-11-08.md`
- Crew AI: `scripts/crew_ai/runner_unified.py`, `hfo_crew_ai_swarm_results/2025-11-07/`
- Knowledge: `scripts/knowledge/`, `ops/vectordb/pgvector/docker-compose.yml`, `scripts/knowledge/healthcheck_cli.py`
- Temporal: `scripts/orchestration/temporal_activities.py`
- Receipts: `hfo_blackboard/obsidian_synapse_blackboard.jsonl`

## Gap matrix (required → status)
- SysML v2 official validator PASS → MISSING (no Pilot JAR wired)
- pgvector up and reachable → FAIL (service not running; healthcheck FAIL)
- NATS JetStream bus → MISSING (no ops manifests; no client dep)
- Temporal worker (feature-flagged) → PARTIAL (scaffold only; no worker)
- SBOM + SLSA provenance → MISSING
- FinOps meter → MISSING (no dedicated module)
- Central feature flags → PARTIAL (env-only)
- GitOps guardrails → PARTIAL (receipts and spans good; add CI for healthcheck + SBOM)

## Actions (2-step canary, ≤200 lines per change)
0) SysML v2 official validation
  - Download official SysML v2 Pilot Implementation JAR.
  - Export: `export SYSML_V2_PILOT_JAR=/abs/path/sysml-v2-pilot-<ver>.jar`
  - Run validation task; expect `temp/mbse/sysml_validation_report.txt` from official CLI (replace heuristic checks).
1) Bring pgvector online and verify
   - Start service (compose):
     - `docker compose -f ops/vectordb/pgvector/docker-compose.yml up -d`
   - Export env (defaults align with compose):
     - `export PGHOST=localhost PGPORT=5432 PGDATABASE=postgres PGUSER=postgres PGPASSWORD=postgres`
   - Healthcheck: `python3 scripts/knowledge/healthcheck_cli.py` → expect PASS
   - Ingest (delta-aware):
     - `python3 scripts/knowledge/ingest_repo.py --root hfo_gem --glob "**/*.{md,markdown,txt,yml,yaml,py,json}"`
   - Query smoke: `python3 scripts/knowledge/query_cli.py --q "hybrid retrieval" --path-prefix hfo_gem/`
2) Minimal platform wiring
   - NATS: add `nats-py` to requirements and an `ops/nats/docker-compose.yml` with a JetStream-enabled NATS; implement `send_nats_event` using async client
   - Temporal: add `temporalio` to requirements and a tiny worker file guarded by `HFO_ENABLE_TEMPORAL`
   - SBOM: add `cyclonedx-bom` or `cyclonedx-python-lib`, script to emit SBOM JSON; append a verify receipt
   - FinOps: add `scripts/crew_ai/finops_meter.py` to estimate token spend, storage, and stream costs; surface in digest

## Risks & mitigations
- DB not running → containerized pgvector with healthcheck CLI ensures readiness
- Token cost drift → FinOps meter in digest and receipts
- Transport flakiness (LLM) → retry-on-empty already present; keep bounded
- Event bus drift → start with a single durable stream `agent.events`, consumers per worker group

## Acceptance for closure (Gen26 canary)
- Healthcheck PASS with `extensions:[vector]` and row_count > 0
- Ingest completed (added/changed/removed counts in span) and hybrid query returns results
- NATS compose runs; `send_nats_event` returns ACK (or file-backed stub replaced)
- SBOM file present under `reports/` with CycloneDX JSON
- Feature flag: `HFO_ENABLE_TEMPORAL=1` starts minimal worker and runs `ingest_delta` + `healthcheck_vector_db`
