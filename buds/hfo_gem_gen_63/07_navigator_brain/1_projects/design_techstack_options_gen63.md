---
holon:
  id: hfo-gen63-techstack-options
  type: design
  status: draft
  author: Swarmlord
  generation: 63
---

# 🧬 Design: Gen 63 Tech Stack Options (The MCP Era)

> **Context**: Gen 63 requires a "Self-Cleaning," "Biological," and "Standardized" architecture.
> **New Constraint**: Must include **MCP (Model Context Protocol)** for standardized tool/context exposure.
> **Theme**: Hydra / Spider / Obsidian.

## 🦅 Executive Summary
We are moving from the **P.L.A.T.F.O.R.M.** (Gen 55) to a Gen 63 stack that embraces the **Model Context Protocol (MCP)**. MCP solves the "Tool Definition" problem by treating every Organ (Sensor, Effector, Memory) as an MCP Server that the Brain (LLM) connects to.

Here are 4 SOTA variants for the Gen 63 Stack.

---

## 🧪 Option 1: P.H.A.N.T.O.M. (The Evolution)
*A direct evolution of PLATFORM, emphasizing the "Ghost in the Machine" (The Agent).*

*   **P**: **Pydantic** (The Immune System - Schema & Validation)
*   **H**: **Host** (Ray - The Body/Compute)
*   **A**: **Agents** (LangGraph - The Cognitive Loops)
*   **N**: **NATS** (The Nervous System - JetStream Messaging)
*   **T**: **Temporal** (The Spine - Durable Execution)
*   **O**: **Observability** (OpenTelemetry - The Senses)
*   **M**: **MCP** (The Interface - Model Context Protocol)

> **Verdict**: **Strongest Contender**. It keeps the best of Gen 55 (NATS/Temporal/Ray) and explicitly adds MCP as the "M" anchor. It feels "Stealthy" and "Ubiquitous."

---

## 💎 Option 2: O.B.S.I.D.I.A.N. (The Namesake)
*A comprehensive, "Heavy" stack that covers every layer of the Fractal Octree.*

*   **O**: **Orchestrator** (Temporal - Workflow Management)
*   **B**: **Bus** (NATS - Event Streaming)
*   **S**: **Schema** (Pydantic/Instructor - Structured IO)
*   **I**: **Intelligence** (LangGraph - Agentic Reasoning)
*   **D**: **Database** (LanceDB - Vector/Hybrid Memory)
*   **I**: **Interface** (MCP - Standardized Tooling)
*   **A**: **Analytics** (OpenTelemetry/Arize - Evaluation)
*   **N**: **Nodes** (Ray - Distributed Actors)

> **Verdict**: **Most Complete**. It maps almost 1:1 to the 8 Pillars of the Octree. It is "Solid" and "Unbreakable," fitting the Obsidian lore perfectly.

---

## 🕷️ Option 3: S.P.I.D.E.R. (The Agile Hunter)
*A lighter, more aggressive stack focused on "Action" and "Stigmergy".*

*   **S**: **Stigmergy** (NATS JetStream - The Core Communication)
*   **P**: **Protocol** (MCP - The Universal Connector)
*   **I**: **Instructor** (Pydantic - The Validation Layer)
*   **D**: **Durable** (Temporal - The Safety Net)
*   **E**: **Engine** (LangGraph - The Brain)
*   **R**: **Resources** (Ray - The Muscle)

> **Verdict**: **Most Agile**. It drops the explicit "Database" and "Observability" letters (assuming they are implicit in Stigmergy/Protocol) to focus on the *movement* of the Swarm.

---

## 🐉 Option 4: C.H.I.M.E.R.A. (The Hybrid Monster)
*A stack that emphasizes the "Hybrid" nature of the system (Hot/Cold, Biological/Digital).*

*   **C**: **Context** (MCP - The Universal Context Layer)
*   **H**: **Hybrid** (LanceDB - Hot/Cold Memory Fusion)
*   **I**: **Intent** (Pydantic - The Gherkin/Schema Bridge)
*   **M**: **Messaging** (NATS - The Signal Bus)
*   **E**: **Execution** (Temporal - The Durable Loop)
*   **R**: **Ray** (The Distributed Body)
*   **A**: **Agents** (LangGraph - The Multi-Agent Orchestration)

> **Verdict**: **Most Thematic to "Hydra"**. It emphasizes "Context" and "Hybrid" memory, which are the two hardest problems we are solving in Gen 63.

---

## 📊 Comparison Matrix

| Feature | **P.H.A.N.T.O.M.** | **O.B.S.I.D.I.A.N.** | **S.P.I.D.E.R.** | **C.H.I.M.E.R.A.** |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Vibe** | Stealth / Evolution | Stability / Completeness | Speed / Agility | Hybrid / Complexity |
| **MCP Role** | The Interface (M) | The Interface (I) | The Protocol (P) | The Context (C) |
| **Memory** | Implicit (in Host) | Explicit (Database) | Implicit | Explicit (Hybrid) |
| **Compute** | Host (Ray) | Nodes (Ray) | Resources (Ray) | Ray |
| **Orchestration** | Temporal | Orchestrator | Durable | Execution |
| **Best For** | **General Purpose** | **Enterprise/Scale** | **Rapid Prototyping** | **Complex Research** |

## 🧠 Swarmlord's Recommendation

I recommend **Option 1: P.H.A.N.T.O.M.** or **Option 2: O.B.S.I.D.I.A.N.** for Gen 63.

*   **Why P.H.A.N.T.O.M.?** It is a clean evolution of PLATFORM. It highlights **MCP** as a top-level citizen ("M").
*   **Why O.B.S.I.D.I.A.N.?** It is the "Ultimate Form." If we are truly building the "Obsidian Spider," this stack defines our body parts perfectly.

### The "MCP" Shift
In all variants, **MCP** replaces custom tool definitions.
*   **Old Way**: We write `tools.py` with `@tool` decorators.
*   **Gen 63 Way**:
    *   The **Assimilator** runs an `sqlite-mcp` server.
    *   The **Sensors** run a `fetch-mcp` server.
    *   The **Swarmlord** connects to them via `stdio` or `sse`.
    *   This allows us to swap out the "Brain" (LLM) easily, as the "Body" speaks a universal protocol.
