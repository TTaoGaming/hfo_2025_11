# Swarmlord Contract (Gen24)

BLUF
- One facade to the human. Orchestrates hex squads of lanes running multi‑round PREY.
- Every artifact is LLM‑generated (Perceive/React/Engage/Yield). Signals go to the blackboard; spans to OTEL JSONL; quorum+ validates.
- Inputs: mission intent (YAML). Outputs: per‑lane artifacts, stigmergy, digest, quorum reports.

## Tiny contract (inputs/outputs)
- Inputs
  - mission.intent: YAML with mission_id, lanes/squads, llm, safety, telemetry, quorum, rounds_per_lane
  - source_documents: paths for RepoScanner to mine findings
- Outputs
  - Per‑lane artifacts (attempt_1/): perception_snapshot.yml, react_plan.yml, engage_report.yml, yield_summary.yml, lane_findings.jsonl
  - Run‑level: mission_pointer.yml, swarmlord_digest.md, quorum_plus_report.yml, RESCUE_INDEX.jsonl, RESCUED_SUMMARY.md
  - Telemetry: temp/otel/trace-<mission_id>-<ts>.jsonl
  - Blackboard receipts: hfo_blackboard/obsidian_synapse_blackboard.jsonl

Success criteria
- Artifacts present per lane (4+1). Enhanced quorum PASS. Digest produced. No placeholders. Chunk limit respected.

## PREY responsibilities (per lane, per round)
- Perceive
  - Create perception_snapshot.yml (LLM). Include mission_id, lane, trace_id, safety, llm config, paths.
- React
  - Create react_plan.yml (LLM). Include cynefin, approach.loop, chunk_limit_lines, tripwires, quorum.
- Engage
  - Create engage_report.yml (LLM). Include actions, bounded tokens, content_preview, latency/status if available.
  - Write lane_findings.jsonl (machine). Extract {source_path, title, snippet} from mission source_documents.
- Yield
  - Create yield_summary.yml (LLM). Include collected_agents, evidence_refs (must reference the three core artifacts).

## Receipts (blackboard JSONL)
Required fields per material action
- mission_id, phase (perceive|react|engage|yield|verify|audit), summary
- evidence_refs (paths, line ranges, or trace IDs)
- timestamp (ISO Z)
- safety_envelope (chunk_size_max, placeholder_ban) when writing files

Policy
- Append‑only; never rewrite. ≤200 lines per write; no placeholders.

## Telemetry (spans JSONL)
- Span fields: trace_id, span_id, name, start_time, end_time, attributes{ lane, phase, role?, ok?, llm_used?, model, latency_ms }
- Required spans: per PREY phase; per role sub‑span; engage_llm span if LLM used.

## Stigmergy (virtual)
- Per‑lane signals: lane_findings.jsonl produced during Engage.
- Run‑level harvest: RESCUE_INDEX.jsonl + RESCUED_SUMMARY.md.
- DuckDB mirror: maintain views to compute consensus, overlap, drift; feed digest.

## Quorum+
- Artifact completeness: 4 core artifacts per lane.
- Coverage: ≥ X% lanes with non‑empty content_preview (configurable; default 0.3).
- Cross‑evidence: references to ≥ M distinct mission source_documents (default 2).
- Report: quorum_plus_report.yml. Digest surfaces PASS/FAIL and key metrics.

## IDs & structure
- trace_id = "trace-<mission_id>-<ts>"
- Run directory = hfo_crew_ai_swarm_results/YYYY‑MM‑DD/run‑<ts>/
- Lane directory = run‑<ts>/lane_<n>/attempt_1..attempt_N/ (compact rounds)

Defaults (pilot)
- rounds_per_lane: 3 (configurable via mission.lanes.rounds or rounds_per_lane)
- post_run: seed stigmergy → run quorum_plus → harvest rescue; digest appends summary and pointers

## Safety envelope
- Canary first; measurable tripwires; explicit revert.
- Chunk size ≤ 200 lines per file write; placeholder ban enforced.

## LLM budget and controls
- Mission llm: { max_tokens, temperature, timeout_seconds, response_format_type, reasoning, reasoning_effort }
- Env overrides supported.
- Reasoning high where beneficial; retry drops response_format on provider incompatibility.

## Rounds (iteration)
- lanes.rounds_per_lane: integer ≥ 1.
- For r in 1..R: run PREY; Perceive includes prior_evidence_refs from the previous Yield.
- Validate each attempt; latest attempt status informs Verify.
- lane_findings.jsonl is written per attempt by RepoScanner (or populated post‑run).

## How to run (ops)
```bash
# pipeline (preferred)
./.venv/bin/python scripts/crew_ai/run_arch_consensus_pipeline.py \
  --intent hfo_mission_intent/_tmp/mission_intent_arch_consensus_100lanes_2025-11-05.v1.yml

# or direct (runner includes post-steps)
./.venv/bin/python scripts/crew_ai/runner.py \
  --intent hfo_mission_intent/_tmp/mission_intent_arch_consensus_100lanes_2025-11-05.v1.yml
```

## Verify checklist (handoff)
- Per lane latest attempt: 4 core artifacts + lane_findings.jsonl
- Run-level: quorum_plus_report.yml PASS; RESCUE_INDEX.jsonl + RESCUED_SUMMARY.md; digest includes Quorum+ summary
- Spans present; receipts appended with evidence_refs

## Error modes & handling
- Missing artifact → lane FAIL → quorum likely FAIL.
- Empty LLM content → record error; preview may be null; proceed with signals.
- Span/receipt write fails → log regen_flag=true and continue with reduced scope.

## Acceptance (contract implementation)
- Runner writes per‑lane artifacts, receipts, and spans for each PREY phase.
- RepoScannerAgent implemented for findings; harvester and quorum_plus run post‑yield.
- Digest includes: lanes×models, Verify result, quorum+ summary, top rescued sources, trace link.
