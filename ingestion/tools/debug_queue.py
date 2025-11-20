import os
import sys
import psycopg2

# Add HiveFleetObsidian to path to use existing config
sys.path.append(os.path.join(os.getcwd(), 'HiveFleetObsidian'))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)

def debug_table():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    cur = conn.cursor()
    
    print("Checking table schema...")
    cur.execute("""
        SELECT column_name, data_type 
        FROM information_schema.columns 
        WHERE table_name = 'ingestion_queue';
    """)
    
    columns = cur.fetchall()
    for col in columns:
        print(f" - {col[0]}: {col[1]}")
        
    conn.close()

if __name__ == "__main__":
    debug_table()
