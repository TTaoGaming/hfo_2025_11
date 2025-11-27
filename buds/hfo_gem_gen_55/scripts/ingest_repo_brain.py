"""
# ==================================================================
# 🧠 REPO BRAIN INGESTION: AGENTS.MD & BRAIN/
# ==================================================================
# Purpose: Ingest the canonical repository brain files into LanceDB.
# Targets: AGENTS.md, README.md, brain/ directory.
# Features:
#   - Parses Stigmergy Headers (YAML Frontmatter)
#   - Extracts Generation & Timestamp
#   - Sets High Confidence (0.95) for Canonical Files
"""

import os
import sys
import yaml
import re
from pathlib import Path

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add parent directory to path (to reach memory module)
# We need to reach buds/hfo_gem_gen_55/memory
REPO_ROOT = Path(__file__).resolve().parents[3]
GEN55_ROOT = REPO_ROOT / "buds/hfo_gem_gen_55"
sys.path.append(str(GEN55_ROOT))

from memory.lancedb_store import HFOStigmergyMemory

# Files to ingest explicitly
ROOT_FILES = ["AGENTS.md", "README.md"]
# Directories to ingest recursively
TARGET_DIRS = ["brain"]


def parse_frontmatter(content):
    """
    Extracts YAML frontmatter from the content.
    Returns (metadata_dict, clean_content)
    """
    # Regex for frontmatter: ^---\n(.*?)\n---\n
    match = re.search(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if match:
        yaml_text = match.group(1)
        try:
            metadata = yaml.safe_load(yaml_text)
            # Remove frontmatter from content for storage if desired,
            # but keeping it is also fine. Let's keep it but return metadata separately.
            return metadata, content
        except yaml.YAMLError as e:
            print(f"  ⚠️ YAML Error: {e}")
            return {}, content
    return {}, content


def extract_stigmergy_info(metadata):
    """
    Extracts generation and timestamp from the nested Stigmergy structure.
    """
    info = {
        "generation": "unknown",
        "timestamp": "unknown",
        "id": "unknown",
        "type": "unknown",
    }

    # Try to find generation in hexagon.chronos
    try:
        info["generation"] = (
            metadata.get("hexagon", {}).get("chronos", {}).get("generation", "unknown")
        )
    except:
        pass

    # Try to find timestamp in holon or hexagon.chronos
    try:
        # Prefer holon timestamp if available
        info["timestamp"] = metadata.get("holon", {}).get("timestamp")
        if not info["timestamp"]:
            info["timestamp"] = (
                metadata.get("hexagon", {}).get("chronos", {}).get("created")
            )
    except:
        pass

    # Try to find ID
    try:
        info["id"] = metadata.get("holon", {}).get("id") or metadata.get(
            "hexagon", {}
        ).get("ontos", {}).get("id")
    except:
        pass

    return info


def ingest_repo_brain():
    print(f"🧠 Starting Repo Brain Ingestion from {REPO_ROOT}...")
    # Point to the Gen 55 LanceDB
    db_path = GEN55_ROOT / "memory/lancedb"
    print(f"  💾 Using Database: {db_path}")
    mem = HFOStigmergyMemory(db_path=str(db_path))

    count = 0

    # 1. Ingest Root Files
    for filename in ROOT_FILES:
        file_path = REPO_ROOT / filename
        if file_path.exists():
            print(f"  📄 Processing {filename}...")
            try:
                content = file_path.read_text(encoding="utf-8")
                metadata, _ = parse_frontmatter(content)
                stig_info = extract_stigmergy_info(metadata)

                payload = {
                    "id": stig_info.get("id") or filename,
                    "filename": filename,
                    "path": str(file_path),
                    "type": "documentation",
                    "content": content,
                    "confidence_score": 0.95,  # High confidence for root files
                    "verification_status": "verified_canonical",
                    "ingestion_source": "repo_brain_ingest",
                    "generation": stig_info["generation"],
                    "timestamp": stig_info["timestamp"],
                    "raw_metadata": metadata,
                }

                mem.store("root", payload, privilege_level=1)
                count += 1
            except Exception as e:
                print(f"  ❌ Error processing {filename}: {e}")
        else:
            print(f"  ⚠️ {filename} not found.")

    # 2. Ingest Brain Directory
    for target_dir in TARGET_DIRS:
        dir_path = REPO_ROOT / target_dir
        if dir_path.exists():
            print(f"  📂 Processing directory: {target_dir}...")
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    if (
                        file.endswith(".md")
                        or file.endswith(".txt")
                        or file.endswith(".yaml")
                    ):
                        file_path = Path(root) / file
                        rel_path = file_path.relative_to(REPO_ROOT)

                        try:
                            content = file_path.read_text(encoding="utf-8")
                            metadata, _ = parse_frontmatter(content)
                            stig_info = extract_stigmergy_info(metadata)

                            payload = {
                                "id": stig_info.get("id") or str(rel_path),
                                "filename": file,
                                "path": str(file_path),
                                "type": "brain_concept",
                                "content": content,
                                "confidence_score": 0.95,
                                "verification_status": "verified_canonical",
                                "ingestion_source": "repo_brain_ingest",
                                "generation": stig_info["generation"],
                                "timestamp": stig_info["timestamp"],
                                "raw_metadata": metadata,
                            }

                            mem.store("brain", payload, privilege_level=1)
                            count += 1
                            if count % 10 == 0:
                                print(f"    ... Ingested {count} files")
                        except Exception as e:
                            print(f"  ❌ Error processing {file}: {e}")

    print(f"\n✅ Repo Brain Ingestion Complete. Total Files: {count}")


if __name__ == "__main__":
    ingest_repo_brain()
