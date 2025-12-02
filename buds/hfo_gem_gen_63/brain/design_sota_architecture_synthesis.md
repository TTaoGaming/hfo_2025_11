---
holon:
  id: hfo-gen63-sota-synthesis
  type: design
  status: active
  author: Swarmlord
  generation: 63
  context: SOTA Architecture Synthesis
---

# 🧬 Design: The Synthetic Organism (SOTA Synthesis)

> **Context**: Synthesized from "AI Chat Architecture Audit" (2025-12-01).
> **Purpose**: To define the **High-Signal** architectural pillars of Gen 63.
> **Core Concept**: HFO is not an app; it is a **Digital Organism** that evolves via **Declarative Intent**.

## 🦅 Executive Summary (The High Signals)
We have identified 5 "High Signal" pillars that define the Gen 63 architecture. These separate the **Roles** (Who) from the **Tech** (How).

1.  **The Body Plan**: Fractal Octree & JADC2 Mapping.
2.  **The Nervous System**: Hot/Cold Stigmergy & The Phoenix Protocol.
3.  **The Brain**: MAP-Elites & Grammar-Guided Genetic Programming (GGGP).
4.  **The Immune System**: Byzantine Fault Tolerance (BFT).
5.  **The Traversal**: Indra's Net & Triangulation.

---

## 1. The Body Plan: Roles vs. Tech
We distinguish between the **O.B.S.I.D.I.A.N. Roles** (The Agents) and the **O.B.S.I.D.I.A.N. Stack** (The Tools).

| Letter | **Role (The Agent)** | **JADC2 Function** | **Tech (The Tool)** | **Connection** |
| :--- | :--- | :--- | :--- | :--- |
| **O** | **Observer** | **SENSE** (ISR) | **Orchestrator** (Temporal) | The Observer uses the Orchestrator to schedule monitoring loops. |
| **B** | **Bridger** | **CONNECT** (Comms) | **Bus** (NATS) | The Bridger manages the Bus to route signals. |
| **S** | **Shaper** | **ACT** (Effectors) | **Schema** (Pydantic) | The Shaper executes actions validated by the Schema. |
| **I** | **Immunizer** | **DEFEND** (Assurance) | **Intelligence** (LangGraph) | The Immunizer uses Intelligence to validate logic and run tests. |
| **D** | **Disruptor** | **RED TEAM** (Test) | **Database** (LanceDB) | The Disruptor attacks the Database to test resilience. |
| **I** | **Infuser** | **SUSTAIN** (Logistics) | **Interface** (MCP) | The Infuser manages Resources via the Standard Interface. |
| **A** | **Analyzer** | **MAKE SENSE** (Fusion) | **Analytics** (OpenTel) | The Analyzer fuses data from Analytics traces. |
| **N** | **Navigator** | **DECIDE** (C2) | **Nodes** (Ray) | The Navigator spins up Nodes to execute the Mission. |

> **Insight**: The **Roles** are the "Soft Logic" (Prompts/Policies). The **Tech** is the "Hard Infrastructure" (Code/Servers).

---

## 2. The Nervous System: The Phoenix Protocol
We solve the "Split-Brain" problem using a **Crash-Only CQRS** architecture.

*   **Source of Truth**: **SQLite** (Write-Ahead Log). All events are append-only.
*   **Projections (The Views)**:
    *   **LanceDB**: Semantic Index (Rebuilt from SQLite).
    *   **NetworkX**: Knowledge Graph (Rebuilt from SQLite).
*   **The Phoenix Rule**: If an agent suspects corruption (Hallucination), it **Burns** the LanceDB index and **Regenerates** it from the SQLite logs.
*   **Stigmergy**:
    *   **Hot (Reflex)**: NATS JetStream (TTL=1h). "Scent Trails".
    *   **Cold (Instinct)**: LanceDB (Permanent). "Muscle Memory".

---

## 3. The Brain: Evolution, Not Learning
The system does not "learn" (update weights) at runtime. It **Evolves** (updates code).

*   **Gene Seed**: Gherkin Feature Files (`.feature`) are the DNA. They define **Intent**.
*   **Genesis Engine**: A **Grammar-Guided Genetic Programming (GGGP)** engine.
    *   *Input*: Gherkin Tests + Atomic Primitives (MCP Tools).
    *   *Process*: Combinatorial Evolution.
    *   *Output*: Valid Python Code that passes the Gherkin tests.
*   **MAP-Elites**: We do not seek one "Best" agent. We seek a **Quality-Diversity Archive**.
    *   *Niche 1*: Fast & Cheap (for simple queries).
    *   *Niche 2*: Slow & Deep (for complex reasoning).
    *   *Niche 3*: Novel & Weird (for creative tasks).

---

## 4. The Immune System: Byzantine Consensus
We assume **2 Traitors** (Hallucinating Agents) in every group of 8.

*   **Protocol**: **3f+1 Consensus**.
*   **Mechanism**: Before executing a High-Risk Action (e.g., `delete_file`), the Squad must Vote.
*   **The Disruptor**: A specialized agent whose **Goal** is to lie and subvert the vote. If the system succumbs to the Disruptor, the Immune System fails and triggers a **Phoenix Burn**.

---

## 5. The Traversal: Indra's Net
The Navigator views the world as a **State-Action Manifold**.

*   **Triangulation**:
    *   **Past**: CBR (Case-Based Reasoning) from LanceDB.
    *   **Present**: Telemetry from OpenTelemetry.
    *   **Future**: Short-horizon rollouts (Simulations).
*   **Fractal Octree**: The search space is partitioned recursively by powers of 8.
*   **Zero Invention**: The Navigator cannot invent new actions. It can only **Compose Exemplars** found in the Octree.

---

## 🚀 Implementation Roadmap (Gen 63)
1.  **Formalize the Roles**: Update `AGENTS.md` to reflect the JADC2 mapping.
2.  **Implement Phoenix**: Ensure `sqlite-mcp` server supports "Replay/Regenerate".
3.  **Deploy MAP-Elites**: Use `ribs` (Python lib) to manage the Agent Archive.
4.  **Activate the Disruptor**: Create a "Red Team" test suite that intentionally feeds bad data to the Assimilator.
