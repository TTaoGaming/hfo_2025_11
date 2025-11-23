---
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: c0d498e7-22d1-40b0-b8ad-a74a96944a08
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.499676+00:00'
  topos:
    address: brain/research_metadata_alternatives.md
    links: []
  telos:
    viral_factor: 0.0
    meme: research_metadata_alternatives.md
---

# 🧬 Rich Metadata: 4 Viable Evolutionary Paths

> **Status**: Research
> **Context**: Stigmergy Architecture (Static/Hot/Cold)
> **Goal**: Evaluate 4 distinct SOTA/Biomimetic approaches to handling metadata across the HFO Tri-State (Text, NATS, DB).

## 1. The "Obsidian Facet" (State-Change Model)
*The Baseline / Engineering Approach.*

### Concept
Information is **Matter**. It changes state based on temperature (activity).
*   **Biomimicry**: **Geology / Hydrology**. The Water Cycle. Ice (Static) $\to$ Water (Hot) $\to$ Sediment (Cold).
*   **SOTA Reference**: **Data Lakehouse** architectures (Databricks Delta Lake) combined with **Material Science** ontologies.

### Implementation
*   **Static (Crystal)**: Strict Pydantic Schema serialized to YAML headers. (High Structure, Low Entropy).
*   **Hot (Liquid)**: Lightweight JSON signals carrying only `id`, `urgency`, and `pointer`. (High Flow, High Entropy).
*   **Cold (Sediment)**: Relational Rows + Vector Embeddings. (High Density, Zero Entropy).

### Tradeoffs
*   **Pros**: Extremely robust. Strong typing. Easy to debug. "Single Source of Truth" is clear.
*   **Cons**: Rigid. Changing the schema requires a "migration" across all 3 states. Can feel bureaucratic.

---

## 2. The "Active Inference" (Markov Blanket Model)
*The Cognitive / Neuro-AI Approach.*

### Concept
Information is **Surprise**. Metadata represents the difference between expectation and reality.
*   **Biomimicry**: **Neuroscience**. Karl Friston's **Free Energy Principle**. The brain is a prediction machine.
*   **SOTA Reference**: **Active Inference Agents** (Verses AI, Spatial Web).

### Implementation
*   **Static (Prior)**: Files represent the Agent's **Generative Model** (Current Beliefs). Metadata = `confidence`, `precision`.
*   **Hot (Error)**: NATS signals are **Prediction Errors**. "I expected X, but found Y." High error = High attention.
*   **Cold (Posterior)**: The DB stores the **Updated Model** after integrating the error.

### Tradeoffs
*   **Pros**: Self-correcting. Naturally handles uncertainty and "hallucination" (it's just high variance).
*   **Cons**: High cognitive complexity. Hard to visualize "Surprise" in a YAML header. Requires advanced math to tune.

---

## 3. The "Mycelial Hyphae" (Resource Flow Model)
*The Network / Graph-First Approach.*

### Concept
Information is **Nutrient**. Metadata describes the flow of resources and connections.
*   **Biomimicry**: **Mycology**. Fungal networks (Wood Wide Web). Slime molds (Physarum polycephalum).
*   **SOTA Reference**: **Graph Neural Networks (GNNs)** and **Flow-Based Programming**.

### Implementation
*   **Static (Hyphae)**: Files are Nodes. Metadata is purely **Links/Edges** (`connects_to`, `feeds_from`). No rigid schema, just topology.
*   **Hot (Pulse)**: NATS signals are **Resource Packets** (Tokens/Energy) moving along the edges. "Sending 5 units of Compute to Node A."
*   **Cold (Mycorrhiza)**: The DB stores the **Topology** and **Flow Rates**. Who feeds whom?

### Tradeoffs
*   **Pros**: Unbeatable for discovery and connection. "Swarmlord of Webs" native. Self-optimizing paths.
*   **Cons**: Weak on content. Great at telling you *that* things are connected, bad at telling you *what* they are.

---

## 4. The "Digital Pheromone" (Field Gradient Model)
*The Pure Stigmergy / Swarm Approach.*

### Concept
Information is **Scent**. Metadata is a volatile scalar field that decays over time.
*   **Biomimicry**: **Entomology**. Ant Colony Optimization (ACO). Chemotaxis.
*   **SOTA Reference**: **Dissipative Structure Theory** and **Swarm Robotics** (Harvard Wyss Institute).

### Implementation
*   **Static (Scent Mark)**: YAML headers contain **Isotopes**. `pheromone_type: food`, `intensity: 100`.
*   **Hot (Evaporation)**: NATS signals are **Decay Updates**. "Pheromone at ID:123 has decayed to 80."
*   **Cold (Heatmap)**: The DB stores **Density Fields**. Not individual records, but "Hotspots" of activity.

### Tradeoffs
*   **Pros**: Extremely fast. Perfect for "Heat" and "Urgency". No schema management (it's just numbers).
*   **Cons**: Lossy. Information evaporates. You lose the history of "Why" something happened, only that it was "Hot".

---

## Summary & Recommendation

| Feature | Obsidian Facet | Active Inference | Mycelial Hyphae | Digital Pheromone |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Metric** | Structure | Surprise | Connectivity | Intensity |
| **Best For** | **Knowledge Mgmt** | **Learning/Adaptation** | **Discovery/Routing** | **Real-time Coordination** |
| **Complexity** | Medium | High | Medium | Low |
| **HFO Fit** | 🟢 **High** | 🟡 Medium | 🟢 **High** | 🟡 Medium |

**Verdict**:
For **Hive Fleet Obsidian**, which balances *Knowledge* (Obsidian) and *Action* (Fleet), a hybrid is best.
*   Use **Obsidian Facet** as the backbone (Structure).
*   Borrow **Pheromones** for the "Pulse" primitive (Decay/Urgency).
*   Borrow **Mycelial** linking for the "Vector" primitive (Graph).
