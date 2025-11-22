# 🧠 The Brain (Navigator)

> **Role**: Navigator / Strategist
> **JADC2 Mapping**: Commander (C2)
> **Gherkin Source**: `brain/gen50_core.feature`

## 🧬 Biological Function
The **Brain** is the seat of **Intent** and **Strategy**. It does not execute code; it defines *what* must be done. It holds the "Holocron" (Registry) and the Gherkin feature files.

## 📂 Contents
*   **Feature Files**: Gherkin specs (`*.feature`).
*   **Registry**: The SSOT (`registry.yaml`).
*   **Architecture**: Maps and diagrams.

## 🤖 Agent Instructions
*   **Read-Only**: Do not modify files here unless you are updating the Grand Strategy.
*   **Validation**: All actions in the `body/` must trace back to an intent defined here.

---
## 🧬 HFO DNA (System Context)
> **System**: Hive Fleet Obsidian (Gen 50)
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

### 📜 The Golden Rule
1.  **Intent (Brain)**: Defined in Gherkin/Mermaid.
2.  **Implementation (Body)**: Executed via R.A.P.T.O.R. stack.

### 🏆 The Golden Pattern (Async Swarm)
*   **Architecture**: NATS Queue Groups + AsyncIO Workers.
*   **Coordination**: Stigmergy (Read Stream -> Act -> Write Stream).
*   **Constraint**: NO blocking calls. NO synchronous loops.

### 🧬 Regeneration Protocol (Stem Cells)
If this system is corrupted or lost, use the **Genesis Script** to regenerate the Hive from this DNA:
```bash
python3 genesis.py --regenerate --source "https://github.com/TTaoGaming/hfo_2025_11"
```
