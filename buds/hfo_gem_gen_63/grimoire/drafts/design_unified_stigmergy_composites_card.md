---
card:
  id: bc592351-6150-422e-8d41-22be2101993c
  source: design_unified_stigmergy_composites.md
  type: Concept
---

# 🃏 Hexagonal Stigmergy

> **Intuition**: A hexagonal substrate unifies stigmergic signals into a tunable holon across Ontos, Telos, Chronos, Topos, Logos, and Pathos, composing missions from crystalline archives to reflexive pheromone swarms.

## 📜 The Incantation (Intent)
```gherkin
Feature: Unified Stigmergy via Hexagonal Substrate

  Scenario: Composing a "Living Crystal" Mode for Knowledge Preservation
    Given a mission requiring long-term schema enforcement at HFO L3 (Hive)
    When tuning the Hexagon with high ONTOS crystallinity, high LOGOS precision, and low CHRONOS volatility
    Then the swarm instantiates a rigid, persistent crystal guided by minimal pheromones for attention
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from dataclasses import dataclass
from typing import Dict, Any
import uuid
import hashlib

@dataclass
class Hexagon:
    ontos: Dict[str, Any]
    telos: Dict[str, Any]
    chronos: Dict[str, Any]
    topos: Dict[str, Any]
    logos: Dict[str, Any]
    pathos: Dict[str, Any]

def create_hexagon(mode: str = "living_crystal", intent: str = "preserve_knowledge") -> Dict[str, Dict[str, Any]]:
    """
    Factory for Hexagonal payloads, tunable by mode.
    Serializes to NATS JSON substrate.
    """
    base = {
        "ontos": {"id": str(uuid.uuid4()), "type": "artifact", "crystallinity": 0.0},
        "telos": {"intent": intent, "vector": 0.0},
        "chronos": {"urgency": 0.5, "decay": 0.5, "volatility": 0.0},
        "topos": {"links": [], "connectivity": 0.0},
        "logos": {"hash": "", "validator": "pydantic", "precision": 0.0},
        "pathos": {"sentiment": 0.0, "surprise": 0.0, "energy": 0.0}
    }
    
    modes = {
        "living_crystal": {
            "ontos__crystallinity": 1.0,
            "logos__precision": 1.0,
            "chronos__volatility": 0.1
        }
    }
    
    profile = modes.get(mode, {})
    for key, value in profile.items():
        k1, k2 = key.split("__")
        base[k1][k2] = value
        if k1 == "logos" and k2 == "hash":
            base[k1][k2] = hashlib.sha256(str(base).encode()).hexdigest()
    
    return base
```

## ⚔️ Synergies
*   **HFO Holarchy**: Maps to L0 Prey (Thermodynamic Web), L1 Swarm (Holographic Prediction), L2 Campaign (Neural Mycelium), L3 Hive (Living Crystal).
*   **GROWTH/PREY Loops**: Defines mission profiles at launch; adapts agent reflexes via dimensional knobs.
*   **NATS Substrate**: Serializes directly to payloads for signal propagation across the Hive.
*   **Adversarial Resilience**: Enables Immunizers to monitor and restore hexagonal integrity against dimension-specific attacks.
*   **Fractal Scaling**: Composes higher-order missions by aggregating tuned hexagons into holons.