---
holon:
  id: obsidian-stack-v1
  type: intent
octagon:
  ontos:
    id: obsidian-stack-v1
    type: intent
    owner: Swarmlord
  logos:
    protocol: OBSIDIAN-STACK
    format: literate-gherkin
  techne:
    stack:
    - temporal
    - nats
    - pydantic
    - langgraph
    - lancedb
    - mcp
    - opentelemetry
    - ray
    complexity: high
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-12-01T12:00:00Z'
    generation: 63
  pathos:
    stress_level: 0.0
    validation: pending
  ethos:
    security_level: internal
    compliance:
    - hfo-standard-gen63
  topos:
    address: buds/hfo_gem_gen_63/brain/intent_techstack_obsidian.md
    links:
    - buds/hfo_gem_gen_63/brain/design_organ_renaming_v2.md
  telos:
    viral_factor: 1.0
    meme: The Body of the Spider.
---

# 🕷️ Intent: The OBSIDIAN Stack (O.B.S.I.D.I.A.N.)

> **Context**: Gen 63 (The MCP Era)
> **Philosophy**: "The Spider weaves the Web, but the Web holds the Spider."
> **Core Framework**: **JADC2** (Joint All-Domain Command and Control). The OBSIDIAN Stack is the *implementation* of the JADC2 architecture.
> **Objective**: To formalize the **O.B.S.I.D.I.A.N.** stack as the canonical implementation of the HFO Octree, integrating the **Model Context Protocol (MCP)** as a first-class citizen.

## ⚡ BLUF (Bottom Line Up Front)
The **OBSIDIAN Stack** is the unified Tech Stack for Gen 63. It evolves the Gen 55 "PLATFORM" by explicitly adopting **MCP** (Model Context Protocol) to standardize the interface between the Brain (LLM) and the Body (Tools). It maps the 8 letters of "OBSIDIAN" to the 8 Pillars of the Fractal Octree, which in turn implement the **JADC2** core functions (Sense, Make Sense, Act, etc.).

## 🏛️ The O.B.S.I.D.I.A.N. Matrix

| Letter | Mnemonic | HFO Role (Organ) | Primary Tool | The Universal Problem Solved |
| :--- | :--- | :--- | :--- | :--- |
| **O** | **Orchestrator** | **Navigator** (Telos) | **Temporal** | **Entropy**: Durable execution that survives crashes and long sleeps. |
| **B** | **Bus** | **Bridger** (Logos) | **NATS JetStream** | **Coupling**: Decoupled, asynchronous communication between Holons. |
| **S** | **Schema** | **Immunizer** (Ethos) | **Pydantic** | **Toxicity**: Enforces strict contracts (DNA) to prevent hallucination. |
| **I** | **Intelligence** | **Shaper** (Techne) | **LangGraph** | **Stochasticity**: Cyclic loops for structured reasoning and state management. |
| **D** | **Database** | **Assimilator** (Topos) | **LanceDB** | **Amnesia**: Provides Time-Travel Memory (Vector + SQL) for the Hive. |
| **I** | **Interface** | **Sensors/Effectors** | **MCP** | **Fragmentation**: Standardizes how the Brain connects to Tools and Context. |
| **A** | **Analytics** | **Observer** (Ontos) | **OpenTelemetry** | **Opacity**: Deep visibility into Metrics, Traces, and Evals. |
| **N** | **Nodes** | **Injector** (Chronos) | **Ray** | **Scarcity**: Elastic, distributed compute for parallel execution. |

## 📜 Declarative Intent (Gherkin)

```gherkin
Feature: The OBSIDIAN Stack
  As the Swarmlord
  I want to standardize the Tech Stack using the O.B.S.I.D.I.A.N. mnemonic
  So that the Hive has a "Self-Cleaning", "Biological", and "Standardized" architecture.

  Rule: O is for Orchestrator (The Navigator)
    Given the System Need is "Durable Execution"
    When a Workflow is initiated (e.g., "Research Topic")
    Then the Navigator must execute it using "Temporal"
    And the state must be persisted across failures.

  Rule: B is for Bus (The Bridger)
    Given the System Need is "Signal Propagation"
    When a Holon emits a "Pheromone" (Event)
    Then the Bridger must route it via "NATS JetStream"
    And the message must be durable and replayable.

  Rule: S is for Schema (The Immunizer)
    Given the System Need is "Validation"
    When data enters or leaves a Holon
    Then the Immunizer must validate it using "Pydantic"
    And any violation must trigger a "Rejection" signal.

  Rule: I is for Intelligence (The Shaper)
    Given the System Need is "Reasoning"
    When the Agent processes a task
    Then the Shaper must use "LangGraph" to define the cognitive loop
    And the loop must be cyclic (Plan -> Act -> Observe -> Reflect).

  Rule: D is for Database (The Assimilator)
    Given the System Need is "Memory"
    When the Swarm generates "Wisdom" (Artifacts)
    Then the Assimilator must persist it in "LanceDB"
    And the memory must be queryable via Vector Search.

  Rule: I is for Interface (The Sensors & Effectors)
    Given the System Need is "Tool Use"
    When the Brain needs to interact with the World (File System, Web, API)
    Then it must connect to an "MCP Server"
    And the protocol must be "Model Context Protocol" (JSON-RPC).

  Rule: A is for Analytics (The Observer)
    Given the System Need is "Observability"
    When the System is running
    Then the Observer must emit traces via "OpenTelemetry"
    And the traces must be visualized in a dashboard.

  Rule: N is for Nodes (The Injector)
    Given the System Need is "Scale"
    When the workload exceeds a single process
    Then the Injector must spawn "Ray Actors"
    And the actors must be distributed across the cluster.
```

## 🦅 Executive Digest

### The "MCP" Shift (The Second "I")
The most significant change in Gen 63 is the adoption of **MCP** (Model Context Protocol).
*   **Old Way**: We wrote custom Python functions (`@tool`) for the LLM. This created "Vendor Lock-in" and "Fragile Glue Code."
*   **New Way**: We treat every Organ as an **MCP Server**.
    *   The **Assimilator** is an MCP Server that exposes "Memory Tools" (Search, Store).
    *   The **Sensors** are MCP Servers that expose "Perception Tools" (Read File, Fetch URL).
    *   The **Effectors** are MCP Servers that expose "Action Tools" (Write File, Run Command).
    *   The **Brain** (LangGraph) simply connects to these servers via `stdio` or `sse`.

### The "Biological" Alignment
The **O.B.S.I.D.I.A.N.** stack aligns perfectly with the biological renaming:
*   **Navigator** -> Temporal (The Circadian Rhythm)
*   **Bridger** -> NATS (The Nervous System)
*   **Immunizer** -> Pydantic (The Immune System)
*   **Shaper** -> LangGraph (The Frontal Cortex)
*   **Assimilator** -> LanceDB (The Hippocampus)
*   **Sensors/Effectors** -> MCP (The Peripheral Nervous System)
*   **Observer** -> OpenTelemetry (The Senses)
*   **Injector** -> Ray (The Muscle Fibers)

### Next Actions
1.  **Update Registry**: Ensure `REGISTRY.yaml` reflects the new Organ names.
2.  **Update Requirements**: Ensure `requirements.txt` includes `mcp`, `temporalio`, `nats-py`, `ray`, `lancedb`, `langgraph`, `pydantic`, `opentelemetry-api`.
3.  **Implement MCP Servers**: Begin creating the `src/servers/` directory for our internal MCP servers.
