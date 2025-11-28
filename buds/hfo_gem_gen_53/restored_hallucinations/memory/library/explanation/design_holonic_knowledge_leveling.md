---
title: 'Holonic Knowledge Leveling: Cooling & Crystallization'
bluf: We implement a "Cooling System" for Truth, grounded in Thermodynamics and Stigmergy.
  Information starts as Hot Plasma (NATS) and cools into Solid Crystal (Graph) through
  Log-10 Swarm Consensus. No invention, only composition of exemplars.
story: "> **The Metaphor**: Truth is a phase transition. > 1. **Plasma (Lvl 0)**:\
  \ High Energy, Low Structure. (NATS Signals) > 2. **Gas (Lvl 1)**: Coalescing Clouds.\
  \ (Markdown Files) > 3. **Liquid (Lvl 2)**: Flowing Vectors. (pgvector) > 4. **Crystal\
  \ (Lvl 3)**: Rigid, Durable Structure. (Knowledge Graph)\n> **The Hexagon**: The\
  \ 6 Facets of Crystallization (Ontos, Chronos, Topos, Telos, Logos, Ethos).\n> **The\
  \ Exemplars**: > - **Stigmergy** (Grass\xE9, 1959): Indirect coordination via environment.\
  \ > - **Dunbar's Number** (150): Limits of Lvl 2 Squads. > - **Byzantine Fault Tolerance**\
  \ (Lamport): Consensus mechanism. > - **MAP-Elites** (Mouret & Clune): Diversity\
  \ preservation."
tags:
- architecture
- thermodynamics
- knowledge_graph
- stigmergy
- research_grounded
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440100
    type: design
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.9
    decay: 0.05
    created: '2025-11-23T12:30:00Z'
    generation: 51
  topos:
    address: brain/design_holonic_knowledge_leveling.md
    links:
    - brain/spec_holonic_leveling.feature
    - brain/design_mountain_web_stigmergy.md
  telos:
    viral_factor: 0.95
    meme: "\u2744\uFE0F Truth Cools: Plasma -> Gas -> Liquid -> Crystal"
---


# ❄️ Holonic Knowledge Leveling: The Cooling System

## 1. The Phase Transitions (Log 10 Scale)

We map the state of matter to the scale of consensus.

| Level | Phase | Agent Count (Log 10) | Exemplar | Storage | Properties |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Lvl 0** | **Plasma** | $10^0$ (1) | **Stigmergy** (Pheromone) | NATS (Hot) | High Energy, Ephemeral, No Structure. |
| **Lvl 1** | **Gas** | $10^1$ (10) | **Agile Squad** (Scrum) | File (Warm) | Loose coupling, Human-readable, Drafts. |
| **Lvl 2** | **Liquid** | $10^2$ (100) | **Dunbar's Tribe** | Vector (Cool) | Flowing, Semantic, Searchable, Dense. |
| **Lvl 3** | **Crystal** | $10^3$ (1000) | **Byzantine Quorum** | Graph (Cold) | Rigid, Durable, Interconnected, True. |

## 2. The Hexagonal Lattice (Attributes)

For a Holon to crystallize, it must satisfy the **Hexagonal Quality Metrics** (HQM). These map to our Header Schema.

1.  **ONTOS (Identity)**: Does it have a unique, persistent UUID? (No duplicates).
2.  **CHRONOS (Time)**: Does it have a valid decay rate and timestamp? (Thermodynamics).
3.  **TOPOS (Space)**: Is it linked to at least 3 other Crystals? (Triangulation).
4.  **TELOS (Purpose)**: Does it have a Viral Factor > 0.5? (Utility).
5.  **LOGOS (Logic)**: Is the Vector Density (Information/Token) high? (Compression).
6.  **ETHOS (Trust)**: Is the Consensus Score > 99%? (Verification).

## 3. The Cooling Process (Workflow)

### Step 1: Ionization (Lvl 0 -> 1)
*   **Action**: An agent emits a thought (Plasma).
*   **Filter**: **Stigmergic Pheromone Decay**. If not reinforced by 9 other agents within $T_{decay}$, it evaporates.
*   **Result**: If reinforced, it condenses into a Markdown File (Gas).

### Step 2: Condensation (Lvl 1 -> 2)
*   **Action**: A Research Swarm (100 agents) ingests the File.
*   **Filter**: **MAP-Elites Diversity**. Is this new? Is it high performing?
*   **Result**: If unique and valuable, it is embedded into `pgvector` (Liquid).

### Step 3: Crystallization (Lvl 2 -> 3)
*   **Action**: The Assimilator (1000-node simulation) tests the Vector against the Graph.
*   **Filter**: **Byzantine Fault Tolerance**. Can 1/3rd of the network attack this truth and fail?
*   **Result**: If robust, it is linked into the Knowledge Graph (Crystal) as a permanent node.

## 4. Research Grounding (Exemplars)

We do not invent. We compose.

*   **Stigmergy**: We use NATS as the "Environment" for indirect coordination (Grassé).
*   **Thermodynamics**: We use "Cooling" (Simulated Annealing) to find global optima (Truth).
*   **Fractal Geometry**: The Hexagon repeats at every scale (1, 10, 100, 1000).
*   **Complex Systems**: We respect "More is Different" (Anderson, 1972). Lvl 3 behavior cannot be predicted by Lvl 0 agents.

## 5. GraphRAG Implementation

*   **Hot Query**: "What is happening *now*?" -> Subscribe to NATS (Plasma).
*   **Warm Query**: "What are we working on?" -> Search Files (Gas).
*   **Cool Query**: "What is the context?" -> Search Vectors (Liquid).
*   **Cold Query**: "What is TRUE?" -> Traverse Graph (Crystal).
