"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 085c3ab7-a9b7-4ba6-9273-cd1c700f6c4f
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:20:43.132500+00:00'
    generation: 51
  topos:
    address: test_ddgs_direct.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_ddgs_direct.py
"""

try:
    from ddgs import DDGS
    import json

    print("Testing DDGS (New Package)...")
    with DDGS() as ddgs:
        results = list(ddgs.text("stigmergy", max_results=3))
        if results:
            print(f"Success! Found {len(results)} results.")
            print(json.dumps(results[0], indent=2))
        else:
            print("No results found.")
except ImportError:
    print("Could not import ddgs directly.")
except Exception as e:
    print(f"Error: {e}")
