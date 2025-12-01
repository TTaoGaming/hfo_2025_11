import sys
import os
import logging

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_61.brain.assimilator import Assimilator

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("SafeAssimilate")

def safe_assimilate():
    logger.info("🚀 Starting Assimilation Cycle (Step 2)...")
    
    try:
        assimilator = Assimilator()
        # Run a cycle to process the newly added items
        # We added 5 items, so batch_size=10 covers it.
        assimilator.run_sync_cycle(batch_size=10)
        logger.info("✅ Assimilation Complete.")
    except Exception as e:
        logger.error(f"❌ Assimilation Failed: {e}")

if __name__ == "__main__":
    safe_assimilate()
