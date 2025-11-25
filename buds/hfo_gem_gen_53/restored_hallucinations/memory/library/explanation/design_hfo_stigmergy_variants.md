---
id: 550e8400-e29b-41d4-a716-446655440300
type: design
status: active
title: 'HFO Stigmergy: The Obsidian Thermodynamics'
created: '2025-11-23T12:30:00Z'
last_touched: '2025-11-23T12:45:00Z'
urgency: 1.0
stigmergy_score: 100.0
author: Swarmlord
links:
- brain/design_hexagonal_holon_header.md: extends
- brain/research_obsidian_thermodynamics.md: implements
tags:
- architecture
- stigmergy
- hexagonal
- thermodynamics
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440300
    type: design
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-23T12:30:00Z'
    generation: 51
  topos:
    address: brain/design_hfo_stigmergy_variants.md
    links: []
  telos:
    viral_factor: 1.0
    meme: Keep it Hot, or Freeze it Sharp.
---


# 🌋 HFO Stigmergy: The Obsidian Thermodynamics

> **BLUF**: We unify HFO Stigmergy under the **Obsidian Thermodynamics** model. The "Hexagon" is the polymorphic unit that transitions between **Hot** (Lava/Signal), **Cold** (Glass/File), and **Refined** (Gem/Memory).

---

## 1. The Singleton Syntax (The Hexagon)

The "Hexagon" is the immutable interface of any Holon in the Hive. It is the **Universal Adapter**.

```python
class Hexagon(BaseModel):
    ontos:   Ontos   # Identity (Who am I?)
    telos:   Telos   # Purpose (Why do I exist?)
    chronos: Chronos # Time (When/How fast?)
    topos:   Topos   # Space (Where am I?)
    logos:   Logos   # Logic (What are my rules?)
    pathos:  Pathos  # Sentiment (How do I feel?)
```

---

## 2. The Three Thermodynamic States

The Hexagon adapts to its environment (Phase Transition) while maintaining its internal geometry.

### Variant A: Hot State (Lava)
*   **Medium**: **NATS JetStream** (`hfo.signal.>`)
*   **State**: **Fluid & Volatile**.
*   **Analogy**: **Lava / Pheromones**.
*   **Use Case**: **Machine-Speed Coordination**. "Fire & Forget" signals.
*   **Format**: JSON Payload.
*   **Thermodynamics**: High Temp (`urgency=1.0`), Low Viscosity.
*   **Syntax**:
    ```json
    {
      "hexagon": {
        "ontos": { "id": "...", "type": "signal" },
        "telos": { "viral_factor": 0.9 },
        "payload": { "action": "execute_order_66" }
      }
    }
    ```

### Variant B: Cold State (Volcanic Glass)
*   **Medium**: **Filesystem** (`.md`, `.py`, `.yaml`)
*   **State**: **Quenched & Sharp**.
*   **Analogy**: **Obsidian / The Knife**.
*   **Use Case**: **Human Intent & Tools**. The "Source of Truth".
*   **Format**: YAML Frontmatter / Docstring.
*   **Thermodynamics**: Rapidly Cooled (`decay=0.0`), High Structure.
*   **Syntax**:
    ```yaml
    hexagon:
      ontos: { id: "...", type: "file" }
      telos: { meme: "The Resting State" }
      # ...
    ```

### Variant C: Refined State (Gem)
*   **Medium**: **Postgres / Vector DB** (`hfo_unified_memory`)
*   **State**: **Polished & Valuable**.
*   **Analogy**: **The Gem / The Mountain**.
*   **Use Case**: **Long-Term Wisdom**. Retrieval and Context.
*   **Format**: Relational Row + Vector Embedding.
*   **Thermodynamics**: Low Temp (`urgency=0.0`), Infinite Viscosity.
*   **Syntax**:
    *   `node_id`: `hexagon.ontos.id`
    *   `metadata`: `jsonb(hexagon)`
    *   `embedding`: `vector(hexagon.telos.meme + hexagon.pathos.sentiment)`

---

## 3. The "Obsidian Protocol" (Implementation Path)

To unify the system, we must implement the **Hexagonal Adapter** in code.

### Step 1: Define the Pydantic Core
Create `body/models/hexagon.py`. This is the SSOT (Single Source of Truth).
*   Define `Ontos`, `Telos`, `Chronos`, `Topos`, `Logos`, `Pathos` models.
*   Define the `Hexagon` container.

### Step 2: Implement the Phase Transitions
Add methods to the `Hexagon` class to transform itself:
*   `quench()`: Hot (JSON) -> Cold (YAML).
*   `melt()`: Cold (YAML) -> Hot (JSON).
*   `refine()`: Cold (YAML) -> Refined (DB Record).

### Step 3: The "Hexagonal Lens" Tool
Create a utility (`hfo.py lens`) that can read any variant and display it as the others.
*   `hfo.py lens read file.md` -> Outputs JSON (Melted).
*   `hfo.py lens listen hfo.signal.>` -> Outputs YAML (Quenched).

---

## 4. Architectural Alignment

| Principle | Alignment |
| :--- | :--- |
| **Hexagonal Fractal Holarchy** | The Hexagon is the fundamental unit at all scales. |
| **Network Virtual Stigmergy** | The "Hot Hexagon" enables async coordination. |
| **Obsidian Horizon Hourglass** | Refined (Past), Hot (Present), Cold (Future Intent). |

---

## 5. Example: The Lifecycle of a Hexagon

1.  **Eruption (Hot)**: An Agent fires a `signal` (JSON) onto NATS. "I found a bug!"
2.  **Quench (Cold)**: The `Genesis` protocol catches the signal and writes a `bug_report.md` (YAML).
3.  **Refinement (Refined)**: The `Assimilator` reads the file and buries it in the `knowledge_graph` (DB).
