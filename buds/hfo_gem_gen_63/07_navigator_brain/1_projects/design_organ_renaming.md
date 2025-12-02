---
holon:
  id: hfo-design-organ-renaming
  type: design
  status: draft
  generation: 63
  author: Swarmlord
  theme: Biological SOTA Architecture
---

# 🧬 Design: The Organ System (Renaming & Alignment)

> **Objective**: Align the "Obsidian Roles" (Metaphysical) with "Biological Organs" (Physical Directories) and "SOTA AI Platform Components" (Technical).

## 1. The Philosophy: "Biology is the ultimate Tech Stack"
A SOTA AI Platform is an organism. It needs to sense, think, act, remember, and protect itself.
We are renaming the physical directories to better reflect their **function** in a self-healing, autonomous system.

## 2. The Mapping: Roles vs. Organs vs. Tech

| Obsidian Role (The Soul) | Old Organ (Gen 61) | **New Organ (Gen 63)** | **SOTA Component (The Tech)** | Description |
| :--- | :--- | :--- | :--- | :--- |
| **1. Navigator** | `brain/` | **`brain/`** | **Control Plane / Intent Store** | Gherkin features, Manifestos, Strategy. The "Why" and "What". |
| **2. Observer** | `eyes/` | **`sensors/`** | **Telemetry & Ingress** | NATS Listeners, Webhooks, Pollers, Log Aggregators. The "Input". |
| **3. Bridger** | `memory/` | **`memory/`** | **State Store / Knowledge Graph** | LanceDB (Vector), SQLite (Relational), Markdown (Docs). The "Context". |
| **4. Shaper** | `forge/` | **`tools/`** (or `actuators/`) | **Tool Registry / MCP Servers** | Python Scripts, API Clients, Bash Wrappers. The "Output". |
| **5. Injector** | `pulse/` | **`heartbeat/`** | **Orchestrator / Scheduler** | Temporal Workflows, Cron Jobs, The Main Loop. The "Time". |
| **6. Disruptor** | `venom/` | **`entropy/`** (or `labs/`) | **Evaluation & Red Teaming** | Unit Tests, Chaos Monkey, Drift Detectors. The "Stress". |
| **7. Immunizer** | `carapace/` | **`immune_system/`** | **Governance & Guardrails** | Pydantic Models, Config, Auth, PII Filters. The "Defense". |
| **8. Assimilator** | `digest/` | **`digestion_pool/`** | **ETL & Data Engineering** | RAG Pipelines, Document Parsers, Normalizers. The "Metabolism". |

## 3. Deep Dive: The New Organs

### 🧠 `brain/` (Navigator)
*   **Tech**: Markdown, Gherkin.
*   **Role**: Pure Intent. No code. This is the "Constitution" of the AI.

### 📡 `sensors/` (Observer) - *Was `eyes/`*
*   **Tech**: Fast Python scripts, NATS subscribers.
*   **Role**: "Active Listening". It converts external chaos (Web, API, Logs) into internal order (Standardized Signals).

### 💾 `memory/` (Bridger)
*   **Tech**: LanceDB, NetworkX, SQLite.
*   **Role**: The "Graph". It links Concepts (Nodes) to Data (Vectors). It is the "Source of Truth".

### 🛠️ `tools/` (Shaper) - *Was `forge/`*
*   **Tech**: MCP Servers, Python Functions.
*   **Role**: "Capabilities". These are the hands. They *do* things. They are stateless and functional.

### 💓 `heartbeat/` (Injector) - *Was `pulse/`*
*   **Tech**: Asyncio Loops, Temporal.
*   **Role**: "Liveness". It ensures the system doesn't freeze. It pumps signals (`hfo.heartbeat`) to keep the `sensors` and `tools` synchronized.

### 🧪 `entropy/` (Disruptor) - *Was `venom/`*
*   **Tech**: Pytest, Adversarial Scripts.
*   **Role**: "Evolution Pressure". It actively tries to break the system (Chaos Engineering) to prove it is Antifragile.

### 🛡️ `immune_system/` (Immunizer) - *Was `carapace/`*
*   **Tech**: Pydantic, Instructor, OPA (Open Policy Agent).
*   **Role**: "Validation". It checks every input and output. It rejects "Hallucinations" and "Malware". It holds the `config.py`.

### ♻️ `digestion_pool/` (Assimilator) - *Was `digest/`*
*   **Tech**: Unstructured.io, LlamaIndex.
*   **Role**: "Nutrient Extraction". It takes raw dumps (PDFs, HTML) and turns them into clean Markdown/Vectors for `memory`.

## 4. Migration Action Plan
1.  **Rename Directories**:
    *   `eyes/` -> `sensors/`
    *   `carapace/` -> `immune_system/`
    *   `digest/` -> `digestion_pool/`
    *   `pulse/` -> `heartbeat/`
    *   `forge/` -> `tools/` (Optional: Do you prefer `forge` or `tools`?)
    *   `venom/` -> `entropy/` (Optional: Do you prefer `venom` or `entropy`?)
2.  **Update Registry**: Modify `REGISTRY.yaml` to reflect new paths.
3.  **Update Enforcer**: Ensure `structure_enforcer.py` respects the new schema.
