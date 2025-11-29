import sqlite3
import os
import sys

# Target Gen 60 Memory (Iron Ledger)
DB_PATH = "/home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_60/memory/hfo_gen_60_memory.db"

if not os.path.exists(DB_PATH):
    print(f"Database not found: {DB_PATH}")
    sys.exit(1)

try:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Get tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables: {tables}")

    # Inspect schema of likely tables
    for table in tables:
        t_name = table[0]
        print(f"\nSchema for {t_name}:")
        cursor.execute(f"PRAGMA table_info({t_name})")
        columns = cursor.fetchall()
        for col in columns:
            print(f"  {col[1]} ({col[2]})")

    conn.close()

except Exception as e:
    print(f"Error inspecting SQLite: {e}")
