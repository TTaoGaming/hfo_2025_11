---
holon:
  id: 678c8e52-3c1c-487e-8d8e-4b38adb4f301
  type: codex_entry
  quadrant: how-to
  source_ref: /home/tommytai3/hive_fleet_obsidian_2025_11/buds/hfo_gem_gen_63/src/init_memory.py
hexagon:
  ontos: owner
  logos: diataxis
---

# How to Initialize SQLite and LanceDB

In this article, we will describe the steps required to initialize both SQLite and LanceDB databases as implemented in the provided source code.

## Why Initialize SQLite and LanceDB?

This process is essential for setting up the databases that will store data for your application. SQLite serves as a lightweight database for storing structured data, while LanceDB is utilized for managing vector data, which is crucial for functionalities like searching and retrieval based on vector embeddings.

## Step-by-Step Instructions

### Step 1: Set Up Your Environment
Before running the script, ensure that you have the necessary libraries installed:
- sqlite3
- lancedb

You can usually install them with pip if they aren't already available.

### Step 2: Prepare Your Configuration
Make sure the configuration is set correctly in the `settings` module. The paths for the SQLite and LanceDB should be defined in `settings.SQLITE_PATH` and `settings.LANCEDB_PATH`, respectively.

### Step 3: Import the Script
Import the necessary modules and functions in your script as shown:
```python
import sqlite3
import lancedb
import os
import sys
import shutil

from src.config import settings
```

### Step 4: Define the Initialization Functions
Define the functions to initialize SQLite and LanceDB if they are not already defined in the provided script:

#### Initialize SQLite
```python
def init_sqlite():
    """Initialize the SQLite database (Iron Ledger)."""
    print(f"🗄️ Initializing SQLite at {settings.SQLITE_PATH}...")
    os.makedirs(os.path.dirname(settings.SQLITE_PATH), exist_ok=True)
    conn = sqlite3.connect(settings.SQLITE_PATH)
    cursor = conn.cursor()
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
```

#### Initialize LanceDB
```python
def init_lancedb():
    """Initialize LanceDB (Vector Mirror)."""
    print(f"🪞 Initializing LanceDB at {settings.LANCEDB_PATH}...")
    os.makedirs(os.path.dirname(settings.LANCEDB_PATH), exist_ok=True)
    db = lancedb.connect(settings.LANCEDB_PATH)
    try:
        if "test_memory" not in db.table_names():
            data = [{"vector": [0.0]*1536, "text": "init", "id": "0"}]
            db.create_table("test_memory", data)
            print("✅ LanceDB Initialized. Table 'test_memory' created.")
        else:
            print("✅ LanceDB already initialized.")
    except Exception as e:
        print(f"❌ LanceDB Initialization Failed: {e}")
```

### Step 5: Run the Main Function
Invoke the initialization functions when executing the script:
```python
if __name__ == "__main__":
    init_sqlite()
    init_lancedb()
```

### Conclusion
After completing the above steps, both your SQLite and LanceDB should be initialized and ready for use in your application.