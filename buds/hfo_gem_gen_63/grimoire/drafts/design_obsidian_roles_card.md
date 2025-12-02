---
card:
  id: obsidian-roles-stigmergy-matrix
  source: design_obsidian_roles.md
  type: Concept
---

# 🃏 OBSIDIAN: Physics of the Swarm

> **Intuition**: OBSIDIAN encodes the immutable archetypes of hive intelligence as a fractal mnemonic, mapping agent roles to JADC2 operations and biological stigmergy for emergent, self-organizing swarms.

## 📜 The Incantation (Intent)
```gherkin
Feature: OBSIDIAN Role Validation
  As the Swarmlord
  I want to ensure every agent is assigned a valid OBSIDIAN role
  So that the Hive maintains semantic integrity

  Scenario Outline: Validate Agent Role Mapping
    Given an agent with role "<Role>"
    When the agent initializes
    Then it should inherit the "<JADC2_Function>" capability
    And it should utilize the "<Stigmergy_Mechanism>" behavior

    Examples:
      | Role        | JADC2_Function | Stigmergy_Mechanism |
      | Observer    | Sensors        | Olfaction           |
      | Bridger     | Gateways       | Boundary            |
      | Shaper      | Effectors      | Secretion           |
      | Injector    | Logistics      | Intensification     |
      | Disruptor   | Red Cell       | Dissipation         |
      | Immunizer   | Shields        | Inhibition          |
      | Assimilator | Fusion         | Accretion           |
      | Navigator   | Command        | Nucleation          |
```

## 🧪 The Catalyst (Code)
```python
# The Essence: OBSIDIAN Role Registry & Validator
OBSIDIAN_ROLES = {
    'Observer': {'jadc2': 'Sensors', 'stigmergy': 'Olfaction', 'desc': 'Detects signals'},
    'Bridger': {'jadc2': 'Gateways', 'stigmergy': 'Boundary', 'desc': 'Translates interfaces'},
    'Shaper': {'jadc2': 'Effectors', 'stigmergy': 'Secretion', 'desc': 'Modifies environment'},
    'Injector': {'jadc2': 'Logistics', 'stigmergy': 'Intensification', 'desc': 'Allocates resources'},
    'Disruptor': {'jadc2': 'Red Cell', 'stigmergy': 'Dissipation', 'desc': 'Simulates failure'},
    'Immunizer': {'jadc2': 'Shields', 'stigmergy': 'Inhibition', 'desc': 'Enforces governance'},
    'Assimilator': {'jadc2': 'Fusion', 'stigmergy': 'Accretion', 'desc': 'Synthesizes wisdom'},
    'Navigator': {'jadc2': 'Command', 'stigmergy': 'Nucleation', 'desc': 'Orchestrates intent'},
}

def validate_obsidian_role(role: str) -> dict | None:
    """
    Validate and retrieve capabilities for an OBSIDIAN role.
    """
    role_data = OBSIDIAN_ROLES.get(role)
    if not role_data:
        raise ValueError(f"Invalid OBSIDIAN role: {role}")
    return role_data
```

## ⚔️ Synergies
*   **Fractal Mnemonics**: Layers with HIVE (vision), GROWTH (strategy), SWARM (tactics), FLEET (lifecycle) for scalable hive governance.
*   **JADC2/MAS Integration**: Maps directly to OODA loops, sensors-effectors, and command chains via Mermaid visualizations.
*   **Hybrid Memory**: Powers Assimilator with NATS JetStream (hot pheromones) + LanceDB/Postgres (cold GraphRAG wisdom).
*   **Stigmergy Cycle**: Enables biological-inspired coordination, regulation (Disruptor/Immunizer), and environmental modification (Shaper/Bridger).