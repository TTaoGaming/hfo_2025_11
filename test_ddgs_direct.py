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
