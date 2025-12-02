---
card:
  id: hexagonal-holon-metadata-sota
  source: research_header_sota_options.md
  type: Concept
---

# 🃏 Hexagonal Holon Metadata Protocol

> **Intuition**: Model universal metadata as a biomimetic hexagonal holon—Ontos, Telos, Chronos, Topos, Logos, Pathos—to enable fractal, stigmergic coordination across files, signals, vectors, and graphs while prioritizing human-readable intent.

## 📜 The Incantation (Intent)
```gherkin
Feature: Universal Metadata Protocol for Fractal Holarchy

  Scenario: Select optimal metadata structure supporting Stigmergy and Intent
    Given SOTA options including Hexagonal Holon, Kubernetes Manifest, JSON-LD, and CloudEvents
    When evaluating against requirements for self-similarity, human-centric readability, and adaptability
    Then adopt Hybrid Hexagonal Holon with adaptations from K8s spec/status split, JSON-LD link relations, and CloudEvent signaling
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Polymorphic Pydantic Hexagonal Holon
from pydantic import BaseModel
from typing import Dict, Any
from uuid import UUID

class Ontos(BaseModel):
    id: UUID
    type: str
    owner: str

class Telos(BaseModel):
    viral_factor: float
    meme: str

class Chronos(BaseModel):
    status: str
    urgency: float
    decay: float
    created: str
    generation: int

class Topos(BaseModel):
    address: str
    links: list

class HexagonalHolon(BaseModel):
    ontos: Ontos
    telos: Telos
    chronos: Chronos
    topos: Topos
    logos: Dict[str, Any] = {}  # Logic/Annotations
    pathos: Dict[str, Any] = {}  # Quality/Metadata

    def to_cloudevent(self) -> Dict[str, Any]:
        """Adapt to CloudEvents for signaling."""
        return {"specversion": "1.0", "type": f"hfo.{self.ontos.type}", "data": self.dict()}

    def to_jsonld(self) -> Dict[str, Any]:
        """Adapt to JSON-LD for graph export."""
        return {"@context": "http://hfo.io/schema", "@type": self.ontos.type, **self.dict(exclude={"ontos", "telos"})}
```

## ⚔️ Synergies
*   **Fractal Holarchy**: Self-similar structure applies identically to L0 code artifacts, L1 signals, L2 vectors, and L3 strategies.
*   **Stigmergy Engine**: Leverages `chronos.urgency` and `telos.viral_factor` for environment-based coordination and decay.
*   **Adapters**: Exports to Kubernetes `spec/status` via `telos/chronos` mapping; JSON-LD triples via `topos.links`; CloudEvents for NATS bus.
*   **Design Pipeline**: Critiques/informs `brain/design_unified_hexagonal_adapter.md` for polymorphic YAML parsing.
*   **Swarm Lifecycle**: Supports "Crystalline/Liquid/Sedimentary" phases with human-readable YAML frontmatter.