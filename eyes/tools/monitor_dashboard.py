"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 37d54061-3104-4348-b09f-bdbefe263bc4
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.580807+00:00'
    generation: 51
  topos:
    address: eyes/tools/monitor_dashboard.py
    links: []
  telos:
    viral_factor: 0.0
    meme: monitor_dashboard.py
"""

import psycopg2
import time
import os

# Database connection parameters - matching the other scripts
DB_NAME = "vectordb"
DB_USER = "postgres"
DB_PASSWORD = "mysecretpassword"
DB_HOST = "localhost"


def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST
        )
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_progress_bar(
    iteration,
    total,
    prefix="",
    suffix="",
    decimals=1,
    length=50,
    fill="█",
    printEnd="\r",
):
    """
    Call in a loop to create terminal progress bar
    """
    if total == 0:
        percent = 0
        filledLength = 0
    else:
        percent = ("{0:." + str(decimals) + "f}").format(
            100 * (iteration / float(total))
        )
        filledLength = int(length * iteration // total)

    bar = fill * filledLength + "-" * (length - filledLength)
    print(f"\r{prefix} |{bar}| {percent}% {suffix}", end=printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()


def monitor():
    conn = get_db_connection()
    if not conn:
        return

    try:
        while True:
            with conn.cursor() as cur:
                # Get counts by status
                cur.execute(
                    """
                    SELECT status, COUNT(*)
                    FROM ingestion_queue
                    GROUP BY status
                """
                )
                results = cur.fetchall()

                stats = {
                    "PENDING": 0,
                    "PROCESSING": 0,
                    "COMPLETED": 0,
                    "FAILED": 0,
                    "SKIPPED": 0,
                }

                total_files = 0
                for status, count in results:
                    stats[status] = count
                    total_files += count

                # Calculate processed count (everything not pending or processing)
                processed = stats["COMPLETED"] + stats["FAILED"] + stats["SKIPPED"]

                clear_screen()
                print("=== HFO Ingestion Dashboard ===")
                print(f"Total Files: {total_files:,}")
                print("-" * 30)
                print(f"PENDING:    {stats['PENDING']:,}")
                print(f"PROCESSING: {stats['PROCESSING']:,}")
                print(f"COMPLETED:  {stats['COMPLETED']:,}")
                print(f"SKIPPED:    {stats['SKIPPED']:,}")
                print(f"FAILED:     {stats['FAILED']:,}")
                print("-" * 30)

                # Progress bar
                print_progress_bar(
                    processed,
                    total_files,
                    prefix="Progress:",
                    suffix="Complete",
                    length=40,
                )

                print("\n\nPress Ctrl+C to exit monitor (worker will continue running)")

            time.sleep(2)

    except KeyboardInterrupt:
        print("\nMonitor stopped.")
    finally:
        conn.close()


if __name__ == "__main__":
    monitor()
