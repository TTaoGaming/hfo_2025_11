import sqlite3
import lancedb
import os
import sys
import shutil

# Add root to path to import config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings

def init_sqlite():
    """Initialize the SQLite database (Iron Ledger)."""
    print(f"🗄️ Initializing SQLite at {settings.SQLITE_PATH}...")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(settings.SQLITE_PATH), exist_ok=True)
    
    conn = sqlite3.connect(settings.SQLITE_PATH)
    cursor = conn.cursor()
    
    # Create Holons Table (The fundamental unit)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS holons (
        id TEXT PRIMARY KEY,
        type TEXT NOT NULL,
        generation INTEGER,
        payload TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    conn.commit()
    conn.close()
    print("✅ SQLite Initialized. Table 'holons' ready.")

def init_lancedb():
    """Initialize LanceDB (Vector Mirror)."""
    print(f"🪞 Initializing LanceDB at {settings.LANCEDB_PATH}...")
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(settings.LANCEDB_PATH), exist_ok=True)
    
    db = lancedb.connect(settings.LANCEDB_PATH)
    
    # Create a dummy table if it doesn't exist to verify access
    # In a real scenario, we'd define a schema with Pydantic
    try:
        if "test_memory" not in db.table_names():
            data = [{"vector": [0.0]*1536, "text": "init", "id": "0"}]
            db.create_table("test_memory", data)
            print("✅ LanceDB Initialized. Table 'test_memory' created.")
        else:
            print("✅ LanceDB already initialized.")
            
    except Exception as e:
        print(f"❌ LanceDB Initialization Failed: {e}")

if __name__ == "__main__":
    init_sqlite()
    init_lancedb()
