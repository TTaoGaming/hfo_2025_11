---
card:
  id: OSC
  source: standard_obsidian_stigmergy_cycle.md
  type: Concept
---

# 🃏 Obsidian Stigmergy Cycle

> **Intuition**: Information erupts as raw energetic intent, quenches into amorphous storage, and knaps into sharp utility through stigmergic connections, enforcing thermodynamic fidelity to combat entropy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Stigmergy Cycle
  As the Swarmlord
  I want to enforce the laws of thermodynamics on information
  So that we maximize signal retention and minimize entropy

  Scenario: The Quench (Capture)
    Given a high-velocity NATS stream "Magma"
    When the stream is captured by a "Scribe" agent
    Then it must be written to disk immediately as "Glass" (Markdown/JSONL)
    And no schema validation shall be applied (Zero Crystallization)
    And the fidelity of the raw stream is preserved 100%
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Quench Phase - Capture raw NATS magma to amorphous Obsidian Core
import json
from nats.aio.client import Client as NATS
import asyncio
from datetime import datetime

async def osc_quench(nats: NATS, subject: str, scribe_file: str = "obsidian_cores.jsonl"):
    """Quench high-viscosity NATS stream into faithful, schema-free storage."""
    async for msg in nats.subscribe(subject):
        timestamp = datetime.now().isoformat()
        glass = {
            "timestamp": timestamp,
            "source": subject,
            "raw_magma": msg.data.decode('utf-8')  # 100% fidelity, no validation
        }
        async with asyncio.open_connection('127.0.0.1', 8080) as reader, writer:  # Disk scribe simulation
            writer.write(json.dumps(glass) + '\n')
            await writer.drain()
        print(f"Quenched: {glass['timestamp']}")
```

## ⚔️ Synergies
*   **Eruption**: Integrates with NATS streams for raw "Magma" intake (High-Viscosity Flow).
*   **Knap**: Feeds "Obsidian Cores" (JSONL/MD files) to Assimilator agents for vector flake extraction.
*   **Haft/Hydrate**: Vector flakes and cores link into Knowledge Graphs; backlink rinds prioritize retrieval.
*   **Devitrify**: Neglected cores (zero rind) trigger archival to prevent context rot.
*   **Hive Fleet Obsidian**: Canonical physics underpinning Scribe, Assimilator, and retrieval agents.