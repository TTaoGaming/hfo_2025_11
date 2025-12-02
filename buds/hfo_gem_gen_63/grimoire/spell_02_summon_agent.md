---
card:
  id: spell-summon-agent
  name: Summon Agent (Octree Node)
  type: Creature (Summon)
  cost: 1 Intent File (.feature) + 1 Role Assignment
  tags: [agent, octree, jadc2, swarm]
---

# 🕷️ Spell 02: Summon Agent

> **Flavor Text**: *"The Spider does not weave the web alone. It births the weavers."* — Codex of the Obsidian Spider

## 🔮 The Intuition
You are a **Summoner**. You do not "write a class". You **Summon an Entity** to inhabit a specific node in the Fractal Octree.
This spell brings a new Agent into existence, assigns it a Role (0-7), and binds it to the NATS bus.

---

## 📜 The Incantation (The Intent)
*Write this in a `.feature` file (e.g., `buds/hfo_gem_gen_63/features/summon_navigator.feature`).*

```gherkin
Feature: Summon the Navigator (Agent 07)

  Background:
    Given the Octree is active
    And the "JADC2" protocol is in effect

  Scenario: Summoning Ritual
    Given I need a decision-making entity
    When I cast "Summon Agent" with:
      | Role | 07_navigator_brain |
      | Type | Telos (Decide)     |
      | Bus  | hfo.gen63.brain.>  |
    Then the Agent should be instantiated
    And it should subscribe to "hfo.gen63.brain.>"
    And it should possess the "Planner" capability
    And it should log "I am the Navigator" to the Iron Ledger
```

---

## 🧪 The Catalyst (The Code)
*The Python logic that binds the spirit to the shell.*

```python
# The Essence of the Spell
def cast_summon_agent(role_id: str, capabilities: list):
    """
    1. VALIDATE the Role ID (Must be 00-07).
    2. INFLATE the 'PreyAgent' base class.
    3. INJECT the specific capabilities (Tools).
    4. BIND to the NATS subject.
    5. AWAKEN the loop.
    """
    from body.hexagonal_holon import HexagonalHolon
    from body.pattern_async_swarm import PreyAgent

    # The Shell
    agent = PreyAgent(
        holon_id=f"hfo-agent-{role_id}",
        role=role_id,
        capabilities=capabilities
    )

    # The Awakening
    agent.connect_to_stigmergy()
    agent.announce_presence()
    
    return agent
```

---

## ⚔️ Combo Synergies
*   **With "The Heartbeat"**: The summoned agent immediately syncs its pulse with the Swarm.
*   **With "Map Elites"**: If you summon multiple variants, they compete for survival based on fitness.
