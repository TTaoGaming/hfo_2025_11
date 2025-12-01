import sys
import os
import logging
import sqlite3

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_61.memory.database import IronLedger

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BacklogCheck")

def check_backlog():
    db_path = "buds/hfo_gem_gen_61/memory/hfo_gen_61_memory.db"
    if not os.path.exists(db_path):
        logger.error(f"Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Count total items
    cursor.execute("SELECT COUNT(*) FROM memory_items")
    total = cursor.fetchone()[0]
    
    # Count unvectorized items
    cursor.execute("SELECT COUNT(*) FROM memory_items WHERE vectorized = 0")
    pending = cursor.fetchone()[0]
    
    logger.info(f"📊 Iron Ledger Status:")
    logger.info(f"   Total Memories: {total}")
    logger.info(f"   Pending Vectorization: {pending}")
    
    if pending > 0:
        logger.info("   ⚠️  Backlog detected. This explains the delay.")
        # Show top 5 pending
        cursor.execute("SELECT id, source_path, length(content) FROM memory_items WHERE vectorized = 0 LIMIT 5")
        rows = cursor.fetchall()
        for r in rows:
            logger.info(f"      - ID {r[0]}: {r[1]} ({r[2]} chars)")
    else:
        logger.info("   ✅ No backlog. System should be fast.")

    conn.close()

if __name__ == "__main__":
    check_backlog()
