"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 5118a061-b09c-46f7-a28a-e6ec990b37fc
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.271608+00:00'
  topos:
    address: venom/ingest_gen50.py
    links: []
  telos:
    viral_factor: 0.0
    meme: ingest_gen50.py
"""

import asyncio
import logging
from pathlib import Path
from body.digestion.crystal_spinner import CrystalSpinner

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ingest_gen50")


class OfflineCrystalSpinner(CrystalSpinner):
    async def connect(self):
        logger.info("🔌 Offline Mode: Skipping NATS connection.")
        pass

    async def close(self):
        pass

    async def weave(self, original_path: Path, new_content: str, metadata):
        # Override to skip NATS signal but keep file writing
        # 1. Determine Destination
        dest_dir = Path(
            f"memory/semantic/library/{metadata.domain.lower().replace(' ', '_')}"
        )
        dest_dir.mkdir(parents=True, exist_ok=True)

        dest_file = dest_dir / original_path.name

        # 2. Write File
        with open(dest_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info(f"💎 Crystallized: {dest_file}")
        # Skip NATS signal


async def main():
    archive_dir = Path("memory/episodic/gen_50_archive")
    if not archive_dir.exists():
        logger.error(f"Archive directory not found: {archive_dir}")
        return

    spinner = OfflineCrystalSpinner()
    # No connect needed for offline

    files = list(archive_dir.glob("**/*.md")) + list(archive_dir.glob("**/*.feature"))
    logger.info(f"Found {len(files)} files to ingest.")

    for file_path in files:
        if file_path.is_dir():
            continue

        logger.info(f"Processing {file_path}...")
        try:
            content = file_path.read_text(encoding="utf-8")

            # 1. Spin
            metadata = await spinner.spin(content, file_path.name)

            # 2. Harden
            hardened_content = spinner.harden(content, metadata)

            # 3. Weave
            await spinner.weave(file_path, hardened_content, metadata)

        except Exception as e:
            logger.error(f"Failed to process {file_path}: {e}")


if __name__ == "__main__":
    asyncio.run(main())
