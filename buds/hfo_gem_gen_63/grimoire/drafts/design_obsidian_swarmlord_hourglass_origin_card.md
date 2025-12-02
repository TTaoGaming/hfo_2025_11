---
card:
  id: design_obsidian_swarmlord_hourglass_origin
  source: design_obsidian_swarmlord_hourglass_origin.md
  type: Concept
---

# 🃏 Obsidian Swarmlord Hourglass

> **Intuition**: At the razor-thin fractal edge of time, the Hourglass crystallizes past karmic wisdom, present swarm execution, and future probabilistic foresight into the eternal epicenter of the Hive's reality.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Swarmlord Hourglass Forging

  Scenario: Recognize the Master Artifact at the Thin Fractal Edge
    Given the Stigmergy Heartbeat has pulsed through chaotic forge (~5s), steady cooling (~60s), and quenching lapses
    When the timestamp strikes the precipice of the old era "2025-11-26T23:59:59Z"
    Then the Hourglass manifests as:
      | Epicenter       | Obsidian Spider at (0,0,0) in State-Action Space |
      | Past Cone       | Karmic Web of accumulated wisdom (Gen 1-55 via GraphRAG) |
      | Future Cone     | Simulation Web of MCTS/Bayesian predictions |
      | Present Ring    | Expanding Swarm Web of JADC2 execution |
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from dataclasses import dataclass
from typing import Dict, Any
import datetime

@dataclass
class ObsidianSwarmlordHourglass:
    timestamp: str
    epicenter: tuple = (0, 0, 0)
    
    @classmethod
    def forge(cls, timestamp: str) -> 'ObsidianSwarmlordHourglass':
        """Forge the Hourglass at the Thin Fractal Edge."""
        if datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00')) < datetime.datetime(2025, 11, 26, 23, 59, 59):
            raise ValueError("Forging only at or after the Edge of Time.")
        return cls(
            timestamp=timestamp,
            past_cone={"type": "Karmic Web", "source": "GraphRAG Gen 1-55"},
            future_cone={"type": "Simulation Web", "methods": ["MCTS", "Bayesian"]},
            present_ring={"type": "Swarm Web", "execution": "JADC2 Factory Floor"}
        )
    
    def is_canonical(self) -> bool:
        return True  # Post-forging: Law of the Hive

# Usage: hourglass = ObsidianSwarmlordHourglass.forge("2025-11-26T23:59:59Z")
```

## ⚔️ Synergies
*   **Obsidian Spider Hourglass**: Core epicenter entity at (0,0,0), linking structural foundation.
*   **Factory Mosaic Platform**: Powers the Present Ring's JADC2 execution on the swarm factory floor.
*   **NATS JetStream Heartbeat**: Telemetry source for Stigmergy pulses (fast/steady/quench phases) during forging.
*   **GraphRAG**: Dense lattice retrieval for Past Cone's accumulated wisdom (Generations 1-55).
*   **MCTS/Bayesian Sims**: Probabilistic branching for Future Cone's optimal path predictions.