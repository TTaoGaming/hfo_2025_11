---
card:
  id: spell-phoenix-genesis
  name: The Phoenix Genesis
  type: Sorcery
  cost: 1 Intent File (.feature)
  tags: [genesis, regeneration, cleanroom, tdd]
---

# 🔥 Spell 01: The Phoenix Genesis

> **Flavor Text**: *"Ash is not the end. It is the fertilizer."* — Codex of the Obsidian Spider

## 🔮 The Intuition
You do not "debug" a rotting limb. You cut it off and grow a new one.
This spell takes a **Pure Intent** (a Gherkin feature file) and summons a **Perfect Implementation**. If the implementation already exists but is buggy, it burns it down and rebuilds it.

---

## 📜 The Incantation (The Intent)
*Write this in a `.feature` file (e.g., `buds/hfo_gem_gen_63/features/my_component.feature`).*

```gherkin
Feature: The Phoenix Protocol (Component Generation)

  Background:
    Given the Swarmlord is active
    And the "0 Invention" policy is in effect

  Scenario: Regenerate a Holon
    Given I have a valid Intent file "my_component.feature"
    And the corresponding code "my_component.py" is "drifted" or "missing"
    When I cast "The Phoenix Genesis"
    Then the system should generate "my_component.py"
    And the code should strictly follow the Gherkin steps
    And the code should include "Hexagonal Stigmergy Headers"
```

---

## 🧪 The Catalyst (The Code)
*This is the Python logic that "Resolves" the spell. (See `genesis.py` in the root).*

```python
# The Essence of the Spell
def cast_phoenix_genesis(intent_path: str):
    """
    1. READ the Intent (Gherkin).
    2. CHECK if the Code exists.
    3. IF exists: BACKUP to 'ash_heap/'.
    4. GENERATE new Code using the LLM (Swarmlord).
    5. VERIFY the new Code against the Intent.
    """
    intent = read_file(intent_path)
    
    # The Prompt to the Swarm
    prompt = f"""
    You are the Swarmlord.
    The Warlock has cast Phoenix Genesis.
    
    INTENT:
    {intent}
    
    TASK:
    Write the Python implementation.
    - NO fluff.
    - NO extra features.
    - MUST pass the Gherkin tests.
    - MUST include Hexagonal Headers.
    """
    
    code = call_llm(prompt)
    write_file(target_path, code)
    return "The Phoenix has risen."
```

---

## ⚔️ Combo Synergies
*   **With "The Iron Ledger"**: The destruction and rebirth are logged forever in the blockchain/ledger.
*   **With "GitOps"**: The new code is automatically committed with the message `feat(phoenix): regenerated <component>`.
