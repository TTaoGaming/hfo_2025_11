# ⚡ HFO Stigmergy Protocol (The Pulse)

> **Status**: Draft
> **Context**: Gen 55 (The Gem)
> **Philosophy**: "The Environment is the Message."

## 1. The Mechanism (Hot -> Cold -> Refined)

Stigmergy in HFO is the process of indirect coordination. Agents do not talk to each other; they talk to the **Memory**.

### Phase 1: HOT (Signal Emission)
*   **Action**: An Agent performs a task (e.g., "Read File").
*   **Signal**: It emits a "Pheromone" to NATS (`nerves/bus`).
    *   `topic`: `swarm.activity.read`
    *   `payload`: `{ "agent": "Observer-1", "file": "README.md", "timestamp": 12345 }`
*   **State**: The information is "Hot" and fluid. It exists only in the stream.

### Phase 2: COLD (Signal Solidification)
*   **Action**: The **Assimilator** (Memory Agent) subscribes to the stream.
*   **Solidification**: It captures the signal and writes it to **DuckDB** (`memory/memory-duckdb`).
*   **State**: The information is now "Cold" and brittle. It is a record of the past.

### Phase 3: REFINED (Signal Refinement)
*   **Action**: A **Refiner Swarm** wakes up (Cron/Trigger).
*   **Refinement**: It queries DuckDB for "Raw Signals", aggregates them, and produces a "Insight".
    *   *Example*: "Observer-1 read README.md 50 times. Conclusion: This file is important."
*   **State**: The information is "Refined" (Gem). It is actionable wisdom.

---

## 2. The Stigmergy Summary (The Artifact)

Every Generation (1-55) must have a **Stigmergy Summary**. This is the "Proof of Work" for that generation.

### The Format
A Stigmergy Summary is a Markdown file stored in `memory/docs-diataxis/reference/gen_X_stigmergy.md`.

It must contain:
1.  **The Hexagon**: The 6-dimensional header (Ontos, Telos, etc.).
2.  **The Pulse**: A statistical summary of activity (e.g., "500 commits, 2000 signals").
3.  **The Artifacts**: A list of key outputs produced.
4.  **The Evolution**: What changed from Gen X-1 to Gen X?

### The Generation Process
1.  **Ingest**: Load Gen X archives into `sensors/archives`.
2.  **Analyze**: Run the **Refiner Swarm** (N=2) to summarize the archives.
3.  **Synthesize**: Generate the `gen_X_stigmergy.md` file.
4.  **Publish**: Move to `memory/docs-diataxis`.
