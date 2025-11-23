"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 2bd399a5-685f-4661-ad89-6546c9c37cff
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.585922+00:00'
  topos:
    address: eyes/tools/setup_ingestion_queue.py
    links: []
  telos:
    viral_factor: 0.0
    meme: setup_ingestion_queue.py
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


def setup_queue():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    conn.autocommit = True
    cur = conn.cursor()

    print("Setting up 'ingestion_queue' table...")

    # Status enum: PENDING, PROCESSING, COMPLETED, FAILED, SKIPPED
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS ingestion_queue (
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

    print("Queue table ready.")
    cur.close()
    conn.close()


if __name__ == "__main__":
    setup_queue()
