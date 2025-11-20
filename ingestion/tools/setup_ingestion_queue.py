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

def setup_queue():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    conn.autocommit = True
    cur = conn.cursor()

    print("Setting up 'ingestion_queue' table...")

    # Status enum: PENDING, PROCESSING, COMPLETED, FAILED, SKIPPED
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ingestion_queue (
            id SERIAL PRIMARY KEY,
            file_path TEXT UNIQUE NOT NULL,
            status VARCHAR(20) DEFAULT 'PENDING',
            attempts INT DEFAULT 0,
            last_error TEXT,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
    """)

    # Index for fast fetching of pending items
    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_queue_status 
        ON ingestion_queue(status);
    """)

    print("Queue table ready.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    setup_queue()
