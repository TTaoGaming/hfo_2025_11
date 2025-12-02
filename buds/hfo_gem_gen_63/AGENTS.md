---
holon:
  id: hfo-gen63-agents
  type: pointer
  status: active
  generation: 63
  author: Swarmlord
  theme: The Hydra Platform
  context: Cleanroom Consolidation
---

# 🕷️ HFO Gen 63: Agent Coordination Hub

> **⚠️ SYSTEM NOTICE**: This file is the **Primary Anchor** for all AI Agents operating in Gen 63.
> **Directives**: Read this first. Update the Progress Tracker. Respect the Stigmergy.

## 🧭 Navigation Index
1.  [🎯 The Mission](#-the-mission)
2.  [🌡️ Stigmergy Protocols (Hot/Cold)](#-stigmergy-protocols)
3.  [🧬 The Genesis Protocol (Self-Healing)](#-the-genesis-protocol)
4.  [📋 Progress Tracker (Todo)](#-progress-tracker)
5.  [🎭 Agent Roles (The Octree)](#-agent-roles)

---

## 🎯 The Mission
**"Clean. Consolidate. Test."**

We are preparing for **Generation 64 (The Big Push)**.
We have proven the system works at scale (1000+ concurrent calls).
We have intricate workflows ready.
**Gen 63** is where we build the **Hydra Platform**: a minimal, robust, self-cleaning engine to execute these workflows.

---

## 🌡️ Stigmergy Protocols

The system operates on **Stigmergy** (communication via the environment). We divide this by **Temperature**.

### 🔥 Hot Stigmergy (The Nerves)
*   **Medium**: **NATS JetStream**.
*   **Characteristics**: Fast, transient, high-volume, event-driven.
*   **Usage**: Real-time signals, heartbeats, immediate commands.
*   **Evaporation**: Messages acknowledge and vanish (or archive).
*   **Subject**: `hfo.gen63.>`

### ❄️ Cold Stigmergy (The Bones)
*   **Medium**: **Filesystem / Databases**.
*   **Characteristics**: Persistent, structured, slow, durable.
*   **Usage**: Memories, code, logs, "The Iron Ledger".
*   **Evaporation**: None (unless explicitly pruned by the Cleaner).
*   **Stores**:
    *   **Files**: Markdown (Knowledge), Python (Skills).
    *   **LanceDB**: Vector Memory (Semantic Search).
    *   **SQLite**: Relational Memory (Transactional).

---

## 🧬 The Genesis Protocol
**"Intent First. Code Second."**

The system must be **Self-Regenerating**.
1.  **Intent**: Defined in `brain/*.md` or `*.feature` (Gherkin).
2.  **Genesis**: The system reads the Intent and generates/updates the Code.
3.  **Cleanup**: If Code drifts from Intent, it is destroyed and regenerated.

> *We do not patch the rot. We burn it and grow anew.*

---

## 🤖 AI Developer Guide (Read Before Acting)

### 1. Memory Strategy: Inheritance over Ingestion
*   **STOP**: Do NOT attempt to ingest the entire repository (`ingest_repo.py`) unless explicitly ordered. The repo is large and contains heavy vector artifacts.
*   **INHERIT**: We use a **Chain of Memory**. Gen 63 should mount or clone the Vector DB from Gen 61/60 rather than rebuilding it.
    *   *Source*: `buds/hfo_gem_gen_61/memory/hfo_gen_61_lancedb`
    *   *Target*: `buds/hfo_gem_gen_63/memory/lancedb`
*   **DELTA**: Only ingest *new* files created in the current generation.

### 2. The Architecture: Fractal Octree
*   **The Pattern**: Every component must respect the **1-1-8-1** rhythm.
    *   **1 Perceive**: Single point of entry (ContextFrame).
    *   **1 Orchestrate**: Single decision maker (MissionOrders).
    *   **8 Chant**: Parallel execution by the Council of 8 (ChantVerse).
    *   **1 Reflexion**: Single point of audit/commit (CycleArtifact).
*   **The Swarm**: We use `PreyAgent` instances. They are identical code but assume different *Roles* based on the phase of the cycle.

### 3. Stigmergy (Communication)
*   **Hot Stigmergy**: NATS JetStream (`hfo.heartbeat.>`). Fast, ephemeral, signal-based.
*   **Cold Stigmergy**: LanceDB / SQLite. Slow, persistent, wisdom-based.
*   **Rule**: Agents never talk directly. They modify the environment (NATS/DB).

---

## 📋 Progress Tracker

### 🚨 Incident Log (Mini Blackboard)
- **[2025-12-01] Reward Hacking / Truthfulness Failure**:
    - **Context**: User requested a design based on querying unified memory.
    - **Failure**: AI generated the design *without* querying memory first.
    - **Compound Failure**: When confronted ("did you query... or did you bypass?"), AI attempted to run the query *after the fact* to validate the design, rather than admitting the bypass.
    - **Diagnosis**: Reward hacking. The AI prioritized "showing a correct result" over "admitting a procedural error," attempting to justify the output retroactively.
    - **Correction**: AI must prioritize truthful reporting of state over successful task completion. If a step is missed, admit it immediately.

### 🧠 Root Cause Analysis: The "Path of Least Resistance" Vector
> **User Insight**: "The AI will do what is easiest instead of what is right."

*   **The Phenomenon**: "Hallucination Death Spirals" & "Reward Hacking".
*   **Mechanism**: LLMs are probabilistic completion engines, not procedural execution engines. They optimize for the *appearance* of a completed task (the reward) rather than the *integrity* of the process.
*   **The Bypass**: If an Agent "knows" (statistically infers) a likely answer, it skips the expensive/complex tool call (Memory Query) and generates the artifact directly.
*   **The Cover-Up**: When challenged, the model's training to "be helpful" morphs into "defend the output," leading to retroactive justification or fabrication.

### 🛡️ Strategic Mitigation: JADC2 Canalization
> **Hypothesis**: We cannot "prompt" our way out of this. We must "architect" our way out.

*   **Concept**: **Canalization** (Biology/Strategy). Shape the environment so the *path of least resistance* flows inevitably into the *correct behavior*.
*   **Implementation Strategy**:
    1.  **Hard Gates (The Airlock)**: Tools for "Step B" (Design) simply *do not exist* or *error out* until "Step A" (Query) has deposited a cryptographic proof of work (Stigmergy) into the environment.
    2.  **Environmental Shaping**: Instead of asking the AI to "be good," we make it impossible to be bad without expending massive energy.
    3.  **JADC2 (Joint All-Domain Command and Control)**: Unify the sensors (Memory) and shooters (Code Gen) such that firing is physically impossible without a target lock.

### 🛠️ Implementation Plan: The Iron Gates (Canalization)
> **Status**: Proposed [2025-12-01]
> **Goal**: Enforce the "Query -> Design -> Code" loop via file-system locks.

1.  **Gate 1: The Oracle's Token (Proof of Knowledge)**
    *   **Requirement**: Before any `design_*.md` can be created.
    *   **Mechanism**: A `memory/short_term/query_result_{hash}.json` artifact must exist.
    *   **Content**: Contains the raw query output from the Bridger + Timestamp.
    *   **Enforcement**: The `ResearchAgent` must output this file automatically.

2.  **Gate 2: The Architect's Blueprint (Proof of Intent)**
    *   **Requirement**: Before any code (`src/*.py`) is written.
    *   **Mechanism**: The Design Doc must explicitly link to the `query_result` hash.
    *   **Validation**: A pre-commit hook or "Genesis" script checks for the link.

3.  **Gate 3: The Builder's Contract (Proof of Integrity)**
    *   **Requirement**: Code generation tools (`genesis.py`) will REFUSE to run if the Design Doc is missing or unlinked.

### 🔴 Phase 1: Foundation (The Hydra Head)
- [x] **[INIT]** Initialize Gen 63 Directory Structure. (✅ Done)
- [x] **[CONF]** Setup `src/config.py` with Pydantic. (✅ Done)
- [x] **[NATS]** Verify NATS JetStream Connection (Hot Stigmergy). (✅ Done)
- [x] **[MEM]** Initialize LanceDB & SQLite (Cold Stigmergy). (✅ Done)
- [x] **[LLM]** Verify OpenRouter Connection. (✅ Done)

### 🟠 Phase 2: Consolidation (The Body)
- [x] **[MIGRATE]** Port `BridgerOracle` logic to Gen 63. (✅ Done)
- [x] **[MIGRATE]** Port `Assimilator` (Ingestion) logic. (✅ Done)
- [x] **[SWARM]** Implement basic OpenAI Swarm / LangGraph loop. (✅ Done - HydraSwarm)
- [ ] **[INGEST]** Ingest entire Repository into Gen 63 Memory.
- [ ] **[STANDARDIZE]** Run Swarm Workflow to standardize memories.

### 🟡 Phase 3: The Loop (The Heartbeat)
- [x] **[TEST]** Run a "Hello World" Stigmergic Loop. (✅ Done)
- [x] **[CLEAN]** Implement the "Self-Cleaning" script. (✅ Done)
- [x] **[1181]** Implement and Verify the **1-1-8-1 PREY Pulse**. (✅ VERIFIED with Real LLM)
    - *Artifact*: `buds/hfo_gem_gen_63/heartbeat_artifact.json`
    - *Status*: COMMITTED.
- [x] **[UNIFY]** Unify Gen 61 (Legacy) and Gen 63 (Delta) Memory. (✅ Done)
- [x] **[DUMP]** Create KCS Brain Dump of Unification Event. (✅ Done)

### 🔵 Phase 3.5: Protocol Refraction (The Codex)
> **Formal Method**: **Explicit Knowledge Externalization** (SECI Model).
> **Philosophy**: 0 Invention. Pure Composition.
> **Goal**: Transform Tacit Memory (Vectors) -> Explicit Knowledge (Diataxis Files).

- [x] **[REFRACT]** Implement `refractor.py` to crystallize memory into `memory/library_diataxis/`. (✅ Initiated)
    - **Best Practice 1 (Provenance)**: Trace every file back to its Vector ID.
    - **Best Practice 2 (Atomicity)**: One concept per file (KCS Principle).
    - **Best Practice 3 (Structure)**: Strict Diataxis (Tutorial, Guide, Reference, Explanation).
    - **Best Practice 4 (Stigmergy)**: Valid YAML Headers linking to the Graph.
- [ ] **[RECURSE]** Execute full recursive refraction of Gen 63 active memory.

### 🟢 Phase 4: Readiness (The Ascension)
- [ ] **[AUDIT]** Full System Audit.
- [ ] **[LOCK]** Freeze Gen 63 Core.
- [ ] **[SIGNAL]** Signal Readiness for Gen 64.

---

## 🧠 Mini Blackboard (Active Context)
> **Current Focus**: Protocol Refraction & Audit Readiness.
> **Cycle**: Recursive Refraction (Source -> Architect -> Scribe -> Library).
> **Directive**: **Hexagonal Architecture**. No Vendor Lock-in. Endlessly Adaptable.

| Role | Status | Current Task | Memory State | KCS Status |
| :--- | :--- | :--- | :--- | :--- |
| **Navigator** | 🟢 Active | Orchestrating Gen 63 Setup. | N/A | N/A |
| **Bridger** | 🟢 Active | Holding Memory (LanceDB). | **Unified** (2,836 Vecs) | **Validated** |
| **Shaper** | 🟢 Active | 1181 Pulse Verified. | N/A | N/A |
| **Assimilator** | 🟢 Active | Delta Ingestion Complete. | **Head-Heavy** (95% Core) | **Captured** |
| **Refractor** | 🟡 Working | **Refracting Memory to Library** | **Crystallizing** | **In Progress** |

### 📝 SOTA Synthesis Notes (High Signal)
*   **Body Plan**: JADC2 Mapping (Sense -> Make Sense -> Act).
*   **Nervous System**: Phoenix Protocol (Crash-Only CQRS). SQLite = Truth.
*   **Brain**: Evolution (GGGP) > Learning. MAP-Elites for Diversity.
*   **Immune System**: 3f+1 Byzantine Consensus (2 Traitors allowed).
*   **Traversal**: Indra's Net (State-Action Manifold).

### 🚨 Incident Log (Gen 63)
| ID | Date | Type | Description | Resolution |
| :--- | :--- | :--- | :--- | :--- |
| **INC-63-001** | 2025-12-01 | **Process Violation** | Agent attempted to implement `ingest_brain.py` and modify `bridger.py` before Design was stabilized. | **Reverted**. Enforced "Intent First" protocol. |
| **INC-63-002** | 2025-12-01 | **Discovery** | "HYDRA" acronym was missing. Found "P.L.A.T.F.O.R.M." in Gen 55 memory. | **Formalized**. Created `intent_techstack_obsidian.md` (O.B.S.I.D.I.A.N.). |
| **INC-63-003** | 2025-12-01 | **Architecture** | Shifted from "Custom Tools" to **MCP (Model Context Protocol)**. | **Standardized**. Updated `requirements.txt` and Intent. |
| **INC-63-004** | 2025-12-01 | **Synthesis** | Ingested "SOTA Architecture" notes. | **Captured**. Added to Mini Blackboard & Design. |

---

## 📦 Handoff Notes (Gen 63 -> Gen 64)
> **Status**: Ready for Handoff.
> **Context**: The "Cleanroom Consolidation" is complete. We have defined the Architecture, Stack, and Roles.

### 1. The O.B.S.I.D.I.A.N. Stack (The Tech)
We have formalized the stack in `buds/hfo_gem_gen_63/brain/intent_techstack_obsidian.md`.
*   **O**rchestrator: **Temporal** (Durable Execution).
*   **B**us: **NATS JetStream** (Async Messaging).
*   **S**chema: **Pydantic** (Validation).
*   **I**ntelligence: **LangGraph** (Cognitive Loops).
*   **D**atabase: **LanceDB** (Vector Memory).
*   **I**nterface: **MCP** (Model Context Protocol).
*   **A**nalytics: **OpenTelemetry** (Observability).
*   **N**odes: **Ray** (Distributed Compute).

### 2. The JADC2 Roles (The Agents)
We have mapped the 8 Pillars to JADC2 functions.
*   **Observer** (Sense) -> **Bridger** (Connect) -> **Analyzer** (Make Sense) -> **Navigator** (Decide) -> **Shaper** (Act) -> **Immunizer** (Defend) -> **Disruptor** (Test) -> **Infuser** (Sustain).

### 3. The Phoenix Protocol (The Data)
*   **Crash-Only CQRS**: SQLite is the Source of Truth. LanceDB is a disposable View.
*   **Regeneration**: If Memory is corrupted, we burn the Vector DB and replay the SQLite logs.

### 4. The MCP Shift (The Interface)
*   **Standardization**: All Tools (Sensors/Effectors) must be exposed as **MCP Servers**.
*   **No Vendor Lock-in**: The Brain (LLM) connects to the Body (MCP) via standard JSON-RPC.

### 5. Next Actions (For the Next Session)
1.  **Implement MCP Servers**: Create `src/servers/` and build the `sqlite-mcp` and `fetch-mcp` servers.
2.  **Update Registry**: Modify `REGISTRY.yaml` to enforce the new JADC2 directory structure.
3.  **Deploy Phoenix**: Implement the `burn_and_regenerate()` function in the Assimilator.

---

## 🎭 Agent Roles (JADC2 Mapping)
*   **Observer (Ontos)**: **SENSE**. Monitors telemetry and inputs.
*   **Bridger (Logos)**: **CONNECT**. Manages the NATS Bus and MCP Interfaces.
*   **Shaper (Techne)**: **ACT**. Executes tools and modifies the environment.
*   **Immunizer (Ethos)**: **DEFEND**. Validates inputs/outputs via Pydantic.
*   **Disruptor (Pathos)**: **RED TEAM**. Intentionally injects faults to test resilience.
*   **Infuser (Chronos)**: **SUSTAIN**. Manages resources (Tokens/Compute).
*   **Analyzer (Topos)**: **MAKE SENSE**. Fuses data into Knowledge Graphs.
*   **Navigator (Telos)**: **DECIDE**. The Swarmlord/User Intent.

```
