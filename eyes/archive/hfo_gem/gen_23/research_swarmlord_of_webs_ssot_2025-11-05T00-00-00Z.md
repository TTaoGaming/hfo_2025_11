---
hexagon:
  ontos:
    id: f230c2ea-212a-400b-a4f2-381e7f270c9d
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.890272Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_23/research_swarmlord_of_webs_ssot_2025-11-05T00-00-00Z.md
    links: []
  telos:
    viral_factor: 0.0
    meme: research_swarmlord_of_webs_ssot_2025-11-05T00-00-00Z.md
---

# Research — Swarmlord of Webs (Gen23 SSOT) — 2025‑11‑05T00:00:00Z

BLUF
- The Swarmlord of Webs is your alter‑ego: a symbiotic cognitive exoskeleton that takes over the execution/tactical layer so you can stay at vision/strategy.
- It never creates a Mission Intent until at least three separate Clarification Passes exist (CP≥3). It then runs many tasks in parallel, verifies independently, and produces one review: the Swarmlord Digest.
- This page gives three practical variants you can use today and shows how the Obsidian Horizon Hourglass fits in—all while keeping a single source of truth (the model).

What “single source of truth (SSOT)” means here
- The model (YAML) is the one place that names parts and connections (Swarmlord, PREY lanes, Verify/Quorum, Blackboard, Clarification Gate).
- Diagrams and helpers are generated from the model—no hand‑edited diagrams.
- This page explains options in plain language and points to the model; it isn’t the model itself.

Crew AI framing (roles and lanes)
- PREY phases map to roles used across this repo:
  - Observer = Perceive, Bridger = React, Shaper = Engage, Assimilator = Yield.
  - Post‑lane validators: Immunizer + Disruptor (quorum/verify) before anything “ships”.
- Swarmlord is the single facade (human interface) that orchestrates lanes and enforces safety (CP≥3, receipts, ≤200 lines, no placeholders) and only delivers one digest after Verify PASS.

Obsidian Horizon Hourglass (what/why/how now)
- What: A simple way to think across time—near, next, later. It flips past/present/future and runs small “what‑if” probes, anytime, then estimates which path is most promising.
- Why: You already run 100+ lanes. Turning some lanes into “scenario probes” gives better choices without extra babysitting.
- How to use today: Tag lanes by horizon (near/next/later) and topic (hex‑cell). Run them in parallel exactly like your current lanes. Record the horizon/topic in receipts and digest. Pick the best plan from the results.

Your current flow (simple)
- Chat back‑and‑forth → Clarification Passes (documented files)
- After CP≥3 → create Mission Intent → run many lanes in parallel
- Each lane writes four files (snapshot, plan, report, summary)
- Verify independently (quorum) → then compile one Swarmlord Digest
- Append receipts to the Blackboard JSONL; spans prove parallelism

Guardrails we keep in every variant
- CP≥3 before any mission intent; if fewer than 3, mark hallucination and don’t proceed
- ≤200 lines per write; no placeholders; receipts with evidence paths
- Allow‑listed models and safe token budgets; independent Verify before “done”

Three variants you can use now (Crew AI first)

S1) Crew‑Orchestrated Swarmlord (today, minimal change)
- Shape: Keep your current runner and roles, but make the PREY lanes explicit as crew roles: Observer→Bridger→Shaper→Assimilator, then Immunizer/Disruptor for quorum.
- What changes today: Ensure CP≥3 before any mission intent; add simple tags per lane: horizon={near|next|later}, hex_cell=topic. Digest shows horizon/hex‑cell matrices.
- Why it helps: You keep everything you know; the roles are explicit and auditable; Hourglass appears as tagged “scenario lanes” with zero new infra.

S2) Hourglass Navigator Lanes (smarter choices on the same engine)
- Shape: Add a tiny “scenario planner” that spawns a few extra crew lanes per horizon and topic (stigmergy‑weighted). Roles inside each lane stay the same.
- What changes today: A small planner function proposes scenarios; the existing runner executes; receipts include {scenario_id, horizon, hex_cell}.
- Why it helps: Better decisions from the same compute by exploring near/next/later in parallel; still no infrastructure changes.

S3) Holonic Squads (ready for thousands later; same Crew AI semantics)
- Shape: Group lanes into “squads” per topic (hex‑cell). Each squad runs the same crew roles concurrently. Swarmlord allocates energy across squads based on stigmergy.
- What changes today: Introduce squad tags and per‑squad caps; optionally run multiple runner processes. From the Crew AI point of view nothing new to learn.
- Why it helps: Natural path to many agents without changing how lanes behave. When you add a scheduler/queue later, the squad shape already fits.

Optional: Where Prefect/Temporal fit (not required for Crew semantics)
- You can drop a scheduler behind the runner later for retries/visibility/queues. This does not change roles, lanes, receipts, or the digest—it only improves scheduling.

Which to pick (quick guide)
- Quick win, least change → S1 (Crew‑Orchestrated Swarmlord)
- Smarter choices today → S2 (Hourglass Navigator Lanes)
- Shape for many agents tomorrow → S3 (Holonic Squads)

How the model (SSOT) fits in
- We’ll add/update `models/hfo.yml` to declare:
  - Blocks: swarmlord, clarification_gate, hourglass, prey_lane, quorum, blackboard, digest, and (optionally) queue/engine
  - Interfaces: chat→swarmlord (consult), swarmlord→lanes (orchestrate), lanes→quorum (verify), swarmlord→blackboard (receipts)
  - Allocations: map each block to the real files in this repo (runners, validators, consult, digest)
- You still read one digest; the model keeps the wiring consistent.

References (repo paths)
- Hourglass background: `hfo_research_doc/ai-chat-obsidian-horizon-hourglass-10252025.md`
- Kilo‑code v12 hourglass mentions (flow viz/audit): `hfo_swarmlord_of_webs_kilo_code_mode/archive/`
- Crew runner & analyzer: `scripts/crew_ai/runner_unified.py`, `scripts/crew_ai/analyze_traces.py`
- Verify & digest: `scripts/crew_ai/validate_run.py`, `scripts/crew_ai/build_research_digest.py`
- Consult & gateway: `scripts/swarmlord/repo_consult.py`, `scripts/swarmlord/telegram_bot.py`
- Model roadmap: `hfo_gem/gen_23/HFOMBSE_Gen23_Roadmap_2025-11-05T00-00-00Z.md`

Next steps
- Pick one: “Prefect Lite”, “Prefect Worker Queue”, or “Temporal Minimal”.
- We then update the model file (`models/hfo.yml`) to reflect the choice and keep the system consistent.
- After that: add the tiny flow/workflow file, run a 100‑lane test, confirm one digest.
