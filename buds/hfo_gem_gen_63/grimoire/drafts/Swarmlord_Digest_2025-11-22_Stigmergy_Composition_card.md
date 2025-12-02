---
card:
  id: cbba5090-8a52-41e4-9d89-9d94d480d192
  source: Swarmlord_Digest_2025-11-22_Stigmergy_Composition.md
  type: Concept
---

# 🃏 Synapse APEX Stigmergy Triad

> **Intuition**: Like a hive's nerves flashing pheromones while the brain hoards memories, the Hot-Cold-Static triad with Claim Checks ensures swift, unclogged coordination at antifragile scale.

## 📜 The Incantation (Intent)
```gherkin
Feature: Stigmergy Composition via Claim Check Pattern

  Scenario: Agent emits lightweight signal for heavy artifact
    Given an agent has generated an artifact payload
     And cold storage is available for persistence
    When the agent persists the artifact to cold storage and retrieves its claim ID
    When the agent emits a signal to hot storage containing only the claim ID and metadata
    Then hot storage enforces size limits and TTL decay on the signal
    Then consumers claim the full payload from cold storage using the ID as needed
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Publish Claim Check to Stigmergy Hot Layer
import uuid
import nats
from pydantic import BaseModel
from sqlalchemy.orm import Session  # Assuming Postgres cold storage

class ClaimCheck(BaseModel):
    id: str
    metadata: dict
    ttl: float = 3600.0  # Exponential decay base

async def publish_claim_check(payload: str, metadata: dict, db: Session, nc: nats.NATS):
    """Persist artifact to cold, emit lightweight claim to hot."""
    # 1. Persist to Cold (Postgres)
    artifact_id = str(uuid.uuid4())
    # db.execute(insert_artifact(artifact_id, payload))  # Simplified
    db.commit()
    
    # 2. Emit Claim Check to Hot (NATS JetStream)
    claim = ClaimCheck(id=artifact_id, metadata=metadata)
    await nc.publish("swarm.pheromones", claim.model_dump_json().encode())
```

## ⚔️ Synergies
*   **Hot Layer**: NATS JetStream for ephemeral pheromones with TTL decay (ACO-inspired).
*   **Cold Layer**: Postgres (pgvector) for structured artifacts and semantic search.
*   **Static Layer**: Markdown filesystem as regenerative DNA (e.g., via `generate_readmes.py`).
*   **Enforcement**: `guard_stigmergy.py` rejects oversized NATS messages (>1MB).
*   **Producers**: Refactored `research_swarm.py` writes to cold first.
*   **Consumers**: `Assimilator` agent claims signals to build Knowledge Graph.