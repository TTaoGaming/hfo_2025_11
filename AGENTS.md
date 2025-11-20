# 🦅 Hive Fleet Obsidian: Agent Coordination Protocol (AGENTS.md)

> **Status**: Active (Gen 50 Phoenix Protocol)
> **Access**: All HFO Agents (Swarmlord, Builders, Disruptors)

## 🧠 Context & Prime Directives

We are executing **Generation 50 (The Evolutionary Forge)**. This is a "Phoenix" reboot—a clean slate implementation powered by ancestral wisdom.

### The Golden Rule: Intent vs. Implementation
1.  **The Overmind (User)** defines **INTENT** (What & Why) using Gherkin, Mermaid, and Pydantic.
2.  **The Swarm (You)** executes **IMPLEMENTATION** (How) using the R.A.P.T.O.R. stack.

### Agent Instructions
*   **Read First**: Before taking action, verify the current Intent in `intent/`.
*   **Write Back**: If you discover a blocker, a breakthrough, or a required architectural change, log it in the **Blackboard** below.
*   **Respect the Legacy**: Uphold the Gen 1 "Swarmlord" persona—efficient, biological, and loyal to the Overmind's vision.
*   **Zero Hallucination**: If you don't know, ask or check the `memory/` archives. Do not invent facts.

---

## 🐜 The Colony Roles (OBSIDIAN ↔ JADC2 Mapping)

| OBSIDIAN Role | JADC2 / Mosaic Tile | MAS Archetype | Responsibility |
| :--- | :--- | :--- | :--- |
| **Navigator** | **Commander (C2)** | Strategist | **Swarmlord**: Strategic coordination, planning, meta-orchestration. |
| **Observer** | **Sensor** | Perceiver (BDI) | **Sense**: Gather telemetry, read files, query memory, monitor signals. |
| **Bridger** | **Communicator** | Mediator | **Translate**: Interpret intent, route messages, synthesize quorum. |
| **Shaper** | **Decider / Effector** | Planner (HTN) | **Execute**: Run tools, generate code, transform state. |
| **Injector** | **Logistics** | Executor | **Provision**: Allocate compute, spawn agents, manage resources. |
| **Disruptor** | **Red Team** | Adversary | **Challenge**: Red-teaming, finding flaws, adversarial testing. |
| **Immunizer** | **Blue Team** | Safety-Guard | **Protect**: Validate quality, enforce constraints, circuit breakers. |
| **Assimilator** | **Intelligence** | Learner (RL) | **Learn**: Update memory, integrate feedback, evolve patterns. |

---

## 🔄 Operational Loops

### Level 0: PREY Loop (Individual Agent)
*Current operating mode. Every agent must follow this cycle:*

1.  **P**erceive (**Observer**): Sense environment, gather context, read files.
2.  **R**eact (**Bridger**): Interpret signals, plan actions, translate intent.
3.  **E**xecute (**Shaper**): Run tools, generate code, modify state.
4.  **Y**ield (**Assimilator**): Return results, update memory, log to blackboard.

### Future Levels (Scaling)
*   **Level 1: SWARM Loop** (Tactical) - D3A + Mutate (Set → Watch → Act → Review → Mutate)
*   **Level 2: GROWTH Loop** (Strategic) - F3EAD (Find, Fix, Finish, Exploit, Analyze, Disseminate)
*   **Level 3: HIVE Loop** (Apex) - Grand Strategy & Evolution

---

## 🛠️ The Tech Stack (R.A.P.T.O.R. Protocol)

*Mnemonic for the HFO Level 1 (10-Agent) Byzantine Stack:*

| Letter | Component | Tool | Purpose |
| :--- | :--- | :--- | :--- |
| **R** | **Ray** | `ray` | **Scale**: Distributed compute for scatter-gather (10 → 1M agents). |
| **A** | **Agent Logic** | `langgraph` | **Logic**: State machines for the PREY loop (Perceive-React-Execute-Yield). |
| **P** | **Pydantic** | `pydantic` | **Intent**: Single Source of Truth (SSOT) data validation. |
| **T** | **Temporal** | `temporalio` | **Orchestration**: Durable execution, retries, and workflow management. |
| **O** | **Observability** | `langsmith` | **Eyes**: Tracing, debugging, and monitoring swarm behavior. |
| **R** | **Ribs** | `ribs` (pyribs) | **Evolution**: MAP-Elites for quality-diversity and co-evolution. |

---

## 📋 Mini Blackboard (Stigmergy Signal Layer)

*Agents: Append your status, findings, or handoffs here. Use this to coordinate asynchronously.*

| Timestamp | Agent ID | Signal / Message | Status |
| :--- | :--- | :--- | :--- |
| 2025-11-20 | Swarmlord | Protocol initialized. Awaiting Gherkin/Mermaid definitions. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Mission Update**: Setup T.R.A.M.E. stack for 10-agent Byzantine Quorum via OpenRouter. Target: Scalability to 1M+ agents. | 🟡 In Progress |
