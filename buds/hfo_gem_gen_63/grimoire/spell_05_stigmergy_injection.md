---
card:
  id: spell-stigmergy-injection
  name: The Stigmergy Injection
  type: Sorcery (Maintenance)
  cost: 1 Script Execution
  tags: [stigmergy, headers, maintenance, greening]
---

# 💉 Spell 05: The Stigmergy Injection

> **Flavor Text**: *"The Spider marks every thread. Unmarked threads are not part of the Web; they are dust."* — Codex of the Obsidian Spider

## 🔮 The Intuition
The system requires **Total Stigmergy**. Every file (Holon) must carry a **YAML Header** defining its ID, Type, and Status.
This spell scans the entire Bud (`buds/hfo_gem_gen_63`) and injects a UUID-based header into any file that lacks one. It turns a "Red Board" (Violations) into a "Green Board" (Compliance).

---

## 📜 The Incantation (The Intent)
*Write this in `buds/hfo_gem_gen_63/features/stigmergy_injection.feature`.*

```gherkin
Feature: Stigmergy Header Injection

  Background:
    Given the "Evo-Devo Protocol" is active
    And the "Fitness Function" is failing due to missing headers

  Scenario: Greening the Board
    Given I have a list of 50+ files without headers
    When I cast "The Stigmergy Injection"
    Then every file should receive a unique "hfo-uuid" header
    And the "Fitness Check" should pass (or reduce violations)
```

---

## 🧪 The Catalyst (The Code)
*The Python logic (`buds/hfo_gem_gen_63/forge/inject_stigmergy.py`).*

```python
def inject_headers():
    """
    Walks the directory tree.
    If file is .md or .py and lacks a header:
      1. Generate a UUID.
      2. Infer type from path (brain=intent, src=implementation).
      3. Prepend the YAML block.
    """
    ...
```

## ⚔️ Combo Synergies
*   **With "The Guard"**: This spell is the *fix* for the Guard's *check*.
*   **With "The Oracle"**: Once injected, these files become indexable by the Bridger Oracle.
