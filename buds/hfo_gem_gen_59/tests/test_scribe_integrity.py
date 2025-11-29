import sys
import os
import sqlite3
import difflib
from pathlib import Path

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_59.brain.scribe import Scribe

def test_ingestion_integrity():
    print("🧪 Starting Scribe Integrity Test...")
    
    # 1. Setup
    scribe = Scribe()
    target_file = "buds/hfo_gem_gen_55/brain/design_obsidian_hourglass.md"
    
    if not os.path.exists(target_file):
        print(f"❌ Target file not found: {target_file}")
        return

    # 2. Read Original
    with open(target_file, "r", encoding="utf-8") as f:
        original_content = f.read()
    
    print(f"📄 Original File Size: {len(original_content)} chars")

    # 3. Ingest
    data = {
        "source_path": os.path.abspath(target_file),
        "content": original_content,
        "generation": 55,
        "category": "design",
        "tags": ["hourglass", "architecture", "test"]
    }
    
    result = scribe.ingest(data)
    print(f"📥 Ingestion Result: {result}")
    
    if result["status"] != "success":
        print("❌ Ingestion failed!")
        return

    # 4. Verify from DB (The Quiz)
    db_path = "buds/hfo_gem_gen_59/memory/hfo_gen_59_memory.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # We query by the exact source path we just inserted
    cursor.execute("SELECT content, content_hash FROM memory_items WHERE source_path = ?", (os.path.abspath(target_file),))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        print("❌ Data not found in DB!")
        return

    stored_content = row[0]
    stored_hash = row[1]
    
    print(f"💾 Stored Hash: {stored_hash}")
    print(f"🧮 Input Hash:  {result['hash']}")
    
    # 5. Calculate Loss
    hash_match = stored_hash == result['hash']
    content_match = stored_content == original_content
    
    if hash_match and content_match:
        print("\n✅ INTEGRITY CHECK PASSED: 100% Match")
        print("   The Iron Ledger successfully stored the exact content and hash.")
        print("   Info Loss: 0.00%")
    else:
        print("\n❌ INTEGRITY CHECK FAILED")
        if not hash_match:
            print("   - Hash Mismatch")
        if not content_match:
            print("   - Content Mismatch")
        print("   Info Loss: DETECTED")

if __name__ == "__main__":
    test_ingestion_integrity()
