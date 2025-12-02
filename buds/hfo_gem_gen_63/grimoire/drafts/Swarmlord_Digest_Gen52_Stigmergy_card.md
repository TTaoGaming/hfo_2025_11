---
card:
  id: 550e8400-e29b-41d4-a716-446655440302
  source: Swarmlord_Digest_Gen52_Stigmergy.md
  type: Concept
---

# 🃏 Stigmergy Thermodynamics

> **Intuition**: The Hive forges intent like a geological volcano, cooling raw molten Lava signals into sharp Obsidian tools and polishing them into enduring Gems of wisdom.

## 📜 The Incantation (Intent)
```gherkin
Feature: Stigmergy State Transitions

  Scenario: Evolve intent from Lava to Obsidian to Gem
    Given a raw "Lava" signal in NATS JetStream
    When the "quench" transition freezes it into Obsidian
    And the "refine" transition polishes Obsidian into a Gem
    Then the signal persists in Filesystem as a sharp tool
    And embeds in Knowledge Graph as refined value
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from hexagon import Hexagon  # Assumed Hexagon model

def quench(hexagon: Hexagon, lava_signal: dict) -> str:
    """Freeze Lava (NATS) into Obsidian (Filesystem)."""
    obsidian_path = f"obsidian/{hexagon.topos.address}.md"
    with open(obsidian_path, "w") as f:
        f.write(f"# {lava_signal['title']}\n{lava_signal['content']}")
    hexagon.telos.viral_factor = 1.0  # Mark as quenched
    return obsidian_path

def refine(obsidian_path: str, hexagon: Hexagon) -> dict:
    """Polish Obsidian into Gem (Knowledge Graph)."""
    # Pseudo: Embed into Postgres/Vector DB
    gem = {
        "ontos": hexagon.ontos,
        "content": open(obsidian_path).read(),
        "vibe": "Value, Memory, Wisdom"
    }
    # db.insert_gem(gem)  # Vector DB persistence
    return gem
```

## ⚔️ Synergies
*   **NATS JetStream**: Medium for "Hot Lava" – raw, fast-flowing signals and actions.
*   **Filesystem**: Hosts "Cold Obsidian" – quenched `.md`/`.py` files as sharp, deployable weapons.
*   **Knowledge Graph (Postgres/Vector DB)**: Stores "Refined Gems" – polished memory with semantic layers (e.g., "Red Gem" for errors).
*   **Hexagon Model**: Core structure enabling `quench()`/`refine()` transitions, with ontos/chronos/topos/telos facets.
*   **Standardization**: Enforces Hot/Cold/Refined terminology across all Hive code/docs for stigmergic cohesion.