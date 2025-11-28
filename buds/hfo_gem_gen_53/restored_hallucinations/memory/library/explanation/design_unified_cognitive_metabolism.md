---
type: design
status: proposal
author: Swarmlord (Gen 53)
date: 2025-11-24
tags: [kcs-v6, diataxis, cognitive-metabolism, assimilator]
---

# 🧠 HFO Gen 53: The Unified Cognitive Metabolism

> **The Problem**: We have been treating `brain/` as a storage locker. In biology, the brain *processes*, it doesn't just *store*.
> **The Solution**: A **Metabolic Knowledge System** using **KCS v6** (Process) and **Diátaxis** (Structure), powered by the **Assimilator** (Organ).

---

## 1. The Organ Re-Alignment (Anatomy of Knowledge)

You asked: *"Maybe brain is the wrong organ?"*
**Answer**: Yes. The Brain is for **Executive Function** (Decisions). **Memory** is for **Storage** (Knowledge).

We will shift from a "Big Brain" model to a **"Tri-Organ Cognitive Loop"**:

| Organ | Biological Role | KCS Role | Diátaxis Content |
| :--- | :--- | :--- | :--- |
| **🧠 Brain** | **Executive Function** | **Strategy** | **Vision & Intent** (Gherkin, Roadmaps) |
| **🩸 Body (Digestion)** | **Metabolism** | **The Evolve Loop** | *N/A (It is the Worker)* |
| **💾 Memory** | **Storage** | **The Knowledge Base** | **The Library** (Tutorials, Guides, Reference, Explanation) |

---

## 2. The Structure: Diátaxis in Memory

We will move the "Static Knowledge" out of `brain/` and into `memory/library/`.

### `memory/library/` (The Long-Term Knowledge Base)
*   **`tutorials/`**: "Onboarding the Swarm." (e.g., `genesis_protocol.md`)
*   **`guides/`**: "Standard Operating Procedures." (e.g., `how_to_add_organ.md`)
*   **`reference/`**: "The Laws of Physics." (e.g., `api_specs/`, `glossary.md`)
*   **`explanation/`**: "The Deep Theory." (e.g., `design_octree.md`, `research_kcs.md`)

### `brain/` (The Executive Center)
*   **`intents/`**: Active Gherkin Features (The Orders).
*   **`strategy/`**: The Current Roadmap (The Focus).
*   **`active_context/`**: The "Workbench" for the current mission.

---

## 3. The Process: KCS v6 (The Metabolism)

Knowledge is not static; it flows. This flow is managed by the **Assimilator** (`body/digestion/assimilator.py`).

### Phase 1: The Solve Loop (Fast / Agents)
*   **Trigger**: An Agent (e.g., `hands/builder.py`) encounters a problem or invents a solution.
*   **Action**:
    1.  **Search**: Check `memory/library/`.
    2.  **Capture**: If not found, log a **Raw Gem** (JSON/Markdown) to `memory/episodic/inbox/`.
    *   *Format*: `Issue` -> `Context` -> `Resolution`.

### Phase 2: The Evolve Loop (Slow / Assimilator)
*   **Trigger**: Scheduled Task (e.g., every 10 mins) or "Sleep Cycle".
*   **Actor**: **The Assimilator**.
*   **Action**:
    1.  **Ingest**: Read `memory/episodic/inbox/`.
    2.  **Refine**: Use LLM to convert **Raw Gems** into **Diátaxis Artifacts**.
        *   *Is it a recipe?* -> Create `memory/library/guides/`.
        *   *Is it a fact?* -> Create `memory/library/reference/`.
    3.  **Link**: Update the Graph (Postgres/NetworkX).
    4.  **Prune**: Archive obsolete docs to `memory/archive/`.

---

## 4. The Unified Workflow (Example)

1.  **The Event**: A Builder Agent figures out how to fix a NATS connection timeout.
2.  **Capture (Solve Loop)**: The Agent writes a quick note:
    > "Fixed NATS timeout by setting `connect_timeout=5` in `infrastructure_stigmergy.py`."
    > Saved to: `memory/episodic/inbox/gem_20251124_nats_fix.json`
3.  **Digestion (Evolve Loop)**: The **Assimilator** wakes up.
    *   Reads the gem.
    *   Recognizes it as a **Guide** ("How to fix NATS timeout").
    *   Checks `memory/library/guides/`.
    *   **Update**: Edits `memory/library/guides/troubleshoot_nats.md` to include the new fix.
4.  **Availability**: The next Agent searches "NATS timeout" and finds the updated Guide.

---

## 5. Implementation Plan

1.  **Restructure**:
    *   Create `memory/library/{tutorials,guides,reference,explanation}`.
    *   Migrate Designs/Research from `brain/` to `memory/library/explanation/`.
    *   Migrate How-Tos from `brain/` to `memory/library/guides/`.
2.  **Purify Brain**:
    *   `brain/` retains only `intents/` (Gherkin), `strategy/` (Vision), and `config/`.
3.  **Empower Assimilator**:
    *   Update `body/digestion/assimilator.py` to implement the **KCS Evolve Loop** (Ingest Inbox -> Update Library).

**Verdict**: This aligns HFO with Biology (Metabolism) and Industry Standards (KCS/Diátaxis).
