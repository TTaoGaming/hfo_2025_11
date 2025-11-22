import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from body.hands.tools import ToolSet  # noqa: E402


def test_search_fix():
    print("Testing search_brain with 'fractal holarchy'...")
    result = ToolSet.search_brain("fractal holarchy")
    print("\n--- Search Results ---")
    print(result)
    print("----------------------\n")

    if "Found in" in result and "..." in result:
        print("SUCCESS: Search returned context-aware snippets.")
    else:
        print("FAILURE: Search did not return expected format.")


if __name__ == "__main__":
    test_search_fix()
