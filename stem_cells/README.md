# 🧬 Stem Cells: The Evolutionary Factory

> **Role**: The Source of Truth for Regeneration
> **Strategy**: Fractal Antifragility
> **Gherkin**: `brain/antifragile_strategy.feature`

## 🧬 Concept
This directory contains the **Pure DNA** (Blueprints) for every Holon in the system. It is the "Factory" that the `genesis.py` script uses to spawn or regenerate components.

## 📂 The Hierarchy

### 1. 🦠 Agents (`stem_cells/agents/`)
*   **Scale**: Micro
*   **Purpose**: Blueprints for individual Ray Actors (Workers, Planners, Guards).
*   **Regeneration**: Fast (< 1s). Triggered by "Suicide Switch".

### 2. 🫀 Organs (`stem_cells/organs/`)
*   **Scale**: Meso
*   **Purpose**: Blueprints for subsystems (Eyes, Memory, Carapace).
*   **Regeneration**: Medium (~10s). Triggered by "Organ Failure".

### 3. 🦅 Hive (`stem_cells/hive/`)
*   **Scale**: Macro
*   **Purpose**: Blueprint for the entire Repository/Infrastructure.
*   **Regeneration**: Slow (~5m). Triggered by "Phoenix Protocol".

## 🛠️ Usage (The Factory Pattern)

We use `make` as the entrypoint to the Stem Cell Factory.

```bash
# Micro: Regenerate a specific agent role
make regenerate-agent role=worker

# Meso: Regenerate an entire organ (e.g., flush and restart Eyes)
make regenerate-organ name=eyes

# Macro: The Phoenix Protocol (Nuke and pave)
make phoenix-protocol
```
