"""
# ==================================================================
# 📜 REPO MANIFEST GENERATOR
# ==================================================================
# Purpose: Scan the entire repository and generate a manifest of files
#          to be ingested into the HFO Memory Bank.
# Excludes: .git, venv, __pycache__, lancedb, node_modules, etc.
"""

import os
import json
from pathlib import Path

# Define Root
REPO_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = REPO_ROOT / "buds/hfo_gem_gen_55/memory/ingestion_manifest.json"

# Ignore Patterns
IGNORE_DIRS = {
    ".git",
    ".github",
    ".vscode",
    ".idea",
    "venv",
    "env",
    "__pycache__",
    "node_modules",
    "lancedb",
    "lancedb_test",
    "lancedb_store",  # Don't ingest the DB itself
    "site-packages",
    "dist",
    "build",
    "egg-info",
}

IGNORE_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".pyd",
    ".so",
    ".dll",
    ".exe",
    ".bin",
    ".iso",
    ".img",
    ".tar",
    ".gz",
    ".zip",
    ".7z",
    ".db",
    ".sqlite",
    ".lance",
    ".arrow",
    ".parquet",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ico",
    ".svg",  # Skip images for text ingestion
    ".pdf",
    ".docx",
    ".xlsx",  # Skip binary docs for now
}


def should_ignore(path):
    # Check directories in path
    for part in path.parts:
        if part in IGNORE_DIRS:
            return True

    # Check extension
    if path.suffix.lower() in IGNORE_EXTENSIONS:
        return True

    # Check specific filenames
    if path.name in {".DS_Store", "Thumbs.db"}:
        return True

    return False


def generate_manifest():
    print(f"🔍 Scanning Repository: {REPO_ROOT}")

    file_list = []
    total_size = 0

    for root, dirs, files in os.walk(REPO_ROOT):
        # Modify dirs in-place to skip ignored directories early
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            file_path = Path(root) / file
            rel_path = file_path.relative_to(REPO_ROOT)

            if should_ignore(rel_path):
                continue

            try:
                size = file_path.stat().st_size
                # Skip empty files or very large files (>10MB)
                if size == 0 or size > 10 * 1024 * 1024:
                    continue

                file_info = {
                    "path": str(rel_path),
                    "filename": file,
                    "extension": file_path.suffix.lower(),
                    "size": size,
                }
                file_list.append(file_info)
                total_size += size

            except Exception as e:
                print(f"⚠️ Error accessing {rel_path}: {e}")

    # Save Manifest
    manifest = {
        "root": str(REPO_ROOT),
        "total_files": len(file_list),
        "total_size_bytes": total_size,
        "files": file_list,
    }

    with open(MANIFEST_PATH, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"✅ Manifest Generated: {MANIFEST_PATH}")
    print(f"📊 Total Files: {len(file_list)}")
    print(f"💾 Total Size: {total_size / (1024*1024):.2f} MB")


if __name__ == "__main__":
    generate_manifest()
