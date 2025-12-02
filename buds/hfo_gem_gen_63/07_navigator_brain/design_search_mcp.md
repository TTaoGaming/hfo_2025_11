---
holon:
  id: hfo-gen63-design-search-mcp
  type: design
  status: draft
  author: Swarmlord
  intent_id: obsidian-stack-v1
  context: Search MCP Tool (2025 Era)
---

# 🕷️ Design: Search MCP Server (The Web Crawler)

> **Context**: The Swarmlord requires real-time access to the 2025 Internet.
> **Problem**: The current Bridger is limited to internal memory. The Agent's internal knowledge is dated (pre-2025).
> **Solution**: Build a **Search MCP Server** that exposes a "Search Tool" to the Hive.

## 1. The Metaphor: The Scout
*   **Role**: **Observer** (Ontos).
*   **Action**: Ventures outside the Hive to gather fresh nectar (Information).
*   **Protocol**: MCP (Model Context Protocol).

## 2. The Architecture: MCP Server
We will wrap a Search API (e.g., Brave Search, Google, or a mock for simulation) in an MCP Server.

### Interface
```json
{
  "name": "search-oracle",
  "tools": [
    {
      "name": "search_web",
      "description": "Search the external internet for real-time information (2025 Era).",
      "inputSchema": {
        "type": "object",
        "properties": {
          "query": { "type": "string", "description": "The search query." },
          "num_results": { "type": "integer", "default": 5 }
        },
        "required": ["query"]
      }
    }
  ]
}
```

### Tech Stack
*   **Runtime**: Python 3.11+
*   **Protocol**: `mcp` (Python SDK)
*   **Provider**: **Brave Search API** (Privacy-focused, robust) or **DuckDuckGo** (No API key needed for basic scraping).
*   **Fallback**: If no API key is present, use a simulated "2025 Mock" that returns plausible future data for testing.

## 3. Implementation Plan
1.  **Scaffold**: Create `src/servers/search_mcp.py`.
2.  **Implement**: Use `duckduckgo-search` (Python lib) for immediate, keyless access.
3.  **Expose**: Register the tool via MCP.
4.  **Test**: Verify the agent can "know" what time it is.

## 4. Integration
*   **Registry**: Add `search-oracle` to the `forge` organ.
*   **Swarm**: The `Navigator` and `Bridger` will have access to this tool.

