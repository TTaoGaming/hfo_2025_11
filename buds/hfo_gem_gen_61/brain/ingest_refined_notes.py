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
logger = logging.getLogger("IngestRefinedNotes")

def ingest_notes():
    # 1. Setup Paths
    brain_dir = Path("buds/hfo_gem_gen_61/brain")
    files_to_ingest = [
        "refined_brain_dump_architecture_critique_2025_11_30.md",
        "refined_brain_dump_temporal_langgraph_2025_11_30.md",
        "refined_brain_dump_sota_orchestration_2025_11_30.md",
        "refined_brain_dump_obsidian_spider_abstract_2025_11_30.md",
        "refined_brain_dump_warlock_patron_architecture_2025_11_30.md"
    ]

    # 2. Connect to Iron Ledger
    ledger = IronLedger()
    logger.info("Connected to Iron Ledger.")

    # 3. Ingest Files
    for filename in files_to_ingest:
        file_path = brain_dir / filename
        if not file_path.exists():
            logger.error(f"File not found: {file_path}")
            continue

        logger.info(f"Reading {filename}...")
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Create Memory Item
        item = MemoryItem(
            source_path=str(file_path.absolute()),
            content=content,
            generation=61,
            category="refined_brain_dump",
            tags=["brain_dump", "architecture", "gen61", "refined"]
        )
        item.compute_hash()

        # Insert into Ledger
        try:
            row_id = ledger.insert(item)
            logger.info(f"Inserted {filename} into Iron Ledger (Row ID: {row_id})")
        except Exception as e:
            logger.error(f"Failed to insert {filename}: {e}")

    # 4. Run Assimilator (Sync to Vector DB)
    logger.info("Starting Assimilation Cycle...")
    assimilator = Assimilator()
    assimilator.run_sync_cycle(batch_size=10)
    logger.info("Assimilation Complete.")

if __name__ == "__main__":
    ingest_notes()
