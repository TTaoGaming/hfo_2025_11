"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: d017a921-47ee-4945-a182-89eb1144c18f
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.268346+00:00'
    generation: 51
  topos:
    address: venom/sort_artifacts.py
    links: []
  telos:
    viral_factor: 0.0
    meme: sort_artifacts.py
"""

import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("artifact_sorter")


def sort_artifacts():
    logger.info("🧹 Starting Artifact Sort Protocol...")

    # Define source directories to check
    sources = ["/tmp/hfo_swarm", "/tmp/hfo_nats_test", "body/digestion"]

    # Define destination
    dest_root = Path("memory/episodic/sorted")
    dest_root.mkdir(parents=True, exist_ok=True)

    moved_count = 0

    for src in sources:
        src_path = Path(src)
        if not src_path.exists():
            logger.info(f"   ⚠️  Source not found: {src}")
            continue

        logger.info(f"   🔍 Scanning {src}...")

        # Walk through source
        for root, dirs, files in os.walk(src_path):
            for file in files:
                if file.endswith(".md"):
                    source_file = Path(root) / file

                    # Try to extract mission_id or agent role from filename or path
                    # Example path: /tmp/hfo_nats_test/Librarian_3/report.md
                    # Example filename: 2025-11-21T..._execution_Librarian_3.md

                    # Simple strategy: preserve relative structure if meaningful, or flatten
                    # Let's flatten but prepend parent folder name if it's an agent name

                    parent_name = Path(root).name
                    new_filename = file

                    if parent_name not in str(src_path):  # If it's a subdir
                        new_filename = f"{parent_name}_{file}"

                    dest_file = dest_root / new_filename

                    # Handle duplicates
                    counter = 1
                    while dest_file.exists():
                        dest_file = (
                            dest_root / f"{dest_file.stem}_{counter}{dest_file.suffix}"
                        )
                        counter += 1

                    shutil.move(str(source_file), str(dest_file))
                    logger.info(f"      📦 Moved: {file} -> {dest_file}")
                    moved_count += 1

    logger.info(f"\n✅ Artifact Sort Complete. Moved {moved_count} files to {dest_root}")


if __name__ == "__main__":
    sort_artifacts()
