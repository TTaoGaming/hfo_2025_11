"""
# ==================================================================
# 📜 REPO MANIFEST INGESTION (WALKER)
# ==================================================================
# Purpose: Walk the ENTIRE repository and ingest into LanceDB.
#          Caps confidence at 0.8.
#          Filters out noise (git, venv, etc).
"""

import os
import sys
import time
import re
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path
REPO_ROOT = Path(__file__).resolve().parents[3]
GEN55_ROOT = REPO_ROOT / "buds/hfo_gem_gen_55"
sys.path.append(str(GEN55_ROOT))

from memory.lancedb_store import HFOStigmergyMemory

# Configuration
DB_PATH = GEN55_ROOT / "memory/lancedb"
IGNORE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    ".ruff_cache",
    ".mypy_cache",
    ".pytest_cache",
    "lancedb",
    "lancedb_test_vectors",
    ".devcontainer",
    ".vscode",
    "site-packages",
    "dist",
    "build",
}
IGNORE_EXTENSIONS = {
    ".pyc",
    ".o",
    ".so",
    ".dll",
    ".class",
    ".exe",
    ".bin",
    ".lance",
    ".manifest",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".ico",
    ".svg",
    ".woff",
    ".woff2",
    ".ttf",
    ".eot",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".rar",
    ".pdf",
    ".sqlite",
    ".db",
}
MAX_FILE_SIZE_MB = 2.0


def extract_generation_from_path(path_str):
    match = re.search(r"gen_(\d+)", path_str, re.IGNORECASE)
    if match:
        return int(match.group(1))
    if "hfo_gem_gen_55" in path_str:
        return 55
    return "unknown"


def get_file_type(file_path):
    ext = file_path.suffix.lower()
    if ext in {".md", ".txt", ".rst"}:
        return "documentation"
    if ext in {".py", ".js", ".ts", ".html", ".css", ".sh", ".json", ".yaml", ".yml"}:
        return "code"
    return "other"


def ingest_repo():
    print("📜 Starting Full Repo Manifest Ingestion...")
    print(f"   Root: {REPO_ROOT}")
    print(f"   DB: {DB_PATH}")

    mem = HFOStigmergyMemory(db_path=str(DB_PATH))

    count = 0
    skipped = 0
    errors = 0

    start_time = time.time()

    for root, dirs, files in os.walk(REPO_ROOT):
        # Modify dirs in-place to skip ignored
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        # Also skip if we are INSIDE an ignored dir
        rel_root = Path(root).relative_to(REPO_ROOT)
        if any(part in IGNORE_DIRS for part in rel_root.parts):
            continue

        for file in files:
            file_path = Path(root) / file

            # Skip ignored extensions
            if file_path.suffix.lower() in IGNORE_EXTENSIONS:
                skipped += 1
                continue

            # Skip huge files
            try:
                if file_path.stat().st_size > MAX_FILE_SIZE_MB * 1024 * 1024:
                    skipped += 1
                    continue
            except OSError:
                skipped += 1
                continue

            try:
                # Read content
                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore")
                except Exception:
                    skipped += 1
                    continue

                if not content.strip():
                    skipped += 1
                    continue

                # Determine Section
                try:
                    rel_path = file_path.relative_to(REPO_ROOT)
                    section = rel_path.parts[0] if rel_path.parts else "root"
                except:
                    section = "unknown"

                generation = extract_generation_from_path(str(rel_path))

                payload = {
                    "id": str(rel_path),
                    "filename": file,
                    "path": str(file_path),
                    "type": get_file_type(file_path),
                    "content": content,
                    "confidence_score": 0.8,  # Cap at 80%
                    "verification_status": "unverified_manifest",
                    "ingestion_source": "manifest_ingest",
                    "generation": generation,
                }

                # Store
                mem.store(section, payload, privilege_level=0)
                count += 1

                if count % 100 == 0:
                    elapsed = time.time() - start_time
                    rate = count / elapsed if elapsed > 0 else 0
                    print(
                        f"   ... Ingested {count} files ({rate:.1f} files/sec). Last: {file}"
                    )

            except Exception as e:
                print(f"   ❌ Error ingesting {file}: {e}")
                errors += 1

    print("\n✅ Manifest Ingestion Complete.")
    print(f"   Total Ingested: {count}")
    print(f"   Skipped: {skipped}")
    print(f"   Errors: {errors}")


if __name__ == "__main__":
    ingest_repo()
