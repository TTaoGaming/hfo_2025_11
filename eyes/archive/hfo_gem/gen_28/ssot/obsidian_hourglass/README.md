---
hexagon:
  ontos:
    id: 982da942-45f4-4846-9a18-3289402446eb
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.975965Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_28/ssot/obsidian_hourglass/README.md
    links: []
  telos:
    viral_factor: 0.0
    meme: README.md
---

# Obsidian Horizon Hourglass SSOT

This folder carries the single source of truth for the Obsidian Horizon Hourglass loop in Generation 28. Keep it tool agnostic: the loop can run by hand, by one assistant, or by a full agent crew.

## Loop in Plain Language
- **Past sweep**: gather precedents from every source you can reach (personal notes, institutional records, open web) with extra attention to Cynefin framing and case-based reasoning.
- **Future runs**: spin up what-if experiments using the best algorithms available (Monte Carlo, tree search, Bayesian sweeps, or quick heuristics when under time pressure).
- **Present artifact**: bake what you learned into a deliverable people or swarms can act on right now. Flip the hourglass and reuse the new lessons inside the precedent store.

Each flip should update risk, cost, and confidence so we gain a live probability view of the best path. You can stop the loop any time once the mission intent is satisfied.

## Stack Guardrails
- Storage stays neutral: Postgres with pgvector is preferred because it handles text, metadata, and vectors in one place, but any vector-ready store works.
- Workflow runner can be manual checklists, Temporal, or LangGraph-based scripts. Pick what fits the mission tempo.
- Simulation tools are swappable. Keep notebooks, Python modules, or external services documented so they can be rerun.
- Use NATS JetStream or Redis pub/sub when you need live updates between helpers. No dependency is mandatory; this SSOT only defines the interfaces.

## Selected Implementation Path (HFO Gen 28)
- **Workflow engine**: Temporal will own durable orchestration, retries, and replayable hourglass flips.
- **Agent graph**: LangGraph will model the Historian/Operator/Forecaster (or solo agent) flow inside each Temporal activity.
- **Knowledge base**: Postgres + pgvector stores precedents, simulation outputs, and risk/cost metrics with provenance fields.
- **Event spine**: NATS JetStream moves status updates and intermediate findings; allows replay when we audit a flip.
- **Parallel compute**: Ray (or native Python async) handles heavy simulations and data transforms triggered by LangGraph nodes.
- **Observability & flags**: OpenTelemetry for traces/metrics/logs, OpenFeature for feature toggles, plus standard structured logging.
- **Interface surface**: FastAPI or CLI shim to trigger hourglass runs; publishes present artifacts into `ssot/obsidian_hourglass/` and downstream swarms.

## Files
- `Obsidian_Hourglass.sysml` encodes the SysML v2 model that captures requirements, structure, and actions for the hourglass.
