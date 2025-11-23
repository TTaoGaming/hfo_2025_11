"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: b64af6ee-94d4-4b4f-97e5-37242599195f
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.445529+00:00'
    generation: 51
  topos:
    address: body/digestion/query_gen43.py
    links: []
  telos:
    viral_factor: 0.0
    meme: query_gen43.py
"""

import json
from pathlib import Path
from typing import List

# 🔍 GEN 43 QUERIER
# Role: Librarian
# Mission: Search the Gen 43 Vector Store for keywords.

VECTOR_STORE_PATH = Path("memory/semantic/gen43_vector_store.ndjson")


def search_store(keywords: List[str], limit: int = 5):
    print(f"🔍 Searching for {keywords} in {VECTOR_STORE_PATH}...")

    if not VECTOR_STORE_PATH.exists():
        print(f"❌ Vector Store not found: {VECTOR_STORE_PATH}")
        return

    results = []

    with open(VECTOR_STORE_PATH, "r", encoding="utf-8") as f:
        for line in f:
            try:
                item = json.loads(line)
                content = item.get("content", "").lower()

                # Simple AND search
                if all(k.lower() in content for k in keywords):
                    results.append(item)
            except Exception:
                pass

    print(f"✅ Found {len(results)} matches.")

    # Sort by length or some other metric? Let's just take the first few.
    for i, res in enumerate(results[:limit]):
        print(f"\n--- Result {i+1} ---")
        print(f"Source: {res.get('source_id')}")
        print(f"Content: {res.get('content')[:500]}...")


if __name__ == "__main__":
    print("--- Query 1: 'Hive Fleet Obsidian' AND 'definition' ---")
    search_store(["Hive Fleet Obsidian", "definition"])

    print("\n--- Query 2: 'Cognitive Symbiote' ---")
    search_store(["Cognitive Symbiote"])

    print("\n--- Query 3: 'Evolution' AND 'Gen' ---")
    search_store(["Evolution", "Gen"])
