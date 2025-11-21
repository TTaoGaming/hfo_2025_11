# Gen23 Research Index (foundational docs for GEM diagrams)

Date: 2025-11-05 (UTC)
Purpose
- This folder contains research artifacts used to synthesize the Gen23 GEM diagrams. These are not the GEM itself; they are the upstream research sources to generate and validate diagrams as code.

Conventions
- File naming: `research_<slug>_<timestamp>Z.md` (UTC ISO 8601 with trailing `Z`).
- Diagrams are parser-safe Mermaid (graph LR/TB; simple labels).

## Files

- `HFOMBSE_Gen23_Roadmap_2025-11-05T00:00:00Z.md`
  - One-stop Gen23 MBSE roadmap and cognitive scaffolding (YAML SSOT, generated views, SysML mirror, tutorials).

- `research_ssot_diagrams_2025-11-05T00:00:00Z.md`
  - Consolidated SSOT diagram pack (end-to-end, lane lifecycle, evidence chain, lanes-per-model, Telegram path, label map).

- `research_diagram_lineage_index_2025-11-05T00:00:00Z.md`
  - Lineage and attribution for each adopted diagram with conflict notes and decisions.

- `research_architecture_diagram_2025-11-05T00:00:00Z.md`
  - Architecture-focused diagrams with evidence pointers to recent validated runs.

- `research_architecture_consensus_delta_2025-11-05T00:00:00Z.md`
  - Consensus delta between runtime outputs and SSOT; highlights missing sections or mismatches.

- `research_gap_report_2025-11-05T00:00:00Z.md`
  - Gaps and immediate remedies for the research runner (digest emission, parallelism signal, config, stripes, tests).

## Next steps (optional)
- Generate GEM diagram files from these research docs (diagram-as-code).
- Add schema helpers to enforce evidence chaining (trace_id, parent_refs, sha256) in lane artifacts.
- Extend validators to check digest sections and parallelism signals.
