---
card:
  id: 2e86e859-fcd9-4808-872d-e1bdd52a0526
  source: pattern_async_swarm.md
  type: Spell
---

# 🃏 🐝 Async Swarm Process Pattern

> **Intuition**: In the hive's emergent intelligence, fire-and-forget pheromones dispatched via NATS Queue Groups awaken stigmergic AsyncIO workers for fault-tolerant, scalable processing without synchronous bottlenecks.

## 📜 The Incantation (Intent)
```gherkin
Feature: High-Throughput Batch Processing via Async Swarm

  Scenario: Dispatcher scales tasks across fault-tolerant workers
    Given a Dispatcher identifies a batch of tasks
    And publishes lightweight JSON payloads to a NATS JetStream subject with Queue Group "workers"
    When messages are load-balanced round-robin to single-threaded AsyncIO Workers
    And each Worker reads recent stream history for stigmergic context
    Then Workers process non-blocking with aiohttp/AsyncOpenAI
    And emit result signals while acknowledging messages
    And unacknowledged messages redeliver on failure for resilience
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Async Worker in the Swarm
import asyncio
import nats
from nats.js import JetStreamContext

async def async_swarm_worker(jsc: JetStreamContext, subject: str = "hfo.task.spin"):
    """Single-threaded stigmergic worker for fire-and-forget tasks."""
    async for msg in jsc.subscribe(subject, queue="workers"):
        try:
            # Stigmergy: Read recent context from stream history
            context = await jsc.stream_info("hfo_tasks").messages()[-5:]  # Last 5 signals

            # Process async (e.g., LLM call)
            payload = msg.data.decode()
            result = await process_task_async(payload, context)  # aiohttp/AsyncOpenAI

            # Emit signal
            await jsc.publish("hfo.signals", result.encode())

            # Ack for success
            await msg.ack()
        except Exception:
            # Nack for redelivery
            await msg.nak()

# Launcher (spawn multiple)
async def spawn_swarm(num_workers: int = 20):
    nc = await nats.connect("nats://localhost:4222")
    jsc = nc.jetstream()
    await asyncio.gather(*[async_swarm_worker(jsc) for _ in range(num_workers)])
```

## ⚔️ Synergies
*   **NATS JetStream**: Core for Queue Groups, load balancing, redelivery, and stream history enabling stigmergy.
*   **AsyncIO Ecosystem**: Pairs with aiohttp, AsyncOpenAI, instructor for non-blocking I/O; replaces multiprocessing/sync loops.
*   **Hive Fleet Obsidian**: Golden Pattern validated in `body/digestion/swarm_spinner.py` (207 gems, 2025-11-21).
*   **Stigmergy Pattern**: Workers read sibling signals from NATS streams for emergent context without shared state.
*   **Dispatcher Integration**: Fire-and-forget publishers (e.g., Queen scanners) in HFO task subjects like `hfo.task.spin`.