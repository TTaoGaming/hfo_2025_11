import os
import json
import re
import uuid
from pathlib import Path

# Configuration
STAGING_DIR = Path("hive_fleet_obsidian_2025_11/ingestion/staging_memory")
OUTPUT_FILE = Path("hive_fleet_obsidian_2025_11/ingestion/hfo_memory_dump.jsonl")

def extract_generation(path_str):
    """
    Attempts to extract the Generation number from the file path.
    Looks for patterns like 'gen_12', 'Gen 50', 'gen-3'.
    """
    # Pattern: gen followed by separator and digits
    match = re.search(r'(?:gen|Gen)[_\-\s]?(\d+)', path_str)
    if match:
        return int(match.group(1))
    return None

def clean_content(content):
    """
    Basic cleaning for 'AI Slop'.
    - Removes null bytes.
    - Could add more heuristics here (e.g. removing 'As an AI...').
    """
    if not content:
        return ""
    # Remove null bytes
    content = content.replace('\x00', '')
    return content

def process_files():
    print(f"Scanning {STAGING_DIR}...")
    
    records = []
    file_count = 0
    
    for root, dirs, files in os.walk(STAGING_DIR):
        for filename in files:
            if filename.endswith(('.md', '.py', '.txt', '.json', '.yaml', '.yml')):
                file_path = Path(root) / filename
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
                        raw_content = f.read()
                        
                    content = clean_content(raw_content)
                    
                    # Skip empty files
                    if not content.strip():
                        continue

                    # Extract Metadata
                    gen = extract_generation(str(file_path))
                    rel_path = str(file_path.relative_to(STAGING_DIR))
                    
                    record = {
                        "id": str(uuid.uuid4()),
                        "content": content,
                        "metadata": {
                            "source_path": rel_path,
                            "filename": filename,
                            "extension": file_path.suffix,
                            "generation": gen,
                            "length": len(content)
                        }
                    }
                    records.append(record)
                    file_count += 1
                    
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"Processed {file_count} files.")
    
    # Sort by Generation (if available) then by filename
    # This helps with chronological ordering in the JSONL
    records.sort(key=lambda x: (x['metadata']['generation'] if x['metadata']['generation'] is not None else -1, x['metadata']['filename']))

    print(f"Writing to {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        for record in records:
            f.write(json.dumps(record) + '\n')
            
    print("Done.")

if __name__ == "__main__":
    process_files()
