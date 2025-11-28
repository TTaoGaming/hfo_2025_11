# 🛠️ Effectors (The Shaper)

> **Role**: Shaper (Executor)
> **Pillar**: Action
> **Stigmergy Dimension**: **Techne** (Craft, Skill, Tool)

## The Cognitive Function
**Effectors** are the seat of **Agency**. They are the hands that modify reality. While the Brain decides *what* to do, the Effectors know *how* to do it. They wrap raw capabilities in safe, executable interfaces.

## The Anatomy
*   **`tools/`**: The "Workshop".
    *   Atomic functions (e.g., `read_file`, `run_command`, `search_web`) exposed to Agents.
*   **`scripts/`**: The "Machinery".
    *   Orchestrated sequences of tools for complex tasks (e.g., `generate_history.py`).

## The HFO Axis
*   **Input**: Commands from the **Brain** via the **Nerves**.
*   **Output**: State Changes in the World (File Edits, API Calls).
*   **Failure Mode**: Paralysis (Broken Tools).
