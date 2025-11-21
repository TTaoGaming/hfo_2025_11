import os
import sys
import time
from datetime import datetime
from typing import List, Dict
import psycopg2
from psycopg2.extras import execute_values, Json
from tqdm import tqdm

# Add HiveFleetObsidian to path
sys.path.append(os.path.join(os.getcwd(), 'HiveFleetObsidian'))

try:
    from hfo_sdk.config import get_config
    from langchain_openai import OpenAIEmbeddings
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)

# Config
BATCH_SIZE = 10
MAX_RETRIES = 3

def get_db_connection():
    config = get_config()
    return psycopg2.connect(config.database.url)

def get_embeddings_model():
    # Set a timeout for the HTTP client
    return OpenAIEmbeddings(model="text-embedding-3-small", timeout=30)

def chunk_text(text: str, chunk_size=2000, overlap=200):
    if len(text) <= chunk_size:
        return [text]
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def determine_metadata(file_path: str) -> Dict:
    meta = {
        "confidence": 0.9,
        "level": "hfo_lvl0",
        "file_type": os.path.splitext(file_path)[1],
        "ingest_timestamp": time.time()
    }
    try:
        mtime = os.path.getmtime(file_path)
        meta["original_timestamp"] = mtime
        meta["original_date"] = datetime.fromtimestamp(mtime).isoformat()
    except:
        pass

    path_parts = file_path.split(os.sep)
    for part in path_parts:
        if part.startswith("gen_") and part[4:].isdigit():
            meta["generation"] = int(part[4:])
            break

    lower_path = file_path.lower()
    if "swarm_results" in lower_path or "consensus" in lower_path:
        meta["level"] = "hfo_lvl1"

    return meta

def process_batch(conn, embeddings_model):
    """
    1. Fetch N pending items
    2. Process them
    3. Update status
    """
    cur = conn.cursor()

    # 1. Claim a batch
    # We select PENDING items.
    cur.execute(f"""
        SELECT file_path FROM ingestion_queue
        WHERE status = 'PENDING'
        LIMIT {BATCH_SIZE}
        FOR UPDATE SKIP LOCKED
    """)
    rows = cur.fetchall()

    if not rows:
        return 0

    file_paths = [r[0] for r in rows]

    # Mark them as PROCESSING so other workers don't grab them (if we ran parallel)
    cur.execute("""
        UPDATE ingestion_queue
        SET status = 'PROCESSING', updated_at = NOW()
        WHERE file_path = ANY(%s)
    """, (file_paths,))
    conn.commit()

    # 2. Process
    success_paths = []
    failed_paths = [] # (path, error_msg)

    vectors_to_insert = [] # (path, chunk, vector, meta)

    for file_path in file_paths:
        try:
            # Double check file exists
            if not os.path.exists(file_path):
                failed_paths.append((file_path, "File not found"))
                continue

            # print(f"Processing: {file_path}") # Verbose logging

            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()

            # Sanitize
            content = content.replace('\x00', '')
            if not content.strip():
                success_paths.append(file_path) # Empty file is "success" (nothing to do)
                continue

            chunks = chunk_text(content)
            if not chunks:
                success_paths.append(file_path)
                continue

            # Embed
            try:
                vectors = embeddings_model.embed_documents(chunks)
            except Exception as e:
                failed_paths.append((file_path, str(e)))
                continue

            meta = determine_metadata(file_path)

            for chunk, vector in zip(chunks, vectors):
                vectors_to_insert.append((file_path, chunk, vector, Json(meta)))

            success_paths.append(file_path)

        except Exception as e:
            failed_paths.append((file_path, str(e)))

    # 3. Bulk Insert Vectors
    if vectors_to_insert:
        try:
            execute_values(cur, """
                INSERT INTO knowledge_bank (source_path, content, embedding, metadata)
                VALUES %s
            """, vectors_to_insert)
        except Exception as e:
            # If bulk insert fails, fail the whole batch of *vectors*, but we need to be careful.
            # For simplicity, we'll mark the whole batch as failed if DB insert fails.
            print(f"CRITICAL DB ERROR: {e}")
            conn.rollback()
            # Mark all as failed
            for fp in file_paths:
                cur.execute("UPDATE ingestion_queue SET status = 'FAILED', error_message = %s WHERE file_path = %s", (str(e), fp))
            conn.commit()
            return len(file_paths)

    # 4. Update Queue Status
    if success_paths:
        cur.execute("""
            UPDATE ingestion_queue
            SET status = 'COMPLETED', updated_at = NOW()
            WHERE file_path = ANY(%s)
        """, (success_paths,))

    for fp, err in failed_paths:
        cur.execute("""
            UPDATE ingestion_queue
            SET status = 'FAILED', error_message = %s, attempts = attempts + 1, updated_at = NOW()
            WHERE file_path = %s
        """, (err, fp))

    conn.commit()
    cur.close()

    return len(file_paths)

def main():
    print("Starting Ingestion Worker...")
    conn = get_db_connection()
    embeddings = get_embeddings_model()

    # Get total pending
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM ingestion_queue WHERE status = 'PENDING'")
    total_pending = cur.fetchone()[0]
    cur.close()

    print(f"Total Pending Items: {total_pending}")

    pbar = tqdm(total=total_pending)

    while True:
        processed_count = process_batch(conn, embeddings)
        if processed_count == 0:
            break
        pbar.update(processed_count)

    print("\nQueue Empty. Worker finished.")
    conn.close()

if __name__ == "__main__":
    main()
