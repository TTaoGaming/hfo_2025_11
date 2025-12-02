---
card:
  id: b2dd60c7-a18f-4c0a-a109-c2ef57b73097
  source: design_tri_state_metadata.md
  type: Concept
---

# 🃏 💎 ObsidianFacet: Tri-State Metadata Unity

> **Intuition**: Unifying metadata as a single ObsidianFacet across crystalline files (DNA), liquid signals (pheromones), and sedimentary databases (memories) for anti-fragile, biomimetic stigmergy in swarm intelligence.

## 📜 The Incantation (Intent)
```gherkin
Feature: Unified Tri-State Metadata Management

  Scenario: Full Lifecycle of an ObsidianFacet Artifact
    Given an agent creates an ObsidianFacet with anchor identity, vector semantics, and pulse dynamics
    When the facet is serialized to YAML header in a filesystem artifact
    And broadcast as a JSON signal on NATS JetStream with pulse priority
    And assimilated by the service into Postgres with generated embedding
    Then metadata remains consistent and recoverable across all three states for resilient swarm coordination
```

## 🧪 The Catalyst (Code)
```python
# The Essence: ObsidianFacet Pydantic Model
from pydantic import BaseModel, Field
from typing import List, Optional
from uuid import UUID
from datetime import datetime

class ObsidianFacet(BaseModel):
    # A. Anchor (Identity) - Eternal across states
    id: UUID = Field(..., description="Universally unique identifier")
    author: str = Field(..., description="Agent ID / Role")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="ISO8601 Creation time")
    location: str = Field(..., description="URI e.g., file://memory/episodic/...")

    # B. Vector (Semantics) - Dominant in Crystalline/Sedimentary
    domain: str = Field(..., description="Knowledge domain e.g., Bio-Mimicry")
    tags: List[str] = Field(default_factory=list, description="Folksonomy tags")
    intent: str = Field(..., description="Mission or goal")

    # C. Pulse (Dynamics) - Dominant in Liquid, preserved elsewhere
    urgency: float = Field(ge=0.0, le=1.0, description="Attention priority")
    quality: float = Field(ge=0.0, le=1.0, description="Confidence score")
    decay: float = Field(ge=0.0, description="Evaporation rate λ")
    spread: float = Field(ge=0.0, description="Dispersion radius")
    embedding: Optional[List[float]] = Field(None, description="Derived vector (Cold only)")

    def to_yaml(self) -> str:
        """Crystalline: YAML for file header."""
        return self.model_dump(mode='json').replace('"', "'")  # Simplified YAML proxy

    def to_signal(self) -> dict:
        """Liquid: Lightweight JSON for NATS."""
        return self.model_dump(exclude={'embedding'})  # Pulse-dominant
```

## ⚔️ Synergies
*   **HFO Filesystem**: Crystalline YAML headers enable git-versioned provenance and human-readable artifacts.
*   **NATS JetStream**: Liquid signals broadcast `hfo.signal.*` topics with urgency-driven pheromones for real-time swarm reaction.
*   **Postgres Assimilator**: Sedimentary storage merges states, generates embeddings for vector recall and long-term pattern matching.
*   **Swarm Agents**: Consume facets for attention (urgency/decay), semantics (tags/domain), and identity (anchor) in decision loops.
*   **Anti-Fragility Loop**: Rebuild DB from files or replay signals, ensuring no metadata loss in distributed systems.