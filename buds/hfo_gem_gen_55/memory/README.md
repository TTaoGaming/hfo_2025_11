# 📚 Memory (The Assimilator)

> **Role**: Assimilator (Learner)
> **Pillar**: Knowledge
> **Stigmergy Dimension**: **Ontos** (Being, Reality, Truth)

## The Cognitive Function
**Memory** is the seat of **Truth**. It crystallizes the fleeting signals of the Hive into enduring structures. It ensures that what is learned is never lost, and what is known is accessible.

## The Anatomy
*   **`lancedb/`**: The "Cold Vault" of the Hive.
    *   **Vector Embeddings**: Semantic storage for fuzzy retrieval using `all-MiniLM-L6-v2`.
    *   **Unified System**: Managed by `UnifiedMemorySystem` (Hot NATS -> Cold LanceDB).
*   **`docs-diataxis/`**: The "Library" of the Hive.
    *   **Tutorials**: Learning-oriented lessons.
    *   **How-To Guides**: Problem-oriented recipes.
    *   **Reference**: Information-oriented technical descriptions.
    *   **Explanation**: Understanding-oriented background.

## Unified Memory System (Gen 55)

> **Architecture**: Hot (NATS) -> Cold (LanceDB)
> **Protocol**: Stigmergy

This module implements the **Unified Memory System**. It bridges the gap between fast, ephemeral coordination (Hot Stigmergy) and long-term semantic storage (Cold Memory).

### Components

1.  **Hot Memory (NATS JetStream)**:
    *   **Purpose**: Real-time coordination, signaling, and "Pheromone" trails.
    *   **Technology**: NATS JetStream (Stream: `HIVE_MIND`).
    *   **Access**: `UnifiedMemorySystem.write_hot()`

2.  **Cold Memory (LanceDB)**:
    *   **Purpose**: Long-term knowledge, semantic search, and "Genetic" memory.
    *   **Technology**: LanceDB + `all-MiniLM-L6-v2` embeddings.
    *   **Access**: `UnifiedMemorySystem.write_cold()` / `query_cold()`

3.  **The Assimilator (Cooling Process)**:
    *   **Purpose**: To move data from Hot to Cold.
    *   **Mechanism**: A background loop that listens to `hfo.>` on NATS and persists payloads to LanceDB.
    *   **Access**: `UnifiedMemorySystem.run_assimilator()`

### Usage

```python
import asyncio
from buds.hfo_gem_gen_55.memory import UnifiedMemorySystem

async def main():
    # Initialize
    mem = UnifiedMemorySystem()
    await mem.start()

    # 1. Hot Write (Fast Signal)
    await mem.write_hot("hfo.agents.scout", {"status": "found_resource", "loc": "x,y"})

    # 2. Cold Write (Direct Knowledge)
    mem.write_cold("agents.scout", {"fact": "The sky is blue"})

    # 3. Semantic Search
    results = await mem.query_cold("sky color")
    print(results)

    await mem.stop()

if __name__ == "__main__":
    asyncio.run(main())
```

## The HFO Axis
*   **Input**: Raw signals from **Sensors** and synthesized reports from **Nerves**.
*   **Output**: Context and Wisdom provided to the **Brain**.
*   **Failure Mode**: Amnesia (Loss of Context).
