"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 3bb358ae-4600-4b6d-86fe-11d21f06b3e5
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.579370+00:00'
  topos:
    address: eyes/tools/inventory_scanner.py
    links: []
  telos:
    viral_factor: 0.0
    meme: inventory_scanner.py
"""

import os
import sys
import psycopg2
from psycopg2.extras import execute_values
from tqdm import tqdm

# Add HiveFleetObsidian to path
sys.path.append(os.path.join(os.getcwd(), "HiveFleetObsidian"))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)

# Configuration
IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "env",
    ".vscode",
    ".idea",
    "dist",
    "build",
    "coverage",
    "site-packages",
    "miniconda3",
    "go",
    "bin",
    "pkg",  # Added system/language dirs to ignore
}
IGNORE_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".pyd",
    ".so",
    ".dll",
    ".class",
    ".exe",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".ico",
    ".svg",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".deb",
    ".rpm",
    ".apk",
    ".iso",
    ".img",
    ".bin",
    ".lock",
    ".log",
    ".jsonl",
    ".map",
    ".wav",
    ".mp3",
    ".mp4",
    ".webm",
    ".ogg",
    ".flac",
    ".aac",
    ".wma",
    ".m4a",
    ".ttf",
    ".woff",
    ".woff2",
    ".eot",
}


def get_db_connection():
    config = get_config()
    return psycopg2.connect(config.database.url)


def main():
    print("Starting Inventory Scan...")
    conn = get_db_connection()
    conn.autocommit = True
    cur = conn.cursor()

    root_dir = os.getcwd()
    files_to_queue = []

    print("Scanning filesystem...")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filter directories in place
        dirnames[:] = [
            d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")
        ]

        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in IGNORE_EXTENSIONS:
                continue

            full_path = os.path.join(dirpath, f)
            files_to_queue.append((full_path,))

    print(f"Found {len(files_to_queue)} potential files.")

    print("Populating queue (ignoring duplicates)...")

    # Insert in batches using ON CONFLICT DO NOTHING
    batch_size = 1000
    total_inserted = 0

    for i in tqdm(range(0, len(files_to_queue), batch_size)):
        batch = files_to_queue[i : i + batch_size]
        execute_values(
            cur,
            """
            INSERT INTO ingestion_queue (file_path)
            VALUES %s
            ON CONFLICT (file_path) DO NOTHING
        """,
            batch,
        )
        total_inserted += len(
            batch
        )  # Approximation, actual count might be lower due to conflicts

    print("Inventory complete. Queue is populated.")
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
