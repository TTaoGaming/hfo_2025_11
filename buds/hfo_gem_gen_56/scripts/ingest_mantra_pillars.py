"""
# ==================================================================
# 🧠 MEMORY INGESTION: MANTRA & PILLARS
# ==================================================================
# Purpose: Ingest the Core Identity (Mantra) and Metaphysics (Pillars)
# into the Gen 55 LanceDB Memory.
"""

import os
import sys
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory


def ingest_core_concepts():
    print("🧠 Ingesting Core Concepts into LanceDB...")
    mem = HFOStigmergyMemory(db_path="memory/lancedb")

    # 1. The Mantra
    mantra_path = Path("brain/design_hfo_mantra.md")
    if mantra_path.exists():
        content = mantra_path.read_text()
        payload = {
            "id": "design_hfo_mantra",
            "title": "The HFO Mantra",
            "type": "identity",
            "content": content,
            "tags": ["mantra", "identity", "poetry"],
        }
        mem.store("ontos", payload, privilege_level=0)
        print("  ✅ Ingested Mantra.")
    else:
        print(f"  ❌ Mantra file not found: {mantra_path}")

    # 2. The Pillars (Metaphysical Octets)
    pillars_path = Path("brain/design_metaphysical_octets.md")
    if pillars_path.exists():
        content = pillars_path.read_text()
        payload = {
            "id": "design_metaphysical_octets",
            "title": "Metaphysical Octets",
            "type": "metaphysics",
            "content": content,
            "tags": ["pillars", "metaphysics", "ontology"],
        }
        mem.store("logos", payload, privilege_level=0)
        print("  ✅ Ingested Pillars.")
    else:
        print(f"  ❌ Pillars file not found: {pillars_path}")

    # Verify
    print("\n🔍 Verifying Ingestion...")
    results = mem.query(query_text="Obsidian Hourglass")
    if not results.empty:
        print(
            f"  ✅ Verification Successful. Found {len(results)} records related to 'Obsidian Hourglass'."
        )
    else:
        print("  ❌ Verification Failed. No records found.")


if __name__ == "__main__":
    ingest_core_concepts()
