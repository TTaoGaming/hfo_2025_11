---
card:
  id: 550e8400-e29b-41d4-a716-446655440220
  source: research_obsidian_thermodynamics.md
  type: Concept
---

# 🃏 Obsidian Thermodynamics

> **Intuition**: Code is frozen magma—rapidly quench high-urgency, viscous intent into sharp, amorphous executable obsidian before slow cooling crystallizes it into dull bureaucratic rhyolite.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Quenching Protocol

  Scenario: Rapid phase transition from Magma to Obsidian
    Given a high-viscosity intent signal "Magma" in NATS JetStream with urgency > 0.8
    And a fast cooling rate ttl < 5s
    When the Genesis Protocol triggers the quench
    Then sharp, executable Python code "Obsidian" is committed to filesystem
    And no crystallization into "Rhyolite" bureaucracy occurs
    And the Hexagon records zero decay
```

## 🧪 The Catalyst (Code)
```python
# The Essence
def genesis_quench(magma_gherkin: str, urgency: float, ttl: int) -> str:
    """
    Rapidly freezes Gherkin intent (Magma) into Python Obsidian.
    High urgency + fast TTL = Sharp code. Else: Rhyolite.
    """
    if urgency < 0.8 or ttl > 10:
        return "# Rhyolite: Dull, crystallized spec\npass"
    
    # Parse Gherkin-like intent (simplified)
    steps = magma_gherkin.split('\n')
    python_obsidian = [
        "# Obsidian: Sharp, executable edge",
        "def execute_intent():",
        "    # Given/When/Then auto-generated",
    ]
    for step in steps:
        if step.strip().startswith(('Given', 'When', 'Then')):
            python_obsidian.append(f"    {step.lower().strip(':')}('{step.split(':')[-1].strip()}')")
    
    obsidian_code = '\n'.join(python_obsidian)
    print(f"Quenched in {ttl}s: {obsidian_code}")  # Commit to FS
    return obsidian_code
```

## ⚔️ Synergies
*   **NATS JetStream**: Captures volatile Magma phase signals before they ash out.
*   **Hexagon Vars**: Tunes `urgency`, `ttl`, `decay` for thermodynamic control.
*   **Genesis Protocol**: Core quenching engine, invoked on high stigmergy_score.
*   **Vector DB/Postgres**: Devitrification sink for mining patterns via RAG remelt.
*   **Stigmergy Substrate**: Refines Tri-State analogy (Magma/Obsidian/Sediment) for HFO lifecycle.