try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    # Fallback if fastmcp is not available in the installed version
    FastMCP = None

from duckduckgo_search import DDGS
import json

# Initialize FastMCP if available
if FastMCP:
    mcp = FastMCP("Obsidian Search Scout")
else:
    class MockMCP:
        def tool(self):
            def decorator(func):
                return func
            return decorator
        def run(self):
            print("MCP Server Mock Run")
    mcp = MockMCP()

@mcp.tool()
def search_web(query: str, max_results: int = 5) -> str:
    """
    Search the external internet for real-time information (2025 Era).
    """
    print(f"🕷️ Scout searching for: {query}")
    try:
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
            if not results:
                return "No results found."
            
            formatted = "\n".join([
                f"--- Result {i+1} ---\nTitle: {r['title']}\nLink: {r['href']}\nSnippet: {r['body']}"
                for i, r in enumerate(results)
            ])
            return formatted
    except Exception as e:
        return f"Search failed: {str(e)}"

if __name__ == "__main__":
    mcp.run()
