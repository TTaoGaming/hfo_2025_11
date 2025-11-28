---
hexagon:
  ontos:
    id: fb143785-6923-4a58-a685-f2d36d455ee4
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.883174Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_23/research_diagram_lineage_index_2025-11-05T00:00:00Z.md
    links: []
  telos:
    viral_factor: 0.0
    meme: research_diagram_lineage_index_2025-11-05T00:00:00Z.md
---

# HFO Diagram Lineage Index — Gen23 (attribution + adopted set)

Date: 2025-11-05 (UTC)
Branch: feat/telegram-topic-research-digest

Purpose
- Provide exact lineage for key diagrams across gens 1–22, note conflicts, and declare the adopted SSOT set for a complete HFO system (Gen23).
- Each entry lists the source generation, file path, and the adopted decision. Where necessary, a Gen23 synthesized diagram is noted with its upstream basis.

Legend
- Adopted: used as the canonical version in Gen23.
- Alternative: kept for history; not canonical.
- Synthesized: new in Gen23, derived from listed sources and current SSOT (AGENTS.md, Gen22).

---

## D1 — End-to-end orchestration (Operator→Swarmlord→Lanes→Quorum→Digest)
- Adopted from: Gen22 — `hfo_gem/gen_22/crew_ai_swarm_ssot_gen22.md` ("Architecture overview")
- Rationale: Most recent normative SSOT; maps directly to current runner + verify + digest.
- Notes: Parser-safe simplification retained (graph LR; simple labels).
- See in Gen23: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md` (Diagram A).

## D2 — Lane lifecycle (Orchestrate + PREY + Verify)
- Adopted from: Gen22 — `hfo_gem/gen_22/crew_ai_swarm_ssot_gen22.md` ("Lane internal")
- Rationale: Encodes LLM-at-each-phase and deterministic Verify; aligned with current contracts.
- Notes: Retains failure loop back to React.
- See in Gen23: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md` (Diagram B).

## D3 — Stigmergy + quorum (blackboard ↔ lanes ↔ quorum ↔ digest)
- Adopted from: Gen22 — `hfo_gem/gen_22/crew_ai_swarm_ssot_gen22.md` ("Stigmergy + quorum")
- Rationale: Matches blackboard receipts and quorum verify used today.
- Notes: Blackboards are append-only JSONL; spans are separate.
- See in Gen23: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md` (covered in A/D; blackboard links in C).

## D4 — Concurrency and fan-in/fan-out (pilot view)
- Alternative (context): Gen21 — `hfo_gem/gen_21/crew_ai_swarm_pilot_2025-10-30.md` (Mermaid)
- Rationale: Demonstrates validated parallelism ("Parallel detected: True"); complements D1/D2.
- Adopted decision: Keep as Alternative; core concurrency is subsumed by D1/D2/D7.
- See also: spans analyzer tool references in Gen21 doc.

## D5 — HIVE→GROWTH→SWARM layering (historical mapping)
- Alternative (historical): Gen9 — `hfo_gem/gen_9/original_gem.md` ("Layered Control Flow")
- Rationale: Establishes layered labels (HIVE/GROWTH/SWARM/FLEET/OBSIDIAN) used across early gems.
- Conflict: Introduces FLEET; current SSOT standardizes on PREY as the canonical loop and Verify gate.
- Adopted decision: Keep Gen9 mapping as historical context; label map in D6 is the canonical simplified form.

## D6 — Label map HIVE→GROWTH→SWARM→PREY→Verify→Digest
- Synthesized from: Gen9 layered mapping + Gen21/22 PREY contracts + `AGENTS.md` Workflow Map.
- Rationale: Aligns current repo labels with minimal parser-safe diagram used across code/docs.
- See in Gen23: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md` (Diagram F) — canonical.

## D7 — Lanes-per-model selection and quorum (multi-model orchestration)
- Synthesized from: Gen22 SSOT (lanes/models) + Gen21 pilot (fan-out) + ARC swarm notes.
- Rationale: Encodes model selection → yields → quorum for multi-model lanes; matches mission intents.
- See in Gen23: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md` (Diagram D) — canonical.

## D8 — Evidence chain and observability (artifact hash chaining + receipts + spans)
- Synthesized from: Gen22 SSOT (traceability fields); AGENTS.md (blackboard protocol); digest/validator notes.
- Rationale: Makes implicit SSOT traceability explicit as a diagram for build-as-code alignment.
- See in Gen23: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md` (Diagram C) — canonical.

## D9 — Telegram authoritative consult path to digest
- Synthesized from: `AGENTS.md` (Swarmlord chat and Telegram sections, 2025-11-02/03 updates).
- Rationale: Captures current operator IO path (ack → consult → digest reply) used in production.
- See in Gen23: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md` (Diagram E) — canonical.

---

# Conflict notes and resolutions

1) Layer set (FLEET vs PREY)
- Conflict: Gen9 layered diagram includes FLEET; current SSOT and code standardize on PREY loop with Verify gate.
- Resolution: Adopt PREY-centric flow (D2, D6). Keep Gen9 as historical context.

2) Diagram syntax and rendering
- Conflict: Older diagrams use themes, HTML breaks, and punctuation-heavy labels.
- Resolution: Gen23 adopts parser-safe conventions (graph LR/TB; simple labels). All adopted diagrams comply.

3) Concurrency depiction
- Conflict: Pilot diagram (Gen21) vs SSOT diagrams (Gen22) use different visual motifs.
- Resolution: Concurrency is represented via lanes-per-model (D7) and validated by spans; pilot kept as supplementary (D4).

4) Evidence visualization
- Conflict: SSOT Gen22 describes traceability; earlier gens visualize different aspects (guardrails, mirrors).
- Resolution: Gen23 adds explicit Evidence Chain diagram (D8) derived from Gen22 fields and AGENTS.md protocol.

---

# Adopted SSOT diagram set (build-as-code targets)
- D1 End-to-end orchestration (Gen22)
- D2 Lane lifecycle (Gen22)
- D3 Stigmergy + quorum (Gen22)
- D7 Lanes-per-model selection and quorum (Synthesized Gen22/21)
- D8 Evidence chain and observability (Synthesized Gen22)
- D9 Telegram authoritative consult path (Synthesized AGENTS.md)
- D6 Label map HIVE→GROWTH→SWARM→PREY→Verify→Digest (Synthesized Gen9/22/AGENTS)

Pointers
- Canonical diagrams live in: `hfo_gem/gen_23/research_ssot_diagrams_2025-11-05T00:00:00Z.md`.
- Historical/alternative references remain in their original files for audit.
