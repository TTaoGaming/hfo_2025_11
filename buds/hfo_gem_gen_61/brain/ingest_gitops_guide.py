import sys
import os
import logging
from pathlib import Path

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_61.memory.database import IronLedger
from buds.hfo_gem_gen_61.blood.schema import MemoryItem
from buds.hfo_gem_gen_61.brain.assimilator import Assimilator

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("IngestGitOps")

def ingest_gitops_guide():
    # 1. Setup Paths
    brain_dir = Path("buds/hfo_gem_gen_61/brain")
    filename = "guide_gitops_philosophy.md"
    file_path = brain_dir / filename

    if not file_path.exists():
        logger.error(f"❌ File not found: {file_path}")
        return

    # 2. Connect to Iron Ledger
    ledger = IronLedger()
    logger.info("✅ Connected to Iron Ledger.")

    # 3. Ingest File
    try:
        logger.info(f"📖 Reading {filename}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Create Memory Item
        item = MemoryItem(
            source_path=str(file_path.absolute()),
            content=content,
            generation=61,
            category="guide",
            tags=["gitops", "philosophy", "guide", "gen61"]
        )
        item.compute_hash()

        # Insert into Ledger
        row_id = ledger.insert(item)
        logger.info(f"✅ Inserted {filename} (Row ID: {row_id})")
        
    except Exception as e:
        logger.error(f"❌ Failed to process {filename}: {e}")
        return

    # 4. Run Assimilator (Sync to Vector DB)
    logger.info("🚀 Starting Assimilation...")
    try:
        assimilator = Assimilator()
        assimilator.run_sync_cycle(batch_size=1)
        logger.info("✅ Assimilation Complete.")
    except Exception as e:
        logger.error(f"❌ Assimilation Failed: {e}")

if __name__ == "__main__":
    ingest_gitops_guide()
