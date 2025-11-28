---
title: Knowledge Management Standard (KCS v6 + Diátaxis)
status: Active
domain: Knowledge
owners:
- Swarmlord
type: Standard
hexagon:
  ontos:
    id: standard-kcs-diataxis-001
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T12:50:00+00:00'
    generation: 53
  topos:
    address: brain/standards/standard_kcs_diataxis.md
    links: []
  telos:
    viral_factor: 1.0
    meme: standard_kcs_diataxis.md
---

# 📚 Knowledge Management: The Dual Core

> **Context**: We use **KCS v6** for the *Process* of capturing knowledge, and **Diátaxis** for the *Structure* of storing it.

## 1. The Structure: Diátaxis (The 4 Quadrants)

Every piece of documentation in `memory/library/` must fall into one of these 4 categories:

| Quadrant | Focus | Direction | Purpose | Location |
| :--- | :--- | :--- | :--- | :--- |
| **Tutorials** | **Learning** | Practical steps | "Take me by the hand." | `memory/library/tutorials/` |
| **How-To Guides** | **Task** | Practical steps | "Solve this specific problem." | `memory/library/guides/` |
| **Reference** | **Information** | Theoretical knowledge | "Describe the machinery." | `memory/library/reference/` |
| **Explanation** | **Understanding** | Theoretical knowledge | "Explain the background." | `memory/library/explanation/` |

## 2. The Process: KCS v6 (The Loop)

We do not write docs "later". We write them **in the flow of work**.

### A. The Solve Loop (Fast)
1.  **Capture**: While coding, if you solve a problem, write a quick "Stub" or "WIP" note in `brain/active_memory/`.
2.  **Structure**: Before closing the PR, convert that note into a **How-To Guide** or **Reference**.
3.  **Reuse**: Before asking the Swarmlord, search the Library.

### B. The Evolve Loop (Slow)
1.  **Content Health**: The **Assimilator Agent** periodically reviews the Library.
2.  **New vs Known**: If a question is asked 3 times, it becomes a **Standard**.
3.  **Archiving**: Old docs (Gen 50) are moved to `memory/archive/` but kept for "Karmic Retrieval".

## 3. The "Cognitive Digest" Format
When the Swarmlord presents information, it is a **Micro-Article**:
*   **Title**: Clear and searchable.
*   **BLUF**: Bottom Line Up Front.
*   **Context**: Links to the Octet (Ontos/Telos).
*   **Content**: The Diátaxis body.
