import sys
import os
import logging
from pathlib import Path

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_61.memory.database import IronLedger
from buds.hfo_gem_gen_61.blood.schema import MemoryItem

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("SafeIngest")

def safe_ingest():
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
    try:
        ledger = IronLedger()
        logger.info("✅ Connected to Iron Ledger.")
    except Exception as e:
        logger.error(f"❌ Failed to connect to Iron Ledger: {e}")
        return

    # 3. Ingest Files
    success_count = 0
    for filename in files_to_ingest:
        file_path = brain_dir / filename
        if not file_path.exists():
            logger.warning(f"⚠️ File not found: {file_path}")
            continue

        try:
            logger.info(f"📖 Reading {filename}...")
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
            row_id = ledger.insert(item)
            logger.info(f"✅ Inserted {filename} (Row ID: {row_id})")
            success_count += 1
            
        except Exception as e:
            logger.error(f"❌ Failed to process {filename}: {e}")

    logger.info(f"🎉 Ingestion Complete. {success_count}/{len(files_to_ingest)} files saved to Iron Ledger.")
    logger.info("ℹ️  NOTE: These items are now in the Database but NOT yet in the Vector Store (Oracle).")
    logger.info("ℹ️  Run the Assimilator separately when Ollama is ready.")

if __name__ == "__main__":
    safe_ingest()
