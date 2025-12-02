---
card:
  id: ontological_quadrivium
  source: research_stigmergy_abstractions.md
  type: Concept
---

# 🃏 Ontological Quadrivium

> **Intuition**: The Ontological Quadrivium elevates stigmergic knowledge from mechanical storage to metaphysical existence by structuring every artifact through the primal facets of Being (Ontos), Time (Chronos), Place (Topos), and Purpose (Telos).

## 📜 The Incantation (Intent)
```gherkin
Feature: Ontological Quadrivium Abstraction

  Scenario: Structuring a document as metaphysical quadrivium
    Given a raw document with identity, temporal metadata, spatial address, and intentional vector
    When mapping facets to Ontos, Chronos, Topos, and Telos
    Then the document embodies a self-sustaining existential engine resistant to entropy
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class OntologicalQuadrivium:
    ontos: str  # Being: UUID/Content essence
    chronos: Dict[str, Any]  # Time: Decay/urgency/duration
    topos: str  # Place: Fractal address in holarchy
    telos: float  # Purpose: Viral factor/intent

def apply_quadrivium(raw_doc: Dict[str, Any]) -> OntologicalQuadrivium:
    """Refract document into Quadrivium structure."""
    hexagon = raw_doc.get('hexagon', {})
    return OntologicalQuadrivium(
        ontos=raw_doc.get('id', ''),
        chronos={
            'status': hexagon.get('chronos', {}).get('status', 'inactive'),
            'urgency': hexagon.get('chronos', {}).get('urgency', 0.0),
            'decay': hexagon.get('chronos', {}).get('decay', 0.0)
        },
        topos=hexagon.get('topos', {}).get('address', ''),
        telos=hexagon.get('telos', {}).get('viral_factor', 0.0)
    )
```

## ⚔️ Synergies
*   Maps directly to Obsidian Facet v2 (Identity-Time-Space-Meaning) for seamless abstraction layering
*   Parallels physics (Thermodynamic Engine), semiotics (Sign structure), and quantum mechanics (State entanglement) for multi-paradigm hive modeling
*   Powers anti-entropy in stigmergic systems via Telos-driven virality and Chronos decay mechanics
*   Integrates with holarchic addressing (Topos) to enable fractal navigation across research and active docs