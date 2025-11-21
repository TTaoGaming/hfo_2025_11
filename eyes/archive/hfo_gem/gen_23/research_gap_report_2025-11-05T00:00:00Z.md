# Gen23 gaps — 2025-11-05

BLUF
- The 100‑lane research run executed successfully with complete lane artifacts, but the research path did not emit a digest by default and our simple parallelism detector disagreed with the analyzer. We added a post‑run digest and a consensus delta; the remaining gaps are straightforward wiring and validation tasks.

## Gaps observed

- Digest emission (research path)
  - Research runner did not produce `swarmlord_digest.md` automatically; we generated one post‑run via `build_research_digest.py`.
  - Impact: Operator lacks a single summary by default; extra step needed.
  - Fix: Add digest emission to research runner, reusing digest builder.

- Parallelism detection source mismatch
  - Analyzer previously reported “Parallel detected: True”, but the digest builder’s conservative heuristic flagged `parallel_detected=False` for this trace.
  - Impact: Quorum marked FAIL despite sufficient votes; misleading status.
  - Fix: Integrate official analyzer result into the digest builder (or compute span overlap windows) and make quorum depend on that signal.

- Quorum evaluation coupling
  - Quorum result tied to `parallel_detected`; with a false negative, PASS becomes FAIL.
  - Fix: Gate PASS on both artifact votes and analyzer-backed parallelism; add an override when spans are intentionally minimal.

- Centralized config loader
  - Tokens/temperature/timeout/reasoning parsing is scattered; drift potential across runners/tools.
  - Fix: Introduce a single config loader used by runner, ARC tools, and digest builder.

- Persist per‑item predictions (research)
  - Lane outputs do not persist per‑item predictions to support downstream consensus/audits.
  - Fix: Add optional per‑item JSONL in `attempt_1/` with prediction + evidence.

- Deterministic striped slicing (ARC‑like flows)
  - Current slicing may overlap across lanes; stripes reduce duplication.
  - Fix: Add stripe strategy with seed + lane index.

- Summarizer vs per‑phase notes
  - Summarizer reported missing perceive/react/yield notes for this research mission.
  - Fix: Either disable notes for research or add scoped note hooks; align summarizer expectations.

- Tests for new utilities
  - No unit tests for `build_research_digest.py` and `architecture_consensus_delta.py`.
  - Fix: Add minimal tests: happy path + parallelism passthrough + line‑cap guard.

- Blackboard receipt for gap reports
  - No structured validator for gap report artifacts.
  - Fix: Add a validator step and append a verify receipt on PASS.

## Immediate remedies (acceptance)

- Wire digest emission into research runner
  - Acceptance: `swarmlord_digest.md` present without post‑run tool; `quorum_report.yml` consistent with analyzer.

- Use analyzer for `parallel_detected`
  - Acceptance: Digest and quorum show the same parallel status as `analyze_traces.py`.

- Centralize config
  - Acceptance: One loader used by runner and tools; env overrides honored; defaults documented.

- Persist predictions
  - Acceptance: Optional JSONL per lane with item‑level predictions saved under `attempt_1/`.

- Add tests
  - Acceptance: New tests green; quality gates updated to include these checks.

## Evidence

- Run: hfo_crew_ai_swarm_results/2025-11-05/run-1762357236847/
- Digest (post‑run): hfo_crew_ai_swarm_results/2025-11-05/run-1762357236847/swarmlord_digest.md
- Quorum: hfo_crew_ai_swarm_results/2025-11-05/run-1762357236847/quorum_report.yml
- Trace: temp/otel/trace-mi_arch_consensus_100lanes_2025-11-05-1762357236847.jsonl
- SSOT: hfo_gem/gen_23/research_architecture_diagram_2025-11-05T00:00:00Z.md
- Consensus delta: hfo_gem/gen_23/research_architecture_consensus_delta_2025-11-05T00:00:00Z.md

## Notes

- Safety envelope respected: gap report is concise, parser‑safe, and contains no placeholders.
- Branch: feat/telegram-topic-research-digest; Date: 2025-11-05.
