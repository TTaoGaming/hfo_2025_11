import os
import sys
import shutil
import logging
import time

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_59.memory.database import IronLedger
from buds.hfo_gem_gen_59.brain.assimilator import Assimilator

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("PhoenixProtocol")

def execute_phoenix_protocol():
    """
    Executes the Phoenix Protocol:
    1. Wipes the VectorDB (LanceDB).
    2. Resets the IronLedger (SQLite) 'vectorized' flags.
    3. Re-assimilates all memories.
    """
    logger.info("🔥 INITIATING PHOENIX PROTOCOL 🔥")
    logger.info("The Old World must burn to make way for the New.")

    # Paths
    lancedb_path = "buds/hfo_gem_gen_59/memory/hfo_gen_59_lancedb"
    
    # 1. Wipe VectorDB
    if os.path.exists(lancedb_path):
        logger.warning(f"🗑️  Deleting VectorDB at: {lancedb_path}")
        shutil.rmtree(lancedb_path)
    else:
        logger.info("VectorDB not found (Clean Slate).")

    # 2. Reset IronLedger
    ledger = IronLedger()
    count = ledger.reset_vectorized_flags()
    logger.info(f"🔄 Reset {count} memories in IronLedger.")

    # 3. Re-Assimilate
    logger.info("🚀 Starting Re-Assimilation...")
    assimilator = Assimilator(lancedb_path=lancedb_path)
    
    start_time = time.time()
    processed_batches = 0
    
    while True:
        # Check if there's work to do
        remaining = ledger.get_unvectorized_items(limit=1)
        if not remaining:
            break
            
        assimilator.run_sync_cycle(batch_size=50)
        processed_batches += 1
        
        if processed_batches % 10 == 0:
            logger.info(f"Still burning... Batch {processed_batches} complete.")

    duration = time.time() - start_time
    logger.info(f"✨ Phoenix Protocol Complete in {duration:.2f}s.")
    logger.info("The VectorDB has been reborn from the IronLedger.")

if __name__ == "__main__":
    execute_phoenix_protocol()
