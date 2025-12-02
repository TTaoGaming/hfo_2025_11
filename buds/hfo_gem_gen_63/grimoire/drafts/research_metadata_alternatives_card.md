---
card:
  id: metadata-evolution-hybrid
  source: research_metadata_alternatives.md
  type: Concept
---

# 🃏 Rich Metadata Hybrids

> **Intuition**: Metadata is living matter, hybridizing geological structure, pheromonal pulses, and mycelial webs to fluidly orchestrate information across static, hot, and cold states in the hive's stigmergy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hybrid Metadata Management for HFO Tri-State

  Scenario: Evolve information metadata across states
    Given an artifact in static YAML with structured "Obsidian Facet" schema including id, owner, and links
    When hot activity triggers a NATS signal with pheromone urgency and decay updates
    Then cold DB persists topology, embeddings, and integrated posterior beliefs ensuring self-optimizing flow
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Hybrid Hexagon Metadata Model
from pydantic import BaseModel, Field
from typing import Dict, List, Any
from datetime import datetime

class Chronos(BaseModel):
    status: str = "active"
    urgency: float = 0.5
    decay: float = 0.5
    created: datetime = Field(default_factory=datetime.utcnow)

class Topos(BaseModel):
    address: str
    links: List[str] = []

class Hexagon(BaseModel):
    """Hybrid: Obsidian structure + Pheromone chronos + Mycelial topos."""
    ontos: Dict[str, Any]
    chronos: Chronos
    topos: Topos
    telos: Dict[str, Any] = {}

    def pulse(self, delta_urgency: float):
        """Hot state: Decay and urgency update (Pheromone evaporation)."""
        self.chronos.urgency = max(0.0, self.chronos.urgency + delta_urgency - self.chronos.decay)
        self.chronos.decay *= 0.9  # Evaporate

    def link(self, target_address: str):
        """Mycelial: Add graph edge."""
        if target_address not in self.topos.links:
            self.topos.links.append(target_address)
```

## ⚔️ Synergies
*   **Stigmergy Core**: Powers Tri-State (YAML Static → NATS Hot → DB Cold) with seamless transitions.
*   **Hive Fleet Obsidian**: Backbone for knowledge mgmt (structure) + action coordination (urgency/links).
*   **NATS Swarm**: Hot pulses carry lightweight `{id, urgency, pointer}` for real-time stigmergy.
*   **Graph/DB Layer**: Mycelial links + embeddings enable discovery and flow optimization.
*   **Extensibility**: Borrow Active Inference for future `confidence` priors in `ontos`.