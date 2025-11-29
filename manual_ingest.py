import asyncio
import os
import sys
import logging

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.blood.schema import MemoryItem  # noqa: E402
from buds.hfo_gem_gen_60.brain.prey_swarm import PreySwarm  # noqa: E402

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ManualIngest")


async def ingest_file(file_path: str, swarm: PreySwarm):
    try:
        with open(file_path, "r") as f:
            content = f.read()

        item = MemoryItem(
            source_path=file_path,
            content=content,
            content_hash="manual_hash",  # Swarm will re-hash
            timestamp="2025-11-29T00:00:00Z",
            generation=60,
            category="core_design",
        )

        logger.info(f"🍽️  Ingesting: {file_path}")
        await swarm.process_item(item)
        logger.info(f"✅ Ingested: {file_path}")

    except Exception as e:
        logger.error(f"❌ Failed to ingest {file_path}: {e}")


async def main():
    swarm = PreySwarm()

    files = [
        "buds/hfo_gem_gen_60/brain/manifesto_obsidian_spider.md",
        "buds/hfo_gem_gen_60/brain/design_obsidian_hourglass_algorithm.md",
    ]

    for f in files:
        await ingest_file(f, swarm)


if __name__ == "__main__":
    asyncio.run(main())
