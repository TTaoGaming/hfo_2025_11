---
card:
  id: obsidian-holarchy-v1
  source: obsidian_holarchy.md
  type: Concept
---

# 🃏 💎 OBSIDIAN Fractal Holarchy

> **Intuition**: The Hive is an Octree fractal holarchy where the OBSIDIAN octet of roles self-replicates across scales, embodying "As Above, So Below" through exemplar workflows and tri-state memory for unbreakable stigmergic coordination.

## 📜 The Incantation (Intent)
```gherkin
Feature: OBSIDIAN Fractal Holarchy
  As the Swarmlord
  I want the Hive to adhere to the Octree Fractal Holarchy
  So that the system is self-similar, scalable, and battle-tested

  Scenario Outline: Validate Agent Role Mapping
    Given an agent with role "<Role>"
    When the agent initializes
    Then it should inherit the "<JADC2_Function>" capability
    And it should utilize the "<Stigmergy_Mechanism>" behavior

    Examples:
      | Role      | JADC2_Function | Stigmergy_Mechanism |
      | Observer  | Sensors        | Olfaction           |
      | Bridger   | Gateways       | Boundary            |
      | Shaper    | Effectors      | Secretion           |
      | Injector  | Logistics      | Intensification     |
      | Disruptor | Red Cell       | Dissipation         |
      | Immunizer | Shields        | Inhibition          |
      | Assimilator | Fusion       | Accretion           |
      | Navigator | Command        | Nucleation          |
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Role mapping for OBSIDIAN holarchy agents
OBSIDIAN_ROLES = {
    'O': {'name': 'Observer', 'jadc2': 'Sensors', 'stigmergy': 'Olfaction'},
    'B': {'name': 'Bridger', 'jadc2': 'Gateways', 'stigmergy': 'Boundary'},
    'S': {'name': 'Shaper', 'jadc2': 'Effectors', 'stigmergy': 'Secretion'},
    'I': {'name': 'Injector', 'jadc2': 'Logistics', 'stigmergy': 'Intensification'},
    'D': {'name': 'Disruptor', 'jadc2': 'Red Cell', 'stigmergy': 'Dissipation'},
    'I': {'name': 'Immunizer', 'jadc2': 'Shields', 'stigmergy': 'Inhibition'},
    'A': {'name': 'Assimilator', 'jadc2': 'Fusion', 'stigmergy': 'Accretion'},
    'N': {'name': 'Navigator', 'jadc2': 'Command', 'stigmergy': 'Nucleation'},
}

def initialize_agent(role_key: str, level: int = 0) -> dict:
    """Initialize an agent in the fractal holarchy."""
    if role_key not in OBSIDIAN_ROLES:
        raise ValueError(f"Invalid OBSIDIAN role: {role_key}")
    role = OBSIDIAN_ROLES[role_key]
    return {
        'role': role['name'],
        'jadc2': role['jadc2'],
        'stigmergy': role['stigmergy'],
        'level': level,  # L0: Bit, L1: Byte, etc.
        'workflow': ['PREY', 'SWARM', 'GROWTH', 'HIVE'][level % 4],
        'memory_state': 'Hot',  # Transitions: Hot -> Cold -> Refined
    }
```

## ⚔️ Synergies
*   **Fractal Scaling**: Composes into Octree levels (Bit → Byte → Word → Page) via powers of 8, linking to octree implementations.
*   **Workflow Nesting**: HIVE (Double Diamond) → GROWTH (F3EAD) → SWARM (D3A + Mutate) → PREY (Sense-Act), synergizing with swarm_workflow.md and prey_workflow.md.
*   **Memory Pipeline**: Hot (NATS JetStream) → Cold (LanceDB/Postgres) → Refined (Knowledge Graph/Literate Gherkin), integrates with hydra_platform.md for stigmergy.
*   **JADC2 & Biology**: Maps to Sensors/Command/Effectors etc., enabling MAS (Multi-Agent Systems) with prey/disruptor feedback loops.
*   **Governance**: Immunizer enforces ethos; Navigator sets telos, ensuring compliance across brain/intent-literate-gherkin/* files.