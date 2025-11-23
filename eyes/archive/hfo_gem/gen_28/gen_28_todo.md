---
hexagon:
  ontos:
    id: ac90c7e7-b557-488c-875d-3737284d898e
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.967008Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_28/gen_28_todo.md
    links: []
  telos:
    viral_factor: 0.0
    meme: gen_28_todo.md
---
# Generation 28 Vision TODO

Keep this list short and force-ranked. Update statuses inline rather than deleting resolved questions; move finished items to the "Answered" section so we preserve context.

- **IDE baseline**: Finish environment setup, extension alignment, and smoke-test rituals so modeling and automation land on stable ground.
  - 2025-11-10T20:20:28-07:00 — `scripts/dev/check_tooling.sh` now exists and runs; CLI inventory largely passes but the script surfaces real gaps (Go check uses `--version` and fails, Continue CLI probe collides with the Bash built-in, Temporal/NATS checks fail because services are down).
- **Documentation spine**: Capture the vision-to-SSOT pipeline clearly enough that assistants can draft SysML assets without new dictation.
  - 2025-11-10T20:20:28-07:00 — SSOT exporter wiring still mismatched (`export_ssot_diagrams.py` expects `--model/--output`, but the tooling script still calls `--input/--output`), so the pipeline is not yet reproducible.
- **Obsidian hourglass**: Lock the three-horizon state-action loop (inputs, flips, outputs, sequential→swarm path) into the vision so SSOT and tooling work can align.
- **Capability stack**: Draft tech stack captured; translate into vendor-agnostic capabilities and blocks before detailing implementations.
- **Tooling smoke test**: Finish IDE setup and run the mission smoke test (`scripts/dev/check_tooling.sh` once available) before exercising the hourglass pipeline.
  - 2025-11-10T20:20:28-07:00 — First run of `scripts/dev/check_tooling.sh` exited non-zero; blockers include the Go/Continue probes above, missing Temporal/NATS services, and the SSOT export flag mismatch.
- **Clarification cadence**: How should the multistage clarification flow adapt when intent changes mid-mission?
- **Knowledge hand-off**: What knowledge artifacts must persist between missions so we avoid repeated rediscovery?
- **Evaluation and safety**: What guardrails or evaluation loops must exist to keep the swarm from shipping hallucinated or unsafe outputs?
- **Workflow canon**: Define the four canonical loops (HIVE, GROWTH, SWARM, PREY) and how the Swarmlord selects/composes them without vendor bias.

## Supporting Investigations
- **Diagram priorities**: Which diagram types (REQ, UC, BDD, IBD, ACT, SEQ, STM) should land first to unlock the rest of the modeling?
- **Hourglass modeling**: Decide the SysML/Mermaid view that will carry the Obsidian Horizon Hourglass graph and how it traces into PREY loops.
- **Documentation pipeline**: Define the doc → SysML → generated artifacts flow so swarm agents know the transformation seams.
- **Tooling alignment**: Do we need additional automation beyond `ssot/export_ssot_diagrams.py` to stay in sync with SysML v2 modeling?
- **Archival hooks**: How will Generation 28 snapshots roll into future molt shells without losing dictation fidelity?
- **Flow inventory**: Validate and detail the three core flows (stack instantiation, mission orchestration, knowledge feedback) before we automate them.
- **Workflow playbooks**: Capture narrator-level descriptions for HIVE, GROWTH, SWARM, PREY so diagrams can stay technology-agnostic.

## Answered / Archived
- **2025-11-09 – Vision promise**: Generation 28 guarantees every user a persistent, personally paired Swarmlord who fronts the full swarm complexity and delivers quorum-backed outcomes from 10–100+ coordinated AI agents.
- **2025-11-09 – Stakeholder map**: Primary actors are `USER` (e.g., TTao), their dedicated `SWARMLORD` (e.g., Swarmlord of Webs), and the back-line `AI_AGENT_SWARM`. Users converse only with the Swarmlord; the Swarmlord orchestrates workflows and mediates all swarm interactions.
- **2025-11-09 – Success signals**: Success is observed when the user confers intent with the Swarmlord, the Swarmlord runs and validates the full swarm workflow, and returns a quorum-approved result without any direct user ↔ swarm interaction.
