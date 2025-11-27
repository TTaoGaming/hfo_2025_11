"""
# ==================================================================
# 🧠 MASS INGESTION: GEN 55 BRAIN DUMP
# ==================================================================
# Purpose: Ingest ALL content from buds/hfo_gem_gen_55 into LanceDB.
# Strategy:
#   - Max Confidence: 0.8 (Acknowledging potential hallucination)
#   - Status: pending_quorum (Requires Byzantine Refinement)
#   - Recursive Walk: brain/, body/, memory/, etc.
"""

import os
import sys
import json
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory

ROOT_DIR = Path("buds/hfo_gem_gen_55")
# We want to ingest these extensions
VALID_EXTENSIONS = {".md", ".py", ".yaml", ".json", ".txt"}
# Skip these directories
SKIP_DIRS = {"__pycache__", ".git", "lancedb", "lancedb_test", "node_modules", "venv"}


def get_file_type(file_path):
    ext = file_path.suffix.lower()
    if ext == ".md":
        return "documentation"
    if ext == ".py":
        return "code"
    if ext in {".yaml", ".json"}:
        return "config"
    return "unknown"


def ingest_directory():
    print(f"🧠 Starting Mass Ingestion from {ROOT_DIR}...")
    mem = HFOStigmergyMemory(db_path="memory/lancedb")

    count = 0

    # Walk the directory tree
    for root, dirs, files in os.walk(ROOT_DIR):
        # Modify dirs in-place to skip unwanted directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for file in files:
            file_path = Path(root) / file

            if file_path.suffix.lower() not in VALID_EXTENSIONS:
                continue

            try:
                # Read content
                try:
                    content = file_path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    print(f"  ⚠️ Skipping binary/encoding issue: {file_path}")
                    continue

                # Determine Section (e.g., 'brain', 'body')
                # Relative path from ROOT_DIR
                try:
                    rel_path = file_path.relative_to(ROOT_DIR)
                    section = rel_path.parts[0] if rel_path.parts else "root"
                except ValueError:
                    # Fallback if running from weird CWD
                    section = "unknown"

                # Construct Payload
                payload = {
                    "id": str(rel_path),
                    "filename": file,
                    "path": str(file_path),
                    "type": get_file_type(file_path),
                    "content": content,
                    "confidence_score": 0.8,  # Max confidence for unverified ingestion
                    "verification_status": "pending_quorum",
                    "ingestion_source": "mass_ingest_script",
                }

                # Store in LanceDB
                # We use the top-level folder as the 'section' key for the DB (e.g., 'brain', 'body')
                mem.store(section, payload, privilege_level=0)
                count += 1

                if count % 10 == 0:
                    print(f"  ... Ingested {count} files (Last: {file})")

            except Exception as e:
                print(f"  ❌ Error ingesting {file_path}: {e}")

    print(f"\n✅ Mass Ingestion Complete. Total Files: {count}")

    # Verification Sample
    print("\n🔍 Verification Sample (Confidence Check)...")
    results = mem.query(limit=1)
    if not results.empty:
        sample = json.loads(results.iloc[0]["payload"])
        print(f"  📄 Sample ID: {sample.get('id')}")
        print(f"  📊 Confidence: {sample.get('confidence_score')}")
        print(f"  🛡️ Status: {sample.get('verification_status')}")


if __name__ == "__main__":
    # Ensure we are running from the right place relative to the script
    # The script assumes it's run from the workspace root or similar,
    # but ROOT_DIR is relative. Let's adjust if we are inside buds/hfo_gem_gen_55

    current_cwd = Path.cwd()
    if current_cwd.name == "hfo_gem_gen_55":
        ROOT_DIR = Path(".")

    ingest_directory()
