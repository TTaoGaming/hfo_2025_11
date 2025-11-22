import logging
import numexpr
from ddgs import DDGS

"""
🦅 Hive Fleet Obsidian: External Tools
Intent: Provides external capabilities (Web Search, Math).
Linked to: brain/capability_external_tools.feature
"""

logger = logging.getLogger("external_tools")


class ExternalTools:
    """
    Tools for interacting with the outside world and performing calculations.
    """

    @staticmethod
    def search_web(query: str, max_results: int = 5) -> str:
        """
        Performs a real web search using DuckDuckGo.
        """
        try:
            results = []
            with DDGS() as ddgs:
                for r in ddgs.text(query, max_results=max_results):
                    results.append(
                        f"Title: {r['title']}\nURL: {r['href']}\nSnippet: {r['body']}\n"
                    )

            if not results:
                return f"No results found for '{query}'."

            return "\n---\n".join(results)
        except Exception as e:
            logger.error(f"Web search failed: {e}")
            return f"Error performing web search: {str(e)}"

    @staticmethod
    def calculator(expression: str) -> str:
        """
        Safely evaluates a mathematical expression.
        Supported operators: +, -, *, /, **, sin, cos, tan, log, etc.
        """
        try:
            # numexpr.evaluate returns a numpy array (0-d for scalars)
            result = numexpr.evaluate(expression)
            return str(result)
        except Exception as e:
            return f"Error calculating '{expression}': {str(e)}"


if __name__ == "__main__":
    # Smoke Test
    print("Testing Calculator:")
    print(ExternalTools.calculator("10 * 5 + 2"))

    print("\nTesting Web Search:")
    print(ExternalTools.search_web("Hive Fleet Obsidian AI"))
