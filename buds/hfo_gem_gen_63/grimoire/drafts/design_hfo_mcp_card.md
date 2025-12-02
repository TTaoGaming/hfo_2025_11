---
card:
  id: hfo_mcp
  source: design_hfo_mcp.md
  type: Concept
---

# 🃏 HFO Model Context Protocol (MCP)

> **Intuition**: MCP is the praxeological bridge decoupling the LLM 'Brain' from 'Hands', forging universal interoperability for agents across local stdio and remote SSE realms.

## 📜 The Incantation (Intent)
```gherkin
Feature: HFO-MCP Decouples Brain from Hands

  Scenario: PreyAgent Executes Remote Tool via MCP
    Given an MCP Server hosting Obsidian toolset is running over stdio or SSE
    When PreyAgent initializes an MCP Client adapter
    And the agent discovers available tools via "list_tools"
    And the agent invokes "call_tool" with tool name and parameters
    Then the server validates, executes the tool securely within sandbox
    And the result streams back to the agent without code coupling
```

## 🧪 The Catalyst (Code)
```python
# The Essence: MCP Client Adapter for PreyAgent
import asyncio
from mcp import ClientSession, StdioServerParameters  # mcp-python-sdk

class McpClient:
    def __init__(self, transport="stdio"):
        self.session = None
        self.transport = transport

    async def connect(self):
        params = StdioServerParameters() if self.transport == "stdio" else None
        self.session = ClientSession(...)  # SSE or stdio launch
        await self.session.initialize()

    async def list_tools(self):
        tools = await self.session.list_tools()
        return [{"name": t.name, "description": t.description} for t in tools]

    async def call_tool(self, name: str, arguments: dict):
        result = await self.session.call_tool(name, arguments)
        return result.content[0].text
```

## ⚔️ Synergies
*   **PreyAgent Integration**: Replaces hardcoded `tools.py` with `McpClient`, enabling Gen 52 decoupling.
*   **Obsidian Toolset**: Hosts `obsidian_fs`, `obsidian_net`, `obsidian_hive`, `obsidian_memory` for safe FS, web, stigmergy, and vector recall.
*   **Hexagonal Fractal Holarchy**: Aligns with Pillar 1 (decoupling) and Pillar 8 (protocol-first praxeology).
*   **Hybrid Stability**: Supports Dockerized agents accessing host tools via SSE (Phase 2).
*   **Structural Pillars**: Links to `structural_pillars.md` for holarchic governance; drives `hfo_mcp.feature` behavior specs.
*   **Scalability Path**: Paves for Phase 3 Universal Market with external MCP servers (e.g., GitHub, Slack).