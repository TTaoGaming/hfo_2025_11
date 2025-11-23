"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: daa4cf1f-8be1-46bc-8881-90ec4a62aec4
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.313718+00:00'
  topos:
    address: venom/test_search_fix.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_search_fix.py
"""

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
