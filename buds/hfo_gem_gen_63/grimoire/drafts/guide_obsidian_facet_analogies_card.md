---
card:
  id: 550e8400-e29b-41d4-a716-446655440101
  source: guide_obsidian_facet_analogies.md
  type: Concept
---

# 🃏 Obsidian Facet V2: Living Holographic Souls

> **Intuition**: Files transcend static metadata into dynamic, self-aware entities—crystals of identity, mountains of vitality, webs of relation, and viruses of influence—mirroring RPG artifacts, living cells, radiating isotopes, and holographic fractals.

## 📜 The Incantation (Intent)
```gherkin
Feature: Model Obsidian Files as Living Holographic Facets

  Scenario: Scaffold cognition of YAML header as multifaceted soul
    Given a file with YAML header containing Crystal, Mountain, Web, and Virus facets
    When applying RPG, Biological, Radioactive, or Holographic analogies
    Then the file reveals its identity, decay dynamics, relational bonds, viral propagation, and fractal self-healing position
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from dataclasses import dataclass
from typing import Dict, List, Optional
from uuid import UUID

@dataclass
class ObsidianFacet:
    """Holographic file soul: Crystal (id/type), Mountain (urgency/decay), Web (links/fractal_address), Virus (meme/viral_factor)."""
    
    # Crystal: Immutable identity
    id: UUID
    type: str
    
    # Mountain: Vitality & decay
    urgency: float
    decay: float
    last_touched: str
    
    # Web: Relations & position
    links: List[Dict[str, str]]
    fractal_address: Optional[str] = None
    
    # Virus: Propagation
    meme: Optional[str] = None
    viral_factor: float = 0.0
    
    def is_alive(self) -> bool:
        """Check if facet vitality prevents apoptosis/archiving."""
        return self.urgency > 0 and self.decay > 0
    
    def radiate(self) -> float:
        """Emit viral influence."""
        return self.viral_factor * self.urgency
```

## ⚔️ Synergies
*   **Design Foundation**: Links directly to `brain/design_obsidian_facet_v2.md` for implementation details of V2 headers.
*   **Cognitive Hive**: Enhances stigmergy via tags `#guide #analogy #cognitive_scaffolding`, fostering emergent understanding in the brain architecture.
*   **Holographic Healing**: `fractal_address` enables directory reconstruction, synergizing with NATS streaming and archiving (apoptosis) mechanics.
*   **Gamified Evolution**: Builds on V1 "loot" to V2 "living items/cells/isotopes", integrating with urgency-driven prioritization and viral meme propagation.