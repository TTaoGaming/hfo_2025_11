---
hexagon:
  ontos:
    id: eaf1129e-6187-48e0-8d49-3144c556ea8a
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.907601Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_25/README.md
    links: []
  telos:
    viral_factor: 0.0
    meme: README.md
---

# Gen25 — SSOT (single README) with direct MD → SysML v2

BLUF
- One write-surface: this README. Author in Markdown (Mermaid allowed). Generate SysML v2 text directly.
- Keep edits ≤200 lines per write; no placeholders; append blackboard receipts.

Why Gen25
- Reduce hallucination and drift by concentrating architecture in one coherent MD.
- Mirror to SysML v2 text for rigor and downstream automation.

How to author (sections and shapes)
- Use level-2 headings (##) with the exact titles below. Lines under each section follow the noted shape.
- ASCII-only labels; avoid punctuation in diagram labels.

## Context
Gen25 defines a single Gene Seed MD as the SSOT that generates everything else without vendor lock in. The system is a biomimetic apex swarm that uses virtual stigmergy layers and quorum to coordinate behavior and mitigate tail risk from hallucinations and errors.

## Blocks
GeneSeed, spec, [ssot]
Swarmlord, service, [core, control]
CrewRunner, worker, [runner]
LLMClient, library, [llm]

## Interfaces
Swarmlord -> CrewRunner, orchestrate PREY, python

## Relationships
CrewRunner uses LLMClient

## Allocations
CrewRunner -> scripts/crew_ai/runner.py

## Tags
ssot: single source of truth
core: required at boot
runner: executes lanes
llm: llm client

## Provenance
hfo_gem/gen_25/README.md (2025-11-06)

Reference diagram: see `hfo_gem/gen_25/vision_gem_gene_seed_regeneration_2025-11-06.md`.

## Vision index
- Gene Seed Regeneration: `hfo_gem/gen_25/vision_gem_gene_seed_regeneration_2025-11-06.md`
- Swarm Lord of Webs: `hfo_gem/gen_25/vision_swarmlord_of_webs_2025-11-06.md`
- Solo AI (PREY anytime): `hfo_gem/gen_25/vision_solo_ai_swarm_lord_of_webs_2025-11-06.md`
- Swarm orchestration (10 • 100 lanes): `hfo_gem/gen_25/vision_swarm_10_100_lanes_2025-11-06.md`
- North Star Horizons: `hfo_gem/gen_25/vision_north_star_2025-11-06.md`
- Holonic Workflows (HIVE • GROWTH • SWARM • PREY): `hfo_gem/gen_25/vision_workflows_holonic_2025-11-06.md`
 - HOLON Roles (OBSIDIAN): `hfo_gem/gen_25/vision_holon_roles_obsidian_2025-11-06.md`
 - PREY Workflow: `hfo_gem/gen_25/vision_prey_workflow_2025-11-06.md`

Generator (MD → SysML v2)
- Script: `scripts/mbse/md_to_sysml.py`
- Run:
	- `python3 scripts/mbse/md_to_sysml.py hfo_gem/gen_25/README.md --out sysml/hfo.sysml`
- Output: `sysml/hfo.sysml` with blocks, interfaces, dependencies, and allocation/tag comments.

Guardrails
- Chunking: ≤200 lines per write; prefer small, composable edits.
- Placeholder ban: Don’t commit "TODO" or "...".
- Receipts: Append to `hfo_blackboard/obsidian_synapse_blackboard.jsonl` with evidence refs to this file.
- Verify: Don’t claim “done” until SysML text renders and receipts exist.
