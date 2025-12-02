---
card:
  id: 550e8400-e29b-41d4-a716-446655440301
  source: design_hfo_stigmergy_variants.md
  type: Concept
---

# 🃏 HFO Stigmergy: Obsidian Thermodynamics

> **Intuition**: Hexagons, as polymorphic holons, phase-transition between Hot (lava signals), Cold (obsidian files), and Refined (gem memories), unifying stigmergy through thermodynamic flows.

## 📜 The Incantation (Intent)
```gherkin
Feature: Unify HFO Stigmergy via Obsidian Thermodynamics

  Scenario: Phase Transition of a Hexagon Holon
    Given a Hexagon in "Hot" state as JSON payload on NATS JetStream
    When the Obsidian Protocol quenches it to "Cold" YAML frontmatter in filesystem
    And refines it to "Refined" state in Postgres vector DB
    Then the Hexagon maintains immutable interface across states
    And enables machine coordination, human intent, and long-term retrieval
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Hexagonal Adapter with Phase Transitions
from pydantic import BaseModel
from typing import Any

class Ontos(BaseModel): id: str; type: str
class Telos(BaseModel): viral_factor: float = 1.0; meme: str = ""
class Chronos(BaseModel): urgency: float = 1.0; decay: float = 0.0
class Topos(BaseModel): address: str; links: list = []
# Logos, Pathos omitted for brevity

class Hexagon(BaseModel):
    ontos: Ontos
    telos: Telos
    chronos: Chronos
    topos: Topos

    def quench(self, payload: dict[str, Any]) -> str:
        """Hot (JSON) -> Cold (YAML)"""
        hex_obj = Hexagon(**payload["hexagon"])
        return hex_obj.model_dump_yaml()

    def melt(self, yaml_str: str) -> dict:
        """Cold (YAML) -> Hot (JSON)"""
        hex_obj = Hexagon.model_validate_yaml(yaml_str)
        return {"hexagon": hex_obj.model_dump()}
```

## ⚔️ Synergies
*   **Hexagonal Fractal Holarchy**: Hexagon as universal adapter extends `design_hexagonal_holon_header.md`.
*   **Obsidian Thermodynamics**: Implements core principles from `research_obsidian_thermodynamics.md`.
*   **Stigmergic Mediums**: Integrates NATS JetStream (Hot), Filesystem (Cold), Postgres/Vector DB (Refined).
*   **Protocols**: Fuels Genesis (signal-to-file), Assimilator (file-to-DB), and Hexagonal Lens tool.
*   **Hive Lifecycle**: Enables eruption/quench/refine flow for agents, knowledge graphs, and human tools.