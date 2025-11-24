---
hexagon:
  ontos:
    id: 492a35af-fbd9-467c-8d95-386c79c52a2a
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.929682Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_26/AGENTS.gen26.md
    links: []
  telos:
    viral_factor: 0.0
    meme: AGENTS.gen26.md
---

# AGENTS — Gen26 (concise, AI-optimized)

This is the Gen26 agent operating guide. It’s compact, parser‑safe, and optimized for LLM/agent consumption. Use this during consults and orchestration; the older root `AGENTS.md` is archived under gen_26.

## BLUF
- Speak through the Swarmlord facade only (never ping the human mid‑loop).
- Follow PREY (Perceive → React → Engage → Yield) and pass Verify/quorum before persisting.
- Enforce safety: ≤200 lines per write, canary first, measurable tripwires, explicit revert, placeholder ban.
- Append receipts to `hfo_blackboard/obsidian_synapse_blackboard.jsonl` for every material action.

## Tiny contract (for any agent)
- Inputs: mission_intent (UTC Z), repo paths, blackboard path, safety plan.
- Outputs: artifacts (code/docs/reports), receipts, spans, digest pointers.
- Success: tripwires ok; Verify PASS; receipts have evidence_refs; constraints honored.

## Roles and loop
- Roles: Observer (Perceive), Bridger (React), Shaper (Engage), Assimilator (Yield); post‑lane: Immunizer + Disruptor (quorum).
- Loop (PREY):
  - Perceive: snapshot targets, safety; record `perception_snapshot.yml`.
  - React: plan, tripwires, stigmergy_readiness; write `react_plan.yml`.
  - Engage: do bounded work; write `engage_report.yml`; log LLM spans/metadata.
  - Yield: synthesize + bundle; write `yield_summary.yml`; request Verify.

## Safety envelope (operational)
- Chunking: ≤200 lines/write; avoid placeholders (“TODO”, “…”, “omitted”).
- Canary/tripwires: start small; gate on tests, placeholder scan, and receipt completeness.
- Revert: restore last good; shrink scope; repeat.

## Receipts (append‑only JSONL)
- Path: `hfo_blackboard/obsidian_synapse_blackboard.jsonl`
- Required fields: mission_id, phase, summary.
- Recommended: evidence_refs (paths[:line‑range]), timestamp (ISO Z), safety_envelope, blocked_capabilities.
- Use helper: `scripts/blackboard_logger.py`.

## Artifacts and spans
- Per lane (attempt_k): `perception_snapshot.yml`, `react_plan.yml`, `engage_report.yml`, `yield_summary.yml` under `hfo_crew_ai_swarm_results/YYYY-MM-DD/run-<ts>/<lane>/attempt_k/`.
- Spans (OTEL‑like JSONL): `temp/otel/trace-*.jsonl`; analyze via `scripts/crew_ai/analyze_traces.py`.
- Digest (run level): `swarmlord_digest.md` with BLUF, Matrix, diagram, Verify.

## LLM policy
- Allowlist enforced: openai/gpt-oss-120b, openai/gpt-oss-20b, x‑ai/grok‑4‑fast, deepseek/deepseek‑v3.2‑exp, minimax/minimax‑m2, qwen/qwen3‑235b‑a22b‑2507.
- Reasoning: auto‑enabled (high effort) when supported; on provider rejection, retry once without reasoning.
- Budgets: favor 400–1000 tokens for Engage on OSS models to reduce empties.

## Telegram facade (Swarmlord)
- Triggers: start‑of‑line `obsidian …` (case‑insensitive). One ack + one summary reply with a consult link.
- Paths: bot in `scripts/swarmlord/telegram_bot.py` (PTB optional). Memory mirrors: `swarmlord_chat/chat.jsonl` and `swarmlord_chat/swarmlord.duckdb`.
- Guards: authoritative mode; message‑id idempotency; dedupe and heartbeat in watcher.

## Knowledge layer (Gen25)
- Ingest: `scripts/knowledge/ingest_repo.py` (delta‑aware, provenance).
- Query: `scripts/knowledge/query_cli.py` (hybrid vector+text; BM25 flaggable).
- Healthcheck: `scripts/knowledge/healthcheck_cli.py` (emits PASS receipt).

## SSOT and SysML mirror (Gen26)
- SSOT (this repo): `hfo_gem/gen_26/README.md` — authoritative blocks, interfaces, allocations.
- Mirror: `python3 scripts/mbse/md_to_sysml.py hfo_gem/gen_26/README.md > sysml/hfo_gen26.sysml` (read‑only).

## Verify gate (independent)
- Lane validator ensures the four artifacts exist; quorum report records votes and threshold.
- PASS gates digest + receipts; FAIL → shrink, regen, repeat.

## Quickstarts
- Run unified PREY: `python3 scripts/crew_ai/runner_unified.py --intent <path>`
- Validate parallelism: `python3 scripts/crew_ai/analyze_traces.py temp/otel/<trace>.jsonl`
- Append receipt: `python3 scripts/blackboard_logger.py --mission-id <id> --phase engage --summary "..."`

## Glossary
- PREY: Perceive/React/Engage/Yield • Quorum: independent verify • Blackboard: append‑only receipts • Stigmergy: virtual signals with TTL • SSOT: single source of truth

## Provenance
- Derived from root `AGENTS.md` (archived snapshot) and aligned to Gen26 SSOT + Knowledge + Telegram paths.
