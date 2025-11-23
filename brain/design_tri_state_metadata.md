---
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: b2dd60c7-a18f-4c0a-a109-c2ef57b73097
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.498524+00:00'
  topos:
    address: brain/design_tri_state_metadata.md
    links: []
  telos:
    viral_factor: 0.0
    meme: design_tri_state_metadata.md
---

# 💎 Tri-State Metadata: The Unified Field Theory of HFO

> **Status**: Proposed
> **Context**: Rich Metadata Stigmergy
> **Goal**: A unified system for Static (File), Hot (Signal), and Cold (DB) metadata.

## 1. The Problem: Fragmentation
Currently, HFO handles metadata in silos:
*   **Files**: Have YAML headers (Tags, ID).
*   **NATS**: Has JSON payloads (Urgency, Type).
*   **DB**: Has Columns (Embeddings, Relations).

**Friction**: When an agent reads a file, it doesn't know the "Urgency" it had when created. When an agent receives a signal, it might miss the deep "Context" stored in the file.

## 2. The Solution: The Obsidian Facet
We define a single **Pydantic Model** (`ObsidianFacet`) that acts as the **Single Source of Truth**. It projects itself into three states of matter.

### The 3 States of Matter

| State | Medium | Format | Analogy | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| **Crystalline** | Filesystem | YAML Header | **DNA / Bone** | Provenance, Human-Readability, Git Versioning. |
| **Liquid** | NATS JetStream | JSON Signal | **Pheromone / Blood** | Coordination, Attention, Real-time Dynamics. |
| **Sedimentary** | Postgres | Row + Vector | **Memory / Fossil** | Recall, Pattern Matching, Long-term Storage. |

---

## 3. Composable Primitives (The Schema)

The `ObsidianFacet` is composed of three primitive groups.

### A. The Anchor (Identity)
*Must exist in ALL states.*
*   `id` (UUID): Universally unique identifier.
*   `author` (String): Agent ID / Role.
*   `timestamp` (ISO8601): Creation time.
*   `location` (URI): Where the payload lives (e.g., `file://memory/episodic/...`).

### B. The Vector (Semantics)
*Dominant in Crystalline & Sedimentary states.*
*   `domain` (String): The knowledge domain (e.g., "Bio-Mimicry").
*   `tags` (List[Str]): Folksonomy tags.
*   `intent` (String): The mission or goal that spawned this.
*   `embedding` (Vector): *Derived* field (Cold only).

### C. The Pulse (Dynamics)
*Dominant in Liquid state, preserved in Sedimentary.*
*   `urgency` (Float 0-1): Priority of attention.
*   `quality` (Float 0-1): Confidence score.
*   `decay` (Float): Evaporation rate ($\lambda$).
*   `spread` (Float): Dispersion radius.

---

## 4. The Lifecycle (The System)

This is how the system works in practice:

1.  **Genesis (Crystalline)**
    *   Agent creates a file `artifact.md`.
    *   Agent instantiates `ObsidianFacet(id=..., urgency=0.9, tags=[...])`.
    *   Agent calls `facet.to_yaml()` and prepends it to the file.
    *   *Result*: A file with a rich header that includes "Urgency".

2.  **Emission (Liquid)**
    *   Agent calls `facet.to_signal()`.
    *   The system broadcasts a NATS message: `hfo.signal.high.artifact.created`.
    *   The payload is lightweight but contains the `Pulse` (Urgency/Decay).
    *   *Result*: The swarm reacts instantly to the "High Urgency" pheromone.

3.  **Assimilation (Sedimentary)**
    *   The **Assimilator** catches the Signal.
    *   It reads the File (Crystalline) to get the full content.
    *   It merges Signal + File data into a `FacetRecord`.
    *   It generates an embedding and writes to Postgres.
    *   *Result*: The "Urgency" is preserved in history ("This was a crisis"), and the content is searchable.

## 5. Why this is "Rich"
*   **Self-Contained**: If you lose the DB, you can rebuild it from the Files (Crystalline) because the YAML contains the `Pulse` data too.
*   **Biomimetic**: It models how biological information works—DNA (Static) creates Pheromones (Hot) which form Memories (Cold).
*   **Anti-Fragile**: The redundancy across 3 states ensures no context is ever lost.
