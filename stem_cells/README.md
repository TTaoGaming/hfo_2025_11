# 🧬 Stem Cells (Regenerator)

> **Role**: Regenerator / Factory
> **JADC2 Mapping**: Logistics (Reserve)
> **Gherkin Source**: `brain/antifragile_strategy.feature`

## 🧬 Biological Function
The **Stem Cells** are the **Source of Truth for Regeneration**. They contain the blueprints for spawning new agents and organs.

## 📂 Contents
*   `agents/`: Micro-scale blueprints.
*   `organs/`: Meso-scale blueprints.
*   `hive/`: Macro-scale blueprints.

## 🤖 Agent Instructions
*   **Preserve**: Keep these blueprints pure.
*   **Clone**: Use these to restore lost functionality.

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
