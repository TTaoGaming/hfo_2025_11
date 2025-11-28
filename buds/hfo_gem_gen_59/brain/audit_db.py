import sqlite3
import json
import sys
from pathlib import Path

DB_PATH = "buds/hfo_gem_gen_59/memory/hfo_memory.db"

def audit_db():
    if not Path(DB_PATH).exists():
        print(f"❌ Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print(f"🔍 Auditing IronLedger at {DB_PATH}...\n")

    # 1. Check Memory Items (Lossless Archive)
    cursor.execute("SELECT * FROM memory_items")
    memories = cursor.fetchall()
    print(f"📚 Memory Items (Lossless Archive): {len(memories)}")
    for mem in memories:
        print(f"   - {mem['source_path']} (Hash: {mem['content_hash'][:8]}...)")

    # Find the manifesto hash
    manifesto_mem = next((m for m in memories if "manifesto" in m['source_path']), None)
    
    if not manifesto_mem:
        print("   ❌ Manifesto not found in memory!")
        return

    target_hash = manifesto_mem['content_hash']
    print(f"\n🎯 Auditing Target: {manifesto_mem['source_path']}")

    # 2. Check Level 0 Artifacts
    cursor.execute("SELECT * FROM level0_artifacts WHERE source_hash = ?", (target_hash,))
    l0_artifacts = cursor.fetchall()
    print(f"\n🐜 Level 0 Artifacts (Agents): {len(l0_artifacts)} (Expected: 8)")
    
    l0_valid = True
    for art in l0_artifacts:
        pillars = json.loads(art['pillars_json'])
        max_conf = 0.0
        # Check confidence of each pillar
        for pillar_name in ['ontos', 'logos', 'telos', 'chronos', 'pathos', 'ethos', 'topos', 'nomos']:
            if pillar_name in pillars:
                conf = pillars[pillar_name]['confidence']
                max_conf = max(max_conf, conf)
                if conf > 0.5:
                    print(f"   ❌ Agent {art['agent_id']} ({art['model_used']}) violated confidence cap! {pillar_name}: {conf}")
                    l0_valid = False
        
        print(f"   - Agent {art['agent_id']} ({art['model_used']}): Max Confidence = {max_conf}")

    if len(l0_artifacts) == 8 and l0_valid:
        print("   ✅ All 8 Agents present and strictly capped at 0.5 confidence.")
    else:
        print("   ❌ Level 0 Audit Failed.")

    # 3. Check Level 1 Artifacts
    cursor.execute("SELECT * FROM level1_artifacts WHERE source_hash = ?", (target_hash,))
    l1_artifacts = cursor.fetchall()
    print(f"\n🦅 Level 1 Artifacts (Quorum): {len(l1_artifacts)} (Expected: 1)")

    l1_valid = True
    for art in l1_artifacts:
        score = art['consensus_score']
        print(f"   - Consensus Score: {score}")
        if score > 0.75:
             print(f"   ❌ Consensus Score violated Byzantine Cap! Score: {score}")
             l1_valid = False
    
    if len(l1_artifacts) == 1 and l1_valid:
        print("   ✅ Quorum reached and strictly capped at 0.75 consensus.")
    else:
        print("   ❌ Level 1 Audit Failed.")

    conn.close()

if __name__ == "__main__":
    audit_db()
