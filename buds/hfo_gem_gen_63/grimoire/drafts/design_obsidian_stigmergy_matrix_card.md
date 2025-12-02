---
card:
  id: 550e8400-e29b-41d4-a716-446655440303
  source: design_obsidian_stigmergy_matrix.md
  type: Concept
---

# 🃏 OBSIDIAN Stigmergy Matrix

> **Intuition**: Fusing biological stigmergy with multi-agent doctrine to define the emergent physics of agent-substrate interactions, stabilizing self-organizing hives through role-mapped feedback loops.

## 📜 The Incantation (Intent)
```gherkin
Feature: OBSIDIAN Stigmergy Matrix stabilizes HFO agent interactions

  Scenario: Agent performs role-specific stigmergic modification
    Given an HFO agent in role "Shaper"
    When it detects a substrate boundary condition
    Then it secretes a trace encoding "work done"
      And reinforces the growth loop via positive feedback
      And triggers decay or inhibition if disrupted
```

## 🧪 The Catalyst (Code)
```python
# The Essence
OBSIDIAN_MATRIX = {
    'O': {'hfo': 'Observer', 'mas': 'Telemetry/Watcher', 'stigmergy': 'Olfaction', 'concept': 'Gradient Analysis'},
    'B': {'hfo': 'Bridger', 'mas': 'Protocol/Interface', 'stigmergy': 'Boundary', 'concept': 'Boundary Conditions'},
    'S': {'hfo': 'Shaper', 'mas': 'Executor/Effector', 'stigmergy': 'Secretion', 'concept': 'Deposition'},
    'I': {'hfo': 'Injector', 'mas': 'Logistics/Sustainment', 'stigmergy': 'Intensification', 'concept': 'Positive Feedback (Amplification)'},
    'D': {'hfo': 'Disruptor', 'mas': 'Red Team/Chaos', 'stigmergy': 'Dissipation', 'concept': 'Adversarial Byzantine (Entropy)'},
    'I': {'hfo': 'Immunizer', 'mas': 'Blue Team/Security', 'stigmergy': 'Inhibition', 'concept': 'Negative Feedback (Anti-Fragility)'},
    'A': {'hfo': 'Assimilator', 'mas': 'Knowledge/Synthesis', 'stigmergy': 'Accretion', 'concept': 'Stigmergic Construction'},
    'N': {'hfo': 'Navigator', 'mas': 'Direction/Goals', 'stigmergy': 'Nucleation', 'concept': 'Cluster Formation'},
}

def resolve_stigmergy(role_key: str) -> dict:
    """Resolve HFO role to stigmergic mechanism for substrate interaction."""
    return OBSIDIAN_MATRIX.get(role_key.upper(), {})
```

## ⚔️ Synergies
*   Maps directly to HFO agent roles (Observer → Navigator), enabling polymorphic agent behaviors in the Hexagon ontology.
*   Integrates with `brain/intent_stigmergy_thermodynamics.feature` via growth/decay/control loops for thermodynamic stability.
*   Powers Bridger's schema boundaries for substrate writes, drawing from Theraulaz & Bonabeau wasp nest research.
*   Fuels adversarial evolution: Disruptor (MITRE ATT&CK) + Immunizer for anti-fragile swarms.
*   Enables Nucleation for goal-directed clustering in Obsidian vaults as stigmergic substrates.