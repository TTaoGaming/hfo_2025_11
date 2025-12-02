---
card:
  id: 550e8400-e29b-41d4-a716-446655440001
  source: holonic_stigmergy_architecture.md
  type: Concept
---

# 🃏 Holonic Stigmergy Architecture

> **Intuition**: A recursive, self-referential holonic system where artifacts phase between static files, hot signals, and cold memories—unified by a shared schema—to enable emergent stigmergic coordination in the swarm.

## 📜 The Incantation (Intent)
```gherkin
Feature: Holonic Stigmergy Across States of Matter

  Scenario: Phasing a Holon Through Layers
    Given a Holon with unified schema in "static" layer as YAML frontmatter
    When an Agent sublimates it to "hot" layer via NATS JetStream signal
    And the Assimilator condenses it to "cold" layer in Postgres with embeddings
    Then the Holon maintains integrity via ID, hash, and refs across all states
    And recursive parent_id enables nested holonic structures
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Unified Holon Factory
import uuid
import hashlib
import datetime
from typing import Optional, List, Dict, Any

def create_holon(
    holon_type: str,
    layer: str,
    status: str = "draft",
    parent_id: Optional[str] = None,
    refs: Optional[List[str]] = None,
    author: str = "Swarmlord",
    content: Optional[str] = None
) -> Dict[str, Any]:
    """
    Forge a Holon header, the DNA shared across static/hot/cold states.
    """
    holon_id = str(uuid.uuid4())
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    content_hash = hashlib.sha256(content.encode()).hexdigest() if content else None
    
    holon = {
        "holon": {
            "id": holon_id,
            "type": holon_type,
            "version": "1.0",
            "parent_id": parent_id,
            "refs": refs or [],
            "layer": layer,
            "status": status,
            "author": author,
            "timestamp": timestamp,
            "hash": content_hash
        }
    }
    return holon
```

## ⚔️ Synergies
*   **NATS JetStream**: Powers "hot" stigmergy for real-time sublimation/deposition of signals.
*   **Postgres/GraphRAG**: Anchors "cold" layer with JSONB headers, TEXT bodies, and VECTOR embeddings for semantic recall.
*   **File System (brain/body/memory)**: Serves as "static" source-of-truth with YAML frontmatter for persistent holons.
*   **Holonic Recursion**: parent_id and refs enable nested missions/tasks/artifacts, fostering emergent swarm hierarchies.
*   **Assimilation Cycle**: Agents trigger phase transitions (e.g., static→hot→cold) for self-reinforcing stigmergy.