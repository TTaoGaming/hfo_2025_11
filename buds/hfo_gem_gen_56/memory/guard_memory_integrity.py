"""
# ==================================================================
# 🛡️ HIVE GUARD: MEMORY INTEGRITY
# ==================================================================
# Purpose: Verify that the Memory System is REAL and not Theater.
# Checks: LanceDB, NetworkX, KCS Structure.
"""

import os

# Fix for OMP Error: Must be set before importing libraries that use OpenMP
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

import sys
import shutil
from pathlib import Path

# Add parent directory to path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory
from memory.graph_store import PortableGraphStore


def check_kcs_structure():
    print("\n🔍 Checking KCS Structure...")
    required_dirs = [
        "memory/kcs/0_draft",
        "memory/kcs/1_review",
        "memory/kcs/2_verified",
        "memory/docs-diataxis/tutorials",
        "memory/docs-diataxis/how-to-guides",
        "memory/docs-diataxis/reference",
        "memory/docs-diataxis/explanation",
    ]

    all_exist = True
    for d in required_dirs:
        path = Path(d)
        if path.exists():
            print(f"  ✅ Found: {d}")
        else:
            print(f"  ❌ MISSING: {d}")
            all_exist = False

    return all_exist


def check_lancedb():
    print("\n🔍 Checking LanceDB (Vector Store)...")
    try:
        # Use a test DB path to avoid polluting main memory
        test_db_path = "memory/lancedb_test"
        if os.path.exists(test_db_path):
            shutil.rmtree(test_db_path)

        mem = HFOStigmergyMemory(db_path=test_db_path)

        # Test Store
        payload = {"id": "guard-test-1", "msg": "This is a reality check."}
        mem.store("guard_check", payload)

        # Test Query
        results = mem.query(section="guard_check", query_text="reality check")

        if not results.empty:
            print(
                f"  ✅ LanceDB Store & Query Successful. Found: {len(results)} records."
            )
            # Cleanup
            shutil.rmtree(test_db_path)
            return True
        else:
            print("  ❌ LanceDB Query returned empty results.")
            return False

    except Exception as e:
        print(f"  ❌ LanceDB Failed: {e}")
        return False


def check_graph_store():
    print("\n🔍 Checking NetworkX (Graph Store)...")
    try:
        test_graph_path = "memory/semantic/guard_test_graph.json"
        if os.path.exists(test_graph_path):
            os.remove(test_graph_path)

        store = PortableGraphStore(storage_path=test_graph_path)

        # Test Add
        store.add_node("Guard", type="program")
        store.add_node("Memory", type="system")
        store.add_edge("Guard", "Memory", relation="protects")

        # Test Persistence
        store.save()

        # Test Reload
        store2 = PortableGraphStore(storage_path=test_graph_path)
        neighbors = store2.get_neighbors("Guard")

        if "Memory" in neighbors:
            print(
                f"  ✅ Graph Store Persistence Verified. 'Guard' protects {neighbors}."
            )
            # Cleanup
            os.remove(test_graph_path)
            return True
        else:
            print(f"  ❌ Graph Store Failed. Neighbors of Guard: {neighbors}")
            return False

    except Exception as e:
        print(f"  ❌ Graph Store Failed: {e}")
        return False


def main():
    print("🛡️ HIVE GUARD: INITIATING MEMORY SCAN")
    print("=======================================")

    kcs_ok = check_kcs_structure()
    lancedb_ok = check_lancedb()
    graph_ok = check_graph_store()

    print("\n=======================================")
    if kcs_ok and lancedb_ok and graph_ok:
        print("🟢 SYSTEM INTEGRITY VERIFIED: REALITY CONFIRMED.")
        sys.exit(0)
    else:
        print("🔴 SYSTEM INTEGRITY COMPROMISED: THEATER DETECTED.")
        sys.exit(1)


if __name__ == "__main__":
    main()
