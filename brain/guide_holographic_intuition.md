---
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 22869021-6fc4-48b6-94a9-c17ee546cc8b
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.501921+00:00'
  topos:
    address: brain/guide_holographic_intuition.md
    links: []
  telos:
    viral_factor: 0.0
    meme: guide_holographic_intuition.md
---

# 🧠 The Holographic Intuition: A Field Guide

> **Context**: Deep Dive into Fractal Holarchy + Obsidian Facet
> **Goal**: Translate "Genetic Intuition" into "Cognitive Form".

## 1. The Atom: The Obsidian Facet
Everything in HFO is an **Artifact**. An Artifact is wrapped in a **Facet**.
Think of the Facet as the "Cell Membrane" that holds the data.

### The Schema (The DNA)
This is the single Pydantic model that rules them all.

```python
class ObsidianFacet(BaseModel):
    # --- Identity (The Anchor) ---
    id: UUID              # Unique Soul
    author: str           # Who made this? (e.g., "Shaper-Squad1")
    timestamp: datetime   # When?
    location: str         # Where is the body? (file://...)

    # --- The Pulse (Hot / Liquid) ---
    urgency: float        # 0.0 to 1.0 (How loud is this?)
    decay: float          # 0.0 to 1.0 (How fast does it die?)
    signal_type: str      # "Discovery", "Danger", "Request"

    # --- The Vector (Cold / Sediment) ---
    tags: List[str]       # Folksonomy
    embedding: List[float]# Semantic Meaning (The "Vibe")
    links: List[UUID]     # Mycelial Connections
```

---

## 2. The Three States (The Phase Transition)

### State A: Crystalline (The File)
*   **Medium**: Markdown File on Disk.
*   **Format**: YAML Frontmatter.
*   **Intuition**: This is a **Book**. It sits on a shelf. It is heavy, detailed, and permanent.

```yaml
---
id: 550e8400-e29b-41d4-a716-446655440000
author: Shaper-Alpha
urgency: 0.1
tags: [research, biology]
---
# The Content
Here is the deep research...
```

### State B: Liquid (The Signal)
*   **Medium**: NATS JetStream Message.
*   **Format**: Lightweight JSON.
*   **Intuition**: This is a **Shout**. It travels instantly. It has no body, only "Urgency" and a "Pointer".

```json
{
  "subject": "hfo.signal.discovery",
  "payload": {
    "id": "550e8400...",
    "urgency": 0.9,
    "location": "file://memory/episodic/...",
    "bluf": "Found a critical vulnerability!"
  }
}
```
*   *Note*: The "Body" is not here. Only the "Pointer" (`location`). This is the **Claim Check Pattern**.

### State C: Sedimentary (The Memory)
*   **Medium**: Postgres Row + Vector.
*   **Format**: SQL Table.
*   **Intuition**: This is a **Fossil**. It is buried in the strata. We find it by digging (Querying).

| ID | Vector | Urgency | Location |
| :--- | :--- | :--- | :--- |
| 550e... | `[0.1, 0.9...]` | 0.1 | `file://...` |

---

## 3. Examples in Action

### Scenario 1: The "Wolf Pack" (Hot Stigmergy)
*   **Context**: A Disruptor finds a security hole.
*   **Action**:
    1.  **Genesis**: Disruptor writes `vuln_report.md` (Crystal).
    2.  **Emission**: Disruptor emits a signal with `urgency: 1.0` (Liquid).
    3.  **Reaction**: The **Immunizer Squad** is subscribed to `urgency > 0.8`. They smell the "Blood" instantly via NATS.
    4.  **Swarm**: They swarm the `location`, read the file, and patch it.
*   **Intuition**: **Pheromone Alarm**.

### Scenario 2: The "Library of Alexandria" (Cold Stigmergy)
*   **Context**: A Navigator needs to plan a strategy based on last year's lessons.
*   **Action**:
    1.  **Query**: Navigator asks "How did we handle the Gen 50 crash?"
    2.  **Recall**: The DB (Sediment) searches for vectors near "Gen 50 crash".
    3.  **Retrieval**: It finds an old artifact `postmortem_gen50.md`.
    4.  **Synthesis**: Navigator reads the file and learns.
*   **Intuition**: **Ancestral Memory**.

---

## 4. Fractal Intuition (As Above, So Below)

How does this scale?

*   **Level 0 (Agent)**: An Agent has a "ToDo List" (Internal Stigmergy).
*   **Level 1 (Squad)**: A Squad has a "NATS Channel" (Local Stigmergy).
*   **Level 2 (Hive)**: The Hive has a "Global Database" (Global Stigmergy).

The **Obsidian Facet** is the same at all levels. A "ToDo Item" is just a Facet with `urgency: 0.5`. A "Global Mission" is a Facet with `urgency: 1.0`.

**You don't change the data structure. You just change the scope.**
