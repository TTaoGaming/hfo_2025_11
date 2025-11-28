import sys
import os
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path
REPO_ROOT = Path(__file__).resolve().parents[3]
GEN55_ROOT = REPO_ROOT / "buds/hfo_gem_gen_55"
sys.path.append(str(GEN55_ROOT))

from memory.lancedb_store import HFOStigmergyMemory


def ingest_file(file_path_str):
    file_path = Path(file_path_str)
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        return

    print(f"📜 Ingesting Single File: {file_path.name}")

    db_path = GEN55_ROOT / "memory/lancedb"
    mem = HFOStigmergyMemory(db_path=str(db_path))

    content = file_path.read_text(encoding="utf-8")
    rel_path = file_path.relative_to(REPO_ROOT)

    # Determine Section (brain, body, etc)
    section = rel_path.parts[0] if rel_path.parts else "root"

    payload = {
        "id": str(rel_path),
        "filename": file_path.name,
        "path": str(file_path),
        "type": "design",  # Hardcoded for this specific task
        "content": content,
        "confidence_score": 0.8,  # Capped at 80% per Overmind Directive
        "verification_status": "verified_manual",
        "ingestion_source": "manual_ingest",
        "generation": 55,
    }

    mem.store(section, payload, privilege_level=0)
    print(f"✅ Successfully Ingested: {rel_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ingest_single_file.py <path_to_file>")
    else:
        ingest_file(sys.argv[1])
