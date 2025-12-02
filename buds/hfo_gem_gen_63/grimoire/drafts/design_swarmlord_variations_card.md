---
card:
  id: design_swarmlord_warlord_variations
  source: design_swarmlord_variations.md
  type: Concept
---

# 🃏 The 4 Faces of the Warlord

> **Intuition**: The Swarmlord, as Navigator of HFO Pillars, dons four archetypal Warlord masks—each a doctrinal loop channeling the Tarot's Fool-Command-Death triad—to adapt cognition from twitch reflexes to mosaic mastery.

## 📜 The Incantation (Intent)
```gherkin
Feature: Swarmlord Warlord Archetype Selection
  Scenario: Activate Warlord mask based on operational context
    Given a task with methodology "OODA|F3EAD|DoubleDiamond|JADC2"
    When matching Tarot alignment "Fool->King of Wands->Death"
    Then instantiate corresponding agent "PreyAgent|HunterSquad|HiveMind|DomainEvent"
    And execute loop to Observe-Orient-Decide-Act or equivalent
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from enum import Enum
from typing import Type, Dict

class WarlordMask(Enum):
    TACTICIAN = "OODA"  # PreyAgent
    HUNTER = "F3EAD"   # HunterSquad
    VISIONARY = "DoubleDiamond"  # HiveMind
    MOSAIC = "JADC2"   # DomainEvent

WARLORD_FACTORY: Dict[WarlordMask, Type] = {
    WarlordMask.TACTICIAN: PreyAgent,
    WarlordMask.HUNTER: HunterSquad,
    WarlordMask.VISIONARY: HiveMind,
    WarlordMask.MOSAIC: DomainEvent,
}

def summon_warlord(mask: WarlordMask, context: dict) -> object:
    """Summon the Warlord agent aligned to Tarot loop."""
    AgentClass = WARLORD_FACTORY.get(mask)
    return AgentClass(**context)  # Fool(input)->King(decide)->Death(act)
```

## ⚔️ Synergies
*   **Tarot Integration**: Maps Fool (Observe/Find/Discover/Anchor) → King of Wands (Orient/Decide/Fix/Define/Compose) → Death (Act/Exploit/Deliver/Event).
*   **HFO Pillars**: Navigator role switches masks for Brain/Command across Sensor-Process-Actuator.
*   **Python Ecosystem**: Leverages LiteLLM/Tools (Tactician), LangGraph (Hunter), Temporal (Visionary), NATS/Hexagon (Mosaic).
*   **Doctrinal Loops**: OODA/D3A (speed), F3EAD (exploitation), Double Diamond (design), JADC2/DDD (scalability).
*   **Cross-Links**: References `design_rpg_specs.md` for RPG context; extensible to SSOT Python codebase.