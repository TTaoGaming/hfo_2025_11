#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 8abf813d-8612-46c9-8fc4-8e249af66048
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.305909+00:00'
  topos:
    address: venom/clean_smart.py
    links: []
  telos:
    viral_factor: 0.0
    meme: clean_smart.py

🦅 Hive Fleet Obsidian: Smart Cleanup
Usage: python venom/clean_smart.py

- Archives episodic memory.
- Removes pycache.
- Removes temporary files.
"""

import shutil
from datetime import datetime
from pathlib import Path


def clean_smart():
    print("🧹 Initiating Smart Cleanup...")

    # 1. Archive Episodic Memory
    episodic_dir = Path("memory/episodic")
    archive_root = Path("memory/archive")
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_dir = archive_root / f"episodic_{timestamp}"

    if episodic_dir.exists():
        files = list(episodic_dir.glob("*.md"))
        if files:
            print(f"📦 Archiving {len(files)} episodic artifacts to {archive_dir}...")
            archive_dir.mkdir(parents=True, exist_ok=True)
            for f in files:
                shutil.move(str(f), str(archive_dir / f.name))
        else:
            print("ℹ️  No episodic artifacts to archive.")

    # 2. Remove __pycache__
    print("🔥 Burning __pycache__...")
    for p in Path(".").rglob("__pycache__"):
        if p.is_dir():
            shutil.rmtree(p)

    # 3. Remove .pytest_cache
    for p in Path(".").rglob(".pytest_cache"):
        if p.is_dir():
            shutil.rmtree(p)

    print("✨ Smart Cleanup Complete.")


if __name__ == "__main__":
    clean_smart()
