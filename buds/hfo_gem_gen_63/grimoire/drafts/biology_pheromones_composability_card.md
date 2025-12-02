---
card:
  id: 6718f2e1-29b1-48c2-960a-f298eda48613
  source: biology_pheromones_composability.md
  type: Concept
---

# 🃏 Pheromones & Composability

> **Intuition**: Antifragile hive intelligence emerges from a tri-layered pheromone landscape—static scents, hot alarms, and cold ancestral wisdom—where stress composes signals into self-strengthening behaviors.

## 📜 The Incantation (Intent)
```gherkin
Feature: Tri-Layered Pheromone Stigmergy for Antifragile Coordination

  Scenario: Composing Signals into Emergent, Hardening Responses
    Given a Hive with Static YAML Headers, Hot NATS JetStream, and Cold Vector DB layers
    When agents emit overlapping pheromone signals exceeding density thresholds
    And Immunizer detects stress from high signal volume or disruptors
    Then composite signals trigger reactive agents and Hive Guard validation
    And the system hardens by spawning stem cells and strictening rules
    And post-stress, the Hive relaxes with stronger ancestral patterns embedded
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Pheromone Composer for Tri-Layer Synthesis
from typing import Dict, List, Any
import yaml  # Static layer
# Assume NATS & Vector clients imported

def compose_pheromones(
    static_header: Dict[str, Any],
    hot_signals: List[Dict],
    cold_patterns: Dict[str, float]
) -> Dict[str, Any]:
    """
    Synthesizes a composite pheromone signal across layers for emergent action.
    """
    # Static: Governance baseline
    validity = static_header.get('governance', {}).get('valid', True)
    if not validity:
        raise ValueError("Static slop detected")
    
    # Hot: Real-time density
    density = len(hot_signals)
    stress_level = min(density / 10.0, 1.0)  # Threshold at 10 signals
    
    # Cold: Ancestral weighting
    composite_strength = sum(cold_patterns.values()) * stress_level
    
    # Emergent composite (e.g., Food + Danger = Caution)
    composite = {
        'type': 'composite',
        'strength': composite_strength,
        'action': 'cautious_harvest' if stress_level > 0.5 else 'full_engage',
        'immunizer_trigger': stress_level > 0.7
    }
    
    # Harden on stress: Simulate Immunizer
    if composite['immunizer_trigger']:
        composite['hardening'] = {'stem_cells': True, 'strictness': 'HIGH'}
    
    return composite

# Usage: Triggers NATS emit or Vector ingest on composite
```

## ⚔️ Synergies
*   **Immunizer**: Activates on high pheromone density for antifragile hardening and stem cell spawning.
*   **Hive Guard**: Validates static YAML headers to prevent "slop" propagation.
*   **Assimilator**: Ingests artifacts into cold Vector/Graph DB for long-term pattern wisdom.
*   **NATS JetStream**: Powers hot layer for real-time alarms, triggers, and agent reactions.
*   **Reactive Agents**: Query cold layer and act on composite signals for stigmergic emergence.