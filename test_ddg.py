"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 1e28e130-5bb3-47b2-81eb-e348d02e22d0
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:20:43.129525+00:00'
  topos:
    address: test_ddg.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_ddg.py
"""

from duckduckgo_search import DDGS
import json

try:
    print("Testing DuckDuckGo Search (Default)...")
    with DDGS() as ddgs:
        results = list(ddgs.text("stigmergy", max_results=3))
        if results:
            print(f"Success! Found {len(results)} results.")
            print(json.dumps(results[0], indent=2))
        else:
            print("No results found (Default).")

    print("\nTesting DuckDuckGo Search (HTML)...")
    with DDGS() as ddgs:
        results = list(ddgs.text("stigmergy", max_results=3, backend="html"))
        if results:
            print(f"Success! Found {len(results)} results.")
            print(json.dumps(results[0], indent=2))
        else:
            print("No results found (HTML).")

    print("\nTesting DuckDuckGo Search (Lite)...")
    with DDGS() as ddgs:
        results = list(ddgs.text("stigmergy", max_results=3, backend="lite"))
        if results:
            print(f"Success! Found {len(results)} results.")
            print(json.dumps(results[0], indent=2))
        else:
            print("No results found (Lite).")

except Exception as e:
    print(f"Error: {e}")
