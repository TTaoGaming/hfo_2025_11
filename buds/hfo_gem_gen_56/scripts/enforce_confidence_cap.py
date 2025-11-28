import sys
import os
import json
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path
REPO_ROOT = Path(__file__).resolve().parents[3]
GEN55_ROOT = REPO_ROOT / "buds/hfo_gem_gen_55"
sys.path.append(str(GEN55_ROOT))

from memory.lancedb_store import HFOStigmergyMemory


def enforce_cap():
    print("🛡️ Enforcing 80% Confidence Cap on LanceDB...")
    db_path = GEN55_ROOT / "memory/lancedb"
    mem = HFOStigmergyMemory(db_path=str(db_path))

    # 1. Get all data
    df = mem.table.to_pandas()
    print(f"   Total Records: {len(df)}")

    updates = 0

    # 2. Iterate and Check
    for index, row in df.iterrows():
        try:
            payload_str = row["payload"]
            payload = json.loads(payload_str)

            current_conf = payload.get("confidence_score", 0.0)

            if current_conf > 0.8:
                # Cap it
                payload["confidence_score"] = 0.8
                new_payload_str = json.dumps(payload)

                # Update DB
                # Using update with where clause on ID
                record_id = row["id"]

                # Escape single quotes in ID for SQL query if necessary,
                # but LanceDB update usually takes a SQL-like filter.
                # IDs are paths, might contain chars that need escaping.
                # Safer to use parameter binding if available, but lancedb python might not support it fully in update string.
                # For now, assuming IDs are safe paths.

                safe_id = record_id.replace("'", "''")

                mem.table.update(
                    where=f"id = '{safe_id}'", values={"payload": new_payload_str}
                )
                updates += 1

                if updates % 100 == 0:
                    print(f"   ... Capped {updates} records.")

        except Exception as e:
            print(f"   ⚠️ Error processing row {index}: {e}")

    print("✅ Enforcement Complete.")
    print(f"   Records Updated: {updates}")


if __name__ == "__main__":
    enforce_cap()
