"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 84865445-51a1-4d3f-aca0-39a0725e97fb
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.581986+00:00'
  topos:
    address: eyes/tools/monitor_progress.py
    links: []
  telos:
    viral_factor: 0.0
    meme: monitor_progress.py
"""

import os
import sys
import time
import psycopg2
from tabulate import tabulate

# Add HiveFleetObsidian to path
sys.path.append(os.path.join(os.getcwd(), "HiveFleetObsidian"))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)


def get_status():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    cur = conn.cursor()

    cur.execute(
        """
        SELECT status, COUNT(*)
        FROM ingestion_queue
        GROUP BY status
    """
    )
    rows = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM knowledge_bank")
    vectors = cur.fetchone()[0]

    conn.close()
    return rows, vectors


def main():
    while True:
        os.system("clear")
        rows, vectors = get_status()

        print("=== Ingestion Progress Monitor ===")
        print(f"Time: {time.strftime('%H:%M:%S')}")
        print(f"Total Vectors in Bank: {vectors}")
        print("\nQueue Status:")

        headers = ["Status", "Count"]
        print(tabulate(rows, headers=headers, tablefmt="pretty"))

        total = sum(r[1] for r in rows)
        if total > 0:
            completed = sum(r[1] for r in rows if r[0] == "COMPLETED")
            _failed = sum(r[1] for r in rows if r[0] == "FAILED")
            _pending = sum(r[1] for r in rows if r[0] == "PENDING")

            progress = (completed / total) * 100
            print(f"\nProgress: {progress:.2f}%")

            # Estimate time remaining?
            # Need rate calculation, maybe later.

        print("\n(Ctrl+C to exit monitor)")
        time.sleep(5)


if __name__ == "__main__":
    main()
