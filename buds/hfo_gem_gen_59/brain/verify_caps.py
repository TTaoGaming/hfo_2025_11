import sqlite3
import json
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Verification")

DB_PATH = "buds/hfo_gem_gen_59/memory/hfo_gen_59_memory.db"

def verify_caps():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    logger.info(f"🔍 Verifying Caps in {DB_PATH}...")

    # Check Level 0
    cursor.execute("SELECT id, pillars_json FROM level0_artifacts")
    l0_rows = cursor.fetchall()
    l0_violations = 0
    
    for row_id, pillars_json in l0_rows:
        try:
            data = json.loads(pillars_json)
            for pillar_name, content in data.items():
                if isinstance(content, dict) and content.get("confidence", 0) > 0.5:
                    l0_violations += 1
                    logger.error(f"❌ L0 Violation ID {row_id} [{pillar_name}]: {content['confidence']}")
        except:
            pass

    # Check Level 1
    cursor.execute("SELECT id, consensus_score FROM level1_artifacts")
    l1_rows = cursor.fetchall()
    l1_violations = 0
    
    for row_id, score in l1_rows:
        if score > 0.750001: # Float tolerance
            l1_violations += 1
            logger.error(f"❌ L1 Violation ID {row_id}: {score}")

    conn.close()
    
    if l0_violations == 0 and l1_violations == 0:
        logger.info("✅ ALL CAPS VERIFIED. System is compliant.")
    else:
        logger.error(f"🛑 Found {l0_violations} L0 violations and {l1_violations} L1 violations.")

if __name__ == "__main__":
    verify_caps()
