import asyncio
import os
import sys
import logging

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.blood.schema import MemoryItem
from buds.hfo_gem_gen_60.brain.prey_swarm import PreySwarm

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IngestNotes")


async def ingest_file(file_path: str, swarm: PreySwarm):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        item = MemoryItem(
            source_path=file_path,
            content=content,
            content_hash="manual_hash_" + os.path.basename(file_path),
            timestamp="2025-11-29T00:00:00Z",
            generation=60,
            category="user_notes",
        )

        logger.info(f"🍽️  Ingesting: {file_path}")
        await swarm.process_item(item)
        logger.info(f"✅ Ingested: {file_path}")

    except Exception as e:
        logger.error(f"❌ Failed to ingest {file_path}: {e}")


async def main():
    swarm = PreySwarm()
    # Ingest the specific notes file
    await ingest_file("buds/hfo_gem_gen_60/obsidian-spider-notes-2025-11.md", swarm)


if __name__ == "__main__":
    asyncio.run(main())
