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

- [ ] **[REFRACT]** Implement `refractor.py` to crystallize memory into `memory/codex/`.
    - **Best Practice 1 (Provenance)**: Trace every file back to its Vector ID.
    - **Best Practice 2 (Atomicity)**: One concept per file (KCS Principle).
    - **Best Practice 3 (Structure)**: Strict Diataxis (Tutorial, Guide, Reference, Explanation).
    - **Best Practice 4 (Stigmergy)**: Valid YAML Headers linking to the Graph.

### 🟢 Phase 4: Readiness (The Ascension)
- [ ] **[AUDIT]** Full System Audit.
- [ ] **[LOCK]** Freeze Gen 63 Core.
- [ ] **[SIGNAL]** Signal Readiness for Gen 64.

---

## 🧠 Mini Blackboard (Active Context)
> **Current Focus**: System Audit & Readiness Signal.
> **Cycle**: 1-1-8-1 (Perceive -> Orchestrate -> Chant -> Reflexion).

| Role | Status | Current Task | Memory State | KCS Status |
| :--- | :--- | :--- | :--- | :--- |
| **Navigator** | 🟢 Active | Orchestrating Gen 63 Setup. | N/A | N/A |
| **Bridger** | 🟢 Active | Holding Memory (LanceDB). | **Unified** (2835 Vecs) | **Validated** |
| **Shaper** | 🟢 Active | 1181 Pulse Verified. | N/A | N/A |
| **Assimilator** | 🟢 Active | Delta Ingestion Complete. | **Head-Heavy** (95% Core) | **Captured** |


---

## 🎭 Agent Roles
*   **Navigator (0)**: The Swarmlord (User). Sets Intent.
*   **Bridger (2)**: The Interface. Connects Hot (NATS) and Cold (DB).
*   **Shaper (3)**: The Worker. Executes tools (Ray/Python).
*   **Assimilator (7)**: The Memory. Digests Hot signals into Cold wisdom.
