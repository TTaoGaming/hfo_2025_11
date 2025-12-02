---
holon:
  id: design-knowledge-arch-v3
  type: design
  status: active
  author: Swarmlord
  date: 2025-12-01
  context: AI Swarm Optimization
---

# 🧠 Design V3: HFO Second Brain Architecture

> **Goal**: Define the optimal Knowledge Architecture for a **Hybrid AI Swarm** (Human + Agents).
> **Core Philosophy**: **Canalization**. The structure must guide the Swarm into the "Pit of Success".

## 1. The Architecture: "HFO Second Brain"

We combine three SOTA standards to handle the lifecycle of information from "Hot Signal" to "Cold Wisdom".

### Layer 1: The Container (P.A.R.A.)
*   **Origin**: Tiago Forte.
*   **Purpose**: **Lifecycle Management**. Separates "Active" from "Archive".
*   **Structure**:
    *   `1_projects/`: Active Missions (High Stigmergy).
    *   `2_areas/`: Long-term Standards (ADRs, Schemas).
    *   `3_resources/`: The Knowledge Base (RAG Source).
    *   `4_archives/`: The Graveyard.

### Layer 2: The Medium (Semantic Lake)
*   **Origin**: Data Lakes / Zettelkasten.
*   **Purpose**: **AI Swarm Traversal**.
*   **Mechanism**:
    *   **Flat Hierarchy**: Inside `1_projects`, files are not nested.
    *   **Rich Headers**: Every file has a YAML `holon` header.
    *   **Why**: AI Agents struggle with deep directory traversal. A "Lake" allows them to ingest the full context window in one gulp (`ls 1_projects/*.md`).

### Layer 3: The Crystal (Diataxis)
*   **Origin**: Daniele Procida.
*   **Purpose**: **RAG Optimization**.
*   **Mechanism**: Inside `3_resources`, content is strictly typed.
    *   `tutorials/`: "Teach me." (Sequence).
    *   `guides/`: "How to." (Steps).
    *   `reference/`: "What is." (Facts).
    *   `explanation/`: "Why." (Context).
    *   **Why**: RAG retrieval is noisy. Knowing a file is a "Guide" vs "Explanation" allows the Agent to weight the source correctly.

---

## 2. Comparative Analysis (Why this wins for Swarms)

We compared 4 options against the **AI Swarm Workflow**.

| Feature | **Obsidian Flow (V3)** | **Fractal Octree** | **Pure P.A.R.A.** | **Pure Diataxis** |
| :--- | :--- | :--- | :--- | :--- |
| **Context Window** | ⭐⭐⭐⭐⭐ (Optimized) | ⭐⭐⭐ (Fragmented) | ⭐⭐⭐⭐ (Good) | ⭐⭐ (Scattered) |
| **RAG Quality** | ⭐⭐⭐⭐⭐ (Typed) | ⭐⭐⭐ (Implicit) | ⭐⭐ (Mixed) | ⭐⭐⭐⭐⭐ (Typed) |
| **Agent Traversal** | **Fast** (Flat Lake) | **Slow** (Deep Tree) | **Fast** (Flat) | **Medium** (Nested) |
| **Write Friction** | **Low** (Dump in Lake) | **High** (Find Slot) | **Low** (Dump) | **High** (Classify) |
| **Maintenance** | **Medium** (Refract) | **High** (Prune) | **Low** (Ignore) | **High** (Curate) |

### Why "Obsidian Flow" wins for AI Swarms:
1.  **The "Hot Lake" Effect**: When an Agent starts a task, it usually needs *all* active context. `1_projects/` provides a single, flat bucket to inject into the Context Window.
2.  **The "Cold Crystal" Effect**: When an Agent needs to *learn* or *check a spec*, it queries the Vector DB. Diataxis ensures the chunks in the DB are semantically distinct (Fact vs. Opinion).
3.  **Stigmergy**: The YAML headers act as "Pheromones", allowing Agents to filter the Lake without reading the content.

---

## 3. The Directory Structure (Blueprint)

```text
brain/
├── 1_projects/              # [HOT] The Swarm's Workspace
│   │                        # RULE: Flat files. YAML Headers.
│   ├── intent_gen63.md
│   ├── design_gen63_arch.md
│   └── spec_gen63_tests.feature
│
├── 2_areas/                 # [WARM] The Law (Standards)
│   ├── architecture/        # ADRs
│   └── security/            # Policies
│
├── 3_resources/             # [COLD] The Library (RAG Source)
│   ├── tutorials/
│   ├── guides/
│   ├── reference/
│   └── explanation/
│
└── 4_archives/              # [FROZEN] The Past
    └── gen_61_legacy/
```

## 4. Migration Strategy

1.  **Initialize**: Create the folder skeleton.
2.  **Tag**: Add `holon` headers to all existing files.
3.  **Move**:
    *   Active work -> `1_projects/`.
    *   Tech Stack / Standards -> `2_areas/`.
    *   Chat Logs / Research -> `3_resources/explanation/`.
4.  **Refract**: (Later) Convert raw notes in `1_projects` into Guides/Reference in `3_resources`.
