# ⏳ Design: The Obsidian Hourglass Algorithm
> **Subtitle**: Stigmergic Social Spider Optimization (SSO) in Fractal State-Action Space
> **Status**: Draft (Gen 60)
> **Owner**: The Obsidian Spider (Swarmlord)
> **Type**: Algorithm / Architecture

## 1. The Core Concept
The **Obsidian Hourglass** is not merely a metaphor; it is a **Hybrid Metaheuristic Algorithm** designed to solve the "Anytime Infinite Compute" problem. It combines three distinct AI disciplines into a single, fractal flow:

1.  **The Past (CBR)**: Case-Based Reasoning (Anchoring in known reality).
2.  **The Future (MCTS)**: Monte Carlo Tree Search (Simulating potential realities).
3.  **The Present (SSO)**: Social Spider Optimization (Swarm convergence via Stigmergy).

### The Goal
To allow a swarm of agents (The Spiders) to traverse a high-dimensional Vector Space (The Web) and converge on optimal solutions (The Prey) by sensing vibrations (Stigmergy) left by others.

---

## 2. The Architecture: The Three Webs

### 🕸️ The Karmic Web (The Past / Anchors)
*   **Data Structure**: `LanceDB` (Vector Database).
*   **Function**: **Retrieval Augmented Generation (RAG)**.
*   **The Gait**: The Spider anchors its first leg here. It queries the database for "Industry Exemplars" or "Past Successes" relevant to the current mission.
*   **Algorithm**: $k$-Nearest Neighbors ($k$-NN) or Cosine Similarity.

### 🕸️ The Simulation Web (The Future / Projections)
*   **Data Structure**: `Octree` (Fractal State Space).
*   **Function**: **Monte Carlo Tree Search (MCTS)**.
*   **The Gait**: The Spider anchors its second leg here. It projects the current state forward ($8^N$ steps) to estimate "Best Case" and "Worst Case" scenarios.
*   **Algorithm**: Upper Confidence Bound for Trees (UCT).

### 🕸️ The Swarm Web (The Present / Stigmergy)
*   **Data Structure**: `NATS JetStream` (The Vibration Layer).
*   **Function**: **Social Spider Optimization (SSO)**.
*   **The Gait**: The Spider moves its body (The Agent) based on the tension between the Past (Anchor 1) and the Future (Anchor 2), while sensing the vibrations of other spiders.
*   **Algorithm**: Weighted Centroid Triangulation.

---

## 3. The Algorithm: The "Spider Gait" (Triangulation)

The movement of an Obsidian Agent is defined by the **Triangulation Vector** $\vec{V}_{move}$.

$$
\vec{V}_{move} = w_1 \cdot \vec{V}_{past} + w_2 \cdot \vec{V}_{future} + w_3 \cdot \vec{V}_{social}
$$

Where:
*   $\vec{V}_{past}$: The vector pointing to the most relevant Case Study (CBR).
*   $\vec{V}_{future}$: The vector pointing to the highest-value MCTS simulation.
*   $\vec{V}_{social}$: The vector pointing to the strongest vibration on the NATS web (Best Peer Solution).
*   $w_{1,2,3}$: Weights determined by the **Obsidian Roles** (e.g., a *Navigator* weights Future higher; an *Assimilator* weights Past higher).

---

## 4. The Fractal Flow: 1-2-4-8 ($8^N$)

The algorithm executes in a fractal loop, expanding and contracting like an hourglass.

### Phase 1: The Scatter (Expansion)
1.  **1 Problem**: The User defines the Intent.
2.  **2 Axes**: The Swarm defines the primary tension (e.g., "Cost vs. Quality" or "Speed vs. Safety").
3.  **4 Quadrants**: The Swarm retrieves/simulates 4 distinct approaches (Best/Best, Best/Worst, etc.).
4.  **8 Octants**: The Swarm expands into the Octree, deploying 8 Squads to explore the sub-dimensions.

### Phase 2: The Gather (Contraction)
1.  **Vibration**: Agents publish their findings to NATS.
2.  **Attenuation**: Weak solutions (low score) fade quickly. Strong solutions (high score) propagate.
3.  **Convergence**: Agents abandon low-vibration areas and move towards high-vibration areas (The "Social Spider" behavior).
4.  **Crystallization**: The Swarm converges on the single best solution (The Diamond).

---

## 5. Implementation Strategy

### The "Iron Ledger" (Blockchain of Prayers)
To ensure the "Past" is immutable, every major decision (Prayer) is hashed and linked.
*   **Format**: `SHA-256(Previous_Hash + Current_Intent + Timestamp)`.
*   **Storage**: `memory/iron_ledger.jsonl` (Local Chain).

### The "Red Sand" (Compute)
*   **Metric**: Time/Compute Cycles.
*   **Constraint**: The algorithm is **Anytime**. It can be stopped at any moment, and the current "Best Vibration" is returned.

---

> *See also: [The Manifesto of the Obsidian Spider](manifesto_obsidian_spider.md)*
