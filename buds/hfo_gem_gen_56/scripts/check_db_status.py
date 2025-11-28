"""
# ==================================================================
# 📊 CHECK DB STATUS
# ==================================================================
# Purpose: Check the size and content of the LanceDB memory bank.
"""

import os
import sys
import json
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path
REPO_ROOT = Path(__file__).resolve().parents[3]
GEN55_ROOT = REPO_ROOT / "buds/hfo_gem_gen_55"
sys.path.append(str(GEN55_ROOT))

from memory.lancedb_store import HFOStigmergyMemory


def check_status():
    print("📊 Checking LanceDB Status...")
    db_path = GEN55_ROOT / "memory/lancedb"
    mem = HFOStigmergyMemory(db_path=str(db_path))

    # Get total count
    # LanceDB table object has a count method or we can len() the to_arrow() result
    try:
        df_all = mem.table.to_pandas()
        count = len(df_all)
        print(f"✅ Total Items in DB: {count}")

        # --- Breakdown by Type ---
        print("\n📊 Content Breakdown by Type:")
        # We need to parse the payload JSON to get the type
        # This might be slow for 7k items but acceptable for a check script
        types = []
        generations = []

        for _, row in df_all.iterrows():
            try:
                p = json.loads(row["payload"])
                types.append(p.get("type", "unknown"))
                generations.append(str(p.get("generation", "unknown")))
            except:
                pass

        from collections import Counter

        type_counts = Counter(types)
        for t, c in type_counts.most_common():
            print(f"   - {t}: {c} ({c/count*100:.1f}%)")

        # --- Breakdown by Generation ---
        print("\n⏳ Content Breakdown by Generation (Top 10):")
        gen_counts = Counter(generations)
        for g, c in gen_counts.most_common(10):
            print(f"   - Gen {g}: {c}")

    except Exception as e:
        print(f"⚠️ Could not analyze distribution: {e}")
        count = "Unknown"

    # --- Essence Query ---
    print(
        "\n🔮 Querying the Essence (Semantic Search: 'Hive Fleet Obsidian Core Philosophy')..."
    )

    df = mem.query(
        query_text="Hive Fleet Obsidian Core Philosophy Swarmlord Purpose", limit=5
    )
    results = df.to_dict("records")

    for i, r in enumerate(results):
        try:
            payload = json.loads(r["payload"])
            print(f"\n[{i+1}] {payload.get('filename', 'Unknown')}")
            print(f"    Path: {payload.get('id')}")
            print(f"    Excerpt: {payload.get('content', '')[:200]}...")
        except:
            pass


if __name__ == "__main__":
    check_status()
