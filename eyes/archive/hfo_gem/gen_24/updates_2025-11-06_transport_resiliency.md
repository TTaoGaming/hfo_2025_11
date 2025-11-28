---
hexagon:
  ontos:
    id: 33cd0b40-5cf3-419a-b98c-f30e24fd6ccb
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.899237Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_24/updates_2025-11-06_transport_resiliency.md
    links: []
  telos:
    viral_factor: 0.0
    meme: updates_2025-11-06_transport_resiliency.md
---

# Gen24 update — transport resiliency and quorum lift (2025-11-06)

BLUF
- Hardened LLM calls across Engage and all agent phases (Observer, Bridger, Shaper, Assimilator) to reduce empty responses and improve quorum preview coverage.
- Small, safe changes: single retry on empty content, compatibility fallback on retry, modest timeout increase. Token budgets remain bounded and allowlist unchanged.

## What changed

- Runner (Engage)
  - retry_on_empty enabled (max one retry); `llm.retry_max` supported (default 1)
  - On retry: drop `response_format` and `reasoning` fields to maximize provider compatibility
  - Timeout bumped to 30s (from 25s) for resilience under load
  - Spans include `reasoning_removed_on_retry` flag for audit

- Agents
  - Observer, Bridger, Shaper (diagram + summary prompts), Assimilator now use the same resiliency profile
  - Shaper still enforces exactly N diagrams per lane (padding with parser-safe templates) when `outputs.require_diagrams` is set

## Why

- Recent diagram-focused missions showed low `preview_rate` in Engage receipts, which pulled quorum_plus below thresholds despite artifacts being correct. Retrying empties and relaxing format constraints reliably raises `preview_rate` at low cost.

## How to run

```bash
# Example: 10 lanes × 3 rounds, 3 diagrams per lane
PYTHONPATH=$PWD ./.venv/bin/python scripts/crew_ai/runner.py \
  --intent hfo_mission_intent/_tmp/mission_intent_diagram_request_10lanes_3x_2025-11-06.v1.yml
```

Optional mission knobs (llm section):
- max_tokens: 1000 (broader tasks) or 200–400 for ARC-like; defaults respected
- timeout_seconds: 30
- retry_max: 1
- temperature: 0.2
- reasoning: true | false
- reasoning_effort: high | medium

## Verify checklist

- Per lane (latest attempt)
  - perception_snapshot.yml, react_plan.yml, engage_report.yml, yield_summary.yml present and valid
  - Exactly 3 diagram_*.md files when requested (validator PASS)
- Run-level
  - Spans at temp/otel/trace-*.jsonl include engage_llm windows; some spans may show `reasoning_removed_on_retry: true`
  - Engage receipts show non-empty `llm.content_preview` more frequently
  - quorum_plus_report.yml: preview_rate meets threshold (e.g., ≥ 0.6) and PASS; distinct_sources meets threshold
  - swarmlord_digest.md includes Consensus section and pointers

## Acceptance

- Quorum+ PASS on the diagram mission with updated resiliency
- Consensus artifacts present and referenced in digest
- No placeholders; edits ≤200 lines; receipts appended by runner as usual

## Notes

- Allowlist remains enforced; reasoning auto-high still used for supported models unless removed on retry for compatibility.
- Costs remain bounded: at most one retry per call and modest timeout increase.

## Next steps (low risk)

- Add consensus quality scoring (coverage/uniqueness) and optional inline Top-3 in digest
- Lane self-audit yml per attempt to retain best diagrams and flag gaps
- Scale to 100 lanes with backoff/rate controls and staged runs (25 → 50 → 100)
