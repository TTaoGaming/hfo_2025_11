---
holon:
  id: hfo-design-organ-renaming-v2
  type: design
  status: draft
  generation: 63
  author: Swarmlord
  theme: SOTA Assimilation & Biological Alignment
  previous_version: buds/hfo_gem_gen_63/brain/design_organ_renaming.md
---

# 🧬 Design V2: The SOTA Organ System

> **Objective**: Refine the directory structure to match State-of-the-Art (SOTA) AI Frameworks while retaining the "Obsidian Soul".
> **Key Changes**: `forge` -> `effectors`, `venom` -> `venom_lab`.

## 1. SOTA Landscape Analysis (What are we assimilating?)
To build a "Hydra Platform", we look at the current titans of AI Orchestration.

| Framework | Key Concept | HFO Equivalent |
| :--- | :--- | :--- |
| **LangGraph** | **Nodes & Edges** (State Machines) | `brain/` (The Graph Definition) + `heartbeat/` (The Runner) |
| **Temporal** | **Durable Execution** (Workflows) | `heartbeat/` (The Orchestrator) |
| **Ray** | **Distributed Compute** (Actors) | `heartbeat/` (The Swarm) |
| **Instructor** | **Structured Output** (Pydantic) | `immune_system/` (The Validator) |
| **NATS JetStream** | **Event Bus** (The Spine) | `sensors/` (The Listener) + `heartbeat/` (The Pulse) |
| **Semantic Kernel** | **Plugins & Skills** | `effectors/` (The Skills) |
| **Guardrails AI** | **Input/Output Rails** | `immune_system/` (The Rails) |
| **Ragas** | **Evaluation & Metrics** | `venom_lab/` (The Test Suite) |
| **LlamaIndex** | **Data Connectors & Indices** | `digestion_pool/` (Connectors) + `memory/` (Indices) |

## 2. The New 8 Pillars (Gen 63 Structure)

We assimilate these concepts into our **Fractal Octree**.

### 🧠 1. `brain/` (Navigator)
*   **SOTA Concept**: **The Control Plane / State Machine**.
*   **Contents**: Gherkin Features (Intent), LangGraph Definitions (Flows), Manifestos.
*   **Why**: In SOTA, "Code is Liability, Config is Asset". The Brain is pure Config/Intent.

### 📡 2. `sensors/` (Observer)
*   **SOTA Concept**: **Event Triggers / Webhooks**.
*   **Contents**: NATS Listeners (JetStream), FastAPI Ingress, File Watchers.
*   **Why**: Agents shouldn't poll. They should react to *Events*. Sensors turn chaos into Events.

### 💾 3. `memory/` (Bridger)
*   **SOTA Concept**: **The Context Window / Vector Store**.
*   **Contents**: LanceDB (Vector), SQLite (Relational), Knowledge Graph (NetworkX).
*   **Why**: "Retrieval Augmented Generation" (RAG) is the standard. Memory is the RAG backend.

### 🦾 4. `effectors/` (Shaper) - *Renamed from `forge`*
*   **SOTA Concept**: **Tools / Plugins / Skills**.
*   **Contents**: MCP Servers, Python Functions, API Clients.
*   **Why**: In Cybernetics, a system has **Sensors** (Input) and **Effectors** (Output). This is where the AI *touches* the world.

### 💓 5. `heartbeat/` (Injector) - *Renamed from `pulse`*
*   **SOTA Concept**: **Orchestrator / Runtime**.
*   **Contents**: Temporal Workflows (Durable), Ray Actors (Parallel), LangGraph Runners (Stateful).
*   **Why**: The "Agent" is just a file. The `heartbeat` is the CPU time that makes it run.

### 🧪 6. `venom_lab/` (Disruptor) - *Renamed from `venom`*
*   **SOTA Concept**: **Evaluation (Evals) / Red Teaming**.
*   **Contents**: Ragas Metrics, Chaos Scripts, Unit Tests, "Adversarial Agents".
*   **Why**: You cannot trust an LLM. You must constantly inject "Venom" (Stress) to test its immunity.

### 🛡️ 7. `immune_system/` (Immunizer) - *Renamed from `carapace`*
*   **SOTA Concept**: **Guardrails / Validators**.
*   **Contents**: Instructor (Pydantic), OPA Policies, Secret Management.
*   **Why**: "Hallucination" is a security risk. The Immune System blocks bad outputs *before* they reach the Effectors.

### ♻️ 8. `digestion_pool/` (Assimilator) - *Renamed from `digest`*
*   **SOTA Concept**: **ETL Pipelines / Data Engineering**.
*   **Contents**: Unstructured.io scripts, PDF parsers, Web Scrapers.
*   **Why**: Garbage In, Garbage Out. Raw data must be "digested" into clean Markdown/Vectors before entering Memory.

## 3. The "Assimilation" Strategy
We do not need to write everything from scratch. We wrap SOTA libraries in our Organs.

*   **`heartbeat/`** wraps **Temporal** (Durable) & **LangGraph** (Logic) & **Ray** (Scale).
*   **`memory/`** wraps **LanceDB**.
*   **`immune_system/`** wraps **Instructor**.
*   **`venom_lab/`** wraps **Pytest/Ragas**.
*   **`sensors/`** wraps **NATS JetStream**.

## 4. Migration Plan
1.  **Update Registry**: `REGISTRY.yaml` with new names.
2.  **Update Enforcer**: `structure_enforcer.py` to handle the rename (move files if they exist).
3.  **Execute**: Run the enforcer to reshape the directory.

