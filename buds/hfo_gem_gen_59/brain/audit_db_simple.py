import sqlite3
import lancedb
import pandas as pd
from pathlib import Path

def audit_sqlite():
    print("\n--- 🧊 Cold Memory (SQLite) Audit ---")
    conn = sqlite3.connect("buds/hfo_gem_gen_59/memory/hfo_gen_59_memory.db")
    cursor = conn.cursor()
    
    # Check Level 0 Artifacts
    print("\n[Level 0 Artifacts (PREY Agents)]")
    cursor.execute("SELECT id, pillars_json FROM level0_artifacts")
    rows = cursor.fetchall()
    print(f"Count: {len(rows)}")
    
    import json
    for row in rows:
        pid = row[0]
        data = json.loads(row[1])
        # Check one pillar
        if "ontos" in data:
            conf = data["ontos"]["confidence"]
            if conf > 0.5:
                print(f"❌ ID {pid} Ontos Confidence: {conf}")
            else:
                # print(f"✅ ID {pid} Ontos Confidence: {conf}")
                pass

    # Check Level 1 Artifacts
    print("\n[Level 1 Artifacts (Synthesizer)]")
    cursor.execute("SELECT id, consensus_score FROM level1_artifacts")
    for row in cursor.fetchall():
        score = row[1]
        if score > 0.75:
            print(f"❌ ID {row[0]} Score: {score}")
        else:
            print(f"✅ ID {row[0]} Score: {score}")

    conn.close()

if __name__ == "__main__":
    audit_sqlite()
