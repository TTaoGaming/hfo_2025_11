---
hexagon:
  ontos:
    id: c9af6da3-2f00-41e6-a150-687a0384450a
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.553938+00:00'
    generation: 51
  topos:
    address: carapace/immune_system/README.md
    links: []
  telos:
    viral_factor: 0.0
    meme: README.md
---


# 🛡️ The Immune System Collective

> **Role**: Active Defense & Evolution
> **Gherkin**: `carapace/immune_system.feature`
> **Status**: Initializing (Gen 50)

## 🧬 Overview
The Immune System is a sub-collective of the Carapace. While the Carapace provides the hard shell (static rules), the Immune System provides the active, adaptive defense against evolving threats.

## 📂 Anatomy

### 1. 🧱 Static Guards (The Cellular Wall)
*   **Location**: `carapace/immune_system/static_guards/`
*   **Function**: Code analysis, type checking, secret scanning.
*   **Tools**: Ruff, Black, Mypy, Whispers.

### 2. 🧠 Neural Guards (The Neural Filter)
*   **Location**: `carapace/immune_system/neural_guards/`
*   **Function**: LLM input/output filtering, hallucination detection.
*   **Tools**: Instructor, NeMo Guardrails (planned).

### 3. ⚖️ Regulators (The Homeostatic Regulator)
*   **Location**: `carapace/immune_system/regulators/`
*   **Function**: Resource management, circuit breaking, quarantine.
*   **Tools**: Temporal Interceptors, Redis Rate Limiters.

### 4. 🧬 The Forge (Evolution)
*   **Location**: `carapace/immune_system/evolution/`
*   **Function**: Evolving defense configurations using MAP-Elites.
*   **Script**: `immunity_archive.py`

## 🔄 The Co-Evolution Loop
1.  **Venom (Red Team)** generates a new attack (e.g., adversarial prompt).
2.  **The Forge** evolves a defense configuration (e.g., stricter filter).
3.  **The Regulator** deploys the new configuration.
4.  **The Swarm** survives and adapts.
