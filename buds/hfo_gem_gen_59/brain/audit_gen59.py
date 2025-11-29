import sqlite3
import lancedb
import os
import sys
import json

# Add root to path
sys.path.append(os.getcwd())

def audit_sqlite():
    print("\n--- Auditing SQLite (IronLedger) ---")
    db_path = "buds/hfo_gem_gen_59/memory/hfo_gen_59_memory.db"
    if not os.path.exists(db_path):
        print(f"❌ DB not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get the latest Memory Item (AGENTS.md)
    # Check vectorized status
    cursor.execute("SELECT id, source_path, content_hash, vectorized FROM memory_items ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    if not row:
        print("No memory items found.")
        return
    
    mem_id, source_path, content_hash, vectorized = row
    print(f"Latest Ingestion: {source_path} (ID: {mem_id})")
    print(f"Vectorized Status: {vectorized} (Expected: 1)")

    # Check Level 0 Artifacts for this item
    # First, get table info to debug schema
    cursor.execute("PRAGMA table_info(level0_artifacts)")
    columns = [info[1] for info in cursor.fetchall()]
    print(f"L0 Columns: {columns}")

    cursor.execute("SELECT count(*) FROM level0_artifacts WHERE source_hash=?", (content_hash,))
    l0_count = cursor.fetchone()[0]
    print(f"Level 0 Artifacts: {l0_count} (Expected: 8)")
    
    # Fetch one artifact to inspect confidence
    cursor.execute("SELECT pillars_json FROM level0_artifacts WHERE source_hash=? LIMIT 1", (content_hash,))
    row = cursor.fetchone()
    if row:
        pillars = json.loads(row[0])
        print("\n--- L0 Confidence Audit ---")
        max_conf = 0
        for p_name, p_data in pillars.items():
            conf = p_data.get('confidence', 0)
            max_conf = max(max_conf, conf)
            if conf > 0.5:
                print(f"❌ VIOLATION: {p_name} confidence {conf} > 0.5")
            else:
                # print(f"✅ {p_name}: {conf}")
                pass
        print(f"Max L0 Confidence Observed: {max_conf}")
        if max_conf <= 0.5:
            print("✅ All L0 Confidence Scores Capped Correctly.")

    # Check Level 1 Artifacts
    cursor.execute("SELECT consensus_score, synthesis FROM level1_artifacts WHERE source_hash=?", (content_hash,))
    row = cursor.fetchone()
    if row:
        score, synthesis = row
        print(f"Level 1 Consensus Score: {score}")
        print(f"Level 1 Synthesis (Snippet): {synthesis[:200]}...")
        
        if score > 0.75:
             print("❌ VIOLATION: Consensus Score > 0.75")
        else:
             print("✅ Consensus Score Capped Correctly.")
    else:
        print("❌ No Level 1 Artifact found.")

    conn.close()

def audit_lancedb():
    print("\n--- Auditing LanceDB (VectorMirror) ---")
    db_path = "buds/hfo_gem_gen_59/memory/hfo_gen_59_lancedb"
    if not os.path.exists(db_path):
        print(f"❌ LanceDB not found at {db_path}")
        return

    try:
        db = lancedb.connect(db_path)
        if "hfo_vectors" not in db.table_names():
             print("❌ Table 'hfo_vectors' not found.")
             return
             
        tbl = db.open_table("hfo_vectors")
        print(f"Total Vectors: {len(tbl)}")
        
        # Search for the latest file
        df = tbl.to_pandas()
        print(f"Latest Vectors:\n{df[['source_path', 'category']].tail(5)}")
        
        # Check for AGENTS.md
        agents_row = df[df['source_path'].str.contains("AGENTS.md")]
        if not agents_row.empty:
            print(f"\n✅ Found AGENTS.md in LanceDB:\n{agents_row[['source_path', 'category']]}")
        else:
            print("\n❌ AGENTS.md NOT found in LanceDB.")
        
    except Exception as e:
        print(f"LanceDB Error: {e}")

if __name__ == "__main__":
    audit_sqlite()
    audit_lancedb()
