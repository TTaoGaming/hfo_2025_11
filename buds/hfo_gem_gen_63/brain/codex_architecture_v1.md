---
holon:
  id: hfo-codex-architecture
  type: documentation
  layer: brain
  status: active
  theme: System Architecture
---

# 🏛️ The Obsidian Codex: Architecture V1

> **System**: Hive Fleet Obsidian (HFO).
> **Generation**: 63 (Gemmation).
> **Core Truth**: The Fractal Octree ($8^N$).

## 1. The Geometry: Fractal Octree
The system is self-similar at all scales.
*   **Root ($8^0$)**: The Swarmlord (TTao) / The Obsidian Spider.
*   **Octet ($8^1$)**: The 8 Pillars (Functional Organs).
*   **Squad ($8^2$)**: The 64 Agents (Specialized Workers).

## 2. The 8 Pillars (The Octarchy)
Every layer of the fractal must implement these 8 functions:

1.  **Observer (Ontos)**: *Input / Sensor*. (Telemetry, Webhooks, Filesystem Watchers).
2.  **Bridger (Logos)**: *Connection / Bus*. (NATS JetStream, API Gateways).
3.  **Shaper (Techne)**: *Action / Tool*. (MCP Servers, Python Scripts, Docker).
4.  **Injector (Chronos)**: *Time / Pulse*. (Temporal Workflows, Cron, Heartbeats).
5.  **Disruptor (Pathos)**: *Test / Chaos*. (Chaos Monkey, Red Team, Fuzzing).
6.  **Immunizer (Ethos)**: *Guard / Safety*. (Pydantic Validators, IAM, Firewalls).
7.  **Assimilator (Topos)**: *Memory / Storage*. (LanceDB, SQLite, Filesystem).
8.  **Navigator (Telos)**: *Direction / Brain*. (LLM Planner, MCTS, LangGraph).

## 3. The Nervous System: Stigmergy
We do not use direct function calls between agents. We use the **Environment**.
*   **Hot Stigmergy**: NATS JetStream. Fast, ephemeral signals. "I am hungry."
*   **Cold Stigmergy**: Filesystem / DB. Slow, persistent facts. "There is food here."

## 4. The Lifecycle: Evo-Devo
*   **Genesis**: Code is born from Intent (Gherkin).
*   **Growth**: Code evolves via Stigmergy.
*   **Death**: Code is burned (Phoenix Protocol) if it drifts from Intent.

## 5. The Tech Stack (O.B.S.I.D.I.A.N.)
*   **O**: Orchestrator -> **Temporal**.
*   **B**: Bus -> **NATS**.
*   **S**: Schema -> **Pydantic**.
*   **I**: Intelligence -> **LangGraph**.
*   **D**: Database -> **LanceDB**.
*   **I**: Interface -> **MCP**.
*   **A**: Analytics -> **OpenTelemetry**.
*   **N**: Nodes -> **Ray**.

---
**Directive**: When in doubt, consult the Octree. If a component does not fit into one of the 8 Pillars, it does not belong in the Hive.
