import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from memory.lancedb_store import HFOStigmergyMemory


def test_vector_hello_world():
    print("=== Testing HFO Vector Memory (Hello World) ===")

    # 1. Initialize Memory (loads model)
    print("\n[1] Initializing Memory (Loading all-MiniLM-L6-v2)...")
    mem = HFOStigmergyMemory(db_path="memory/lancedb_test_vectors")

    # 2. Store Concepts
    print("\n[2] Storing Concepts...")
    concepts = [
        ("ontos", {"id": "apple", "text": "A red fruit that grows on trees."}),
        ("ontos", {"id": "tesla", "text": "An electric car made by Elon Musk."}),
        ("ontos", {"id": "dog", "text": "A loyal pet that barks."}),
        ("ontos", {"id": "cat", "text": "A feline pet that meows."}),
    ]

    for section, payload in concepts:
        mem.store(section, payload)

    # 3. Semantic Query
    print("\n[3] Running Semantic Query: 'vehicle'...")
    results = mem.query(query_text="vehicle", limit=1)

    print("\n--- Results ---")
    print(results[["id", "payload", "_distance"]])

    # Verification
    top_result = results.iloc[0]["payload"]
    if "car" in top_result.lower():
        print("\n✅ SUCCESS: 'vehicle' matched with 'car'.")
    else:
        print(f"\n❌ FAILURE: Expected 'car', got {top_result}")

    # 4. Semantic Query 2
    print("\n[4] Running Semantic Query: 'animal'...")
    results = mem.query(query_text="animal", limit=2)
    print("\n--- Results ---")
    print(results[["id", "payload", "_distance"]])

    # Verification
    top_result = results.iloc[0]["payload"]
    if "pet" in top_result.lower():
        print("\n✅ SUCCESS: 'animal' matched with 'pet'.")
    else:
        print(f"\n❌ FAILURE: Expected 'pet', got {top_result}")


if __name__ == "__main__":
    test_vector_hello_world()
