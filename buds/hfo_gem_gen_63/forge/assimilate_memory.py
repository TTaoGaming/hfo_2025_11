import os
import sqlite3
import json
import yaml
import hashlib
import lancedb
import networkx as nx
from datetime import datetime, date
from typing import Dict, Any

# Configuration
# We scan multiple roots to capture the full history (Gen 1-63)
SEARCH_ROOTS = [
    "buds",                     # Gen 53-63
    "legacy",                   # Gen 51
    "eyes/archive/hfo_gem"      # Gen 1-50
]
# But we store the index in the CURRENT generation (Gen 63)
STORE_ROOT = "buds/hfo_gem_gen_63"

DB_PATH = f"{STORE_ROOT}/memory/iron_ledger.db"
LANCEDB_PATH = f"{STORE_ROOT}/memory/lancedb"
GRAPH_PATH = f"{STORE_ROOT}/memory/knowledge_graph.gml"

def init_db():
    """Initialize the Iron Ledger (SQLite)."""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS holons (
                id TEXT PRIMARY KEY,
                type TEXT,
                file_path TEXT,
                content_hash TEXT,
                metadata JSON,
                last_seen TIMESTAMP
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS links (
                source_id TEXT,
                target_id TEXT,
                relation TEXT,
                PRIMARY KEY (source_id, target_id, relation)
            )
        """)
    print(f"✅ Iron Ledger initialized at {DB_PATH}")

def parse_holon(file_path: str) -> Dict[str, Any]:
    """Extracts Holon metadata from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Simple YAML extraction (assuming Stigmergy Injection worked)
        if file_path.endswith(".md") and content.startswith("---"):
            try:
                parts = content.split("---", 2)
                if len(parts) < 3: return None
                
                meta = yaml.safe_load(parts[1])
                if not isinstance(meta, dict): return None
                
                # Normalize: if 'holon' key exists, use it, else use the whole meta
                if 'holon' in meta:
                    data = meta['holon']
                else:
                    data = meta
                
                # Ensure ID exists
                if 'id' not in data:
                    # Fallback ID generation
                    data['id'] = hashlib.md5(file_path.encode()).hexdigest()
                
                data['content'] = parts[2].strip()
                return data
            except Exception as e:
                # print(f"YAML Error in {file_path}: {e}")
                return None
    except Exception as e:
        print(f"Read Error {file_path}: {e}")
        return None
    return None

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

def assimilate():
    """The Assimilation Loop."""
    print(f"🕷️ Assimilating Memory from {SEARCH_ROOTS} into {STORE_ROOT}...")
    
    # 1. Init Stores
    init_db()
    
    # Ensure LanceDB dir exists
    os.makedirs(LANCEDB_PATH, exist_ok=True)
    db = lancedb.connect(LANCEDB_PATH)
    
    # Create table if not exists (simple schema for now)
    # Note: In a real run, we'd use a proper embedding model. 
    # For now, we just store text to prove the pipeline.
    try:
        tbl = db.create_table("knowledge", data=[{"vector": [0.0]*1536, "text": "init", "id": "init"}], mode="overwrite")
    except:
        tbl = db.open_table("knowledge")

    G = nx.DiGraph()
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    count = 0
    
    # 2. Walk and Ingest
    for search_root in SEARCH_ROOTS:
        if not os.path.exists(search_root):
            print(f"⚠️ Warning: Path not found: {search_root}")
            continue
            
        for root, dirs, files in os.walk(search_root):
            # SKIP BINARY / DB FOLDERS
            if "memory" in root and "lancedb" in root: continue
            if ".git" in root or "__pycache__" in root: continue
            
            for file in files:
                if not file.endswith(".md"): continue
                
                file_path = os.path.join(root, file)
                holon = parse_holon(file_path)
                
                if holon:
                    # A. Iron Ledger (SQL)
                    try:
                        cursor.execute("""
                            INSERT OR REPLACE INTO holons (id, type, file_path, content_hash, metadata, last_seen)
                            VALUES (?, ?, ?, ?, ?, ?)
                        """, (
                            holon.get('id', 'unknown'),
                            holon.get('type', 'unknown'),
                            file_path,
                            hashlib.md5(holon.get('content', '').encode()).hexdigest(),
                            json.dumps(holon, default=json_serial),
                            datetime.now()
                        ))
                        count += 1
                        if count % 100 == 0:
                            print(f"🕷️ Assimilated {count} holons...")
                    except Exception as e:
                        print(f"SQL Error on {file_path}: {e}")

    conn.commit()
    conn.close()
    print(f"✅ Assimilation Complete. Total Holons: {count}")

if __name__ == "__main__":
    assimilate()
