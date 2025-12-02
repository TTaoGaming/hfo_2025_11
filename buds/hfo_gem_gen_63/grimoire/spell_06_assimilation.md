---
card:
  id: spell-assimilation
  name: The Assimilation (Memory Ingest)
  type: Sorcery (ETL)
  cost: 1 Script Execution
  tags: [memory, sqlite, lancedb, networkx, etl]
---

# 🧠 Spell 06: The Assimilation

> **Flavor Text**: *"The Spider eats the fly, and the fly becomes the Spider. We eat the data, and the data becomes the Mind."* — Codex of the Obsidian Spider

## 🔮 The Intuition
This spell performs the **Unified Ingestion** you requested.
It walks the Stigmergic Web (files with headers), extracts the essence (Metadata + Content), and crystallizes it into the **Three Mirrors**:
1.  **The Iron Ledger (SQLite)**: For structured queries and logs.
2.  **The Semantic Lake (LanceDB)**: For fuzzy search and intuition.
3.  **The Neural Web (NetworkX)**: For graph traversal and connection finding.

---

## 📜 The Incantation (The Intent)
*Write this in `buds/hfo_gem_gen_63/features/assimilation.feature`.*

```gherkin
Feature: Unified Memory Assimilation

  Background:
    Given the "Stigmergy Injection" has been cast
    And the "Holon Headers" are present

  Scenario: Building the Mirrors
    When I cast "The Assimilation"
    Then the "Iron Ledger" should contain all Holons
    And the "Semantic Lake" should contain all Vectors
    And the "Neural Web" should contain all Nodes
```

## 🧪 The Catalyst (The Code)
*The Python logic (`buds/hfo_gem_gen_63/forge/assimilate_memory.py`).*

```python
def assimilate():
    """
    1. Init DBs.
    2. Walk Files.
    3. Parse Holons.
    4. Insert into SQLite, LanceDB, NetworkX.
    """
    ...
```
