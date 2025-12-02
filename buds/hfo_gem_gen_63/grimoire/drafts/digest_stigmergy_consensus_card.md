---
card:
  id: d7326e20-06f5-4fc4-a5b8-036f599ba4c1
  source: digest_stigmergy_consensus.md
  type: Concept
---

# 🃏 Holographic Consensus

> **Intuition**: Achieve boundless scalability with cognitive simplicity by mirroring micro-agents fractally into macro-swarms through self-similar holons and tri-state data facets.

## 📜 The Incantation (Intent)
```gherkin
Feature: Holographic Consensus via Fractal Holarchy and Stigmergy

  Scenario: Coordinate swarm intelligence through stigmergic phase transitions
    Given a Crystalline ObsidianFacet artifact exists with YAML header and content
    When an Agent emits a Liquid NATS signal carrying the Facet's ID and urgency
    Then peer Agents react in fast loops via NATS
    And the Assimilator deposits the signal into Sedimentary Postgres with vector embedding
    And future Agents excavate relevant Facets via semantic recall for holographic wisdom
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Unified ObsidianFacet Pydantic model for all states
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ObsidianFacet(BaseModel):
    id: str = Field(..., description="Unique facet ID")
    urgency: float = Field(0.5, ge=0.0, le=1.0, description="Hotness/decay factor")
    decay: float = Field(0.5, ge=0.0, le=1.0)
    content: str = Field(..., description="Core payload")
    created: datetime = Field(default_factory=datetime.utcnow)
    generation: int = 0

    @classmethod
    def from_crystal(cls, path: str) -> 'ObsidianFacet':
        """Sublimate: Load from static YAML file"""
        import yaml
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return cls(**data)

    def to_liquid(self) -> dict:
        """Emit: Serialize for fast NATS pheromone"""
        return {'id': self.id, 'urgency': self.urgency, 'content': self.content}

    async def assimilate(self, pg_conn):
        """Deposit: Vectorize and store in cold DB"""
        # Pseudo: embed, insert to Postgres vector store
        embedding = await embed_content(self.content)  # RAG integration
        await pg_conn.execute("INSERT INTO facets ...", self.dict(), embedding)
```

## ⚔️ Synergies
*   **Fractal Holarchy**: Recursive `Holon` class nests Agents into Squads into Hives, applying single `process(task)` logic at all scales.
*   **NATS Pub/Sub**: Liquid state for real-time stigmergic emission/reaction loops.
*   **Postgres PGVector**: Sedimentary state enables semantic recall fueling agent PERCEIVE-REACT cycles.
*   **Pydantic Ecosystem**: Auto-serialization bridges File/NATS/DB, reducing schema mismatches.
*   **Swarm Agents**: Every Agent is a Level-0 Holon, yielding to parents in recursive coordination.