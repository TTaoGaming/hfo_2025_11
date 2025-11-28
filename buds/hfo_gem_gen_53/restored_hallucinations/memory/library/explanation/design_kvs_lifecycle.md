---
type: design
status: proposal
author: Swarmlord (Gen 53)
date: 2025-11-24
tags: [organization, diataxis, lifecycle, kvs]
---

# 🧠 Design: Knowledge Storage & Lifecycle (KVS v6)

> **Context**: We have adopted **Diátaxis** for *structure* (Tutorials/Guides/Reference/Explanation).
> **Problem**: Diátaxis doesn't solve *maturity*. Where do drafts go? How do we distinguish "SOTA Research" from "Deprecated Ideas"?
> **Goal**: Define a **Knowledge Versioning System (KVS)** to manage the lifecycle of ideas.

---

## 🧬 The Core Concept: Knowledge Lifecycle
Knowledge is not static. It evolves through 4 states:
1.  **Seed (Draft)**: A rough idea, spike, or unverified research.
2.  **Sapling (Proposed)**: A formal design document under review.
3.  **Tree (Canonical)**: The accepted "Truth" (Standard, Spec, Architecture).
4.  **Timber (Archived)**: Old versions, superseded designs, logs.

---

## 🧩 Configuration Options

Here are 4 ways to implement this lifecycle within our Diátaxis brain.

### Option 1: The "Staging Ground" (Physical Separation)
*Best for: Clear separation of "Work in Progress" vs. "Done".*

```text
brain/
├── incubator/          # (Seeds) All drafts start here. No rules.
│   ├── draft_octree_v2.md
│   └── idea_neural_link.md
├── library/            # (Trees) The Diátaxis Canonical Truth.
│   ├── tutorials/
│   ├── guides/
│   ├── reference/
│   └── explanation/
└── archive/            # (Timber)
```
*   **Tradeoff**: Moving a file from `incubator` to `library` breaks links.
*   **Verdict**: **High Purity, Broken Links.**

### Option 2: The "Git-Flow Brain" (Branch-based)
*Best for: Engineering teams who love Git.*

*   **Structure**: The `brain/` folder *only* contains Canonical Truth (Diátaxis).
*   **Drafts**: Live on feature branches (e.g., `feature/design-octree`).
*   **Process**: You write a design doc on a branch. You PR it. Once merged, it is "Truth".
*   **Tradeoff**: Hard to cross-reference multiple drafts. "Hidden" knowledge until merged.
*   **Verdict**: **High Quality Control, Low Visibility.**

### Option 3: The "Metadata State Machine" (Frontmatter-based)
*Best for: Searchability and Link Stability.*

*   **Structure**: Files live in their final Diátaxis home immediately.
*   **Mechanism**: Use YAML frontmatter to denote state.
    ```yaml
    ---
    type: explanation
    status: draft  # <--- The KVS State
    version: 0.1
    ---
    ```
*   **Visuals**: We can use emojis in filenames for quick scanning (e.g., `🚧design_octree.md` vs `✅design_octree.md`), or just rely on the header.
*   **Tradeoff**: The "Explanation" folder contains both Truth and Drafts mixed together.
*   **Verdict**: **High Stability, High Noise.**

### Option 4: The "Hybrid Holarchy" (Recommended)
*Best for: HFO's Biological Metaphor.*

We combine **Diátaxis** (for the crystallized brain) with a **Working Memory** (for active thought).

```text
brain/
├── active_memory/      # (The Workbench) - KVS "Seeds" & "Saplings"
│   ├── current_mission/
│   └── drafts/
├── long_term_memory/   # (The Library) - KVS "Trees" (Diátaxis)
│   ├── tutorials/
│   ├── guides/
│   ├── reference/
│   └── explanation/
└── episodic_memory/    # (The Logs) - KVS "Timber"
    ├── digests/
    └── archive/
```

---

## 🏆 Recommendation: Option 4 (Hybrid Holarchy)

This maps perfectly to the **Human Brain**:
1.  **Working Memory (`active_memory/`)**: What we are thinking about *right now*. High churn. Drafts.
2.  **Long-Term Memory (`long_term_memory/`)**: What we *know*. Structured. Diátaxis.
3.  **Episodic Memory (`episodic_memory/`)**: What *happened*. Logs.

### Implementation Plan (KVS v6)

1.  **Rename `brain/` subfolders**:
    *   Create `brain/long_term_memory/` and move the Diátaxis folders there.
    *   Create `brain/active_memory/` for our current "Spikes" and "Drafts".
2.  **Enforce Headers**:
    *   All files in `long_term_memory` must have `status: active` or `status: stable`.
    *   All files in `active_memory` are implicitly `status: draft`.

### SOTA Industry Exemplars
*   **GitLab Handbook**: Uses "Draft" status in frontmatter (Option 3).
*   **Rust Language RFCs**: Uses a separate "RFCs" repo (Option 1).
*   **Obsidian Users**: Use "Inbox" vs "Zettelkasten" (Option 4).

**Decision**: Shall we proceed with **Option 4 (Hybrid Holarchy)**? It gives you a messy desk (`active_memory`) and a clean library (`long_term_memory`).
