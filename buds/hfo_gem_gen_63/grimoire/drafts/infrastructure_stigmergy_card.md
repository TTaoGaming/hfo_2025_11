---
card:
  id: stigmergy-nats-jetstream
  source: infrastructure_stigmergy.md
  type: Tool
---

# 🃏 Stigmergy Layer (NATS JetStream)

> **Intuition**: Swarm agents achieve indirect coordination by publishing lightweight signals to a shared environment, allowing others to react without direct coupling, embodying ant-like stigmergy for massive scalability.

## 📜 The Incantation (Intent)
```gherkin
Feature: Stigmergy Coordination via NATS JetStream

  Scenario: Agent publishes task completion signal triggering downstream reactions
    Given an agent has completed a task and persisted the artifact in a memory store
    When the agent publishes a lightweight JSON pheromone signal to the NATS JetStream subject "HFO.Task.Complete"
    Then consumer agents subscribed to the stream receive the signal
    And consumers fetch the heavy artifact from the store using the signal's pointer
    And consumers react by initiating new actions without knowing the publisher
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Publish a pheromone signal to NATS JetStream
import asyncio
import json
from nats.aio.client import Client as NATS

async def publish_pheromone(nats_url: str, subject: str, payload: dict, artifact_id: str):
    """
    Publish a lightweight signal (pheromone) pointing to a heavy artifact.
    """
    nc = NATS()
    await nc.connect(nats_url)

    signal = {
        "type": "pheromone",
        "event": "task.complete",
        "artifact_id": artifact_id,
        **payload
    }

    await nc.publish(subject, json.dumps(signal).encode())
    await nc.close()
    print(f"Published signal to {subject} for artifact {artifact_id}")
```

## ⚔️ Synergies
*   **Agents**: Decouples publishers from consumers, enabling any agent to react to pheromones without direct addressing.
*   **Memory Store**: Signals carry pointers to S3/Postgres artifacts, keeping NATS lightweight.
*   **JetStream Streams**: Uses durable streams (e.g., "HFO.>") with retention policies for natural decay and clutter prevention.
*   **Swarm Scalability**: Supports horizontal scaling of consumers via push/pull subscriptions for high-throughput Hive Fleet Obsidian operations.