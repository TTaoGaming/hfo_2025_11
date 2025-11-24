---
hexagon:
  ontos:
    id: b7843586-764b-4023-ae43-2e18228340b2
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:36.096970Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_50/README.md
    links: []
  telos:
    viral_factor: 0.0
    meme: README.md
---

# Hive Fleet Obsidian: Generation 50 (The Evolutionary Forge)

**Status**: Active
**Stack**: T.R.A.M.E. (Temporal, Ray, Agno, MCP, Evolution)
**Philosophy**: Composition Over Invention. Executable Law over Abstract Models.

## Accelerated Cold Start

We have consolidated the entire generation into a single **Gene Seed**. This executable file contains the DNA for the entire system (Constitution, Factory, Evolution Engine, Orchestrator).

To ignite the forge from zero:

1.  **Enter the Gen 50 Holon**:
    ```bash
    cd hfo_gem/gen_50
    ```

2.  **Ignite the Gene Seed**:
    ```bash
    python3 HFO_GENE_SEED.md
    ```

This will automatically:
*   **Materialize Artifacts**: Extract `requirements.txt`, `src/constitution.py`, `src/foundry.py`, etc.
*   **Bootstrap Environment**: Install `uv` (if missing), create a virtualenv, and install SOTA dependencies.
*   **Ready the Swarmlord**: Prepare the Temporal worker for the first batch.

## The Vision

*   **Kill SysML**: Replaced by `src/constitution.py` (Pydantic models).
*   **Kill Docker**: Replaced by `uv` + Ray Actors (Process-based isolation).
*   **Kill LangChain**: Replaced by Agno (Lightweight agents).
*   **Add Evolution**: `src/evolution.py` (pyribs MAP-Elites) ensures quality-diversity.

See `VISION.md` for the full plain-English explanation.
