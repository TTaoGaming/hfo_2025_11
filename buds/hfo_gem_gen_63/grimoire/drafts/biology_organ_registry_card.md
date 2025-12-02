```yaml
card:
  id: f4120552-a3d4-46ab-8e0e-902ba4267cee
  source: biology_organ_registry.md
  type: Concept
```

# 🃏 Biomimetic Organ Registry

> **Intuition**: Biomimicry maps Hive software components to insectoid organs, instilling biological intuition for their function, latency, criticality, and interconnections.

## 📜 The Incantation (Intent)
```gherkin
Feature: Biomimetic Organ Registry

  Scenario: Query organ properties for architectural intuition
    Given a registered organ "Brain"
    When the registry is queried for its biological role, function, latency, and tech stack
    Then it returns:
      | Biological Name | Function          | Latency         | Tech Stack     |
      | Cortex          | Intent & Strategy | High (Seconds)  | Gherkin / LLM  |
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Centralized registry of biomimetic organs
ORGANS = {
    "Brain": {
        "biological": "Cortex",
        "function": "Intent & Strategy",
        "latency": "High (Seconds)",
        "stack": "Gherkin / LLM"
    },
    "Body": {
        "biological": "Soma",
        "function": "Execution & Compute",
        "latency": "Medium (ms)",
        "stack": "Ray / Python"
    },
    "Eyes": {
        "biological": "Ocelli",
        "function": "Perception & Telemetry",
        "latency": "Low (Realtime)",
        "stack": "LangSmith / Logs"
    },
    "Hands": {
        "biological": "Mandibles",
        "function": "Tool Use & I/O",
        "latency": "Variable",
        "stack": "API / FileSystem"
    },
    "Nerves": {
        "biological": "Ganglia",
        "function": "Routing & Reflexes",
        "latency": "Ultra-Low (µs)",
        "stack": "NATS JetStream"
    },
    "Memory": {
        "biological": "Mycelium",
        "function": "Storage & Recall",
        "latency": "Mixed",
        "stack": "Postgres / Vector"
    },
    "Carapace": {
        "biological": "Exoskeleton",
        "function": "Defense & Validation",
        "latency": "Pre-Commit",
        "stack": "Pytest / Ruff"
    },
    "Venom": {
        "biological": "Lysosomes",
        "function": "Testing & Destruction",
        "latency": "On-Demand",
        "stack": "Pytest / Chaos"
    }
}

def get_organ_props(organ_name: str) -> dict:
    """
    Retrieve biological intuition for a Hive organ.
    """
    return ORGANS.get(organ_name, {"error": "Unknown organ"})
```

## ⚔️ Synergies
* **Information Flow**: Brain → Nerves → Hands (intent to action, per Organism graph).
* **Perception Loop**: Eyes → Brain → Nerves → Hands → World (sensory-motor cycle, per Sequence diagram).
* **Support Systems**: Memory (Mycelium) stores wisdom; Carapace/Venom enable defense/testing (per Support graph).
* **Hive Architecture**: Extends to domain `brain/biology`; informs component design across Cortex (LLM), Ganglia (NATS), Soma (Ray).