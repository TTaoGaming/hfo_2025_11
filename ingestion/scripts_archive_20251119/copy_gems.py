import os
import shutil
from pathlib import Path

def copy_hfo_gems():
    archive_root = Path("_ARCHIVE_2025_11_19")
    audit_dest = Path("hive_fleet_obsidian_2025_11/audit_trail/hfo_gems_raw")
    ingest_dest = Path("hive_fleet_obsidian_2025_11/ingestion/staging_memory")
    
    # Ensure destinations exist
    audit_dest.mkdir(parents=True, exist_ok=True)
    ingest_dest.mkdir(parents=True, exist_ok=True)
    
    print(f"Scanning {archive_root} for 'hfo_gem' directories...")
    
    found_dirs = []
    for root, dirs, files in os.walk(archive_root):
        for d in dirs:
            if "hfo_gem" in d:
                found_dirs.append(Path(root) / d)
    
    print(f"Found {len(found_dirs)} directories.")
    
    for src_dir in found_dirs:
        # Create a unique name for the destination based on the path
        # e.g. _ARCHIVE.../HiveFleetObsidian/hfo_gem -> HiveFleetObsidian_hfo_gem
        
        relative_path = src_dir.relative_to(archive_root)
        # Replace path separators with underscores for a flat structure
        flat_name = str(relative_path).replace(os.sep, "_")
        
        dest_audit = audit_dest / flat_name
        dest_ingest = ingest_dest / flat_name
        
        print(f"Copying {src_dir} -> {dest_audit}")
        if dest_audit.exists():
            print(f"  Skipping {dest_audit} (already exists)")
        else:
            shutil.copytree(src_dir, dest_audit)
            
        print(f"Copying {src_dir} -> {dest_ingest}")
        if dest_ingest.exists():
            print(f"  Skipping {dest_ingest} (already exists)")
        else:
            shutil.copytree(src_dir, dest_ingest)

if __name__ == "__main__":
    copy_hfo_gems()
