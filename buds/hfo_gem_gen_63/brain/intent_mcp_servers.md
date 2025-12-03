---
octagon:
  ontos:
    id: intent-mcp-servers
    type: intent
    owner: Swarmlord
  logos:
    protocol: OBSIDIAN-STACK
    format: literate-gherkin
  techne:
    stack:
    - mcp
    - fastmcp
    - python
  chronos:
    status: active
    urgency: 1.0
    generation: 63
  pathos:
    stress_level: 0.0
    validation: pending
  ethos:
    security_level: internal
    compliance:
    - hfo-standard-gen63
  topos:
    address: buds/hfo_gem_gen_63/brain/intent_mcp_servers.md
  telos:
    viral_factor: 1.0
    meme: The Hands of the Hive.
---

# 🕷️ Intent: MCP Servers (The Interface)

> **Context**: Gen 63 (The Hydra Platform)
> **Goal**: To expose the Hive's capabilities (Memory, Search, Tools) as **MCP Servers**, standardizing how the Brain (LLM) interacts with the Body.

## 📜 Declarative Intent (Gherkin)

```gherkin
Feature: MCP Server Infrastructure
  As the Swarmlord
  I want to expose my tools via the Model Context Protocol
  So that any LLM (Claude, Cursor, etc.) can discover and use them without custom glue code.

  Rule: The Bridger MUST be an MCP Server
    Given the file `buds/hfo_gem_gen_63/01_bridger_nerves/servers/bridger_mcp.py`
    Then it must use `FastMCP`
    And it must expose tools:
      | Tool | Description |
      | emit_pheromone(subject, payload) | Publish to NATS |
      | listen_pheromone(subject) | Subscribe to NATS (Stream) |

  Rule: The Assimilator MUST be an MCP Server
    Given the file `buds/hfo_gem_gen_63/06_assimilator_memory/servers/memory_mcp.py`
    Then it must expose tools:
      | Tool | Description |
      | recall(query) | Search LanceDB |
      | remember(text, metadata) | Save to LanceDB |

  Rule: The Immunizer MUST Guard the MCP
    Given the file `buds/hfo_gem_gen_63/05_immunizer_carapace/guard_mcp.py`
    Then it must scan for "Rogue Tools" (tools not exposed via MCP)
    And warn if an Agent tries to bypass the MCP interface.
```
