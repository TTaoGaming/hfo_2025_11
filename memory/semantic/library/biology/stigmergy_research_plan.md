---
title: Evolutionary Stigmergy Patterns Research Plan
summary: A plan to evolve bio-digital stigmergy coordination for HFO by trialing three
  simple, bio-inspired 'species' (Ant, Termite, Slime Mold) under evolutionary pressure
  to let effective patterns emerge naturally.
domain: Biology
concepts:
- Stigmergy
- Evolutionary Pressure
- Pheromone Schema
- Tool Ranking
- Knowledge Graph
owner: Architect
actionable: true
related_files: []
type: crystallized_memory
status: active
last_verified: '2025-11-21'

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: f85983f7-8f18-4d1b-ad03-a1fc1ea7f0f8
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:10.200565+00:00'
  topos:
    address: memory/semantic/library/biology/stigmergy_research_plan.md
    links: []
  telos:
    viral_factor: 0.0
    meme: stigmergy_research_plan.md

---

# 🧪 Research Intent: Evolutionary Stigmergy Patterns

> **Status**: Active Research
> **Objective**: Evolve a bio-digital coordination layer for HFO using evolutionary pressure rather than top-down design.

## 🧬 Core Philosophy: "Evolve, Don't Design"
Instead of architecting a perfect Stigmergy system from day one, we will treat Stigmergy patterns as "species" in an ecosystem. We will introduce simple signal types, subject them to evolutionary pressure (usage and utility), and let the most effective patterns survive to become the standard.

## 🔬 The Experiment: The Cambrian Explosion

We will trial three distinct "Species" of Stigmergy simultaneously. Each must be **Simple**, **Extendable**, and **Composable**.

### Species A: The Ant (Quantitative Utility)
*   **Biology**: Pheromone trails. Stronger scent = better path.
*   **Application**: **Tool & Memory Ranking**.
*   **Mechanism**:
    *   Every successful tool use increments a `utility_score`.
    *   Every day, the score decays (evaporation).
    *   **Hypothesis**: High-utility tools will naturally bubble to the top of context windows; useless tools will fade.

### Species B: The Termite (Qualitative State)
*   **Biology**: Stigmergic building. "If mud here, place more mud."
*   **Application**: **File Organization & Workflow**.
*   **Mechanism**:
    *   Files carry `state_markers` (e.g., `status: draft`, `needs: review`).
    *   Agents (Immunizers) react to markers locally without a central plan.
    *   **Hypothesis**: Complex organization (folders, archives) will emerge from simple local rules.

### Species C: The Slime Mold (Network Flow)
*   **Biology**: Network optimization. Reinforce used tubes, retract unused ones.
*   **Application**: **Knowledge Graph Connections**.
*   **Mechanism**:
    *   Traversing a link between Concept A and Concept B strengthens the `edge_weight`.
    *   Unused edges atrophy and are pruned.
    *   **Hypothesis**: The Knowledge Graph will reshape itself to match the *actual* thinking patterns of the swarm.

---

## 📉 The Evolutionary Pressure (Fitness Function)

How do we decide which patterns survive?

1.  **Signal-to-Noise Ratio**: Does the signal reduce agent confusion? (Measured by `retry_count`).
2.  **Computational Cost**: Is the overhead of maintaining the signal worth the gain? (Measured by `token_usage`).
3.  **Emergence**: Does the pattern solve problems we didn't explicitly program it to solve? (Qualitative observation).

## 🛠️ Implementation Strategy: The "Pheromone" Schema

To allow these species to coexist, we need a minimal, composable base schema.

```yaml
# The Universal Pheromone Protocol (Draft)
pheromone:
  id: "uuid"
  species: "ant" | "termite" | "mold"
  value: 0.0 # Quantitative payload (or string for Termite)
  decay: 0.1 # Evaporation rate
  source: "agent_id"
  timestamp: "iso_date"
```

## 📅 Next Steps
1.  **Define**: Create the Pydantic model for the `Pheromone` schema.
2.  **Inject**: Add "Ant" pheromones to the Tool Execution loop.
3.  **Observe**: Run a simulation and watch if agents naturally prefer "scented" tools.


---
**Grafted by Gardener**: [[gen_50_README|Gen 50 Hub]]
