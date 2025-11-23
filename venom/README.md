# 🧪 The Venom (Disruptor)

> **Role**: Disruptor / Red Team
> **JADC2 Mapping**: Red Team
> **Gherkin Source**: `brain/immune_system.feature`

## 🧬 Biological Function
The **Venom** is the **Testing** and **Validation** suite. It injects chaos, runs tests, and ensures the system is robust.

## 📂 Contents
*   **Tests**: `pytest` suites.
*   **Chaos**: Scripts to break things.
*   **Reports**: Validation outputs.

## 🤖 Agent Instructions
*   **Sting**: Test everything.
*   **Verify**: Trust but verify.

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
