import asyncio
import logging
import json
from typing import Any, Dict, List, Optional
from mcp.server.fastmcp import FastMCP
from duckduckgo_search import DDGS

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SearchOracle")

# Initialize FastMCP Server
mcp = FastMCP("search-oracle")

@mcp.tool()
async def search_web(query: str, num_results: int = 5) -> str:
    """
    Search the external internet for real-time information (2025 Era).
    
    Args:
        query: The search query string.
        num_results: Number of results to return (default: 5).
        
    Returns:
        A JSON string containing the search results.
    """
    logger.info(f"🔍 Searching Web: '{query}' (Limit: {num_results})")
    
    try:
        # Use DuckDuckGo Search (No API Key required)
        # Using the async context manager if available, or synchronous wrapper
        results = []
        with DDGS() as ddgs:
            # ddgs.text() returns a generator
            ddgs_gen = ddgs.text(query, max_results=num_results)
            for r in ddgs_gen:
                results.append(r)
        
        if not results:
            return json.dumps({"status": "no_results", "query": query})
            
        # Format results for the Hive
        formatted_results = {
            "status": "success",
            "source": "duckduckgo",
            "query": query,
            "results": results
        }
        
        return json.dumps(formatted_results, indent=2)

    except Exception as e:
        logger.error(f"❌ Search Failed: {e}")
        return json.dumps({"status": "error", "message": str(e)})

if __name__ == "__main__":
    # Run the MCP server
    print("🕷️ Search Oracle (MCP) Online. Listening on Stdio...")
    mcp.run()
