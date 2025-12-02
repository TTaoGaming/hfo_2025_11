---
card:
  id: e545a071-d7e6-49c8-8f3f-0ecef44b3230
  source: mission_ingest_gems.md
  type: Spell
---
# 🃏 💎 Ingest Gems

> **Intuition**: Crystallize ancestral wisdom from raw gems into enduring semantic structures, bridging archive to collective memory through swarm alchemy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Ingest Ancestral Gems into Semantic Memory

  Scenario: Process Gen 1-50 Gems via Swarm Spinner
    Given gems located at "eyes/archive/hfo_gem/"
    When Swarm Spinner asynchronously reads files and extracts concepts via LLM
    Then structured crystals are saved to "memory/semantic/library/"
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import asyncio
from swarm_spinner import SwarmSpinner  # Async NATS-based processor
from llm_extractor import extract_crystal

async def ingest_gems(source_dir="eyes/archive/hfo_gem/", dest_dir="memory/semantic/library/"):
    spinner = SwarmSpinner()
    gems = await spinner.read_archive(source_dir)
    for gem in gems:
        crystal = await extract_crystal(gem.content)
        await spinner.save_crystal(dest_dir, crystal)
    await spinner.shutdown()
```

## ⚔️ Synergies
*   Links **Archive** (`eyes/archive/hfo_gem/`) to **Semantic Memory** (`memory/semantic/library/`) via **Swarm Spinner** for scalable async ingestion.
*   Integrates **LLM** for concept extraction, transforming raw text into structured "crystals".
*   Follows state machine: Idle → Spinning (task received) → Crystallizing (LLM done) → Idle (saved).
*   Leverages NATS for distributed, non-blocking processing of Gen 1-50 gems.