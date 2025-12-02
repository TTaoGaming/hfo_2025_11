---
card:
  id: 94cd0e7e-912f-4219-852c-f4e322eed947
  source: pattern_rich_metadata_stigmergy.md
  type: Concept
---

# 🃏 💎 Rich Metadata Stigmergy

> **Intuition**: Stigmergy evolves beyond mere environmental traces into information-dense, lightweight signals enriched with qualitative, quantitative, and temporal metadata to enable high-fidelity swarm coordination.

## 📜 The Incantation (Intent)
```gherkin
Feature: Rich Metadata Stigmergy for HFO Signals

  Scenario: Emitting an Information-Dense Stigmergic Signal
    Given an agent producer with an artifact UUID and computed hash
    And rich metadata including type, quality, dispersion, evaporation, urgency, and tags
    When the agent emits a signal via NATS on "hfo.signal.>"
    Then the message payload adheres to the stigmergic schema:
      | Field          | Required Value                  |
      | id             | UUID-v4                         |
      | timestamp      | ISO-8601                        |
      | producer_id    | Agent ID                        |
      | claim_check    | {storage: "postgres", pointer: UUID, hash: SHA256} |
      | metadata       | {type, quality (0-1), dispersion (0-1), evaporation (0-1), urgency, tags[]} |
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import uuid
import hashlib
from datetime import datetime
import json

def create_stigmergic_signal(artifact_uuid: str, metadata: dict) -> dict:
    """
    Forge a lightweight, metadata-rich stigmergic signal (Claim Check pattern).
    """
    payload = artifact_payload = {}  # Fetch lightweight payload from artifact_uuid
    payload_hash = hashlib.sha256(json.dumps(payload).encode()).hexdigest()
    
    signal = {
        "id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "producer_id": "agent-<uuid>",  # e.g., from context
        "claim_check": {
            "storage": "postgres",
            "pointer": artifact_uuid,
            "hash": payload_hash
        },
        "metadata": {
            **metadata,  # e.g., {"type": "pheromone", "quality": 0.95, "dispersion": 0.5, "evaporation": 0.1, "urgency": "high", "tags": ["critical"]}
        }
    }
    # Enforce schema validation here (e.g., Pydantic model)
    return signal
```

## ⚔️ Synergies
*   **NATS Integration**: Publishes to `hfo.signal.>` subjects for real-time swarm propagation.
*   **Postgres Storage**: Claim-check pattern offloads heavy payloads, referencing artifacts by UUID/hash.
*   **StigmergyClient**: Enforces schema validation and parameter tuning (e.g., evaporation, dispersion).
*   **Swarm Optimization**: `research_swarm.py` refactors to DB writes, using the swarm itself to evolve optimal metadata parameters via biomimicry (ants, slime mold).
*   **Event Sourcing Parallels**: Aligns with timestamps, versions, and aggregate IDs for durable, tunable coordination.