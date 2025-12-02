---
card:
  id: spell-mass-refraction
  name: The Mass Refraction (Grok Pulse)
  type: Sorcery (Ritual)
  cost: High Compute (Free Tier) + Time
  tags: [swarm, refraction, migration, grok, async]
---

# 🌊 Spell 03: The Mass Refraction

> **Flavor Text**: *"The Ocean of Memory is vast. We do not drink it with a cup; we channel it through a thousand streams."* — Codex of the Obsidian Spider

## 🔮 The Intuition
You have a massive "Unified Memory" (Legacy Code, Notes, Vectors). You want to convert it all into **Grimoire Cards** (SOTA Composition).
You cannot do this manually. You summon a **Refractor Swarm**—hundreds of small, async agents that pick up a piece of memory, transmute it into a Card, and deposit it in the Grimoire.
You utilize "Free Energy" (Grok/Free Tier LLMs) to power this massive background metabolism.

---

## 📜 The Incantation (The Intent)
*Write this in `buds/hfo_gem_gen_63/features/mass_refraction.feature`.*

```gherkin
Feature: Mass Refraction Swarm

  Background:
    Given the "Grok" model is available via API
    And the "Unified Memory" is accessible

  Scenario: The 24/7 Pulse
    Given I have a list of 1000+ raw memory items
    When I cast "The Mass Refraction"
    Then the system should spawn 100 concurrent "Refractor Agents"
    And each agent should:
      1. Read a memory item
      2. Extract the "SOTA Pattern"
      3. Generate a "Grimoire Card" (Gherkin + Code)
      4. Save it to "buds/hfo_gem_gen_63/grimoire/drafts/"
    And the system should run continuously until the memory is consumed
```

---

## 🧪 The Catalyst (The Code)
*The Python logic (`buds/hfo_gem_gen_63/forge/refractor_swarm.py`).*

```python
import asyncio
from hfo_sdk import llm, memory

async def refractor_drone(memory_chunk):
    """
    The worker bee. Takes raw text, makes a Card.
    """
    # 1. The Prompt (Optimized for Grok/Context)
    prompt = f"""
    You are a SOTA Architect.
    Analyze this memory: {memory_chunk}
    
    Create a 'Grimoire Card' for it.
    Format:
    - YAML Header
    - Intuition (Flavor)
    - Gherkin (Intent)
    - Python (Implementation)
    """
    
    # 2. The Call (Async)
    card_content = await llm.generate(prompt, model="grok-beta")
    
    # 3. The Deposit
    save_card(card_content)

async def cast_mass_refraction():
    """
    The Swarm Controller.
    """
    memories = memory.get_all_unprocessed()
    
    # The Pulse: Batches of 100
    for batch in chunk(memories, 100):
        await asyncio.gather(*[refractor_drone(m) for m in batch])
        print("Pulse Complete. Breathing...")
        await asyncio.sleep(1) # Rate limit protection
```

---

## ⚔️ Combo Synergies
*   **With "The Iron Ledger"**: Every generated card is logged.
*   **With "The Heartbeat"**: The refraction runs in the "diastole" (rest phase) of the system heartbeat.
