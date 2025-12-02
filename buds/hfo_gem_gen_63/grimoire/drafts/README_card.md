---
card:
  id: brain-navigator-v1
  source: README.md
  type: Concept
---

# 🃏 🧠 The Brain (Navigator)

> **Intuition**: The Brain is the immutable throne of strategic intent, defining the swarm's purpose through declarative Gherkin and registry without ever executing a single action.

## 📜 The Incantation (Intent)
```gherkin
Feature: Brain as Seat of Intent and Strategy

  Scenario: Providing Read-Only Strategic Direction
    Given the Brain contains Gherkin feature files and the Holocron registry.yaml
    When the swarm requires validation of actions in the Body
    Then all executions trace back to intents defined in the Brain
    And no modifications occur unless updating the Grand Strategy
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Load and Validate Brain Registry (SSOT)
import yaml
import os

def load_brain_registry(brain_path="brain"):
    """
    Access the Brain's Holocron for intent validation.
    """
    registry_path = os.path.join(brain_path, "registry.yaml")
    if not os.path.exists(registry_path):
        raise FileNotFoundError("Brain Holocron missing: registry.yaml")
    
    with open(registry_path, "r") as f:
        registry = yaml.safe_load(f)
    
    # Validate traceability (example essence)
    intents = registry.get("intents", [])
    if not intents:
        raise ValueError("No intents found in Brain registry")
    
    return registry

# Usage: registry = load_brain_registry()
```

## ⚔️ Synergies
*   **Eyes (Observer)**: Feeds perceptual data into Brain-defined intents for strategic ingestion.
*   **Body (Collective)**: Executes via Nerves/Hands/Blood only if actions trace to Brain Gherkin specs.
*   **Memory (Assimilator)**: Stores swarm wisdom aligned with Brain's registry as SSOT.
*   **Carapace (Immunizer)**: Enforces read-only protection on Brain to prevent corruption.
*   **Regeneration**: Triggers Genesis script from Brain DNA for hive rebirth via GitHub source.