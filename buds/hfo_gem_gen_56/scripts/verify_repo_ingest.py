"""
# ==================================================================
# 🔍 VERIFY REPO INGESTION
# ==================================================================
# Purpose: Verify that the Repo Brain files were ingested correctly
#          with Generation and Timestamp metadata.
"""

import os
import sys
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path (to reach memory module)
REPO_ROOT = Path(__file__).resolve().parents[3]
GEN56_ROOT = REPO_ROOT / "buds/hfo_gem_gen_56"
sys.path.append(str(GEN55_ROOT))

from memory.lancedb_store import HFOStigmergyMemory

import json


def verify_ingestion():
    print("🔍 Verifying Repo Brain Ingestion...")
    db_path = GEN55_ROOT / "memory/lancedb"
    mem = HFOStigmergyMemory(db_path=str(db_path))

    # Query for repo brain items
    df = mem.query(query_text="Swarmlord", limit=50)

    # Convert DataFrame to list of dicts
    results = df.to_dict("records")

    repo_items = []
    for r in results:
        try:
            # Parse the payload JSON string
            payload = json.loads(r["payload"])
            if payload.get("ingestion_source") == "repo_brain_ingest":
                # Add the parsed payload to the result object for easier access
                r["parsed_payload"] = payload
                repo_items.append(r)
        except Exception:
            pass

    print(f"Found {len(repo_items)} items from 'repo_brain_ingest' in top 50 results.")

    if not repo_items:
        print(
            "⚠️ No repo items found in top results. Trying to fetch all and filter (might be slow)."
        )
        # Try a specific filename query
        df = mem.query(query_text="AGENTS.md", limit=5)
        results = df.to_dict("records")
        for r in results:
            try:
                payload = json.loads(r["payload"])
                if payload.get("filename") == "AGENTS.md":
                    r["parsed_payload"] = payload
                    repo_items.append(r)
            except:
                pass

    for item in repo_items[:5]:
        payload = item["parsed_payload"]
        print(f"\n📄 File: {payload.get('filename')}")
        print(f"   ID: {payload.get('id')}")
        print(f"   Generation: {payload.get('generation')}")
        print(f"   Timestamp: {payload.get('timestamp')}")
        print(f"   Source: {payload.get('ingestion_source')}")


if __name__ == "__main__":
    verify_ingestion()
