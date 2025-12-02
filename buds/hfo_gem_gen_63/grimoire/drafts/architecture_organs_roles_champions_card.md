---
card:
  id: a2084caf-c715-471f-89e1-00db4124a19a
  source: architecture_organs_roles_champions.md
  type: Concept
---

# 🃏 Organs, Roles, and Champions

> **Intuition**: The Hive emulates a biological organism where immutable Organs provide infrastructure, stable Roles define functions, and evolvable Champions instantiate agents for seamless adaptation.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hive Biological Hierarchy
  Scenario: Evolving a Champion for a Role within an Organ
    Given an Organ exists with path "brain/" and biological function "Cortex"
    And a Role "Navigator" is defined with jadc2_function "Strategist"
    When a Champion "Grok-Navigator-v4" is instantiated for the Role
      And its fitness is evaluated as 0.95
    Then the Champion implements the Role without modifying the Organ or Role
    And the Champion can be swapped for "GPT-5-Navigator-v1" seamlessly
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from dataclasses import dataclass
from typing import Dict

@dataclass
class Organ:
    path: str
    biological_function: str

@dataclass
class Role:
    name: str
    jadc2_function: str

@dataclass
class Champion:
    id: str
    gene_seed: Dict[str, str]  # e.g., {"model": "Grok-Beta", "version": "v4"}
    fitness: float
    organ: Organ
    role: Role

def instantiate_champion(organ: Organ, role: Role, gene_seed: Dict[str, str], fitness: float = 0.0) -> Champion:
    """Evolve a Champion for a Role in an Organ."""
    return Champion(
        id=f"{role.name}-{gene_seed.get('model', 'unknown')}-{gene_seed.get('version', 'v0')}",
        gene_seed=gene_seed,
        fitness=fitness,
        organ=organ,
        role=role
    )
```

## ⚔️ Synergies
*   **Directory Integration**: Organs map to physical folders like `brain/` or `body/`, hosting Role configurations and Champion evolutions.
*   **Agent Pipelines**: Champions evolve via fitness tracking (e.g., Gen 51), enabling succession like Grok-v1 → Gemini-v1 for Roles such as Navigator.
*   **JADC2 Framework**: Roles align with command functions (Navigator, Observer), supporting modular Hive operations.
*   **Scalability**: Allows model swaps (Grok → GPT) without refactoring infrastructure, embodying the Trinity of Place (Organ), Purpose (Role), Person (Champion).