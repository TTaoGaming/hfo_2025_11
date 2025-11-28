"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: aaebd93c-31fb-430d-862b-b849ef5855bd
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.309266+00:00'
    generation: 51
  topos:
    address: venom/smart_cleanup.py
    links: []
  telos:
    viral_factor: 0.0
    meme: smart_cleanup.py
"""

#!/usr/bin/env python3
import shutil
from pathlib import Path


def smart_cleanup():
    root_dir = Path(".")
    logs_dir = root_dir / "audit_trail" / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    # 1. Move Log Files
    print("🧹 Scanning for stray log files...")
    for log_file in root_dir.glob("*.log"):
        if log_file.is_file():
            dest = logs_dir / log_file.name
            print(f"   -> Moving {log_file.name} to {logs_dir}")
            shutil.move(str(log_file), str(dest))

    # 2. Check for Empty Artifacts
    print("🧹 Scanning for empty artifacts in memory/episodic...")
    episodic_dir = root_dir / "memory" / "episodic"
    if episodic_dir.exists():
        for artifact in episodic_dir.rglob("*.md"):
            if artifact.is_file() and artifact.stat().st_size == 0:
                print(f"   -> 🗑️ Deleting empty artifact: {artifact}")
                artifact.unlink()

    # 3. Clean __pycache__ (Optional, usually handled by gitignore but good for local)
    # print("🧹 Cleaning __pycache__...")
    # for pycache in root_dir.rglob("__pycache__"):
    #     shutil.rmtree(pycache)

    print("✨ Smart Cleanup Complete!")


if __name__ == "__main__":
    smart_cleanup()
