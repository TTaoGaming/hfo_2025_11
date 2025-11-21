# HFO Conceptual Armory

This document defines the core "powerful concepts" equipped for Hive Fleet Obsidian (HFO). These are the keywords and architectural patterns that define the system's intelligence and resilience.

## 1. Structural Concepts

### 🕸️ Hexagonal Architecture (Ports & Adapters)
*   **Definition**: A design pattern that isolates the core application logic (the "Domain") from outside concerns like databases, UIs, or APIs.
*   **HFO Application**: The "Swarm" logic is the core. The `ingestion_queue`, `knowledge_bank`, and external APIs are just "adapters". This allows HFO to switch brains (LLMs) or bodies (platforms) without changing its mind.

### 💠 Hierarchical Holonic Topology
*   **Definition**: A structure where every component is both a whole "system" in itself and a "part" of a larger system (a "holon").
*   **HFO Application**:
    *   **Level 0**: Individual Agents (Worker).
    *   **Level 1**: Squads/Generations (Gen 1, Gen 2...).
    *   **Level 2**: The Hive Fleet (The entire repo).
    *   Each level has its own autonomy but contributes to the higher purpose.

## 2. Behavioral Concepts

### 🐝 Swarm Intelligence & Stigmergy
*   **Definition**: Complex collective behavior emerging from simple local rules. **Stigmergy** is coordination via the environment (e.g., ants leaving pheromone trails).
*   **HFO Application**: Agents don't talk to each other directly; they talk to the **Blackboard** (the Database/Queue).
    *   *Agent A* leaves a "PENDING" file.
    *   *Agent B* sees it, processes it, and marks it "COMPLETED".
    *   The "trail" is the metadata in the `ingestion_queue`.

### ⚔️ Adversarial Co-evolution
*   **Definition**: Two or more systems evolve by competing against each other.
*   **HFO Application**:
    *   **Generator Agent**: Creates code/content.
    *   **Critic/Auditor Agent**: Tries to break it or find flaws.
    *   This loop forces rapid improvement (like the "Molt" cycles).

## 3. Cognitive Concepts

### 🌫️ Epistemic Uncertainty (The 90% Rule)
*   **Definition**: Recognizing the limits of knowledge. Distinguishing between "I know this is false" vs "I don't know".
*   **HFO Application**: We cap confidence at **0.9**. We never assume 100% certainty. This prevents hallucination and allows for future corrections when new data arrives.

### 🧬 Memetic Evolution
*   **Definition**: Ideas (memes) evolving like genes.
*   **HFO Application**: The "Generations" (Gen 1 -> Gen 32) are evolutionary steps. Successful code survives; buggy code is "molted" away.

## Visualization Plan

To visualize this, we will map the **Ingested Data** against these concepts:
1.  **Cluster Analysis**: Group files by which concept they most relate to.
2.  **Evolutionary Graph**: Plot the density of these keywords over time (Gen 1 to Gen 32).
3.  **Holonic Map**: Draw the dependency tree of the codebase to show the nested structure.
