---
card:
  id: 550e8400-e29b-41d4-a716-446655440200
  source: design_unified_hexagonal_adapter.md
  type: Tool
---

# 🃏 Unified Hexagonal Adapter: The Fractal Holon Protocol

> **Intuition**: A polymorphic Hexagon that shapeshifts across states of matter—Crystalline files, Liquid signals, Sedimentary vectors, Holographic graphs—preserving intent as the single source of truth in fractal holarchy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hexagonal Adapter Protocol
  As a Swarmlord
  I want a unified metadata structure
  So that my intent survives the transition from Mind to Code to Memory

  Scenario: Phase Transition (File -> Signal -> Graph)
    Given I have a design file "brain/mission_alpha.md"
    And the file has a valid "Hexagonal Header"
    When the "Observer" agent reads the file
    Then it can instantly convert it to a "NATS Signal" (Liquid)
    And the "Assimilator" can convert that Signal to a "Graph Node" (Holographic)
    And the "Ontos" (Identity) and "Telos" (Purpose) remain identical across all 3 states
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID
from enum import Enum
import hashlib

class HexagonDimension(BaseModel):
    ontos: dict = {}  # id, type, owner
    chronos: dict = {}  # created, urgency, decay, status
    topos: dict = {}  # address, links
    telos: dict = {}  # meme, bluf, viral_factor
    logos: dict = {}  # hash, schema_v, signature
    pathos: dict = {}  # sentiment, quality_score, review_status

class HexagonalHeader(BaseModel):
    hexagon: HexagonDimension

    def to_yaml(self) -> str:
        """Crystalline: File frontmatter."""
        return self.model_dump_yaml()

    def to_signal(self) -> dict:
        """Liquid: NATS JSON pheromone."""
        return {"hexagon": self.hexagon.model_dump(exclude={"logos", "pathos"})}

    def to_vector_meta(self) -> dict:
        """Sedimentary: Vector DB metadata."""
        return self.hexagon.model_dump()

    def to_graph_node(self) -> dict:
        """Holographic: KG node."""
        return {"properties": self.hexagon.topos, "telos": self.hexagon.telos}

    @classmethod
    def from_file(cls, content: str) -> 'HexagonalHeader':
        """Parse YAML frontmatter from Markdown."""
        # Simplified parser logic
        yaml_block = content.split('---')[1]
        data = yaml.safe_load(yaml_block)
        return cls.model_validate(data)
```

## ⚔️ Synergies
*   **Unifies** hexagonal holon headers (links to `design_hexagonal_holon_header.md`), ensuring SSOT across Hive artifacts.
*   **Implements** Obsidian Facet v2 (`design_obsidian_facet_v2.md`), embedding polymorphic metadata in notes.
*   **Enables** Claim-Check pattern (`pattern_claim_check.md`), decoupling payload from lightweight signals.
*   **Drives Stigmergy**: Urgency/decay propagate via NATS pheromones for agent coordination.
*   **Fractal Scaling**: Hexagon nests in files, DBs, graphs, supporting GraphRAG and phase transitions.