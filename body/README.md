# 🦾 The Body (The Swarm)

> **Role**: The Swarm / Executor
> **JADC2 Mapping**: Decider / Effector
> **Gherkin Source**: `brain/swarm_workflow.feature`

## 🧬 Biological Function
The **Body** is the engine of **Execution**. It turns the Brain's intent into reality via three systems: Nerves, Hands, and Blood.

## 📂 Contents
*   `nerves/`: Signal routing.
*   `hands/`: Tools and agents.
*   `blood/`: Logistics and infra.
*   `models/`: Pydantic data models.

## 🤖 Agent Instructions
*   **Action**: This is where work happens.
*   **Coordination**: Use `nerves` to talk to other agents.

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
