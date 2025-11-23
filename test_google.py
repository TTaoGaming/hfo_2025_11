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
