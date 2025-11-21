import os
import json
import shutil
from pathlib import Path

# Configuration
ARCHIVE_ROOT = Path("_ARCHIVE_2025_11_19")
DEST_DIR = Path("hive_fleet_obsidian_2025_11/ingestion/staging_data/test_results")
BLACKBOARD_DEST = Path("hive_fleet_obsidian_2025_11/ingestion/staging_data/blackboard")

def ingest_jsonl():
    print("Scanning archive for JSONL files...")
    
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    BLACKBOARD_DEST.mkdir(parents=True, exist_ok=True)
    
    count = 0
    
    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        for filename in files:
            if filename.endswith(".jsonl"):
                src_path = Path(root) / filename
                
                # Determine destination based on content/name
                if "blackboard" in filename.lower():
                    dest_folder = BLACKBOARD_DEST
                elif "vs_" in filename.lower() or "results" in filename.lower():
                    dest_folder = DEST_DIR
                else:
                    # Skip other random jsonl files for now
                    continue
                
                # Create a unique name to avoid collisions
                # Use UUID to avoid "File name too long" errors
                import uuid
                rel_path = src_path.relative_to(ARCHIVE_ROOT)
                file_uuid = str(uuid.uuid4())
                dest_path = dest_folder / f"{file_uuid}.jsonl"
                
                # Save metadata mapping
                metadata = {
                    "original_path": str(src_path),
                    "relative_path": str(rel_path),
                    "filename": filename,
                    "uuid": file_uuid
                }
                
                # Append to manifest (inefficient but safe for now)
                manifest_path = dest_folder / "manifest.jsonl"
                with open(manifest_path, "a") as f:
                    f.write(json.dumps(metadata) + "\n")
                
                # Copy the file
                shutil.copy2(src_path, dest_path)
                count += 1
                
    print(f"Imported {count} JSONL data files to {DEST_DIR.parent}")

if __name__ == "__main__":
    ingest_jsonl()
