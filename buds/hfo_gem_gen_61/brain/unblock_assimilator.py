import sys
import os
import logging
import sqlite3

# Add root to path
sys.path.append(os.getcwd())

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("UnblockAssimilator")

def unblock_assimilator():
    db_path = "buds/hfo_gem_gen_61/memory/hfo_gen_61_memory.db"
    if not os.path.exists(db_path):
        logger.error(f"Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # 1. Check the backlog
    cursor.execute("SELECT COUNT(*) FROM memory_items WHERE vectorized = 0 AND generation < 61")
    legacy_backlog = cursor.fetchone()[0]
    
    logger.info(f"⚠️ Found {legacy_backlog} legacy items (Gen < 61) pending vectorization.")
    
    if legacy_backlog > 0:
        logger.info("🚀 Marking legacy items as 'vectorized' (skipped) to unblock Gen 61...")
        
        # Mark them as vectorized so the Assimilator ignores them for now
        cursor.execute("UPDATE memory_items SET vectorized = 1 WHERE vectorized = 0 AND generation < 61")
        conn.commit()
        
        logger.info(f"✅ Successfully skipped {legacy_backlog} items.")
    else:
        logger.info("✅ No legacy backlog found.")

    # 2. Verify Gen 61 items are still pending
    cursor.execute("SELECT COUNT(*) FROM memory_items WHERE vectorized = 0 AND generation = 61")
    gen61_pending = cursor.fetchone()[0]
    logger.info(f"ℹ️  Gen 61 Items Pending: {gen61_pending}")
    
    conn.close()

if __name__ == "__main__":
    unblock_assimilator()
