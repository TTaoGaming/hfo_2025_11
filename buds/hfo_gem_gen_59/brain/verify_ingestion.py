import sqlite3
import json
import sys
from pathlib import Path

DB_PATH = "buds/hfo_gem_gen_59/memory/hfo_memory.db"

def verify_ingestion(target_file: str):
    if not Path(DB_PATH).exists():
        print(f"❌ Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print(f"🔍 Verifying Ingestion for: {target_file}\n")

    # 1. Check Memory Item
    cursor.execute("SELECT * FROM memory_items WHERE source_path = ?", (target_file,))
    memory = cursor.fetchone()
    
    if not memory:
        print("❌ Memory Item NOT found in DB.")
        return
    
    print(f"✅ Memory Item Found (ID: {memory['id']})")
    print(f"   - Hash: {memory['content_hash'][:8]}...")
    print(f"   - Gen: {memory['generation']}")

    target_hash = memory['content_hash']

    # 2. Check Level 0
    cursor.execute("SELECT * FROM level0_artifacts WHERE source_hash = ?", (target_hash,))
    l0_artifacts = cursor.fetchall()
    print(f"✅ Level 0 Artifacts: {len(l0_artifacts)}/8")
    
    if len(l0_artifacts) != 8:
        print("   ⚠️  Warning: Not all agents reported.")

    # 3. Check Level 1
    cursor.execute("SELECT * FROM level1_artifacts WHERE source_hash = ?", (target_hash,))
    l1_artifact = cursor.fetchone()
    
    if l1_artifact:
        print(f"✅ Level 1 Artifact Found (ID: {l1_artifact['id']})")
        print(f"   - Consensus Score: {l1_artifact['consensus_score']}")
        print(f"   - Synthesis: {l1_artifact['synthesis'][:100]}...")
    else:
        print("❌ Level 1 Artifact NOT found (Quorum Failed).")

    conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python verify_ingestion.py <file_path>")
        sys.exit(1)
    verify_ingestion(sys.argv[1])
