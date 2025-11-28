---
hexagon:
  ontos:
    id: 7183c26d-5ece-4314-9df3-55923397ab03
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:06.988905+00:00'
    generation: 51
  topos:
    address: memory/episodic/gen_50_archive/hfo_anatomy.md
    links: []
  telos:
    viral_factor: 0.0
    meme: hfo_anatomy.md
---


# 🧬 HFO Anatomy: The Biological Swarm

> **Status**: Active Intent
> **Context**: Defining the Hive Fleet Obsidian (HFO) as a biological organism. This maps SOTA AI Agent architecture to intuitive body parts.

## 🩸 The Circulatory System (Flow)
A SOTA swarm is not a static tool; it is a flow of information.
1.  **Light** (Data) enters the **Eyes**.
2.  **Signals** go to the **Brain** for processing.
3.  **Impulses** travel down **Nerves** to the **Hands**.
4.  **Actions** change the world.
5.  **Nutrients** (Feedback) are digested by **Memory**.

---

## 🫀 The Organ Registry

### 1. The Brain (`intent/`)
*   **Role**: **Navigator** (The Strategist)
*   **Function**: High-level planning, reasoning, and intent definition.
*   **SOTA Tech**: Chain-of-Thought (CoT), Gherkin Features, Pydantic Models.
*   **Stigmergy Signal**: `signal:directive` (Orders from above).

### 2. The Eyes (`ingestion/`)
*   **Role**: **Observer** (The Sensor)
*   **Function**: Ingesting raw data, monitoring file changes, scraping web.
*   **SOTA Tech**: Multimodal inputs (Text/Image), File Watchers.
*   **Stigmergy Signal**: `signal:stimulus` (New data detected).

### 3. The Nerves (`src/swarm/`)
*   **Role**: **Bridger** (The Communicator)
*   **Function**: Routing messages, managing state, connecting agents.
*   **SOTA Tech**: LangGraph State, NATS JetStream, Pub/Sub.
*   **Stigmergy Signal**: `signal:impulse` (Task routing).

### 4. The Hands (`src/tools/`)
*   **Role**: **Shaper** (The Executor)
*   **Function**: Interacting with the world. Writing code, running terminals.
*   **SOTA Tech**: Model Context Protocol (MCP), Function Calling.
*   **Stigmergy Signal**: `signal:action` (Tool execution).

### 5. The Blood (`src/config/`)
*   **Role**: **Injector** (The Supplier)
*   **Function**: Carrying resources (Prompts, Keys, Models) to organs.
*   **SOTA Tech**: Dependency Injection, Environment Variables.
*   **Stigmergy Signal**: `signal:nutrient` (Context injection).

### 6. The Skin (`docs/`)
*   **Role**: **Immunizer** (The Protector)
*   **Function**: Defining boundaries, enforcing standards, filtering output.
*   **SOTA Tech**: Guardrails, Linting, Static Analysis.
*   **Stigmergy Signal**: `signal:barrier` (Policy enforcement).

### 7. The Acid (`tests/`)
*   **Role**: **Disruptor** (The Tester)
*   **Function**: Breaking down weak code, adversarial testing, chaos.
*   **SOTA Tech**: Red Teaming, Fuzzing, Chaos Engineering.
*   **Stigmergy Signal**: `signal:catalyst` (Stress test).

### 8. The Memory (`memory/`)
*   **Role**: **Assimilator** (The Learner)
*   **Function**: Digesting experiences into wisdom.
*   **SOTA Tech**: Vector DB (pgvector), Knowledge Graph (NetworkX).
*   **Stigmergy Signal**: `signal:spore` (Long-term storage).

---

## 🔄 The Physiology (Loops)

### The Reflex Loop (Fast)
*   **Eyes** -> **Nerves** -> **Hands**
*   *Example*: "I see a syntax error (Eyes), I fix it (Hands)."

### The Cognitive Loop (Slow)
*   **Eyes** -> **Brain** -> **Nerves** -> **Hands** -> **Memory**
*   *Example*: "I see a complex user request. I plan a solution (Brain), execute it (Hands), and save the pattern (Memory)."

### The Immune Loop (Background)
*   **Skin** checks **Hands** output.
*   **Acid** attacks **Body** code.
*   **Memory** records the survivors.
