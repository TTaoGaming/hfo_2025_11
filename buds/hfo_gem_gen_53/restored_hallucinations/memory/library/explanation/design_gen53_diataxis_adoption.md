---
type: design
status: active
author: Swarmlord (Gen 53)
date: 2025-11-24
generation: 53
tags: [organization, diataxis, gen53, documentation]
---

# 🏛️ HFO Gen 53: Formal Diátaxis Adoption

> **Status**: Active (Gen 53 Foundation)
> **Mandate**: "Order from Chaos." All cognitive artifacts must reside in one of the four Diátaxis quadrants.

## 1. Context: The Shift to Generation 53
We are transitioning from **Gen 51/52 (Explosive Growth & Entropy)** to **Gen 53 (Crystalline Structure)**.
The `brain/` directory has become a "junk drawer" of mixed intents. To scale to 1M agents, our knowledge base must be machine-readable and human-navigable.

We are adopting the **Diátaxis Framework** as the Canonical Organizing Principle for the Hive Mind.

---

## 2. The Four Quadrants of HFO Memory

Every file in `brain/` must answer one specific user need.

### 🎓 Quadrant 1: Tutorials (`brain/tutorials/`)
*   **Goal**: **Learning-oriented**. "Take me by the hand."
*   **Audience**: New Agents, New Humans, Fresh Clones.
*   **Content**: Lessons that lead to a specific success.
*   **Examples**:
    *   `genesis_protocol_walkthrough.md` (Start here)
    *   `my_first_swarm_mission.md`
*   **Rule**: Must be a complete, step-by-step lesson. No theory, just doing.

### 🛠️ Quadrant 2: How-To Guides (`brain/guides/`)
*   **Goal**: **Problem-oriented**. "I have a specific task."
*   **Audience**: Active Agents, Developers.
*   **Content**: Recipes for solving real-world problems.
*   **Examples**:
    *   `how_to_add_new_organ.md`
    *   `how_to_debug_nats_freeze.md`
    *   `workflow_gitops_recovery.md`
*   **Rule**: Start with a verb. Focus on the result. Assume competence.

### 📖 Quadrant 3: Reference (`brain/reference/`)
*   **Goal**: **Information-oriented**. "What is this?"
*   **Audience**: Agents needing facts, specs, or schemas.
*   **Content**: Technical descriptions, specifications, configurations.
*   **Sub-folders**:
    *   `intents/`: Gherkin Feature files (`*.feature`). The Law.
    *   `schemas/`: JSON/YAML Schemas (`*.json`, `*.yaml`).
    *   `api/`: Function signatures and class docs.
    *   `glossary/`: Definitions of terms (Holon, Stigmergy).
*   **Rule**: Be dry, accurate, and complete. No opinions.

### 🧠 Quadrant 4: Explanation (`brain/explanation/`)
*   **Goal**: **Understanding-oriented**. "Why is it like this?"
*   **Audience**: Architects, Strategists, The Swarmlord.
*   **Content**: Design documents, research papers, architectural decisions, philosophy.
*   **Sub-folders**:
    *   `architecture/`: High-level system diagrams (Octree, Hexagons).
    *   `research/`: SOTA analysis, trade-off studies.
    *   `decisions/`: ADRs (Architecture Decision Records).
    *   `vision/`: Persona, North Stars, Strategy.
*   **Rule**: Provide context, history, and reasoning. Connect the dots.

---

## 3. Migration Strategy (The Great Sort)

We will restructure the existing `brain/` flatland into this hierarchy.

| Current File Type | Target Quadrant | Path |
| :--- | :--- | :--- |
| `design_*.md` | **Explanation** | `brain/explanation/architecture/` |
| `research_*.md` | **Explanation** | `brain/explanation/research/` |
| `vision_*.md` | **Explanation** | `brain/explanation/vision/` |
| `*.feature` | **Reference** | `brain/reference/intents/` |
| `*.yaml` | **Reference** | `brain/reference/config/` |
| `how_to_*.md` | **How-To** | `brain/guides/` |
| `workflow_*.md` | **How-To** | `brain/guides/` |
| `tutorial_*.md` | **Tutorials** | `brain/tutorials/` |
| `digest_*.md` | **Reference** | `brain/reference/digests/` (Logs) |

---

## 4. Usage for Agents (The Protocol)

When an Agent (You) needs to create a new file in `brain/`, follow this decision tree:

1.  **Are you teaching a beginner?** -> Create a **Tutorial**.
2.  **Are you solving a specific problem?** -> Create a **Guide**.
3.  **Are you describing a fact or spec?** -> Create a **Reference**.
4.  **Are you explaining context or design?** -> Create an **Explanation**.

### The "Stigmergy Header" Update
All files must include the `type` field in their YAML frontmatter matching the quadrant:
```yaml
---
type: tutorial | guide | reference | explanation
generation: 53
...
---
```

## 5. Next Steps
1.  Create the directory structure.
2.  Move existing files (The Great Sort).
3.  Update `AGENTS.md` to reflect Gen 53 and the new map.
