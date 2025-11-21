import os
import sys
import psycopg2
from psycopg2.extras import Json

# Add HiveFleetObsidian to path to use existing config
sys.path.append(os.path.join(os.getcwd(), 'HiveFleetObsidian'))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)

def verify_ingestion():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    cur = conn.cursor()
    
    print("\n=== Ingestion Verification Report ===\n")
    
    # 1. Total Count
    cur.execute("SELECT COUNT(*) FROM knowledge_bank;")
    count = cur.fetchone()[0]
    print(f"Total Records Ingested: {count}")
    
    if count == 0:
        print("WARNING: No records found. Ingestion might have failed or is still starting.")
        return

    # 2. Check Levels
    cur.execute("SELECT metadata->>'level', COUNT(*) FROM knowledge_bank GROUP BY metadata->>'level';")
    levels = cur.fetchall()
    print("\nBreakdown by Trust Level:")
    for level, cnt in levels:
        print(f"  - {level}: {cnt}")

    # 3. Check Confidence
    cur.execute("SELECT metadata->>'confidence', COUNT(*) FROM knowledge_bank GROUP BY metadata->>'confidence';")
    confidences = cur.fetchall()
    print("\nBreakdown by Confidence:")
    for conf, cnt in confidences:
        print(f"  - {conf}: {cnt}")

    # 4. Sample Record
    print("\nSample Record (Latest):")
    cur.execute("SELECT source_path, metadata FROM knowledge_bank ORDER BY created_at DESC LIMIT 1;")
    path, meta = cur.fetchone()
    print(f"  File: {path}")
    print(f"  Metadata: {meta}")
    
    print("\n=====================================\n")
    conn.close()

if __name__ == "__main__":
    verify_ingestion()
