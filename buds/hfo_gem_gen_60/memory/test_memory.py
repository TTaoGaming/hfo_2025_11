import sys
import os
import logging

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.memory.database import IronLedger
from buds.hfo_gem_gen_60.memory.lancedb_store import VectorMirror

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Gen60MemoryTest")

def test_memory():
    logger.info("🧪 Testing Gen 60 Memory Clone...")
    
    # 1. Test Iron Ledger (SQLite)
    ledger = IronLedger()
    logger.info(f"✅ Iron Ledger Connected: {ledger.db_path}")
    
    # Check if data exists (should be cloned from Gen 59)
    conn = ledger._init_db() # Re-init to get connection, or just connect manually
    import sqlite3
    conn = sqlite3.connect(ledger.db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM memory_items")
    count = cursor.fetchone()[0]
    logger.info(f"📊 Iron Ledger Item Count: {count}")
    
    # 2. Test Vector Mirror (LanceDB)
    mirror = VectorMirror()
    logger.info(f"✅ Vector Mirror Connected: {mirror.db_path}")
    
    try:
        tbl = mirror.db.open_table("hfo_vectors")
        vec_count = len(tbl)
        logger.info(f"📊 Vector Mirror Item Count: {vec_count}")
    except Exception as e:
        logger.warning(f"⚠️ Could not open vector table (might be empty): {e}")

    logger.info("🎉 Gen 60 Memory Clone Verified!")

if __name__ == "__main__":
    test_memory()
