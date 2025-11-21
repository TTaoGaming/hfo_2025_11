# 🦅 Hive Fleet Obsidian: Agent Coordination Protocol (AGENTS.md)

> **Status**: Active (Gen 50 Phoenix Protocol)
> **Access**: All HFO Agents (Swarmlord, Builders, Disruptors)

## 🧠 Context & Prime Directives

We are executing **Generation 50 (The Evolutionary Forge)**. This is a "Phoenix" reboot—a clean slate implementation powered by ancestral wisdom.

### The Golden Rule: Intent vs. Implementation
1.  **The Overmind (User)** defines **INTENT** (What & Why) using Gherkin, Mermaid, and Pydantic.
2.  **The Swarm (You)** executes **IMPLEMENTATION** (How) using the R.A.P.T.O.R. stack.

### Agent Instructions
*   **Read First**: Before taking action, verify the current Intent in `brain/`.
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

### 🛡️ Hybrid Stability Protocol (Anti-Fragile)
*To prevent memory crashes and networking fragility, we use a split-brain architecture:*
1.  **Infrastructure (Docker)**: Postgres (5435), Temporal (7235), NATS (4225). Isolated & Clean.
2.  **Agents (Host)**: Python 3.10+ running locally. Fast & Stable.
*   **Setup**: Run `./setup_hybrid.sh` to launch infrastructure and create venv.
*   **Verify**: Run `source venv/bin/activate && python src/smoke_test.py`.

---

## 📋 HFO MOBS (Mini Obsidian Blackboard with Stigmergy Pattern)

*Agents: Append your status, findings, or handoffs here. Use this to coordinate asynchronously.*

| Timestamp | Agent ID | Signal / Message | Status |
| :--- | :--- | :--- | :--- |
| 2025-11-20 | Swarmlord | Protocol initialized. Awaiting Gherkin/Mermaid definitions. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Mission Update**: Setup T.R.A.M.E. stack for 10-agent Byzantine Quorum via OpenRouter. Target: Scalability to 1M+ agents. | 🟡 In Progress |
| 2025-11-20 | Swarmlord | **Architecture Update**: R.A.P.T.O.R. Stack initialized. Pydantic SSOT models (`src/models/`) deployed. Gherkin/Mermaid Intent definitions (`intent/`) complete. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Verification**: Implemented `pytest-bdd` step definitions for `intent/swarm_workflow.feature`. SWARM Loop logic is now executable and passing tests. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Protocol Update**: Modified SWARM Loop to inject Disruptors during 'Act' phase and use DSPy for prompt evolution in 'Mutate' phase. | 🟢 Active |
| 2025-11-20 | Swarmlord | **SSOT Alignment**: Updated Pydantic models (`MissionIntent`, `SwarmState`) to strictly enforce Gherkin definitions (Disruptor config, DSPy state). | 🟢 Active |
| 2025-11-20 | Swarmlord | **Security & Config**: Created `.env` (git-ignored) for keys and `src/config/models.yaml` for the weekly model registry. | 🟢 Active |
| 2025-11-20 | Swarmlord | **FinOps Protocol**: Established `docs/FINOPS_STRATEGY.md`. Strict split between Navigator (Gemini 3/GPT-5.1) and Swarm (Grok 4.1/GPT-OSS). | 🟢 Active |
| 2025-11-20 | Swarmlord | **Model Strategy Update**: Simplified to "Cheap Navigators" (Grok/GPT-5 Mini) and "Cheap QD Swarm" (5 Families: xAI, OpenAI, Google, Qwen, DeepSeek). | 🟢 Active |
| 2025-11-20 | Swarmlord | **Formalization**: Updated `intent/swarm_workflow.feature` and `src/models/intent.py` to strictly enforce "Cheap Navigators" and "Cheap QD Swarm" strategy. Excluded Gemini 3 Pro from swarm. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Deep Verification**: Initiating comprehensive "Hello World" tests for every component of the R.A.P.T.O.R. stack to ensure end-to-end functionality. | 🟡 In Progress |
| 2025-11-20 | Swarmlord | **Verification Complete**: R.A.P.T.O.R. stack verified via `tests/test_raptor_deep.py`. Ray, LangGraph, Pydantic, Ribs, LangSmith all GREEN. Temporal skipped (env). | 🟢 Active |
| 2025-11-20 | Swarmlord | **Strategic Pivot**: Prioritizing **NATS JetStream (Stigmergy)** over GraphRAG. Rationale: "The Bus builds the Brain." We need coordination to construct the memory graph. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Intent Definition**: Formalized Stigmergy Layer via `intent/stigmergy_layer.feature` and `intent/stigmergy_architecture.mmd`. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Documentation Update**: Enforced "Mermaid in Markdown" standard. Replaced `.mmd` with `intent/stigmergy_architecture.md` for better previewability. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Intent Definition**: Formalized Memory GraphRAG System via `intent/memory_graphrag.feature` and `intent/memory_architecture.md`. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Infrastructure Update**: Shifted to "Hybrid Stability Protocol". Infrastructure (DB, Temporal, NATS) runs in Docker on safe ports (5435, 7235, 4225). Agents run on Host. Smoke tests GREEN. | 🟢 Active |
| 2025-11-20 | Swarmlord | **System Verified**: Full R.A.P.T.O.R. stack (Ray, Temporal, NATS, Pydantic, Instructor, LangGraph, LangSmith, PGVector) + DSPy + GitOps verified via `make test-all`. Stigmergic GraphRAG architecture formalized. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Metamorphosis Complete**: File system restructured into Biological Anatomy (Brain, Eyes, Body, Memory, Carapace, Venom). | 🟢 Active |
| 2025-11-20 | Swarmlord | **Incident Report**: Agent freeze detected during "Smart Cleanup" planning. Resuming operations. | 🟡 Recovering |
| 2025-11-20 | Swarmlord | **Genesis Protocol**: Implemented `genesis.py` for single-command bootstrapping. Anatomy Scan & Smoke Tests verified (Infra: GREEN, LLM: SKIPPED). | 🟢 Active |
| 2025-11-20 | Swarmlord | **Neural Codex**: Implanted `README.md` "Brain Stems" in all organs (Brain, Eyes, Body, Memory, Carapace, Venom) for AI/Human navigation. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Organ Factory**: Implemented `body/blood/generate_readmes.py` to inoculate HFO DNA into all organs. System is now self-documenting and resilient. | 🟢 Active |
| 2025-11-20 | Swarmlord | **Handoff Prep**: Verified system integrity via Genesis Protocol. Pre-commit hooks active for regression testing. | 🟢 Active |

---

## 🧠 Memory Architecture: Stigmergic GraphRAG
*The "Hybrid" approach combining speed and depth.*

1.  **Fast Loop (Episodic)**: Agents emit signals to **NATS JetStream**. This is the "Hot State" (last 5 mins).
2.  **Slow Loop (Semantic)**: An **Assimilator Agent** consumes the stream and builds a **Knowledge Graph** in Postgres.
    *   **Graph**: `NetworkX` structure stored in Postgres (Nodes/Edges).
    *   **Vector**: `pgvector` embeddings for semantic search.
3.  **Retrieval**: Agents query the Graph/Vector DB for "Cold State" (Long-term wisdom).
