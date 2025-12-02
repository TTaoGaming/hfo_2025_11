---
card:
  id: tool-bridger-oracle
  name: The Bridger Oracle (MCP)
  type: Artifact (Server)
  cost: 1 Running Process
  tags: [mcp, memory, sqlite, lancedb, oracle]
---

# 🔮 Spell 04: The Bridger Oracle

> **Flavor Text**: *"The Spider has many eyes, but only one memory. The Oracle speaks for the Web."* — Codex of the Obsidian Spider

## 🔮 The Intuition
The **Bridger Oracle** is the voice of the system's memory. It is an **MCP Server** that wraps the raw databases (SQLite "Iron Ledger" and LanceDB "Semantic Lake") into a clean, tool-callable interface.
When an Agent needs to "remember" something, it does not touch the disk; it asks the Oracle.

---

## 📜 The Incantation (The Intent)
*Write this in `buds/hfo_gem_gen_63/features/bridger_oracle.feature`.*

```gherkin
Feature: The Bridger Oracle (Memory Access)

  Background:
    Given the "Bridger Oracle" MCP server is running
    And the "Iron Ledger" (SQLite) is mounted
    And the "Semantic Lake" (LanceDB) is mounted

  Scenario: Recalling a Fact (SQL)
    Given I need to know the status of "Gen 63"
    When I ask the Oracle "SELECT status FROM generations WHERE id = 'gen-63'"
    Then the Oracle should return "Active"

  Scenario: Recalling a Concept (Vector)
    Given I need to understand "Stigmergy"
    When I ask the Oracle to search for "How does the spider communicate?"
    Then the Oracle should return relevant markdown snippets
```

---

## 🧪 The Catalyst (The Code)
*The Python logic (`buds/hfo_gem_gen_63/src/servers/bridger_oracle.py`).*

```python
@mcp.tool()
def query_iron_ledger(query: str):
    """Executes SQL against the immutable log."""
    ...

@mcp.tool()
def query_semantic_memory(text: str):
    """Searches the vector space for meaning."""
    ...
```

## ⚔️ Combo Synergies
*   **With "Summon Agent"**: Every summoned agent is automatically configured to use this MCP server.
*   **With "Mass Refraction"**: The Refractor Swarm feeds new cards *into* this memory.
