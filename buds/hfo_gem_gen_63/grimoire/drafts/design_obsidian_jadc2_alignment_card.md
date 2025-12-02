---
card:
  id: 550e8400-e29b-41d4-a716-446655440309
  source: design_obsidian_jadc2_alignment.md
  type: Concept
---

# 🃏 OBSIDIAN JADC2 Alignment

> **Intuition**: Infuse the OBSIDIAN swarm's HFO roles with battle-tested JADC2 semantics—Sensors to Command—replacing alien whimsy with military precision for operational density and clarity.

## 📜 The Incantation (Intent)
```gherkin
Feature: OBSIDIAN Anatomy Alignment to JADC2 Standards

  Scenario: Map HFO Roles to Functional JADC2 Concepts
    Given OBSIDIAN roles are defined as Observer, Bridger, Shaper, Injector, Disruptor, Immunizer, Assimilator, Navigator
    When each role is aligned to its JADC2 functional equivalent per Variation D
    Then the anatomy yields unambiguous, dense semantics enabling OODA-loop orchestration and resilience
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Battle-Tested OBSIDIAN-JADC2 Mapping (Variation D)
OBSIDIAN_JADC2_ANATOMY = {
    'O': {'role': 'Observer', 'jadc2': 'Sensors', 'domain': 'ISR', 'def': 'Collecting raw telemetry'},
    'B': {'role': 'Bridger', 'jadc2': 'Gateways', 'domain': 'Transport', 'def': 'Cross-domain datalinks'},
    'S': {'role': 'Shaper', 'jadc2': 'Effectors', 'domain': 'Fires', 'def': 'Executing mission effects'},
    'I1': {'role': 'Injector', 'jadc2': 'Logistics', 'domain': 'Sustainment', 'def': 'Fueling compute/tokens'},
    'D': {'role': 'Disruptor', 'jadc2': 'Red Cell', 'domain': 'Adversary', 'def': 'Simulating threats'},
    'I2': {'role': 'Immunizer', 'jadc2': 'Shields', 'domain': 'Protection', 'def': 'Active defense checks'},
    'A': {'role': 'Assimilator', 'jadc2': 'Fusion', 'domain': 'PED', 'def': 'Raw data to intel'},
    'N': {'role': 'Navigator', 'jadc2': 'Command', 'domain': 'C2', 'def': 'Intent orchestration'}
}

def get_jadc2_anatomy(role_key: str) -> dict:
    """Retrieve JADC2 mapping for OBSIDIAN role."""
    return OBSIDIAN_JADC2_ANATOMY.get(role_key, {'error': 'Unknown role'})
```

## ⚔️ Synergies
*   **OBSIDIAN Core**: Enhances HFO role semantics, prioritizing functional density over letter-matching mnemonics.
*   **OODA Loop**: Integrates with Sensors → Fusion → Command → Effectors cycle for swarm decision-making.
*   **Alternatives**: Builds on/contrasts Variation C "Alien Anatomy" and links to `design_obsidian_semantic_alignment.md`.
*   **Military Stack**: Supports JADC2-inspired resilience via Red Cell threats, Shields protection, and Logistics sustainment.
*   **Swarm Architecture**: Enables modular injection into agent hierarchies for battle-tested orchestration.