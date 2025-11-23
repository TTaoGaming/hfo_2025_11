"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: fd7c6191-8ddc-44d9-8e93-ca9e659efaaf
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.577678+00:00'
    generation: 51
  topos:
    address: eyes/tools/force_reset_queue.py
    links: []
  telos:
    viral_factor: 0.0
    meme: force_reset_queue.py
"""

import os
import sys
import psycopg2

# Add HiveFleetObsidian to path to use existing config
sys.path.append(os.path.join(os.getcwd(), "HiveFleetObsidian"))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)


def force_reset_queue():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    conn.autocommit = True
    cur = conn.cursor()

    print("Dropping 'ingestion_queue' table...")
    cur.execute("DROP TABLE IF EXISTS ingestion_queue;")

    print("Recreating 'ingestion_queue' table...")
    cur.execute(
        """
        CREATE TABLE ingestion_queue (
            id SERIAL PRIMARY KEY,
            file_path TEXT UNIQUE NOT NULL,
            status VARCHAR(20) DEFAULT 'PENDING',
            attempts INT DEFAULT 0,
            last_error TEXT,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
    """
    )

    # Index for fast fetching of pending items
    cur.execute(
        """
        CREATE INDEX IF NOT EXISTS idx_queue_status
        ON ingestion_queue(status);
    """
    )

    print("Queue table reset complete.")
    cur.close()
    conn.close()


if __name__ == "__main__":
    force_reset_queue()
