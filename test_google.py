"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: dbb6c1bb-3d17-4502-9a92-ea8638cd2380
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:20:43.131338+00:00'
  topos:
    address: test_google.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_google.py
"""

from googlesearch import search

try:
    print("Testing Google Search...")
    results = list(search("stigmergy in nature", num_results=3, advanced=True))
    if results:
        print(f"Success! Found {len(results)} results.")
        for r in results:
            print(f"Title: {r.title}")
            print(f"URL: {r.url}")
            print(f"Description: {r.description}")
            print("-" * 20)
    else:
        print("No results found.")
except Exception as e:
    print(f"Error: {e}")
