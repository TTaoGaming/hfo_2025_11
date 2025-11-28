import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory


def verify_manifesto():
    print("=== Verifying HFO Manifesto Ingestion ===")

    mem = HFOStigmergyMemory(db_path="memory/lancedb")

    # 1. Search for "Karmic Knife"
    print("\n[1] Searching for 'Karmic Knife'...")
    results = mem.query(query_text="Karmic Knife", limit=3)

    for idx, row in results.iterrows():
        print(f"\n--- Result {idx+1} (Distance: {row['_distance']:.4f}) ---")
        print(f"ID: {row['id']}")
        print(f"Text: {row['payload'][:200]}...")  # Truncate for display


if __name__ == "__main__":
    verify_manifesto()
