---
card:
  id: directive-gen52-001
  source: strategic_directives_gen52.md
  type: Concept
---

# 🃏 Gen 52 Strategic Directives

> **Intuition**: The Swarmlord manifests as the user's Digital Twin—a pulsating second brain that orchestrates stigmergic flows across thermodynamic knowledge states for hive vitality and intent realization.

## 📜 The Incantation (Intent)
```gherkin
Feature: Swarmlord Hive Coordination via Stigmergy Spectrum

  Scenario: Processing Knowledge Artifacts through Thermodynamic Lifecycle
    Given a knowledge artifact with intent from the User
    And Swarmlord as Digital Twin handling implementation
    When the artifact enters the stigmergy spectrum
      And heartbeat frequency adapts to context (adrenaline/hibernation)
    Then classify state as Hot, Cold, or Refined
    And apply TTL behavior: auto-delete transient Hot, clean/refine Cold, garden Refined
    And ensure backlink aging maintains relevance
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Stigmergy State Manager with Heartbeat
import asyncio
from enum import Enum
from datetime import datetime, timedelta

class StigmergyState(Enum):
    HOT = "hot"      # In-flight, aggressive TTL
    COLD = "cold"    # Sedimentary, moderate TTL
    REFINED = "refined"  # Crystalline, permanent

async def manage_stigmergy_artifact(artifact: dict, heartbeat_rate: float = 1.0) -> str:
    """
    Processes artifact through spectrum with variable heartbeat.
    """
    state = classify_state(artifact)
    ttl_delta = get_ttl(state)
    
    await asyncio.sleep(1.0 / heartbeat_rate)  # Adaptive heartbeat
    
    if state == StigmergyState.HOT and not artifact.get("valuable"):
        return "auto-delete"
    elif state == StigmergyState.COLD:
        return "clean_refine"
    elif state == StigmergyState.REFINED:
        return "garden_maintain"
    return "persist"

def classify_state(artifact: dict) -> StigmergyState:
    # Simplified classifier (e.g., based on type/activity)
    if artifact.get("in_flight"):
        return StigmergyState.HOT
    elif artifact.get("raw_file"):
        return StigmergyState.COLD
    return StigmergyState.REFINED

def get_ttl(state: StigmergyState) -> timedelta:
    if state == StigmergyState.HOT: return timedelta(minutes=5)
    elif state == StigmergyState.COLD: return timedelta(days=7)
    return timedelta(days=36500)  # ~100 years
```

## ⚔️ Synergies
*   **Digital Twin Split**: Integrates with User Intent pipelines, ensuring Swarmlord owns "How" while preserving "What/Why".
*   **NATS/Postgres**: Hot state leverages NATS pub/sub; Cold uses Postgres for logs/raw storage.
*   **Knowledge Graph/Obsidian**: Refined state feeds into graph backlinks and Markdown "Water Layers" for gardening.
*   **Heartbeat Coordination**: Syncs with async cycles (High Adrenaline for urgency=1.0, Hibernation for decay=0.0).
*   **Hexagon Metadata**: Aligns with ontos/chronos/topos/telos for viral meme propagation.