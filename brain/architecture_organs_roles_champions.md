---
title: Organs, Roles, and Champions
status: Active (Gen 51)
domain: Architecture
owners:
- Swarmlord
type: Physiology

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: a2084caf-c715-471f-89e1-00db4124a19a
    type: doc
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T06:32:09.779370Z'
  topos:
    address: 1.0.0
    links: []
  telos:
    viral_factor: 0.0
    meme: Organs, Roles, and Champions
---


# 🧬 Organs, Roles, and Champions

## ⚡ BLUF (Bottom Line Up Front)
The Hive is structured biologically. **Organs** are the physical infrastructure (folders/code). **Roles** are the functional archetypes (jobs). **Champions** are the specific, evolved instances of an agent filling a role (individuals). This separation allows us to swap out "Grok-Navigator-v4" for "GPT-5-Navigator-v1" without changing the underlying Organ or Role definition.

## 📊 Biological Hierarchy Matrix

| Concept | Analogue | Example | Mutability |
| :--- | :--- | :--- | :--- |
| **Organ** | Body Part | `brain/` (Cortex) | Static (Hardcoded) |
| **Role** | Job Description | Navigator (Strategist) | Stable (Configured) |
| **Champion** | Individual | Grok-Nav-v4 | Volatile (Evolved) |

## 🧠 Concept Visualization

### View 1: The Trinity (Conceptual)
*The relationship between Place, Purpose, and Person.*

```mermaid
graph TD
    Organ[Organ: The Place] -->|Hosts| Role[Role: The Purpose]
    Role -->|Implemented By| Champion[Champion: The Person]

    Organ -.->|Example| Folder[brain/]
    Role -.->|Example| Job[Navigator]
    Champion -.->|Example| Model[Grok-Beta]
```

### View 2: Class Hierarchy (Logical)
*Object-Oriented definition.*

```mermaid
classDiagram
    class Organ {
        +path: str
        +biological_function: str
    }

    class Role {
        +name: str
        +jadc2_function: str
    }

    class Champion {
        +id: str
        +gene_seed: dict
        +fitness: float
    }

    Organ "1" *-- "1" Role : Seats
    Role "1" *-- "*" Champion : Instantiates
```

### View 3: Evolution of Champions (Physical)
*How Champions change over time while Roles remain.*

```mermaid
gantt
    title Champion Succession
    dateFormat YYYY-MM-DD

    section Navigator Role
    Grok-v1 : 2025-11-01, 7d
    Grok-v2 : 2025-11-08, 7d
    Gemini-v1 : 2025-11-15, 7d
```

## 🦅 Executive Summary
The Hive is an organism.
*   **Organs**: Physical directories (`brain/`, `body/`).
*   **Roles**: Functional archetypes (Navigator, Observer).
*   **Champions**: Specific evolved instances (e.g., "Grok-Navigator-v4").
