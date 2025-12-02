---
card:
  id: 60e75863-bbfb-4ead-b384-1634a35532a8
  source: pattern_claim_check.md
  type: Concept
---

# 🃏 Claim Check Pattern (Rich Stigmergy)

> **Intuition**: Heavy artifacts are durably stored while lightweight signals with rich metadata propagate through the nervous system, enabling total decoupling, hexagonal composability, and emergent swarm coordination via rich stigmergy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Claim Check Pattern for Decoupled Artifact Signaling

  Scenario: Agent publishes a claim check signal after storing an artifact
    Given an agent has generated a heavy artifact content
    And durable storage "Postgres/pgvector" is available
    When the agent saves the artifact to storage generating a unique ID and checksum
    And the agent constructs a lightweight signal with rich metadata, ID, location, summary, tags, and confidence
    Then the signal is published to NATS JetStream
    And consumers receive and filter signals heuristically without retrieving the body
    And interested consumers claim the artifact from storage using the location pointer
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Publish a Claim Check Signal
import uuid
import hashlib
import json
import nats
from sqlalchemy import create_engine, text

def publish_claim_check(artifact_content: str, role: str, mission_slug: str, tags: list, summary: str, confidence: float) -> str:
    # 1. Save Artifact to Postgres/pgvector
    artifact_id = str(uuid.uuid4())
    checksum = hashlib.sha256(artifact_content.encode()).hexdigest()
    
    engine = create_engine("postgresql://hfo:hfo@localhost:5435/hfo_memory")
    with engine.connect() as conn:
        conn.execute(
            text("INSERT INTO artifacts (id, content, checksum, embedding) VALUES (:id, :content, :checksum, :embedding)"),
            {"id": artifact_id, "content": artifact_content, "checksum": checksum, "embedding": []}  # Embed via pgvector
        )
        conn.commit()
    
    # 2. Construct Rich Signal (Pheromone)
    signal = {
        "id": artifact_id,
        "role": role,
        "mission_slug": mission_slug,
        "round": 1,  # Example
        "confidence": confidence,
        "tags": tags,
        "location": {
            "type": "postgres",
            "table": "artifacts",
            "id": artifact_id,
            "url": "postgres://hfo:hfo@localhost:5435/hfo_memory"
        },
        "summary": summary[:200],
        "checksum": checksum
    }
    
    # 3. Publish to NATS JetStream
    nc = nats.connect("nats://localhost:4222")
    js = nc.jetstream()
    js.publish("stigmergy.signals", json.dumps(signal).encode())
    nc.close()
    
    return artifact_id
```

## ⚔️ Synergies
*   Powers the SWARM Loop by enabling independent hexagonal phases (Set → Watch → Act → Review) via NATS bus without direct coupling.
*   Integrates NATS JetStream as the high-throughput "nervous system" for signals, preventing message bloat.
*   Leverages Postgres/pgvector for artifact persistence, semantic indexing, and verifiable retrieval.
*   Supports emergence by allowing arbitrary listeners (e.g., dashboards, auditors) to filter and claim without producer changes.
*   Enhances resilience and scalability: artifacts survive crashes, scales to 1:N or N:1 producer-consumer ratios.