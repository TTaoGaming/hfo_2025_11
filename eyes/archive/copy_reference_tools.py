import os
import shutil
from pathlib import Path

def copy_reference_tools():
    archive_root = Path("_ARCHIVE_2025_11_19")
    dest_dir = Path("hive_fleet_obsidian_2025_11/ingestion/reference_tools")

    dest_dir.mkdir(parents=True, exist_ok=True)

    # List of specific files to rescue from the root of the archive
    files_to_rescue = [
        "concept_explorer.py",
        "debug_queue.py",
        "force_reset_queue.py",
        "HFO_CONCEPT_MAP.md",
        "HFO_CONCEPTS.md",
        "INGESTION_SPEC.feature",
        "inventory_scanner.py",
        "monitor_dashboard.py",
        "monitor_progress.py",
        "query_unified.py",
        "queue_worker.py",
        "README_INGESTION.md",
        "setup_ingestion_queue.py",
        "setup_unified_memory.py",
        "step1_inventory.py",
        "step2_worker.py",
        "universal_ingest.py",
        "verify_ingestion.py",
        "visualize_concepts.py",
        "🕸⛰💎🧬🥇_Gem1_Generation18_20251024T000000Z.md"
    ]

    print(f"Rescuing {len(files_to_rescue)} reference tools/docs to {dest_dir}...")

    count = 0
    for filename in files_to_rescue:
        src = archive_root / filename
        dst = dest_dir / filename

        if src.exists():
            shutil.copy2(src, dst)
            count += 1
        else:
            print(f"Warning: Could not find {src}")

    print(f"Successfully copied {count} files.")

if __name__ == "__main__":
    copy_reference_tools()
