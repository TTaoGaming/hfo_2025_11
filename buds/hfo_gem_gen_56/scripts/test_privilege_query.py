import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory


def test_privilege_query():
    print("Initializing HFO Memory for Query Test...")
    memory = HFOStigmergyMemory(db_path="memory/lancedb")

    print("\n--- Query 1: Search for 'Obsidian' (Expected: Lvl 8) ---")
    results_8 = memory.query(query_text="Obsidian", limit=5)
    if not results_8.empty:
        print(results_8[["section", "privilege_level"]])
    else:
        print("No results found.")

    print("\n--- Query 2: Search for 'Heartbeat' (Expected: Lvl 0) ---")
    results_0 = memory.query(query_text="heartbeat", limit=5)
    if not results_0.empty:
        print(results_0[["section", "privilege_level"]])
    else:
        print("No results found.")

    print("\n--- Query 3: Search for 'System' (Mixed Levels?) ---")
    results_mixed = memory.query(query_text="system", limit=5)
    if not results_mixed.empty:
        print(results_mixed[["section", "privilege_level"]])
    else:
        print("No results found.")


if __name__ == "__main__":
    test_privilege_query()
