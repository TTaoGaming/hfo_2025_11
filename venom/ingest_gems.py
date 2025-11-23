"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 80dc30d6-39d5-4e0d-a26f-a82d237b7cda
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.270570+00:00'
  topos:
    address: venom/ingest_gems.py
    links: []
  telos:
    viral_factor: 0.0
    meme: ingest_gems.py
"""

import os
import shutil
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("gem_ingestor")


def ingest_gems():
    """
    Ingests HFO Gems from eyes/archive/hfo_gem into memory/semantic/library.
    Adds Stigmergic Headers if missing.
    """
    logger.info("💎 Starting HFO Gem Ingestion Protocol...")

    source_root = Path("eyes/archive/hfo_gem")
    dest_root = Path("memory/semantic/library")
    dest_root.mkdir(parents=True, exist_ok=True)

    if not source_root.exists():
        logger.error(f"❌ Source not found: {source_root}")
        return

    count = 0

    for root, dirs, files in os.walk(source_root):
        for file in files:
            if file.endswith(".md"):
                src_file = Path(root) / file

                # Determine relative path to maintain structure
                rel_path = src_file.relative_to(source_root)
                dest_file = dest_root / rel_path

                # Create parent dirs
                dest_file.parent.mkdir(parents=True, exist_ok=True)

                # Read content
                try:
                    with open(src_file, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    logger.warning(f"   ⚠️  Could not read {src_file}: {e}")
                    continue

                # Check for header
                has_header = content.strip().startswith("---")

                if not has_header:
                    # Add default header
                    header = (
                        "---\n"
                        "type: knowledge_gem\n"
                        "domain: memory\n"
                        "owner: Swarmlord\n"
                        "status: active\n"
                        "source: hfo_archive\n"
                        "---\n\n"
                    )
                    new_content = header + content

                    with open(dest_file, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    logger.info(f"   ✨ Ingested & Tagged: {rel_path}")
                else:
                    # Just copy
                    shutil.copy2(src_file, dest_file)
                    logger.info(f"   📦 Ingested: {rel_path}")

                count += 1

    logger.info(f"\n✅ Ingestion Complete. Processed {count} gems into {dest_root}")


if __name__ == "__main__":
    ingest_gems()
