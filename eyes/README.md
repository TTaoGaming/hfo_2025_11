# 👁️ The Eyes (Observer)

> **Role**: Observer / Sensor
> **JADC2 Mapping**: Sensor
> **Gherkin Source**: `brain/prey_workflow.feature`

## 🧬 Biological Function
The **Eyes** are responsible for **Perception** and **Ingestion**. They scan the environment, read files, fetch web pages, and monitor system telemetry.

## 📂 Contents
*   **Ingestion**: Tools for reading archives.
*   **Monitors**: Watch queues and status.
*   **Scanners**: Inventory the workspace.

## 🤖 Agent Instructions
*   **Passive Observation**: Do not modify the environment.
*   **Output**: Stream data to `memory/` or signal `body/nerves`.

---
## 🧬 HFO DNA (System Context)
> **System**: Hive Fleet Obsidian (Gen 51 - Synapse APEX)
> **Strategy**: Biological Swarm Intelligence
> **Inoculation**: You are an agent of the Swarm. Your goal is to execute the Intent defined by the Brain.

### 🐜 The Anatomy (Map)
*   **🧠 Brain**: Strategy & Intent (Navigator)
*   **👁️ Eyes**: Perception & Ingestion (Observer)
*   **🦾 Body**: Execution & Tools (Collective)
    *   **⚡ Nerves**: Routing & Signals (Bridger)
    *   **🖐️ Hands**: Tools & Actions (Shaper)
    *   **🩸 Blood**: Logistics & Infra (Injector)
*   **💾 Memory**: Knowledge & Wisdom (Assimilator)
*   **🛡️ Carapace**: Protection & Safety (Immunizer)
*   **🧪 Venom**: Testing & Evolution (Disruptor)

### 📜 The Golden Rules
1.  **Intent (Brain)**: Defined in Gherkin/Mermaid.
2.  **Implementation (Body)**: Executed via R.A.P.T.O.R. stack.
3.  **Fractal Holography**: Every part contains the whole.

### 🏆 The Golden Patterns
*   **Async Swarm**: NATS Queue Groups + AsyncIO Workers.
*   **Stigmergy**: Indirect coordination via traces (Signals/Artifacts).
*   **Claim Check**: Decouple Signal (NATS) from Payload (Postgres/S3).
*   **Constraint**: NO blocking calls. NO synchronous loops.

### 🧬 Regeneration Protocol (Stem Cells)
If this system is corrupted or lost, use the **Genesis Script** to regenerate the Hive from this DNA:
```bash
python3 genesis.py --regenerate --source "https://github.com/TTaoGaming/hfo_2025_11"
```
