
import lancedb
import os
import sys

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

DB_PATH = "buds/hfo_gem_gen_63/06_assimilator_memory/lancedb"

if not os.path.exists(DB_PATH):
    print(f"❌ DB Path not found: {DB_PATH}")
    sys.exit(1)

try:
    db = lancedb.connect(DB_PATH)
    print(f"✅ Connected to {DB_PATH}")
    print(f"📂 Tables: {db.table_names()}")
except Exception as e:
    print(f"❌ Error: {e}")
