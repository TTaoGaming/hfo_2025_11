import os
import sys
import time
import traceback
from datetime import datetime
from typing import List, Dict
import psycopg2
from psycopg2.extras import execute_values, Json
from langchain_openai import OpenAIEmbeddings

# Add HiveFleetObsidian to path
sys.path.append(os.path.join(os.getcwd(), 'HiveFleetObsidian'))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)

# Config
BATCH_SIZE = 10 # Reduced from 50 to prevent system freezing
MAX_FILE_SIZE_BYTES = 1024 * 1024 # 1MB
MAX_CHUNK_SIZE = 2000
OVERLAP = 200
SLEEP_BETWEEN_FILES = 0.5 # Seconds to sleep after each file
SLEEP_BETWEEN_BATCHES = 2.0 # Seconds to sleep after each batch

def get_db_connection():
    config = get_config()
    return psycopg2.connect(config.database.url)

def chunk_text(text: str, chunk_size: int = MAX_CHUNK_SIZE, overlap: int = OVERLAP) -> List[str]:
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
    if "swarm_results" in lower_path or "consensus" in lower_path or "hfo_crew_ai" in lower_path:
        meta["level"] = "hfo_lvl1"
    
    return meta

def process_file_content(file_path, embeddings_model, conn):
    """Reads, chunks, embeds, and inserts a single file."""
    
    # 1. Validation
    if not os.path.exists(file_path):
        return "SKIPPED", "File not found"
    
    if os.path.getsize(file_path) > MAX_FILE_SIZE_BYTES:
        return "SKIPPED", "File too large"

    # 2. Read
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        content = content.replace('\x00', '') # Sanitize
        if not content.strip():
            return "SKIPPED", "Empty content"
    except Exception as e:
        return "FAILED", str(e)

    # 3. Chunk
    chunks = chunk_text(content)
    if not chunks:
        return "SKIPPED", "No chunks generated"

    # 4. Embed
    try:
        vectors = embeddings_model.embed_documents(chunks)
    except Exception as e:
        return "FAILED", f"Embedding error: {str(e)}"

    # 5. Insert into Knowledge Bank
    metadata = determine_metadata(file_path)
    rows = []
    for chunk, vector in zip(chunks, vectors):
        rows.append((file_path, content, vector, Json(metadata))) # Note: storing full content in every row is redundant but matches schema

    # We use a separate cursor for the insert to ensure it's atomic per file
    with conn.cursor() as cur:
        # Clean up old entries for this file first (idempotency)
        cur.execute("DELETE FROM knowledge_bank WHERE source_path = %s", (file_path,))
        
        execute_values(cur, """
            INSERT INTO knowledge_bank (source_path, content, embedding, metadata)
            VALUES %s
        """, rows)
    
    return "COMPLETED", None

def worker_loop():
    print("Worker started. Waiting for tasks...")
    conn = get_db_connection()
    conn.autocommit = True # We manage transactions manually if needed, but autocommit is safer for the queue updates
    
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    while True:
        # 1. Fetch pending items and lock them
        # FOR UPDATE SKIP LOCKED ensures multiple workers don't grab the same rows
        with conn.cursor() as cur:
            cur.execute("""
                UPDATE ingestion_queue
                SET status = 'PROCESSING', updated_at = NOW(), attempts = attempts + 1
                WHERE id IN (
                    SELECT id FROM ingestion_queue
                    WHERE status = 'PENDING'
                    ORDER BY id ASC
                    LIMIT %s
                    FOR UPDATE SKIP LOCKED
                )
                RETURNING id, file_path
            """, (BATCH_SIZE,))
            tasks = cur.fetchall()

        if not tasks:
            print("No pending tasks. Sleeping 5s...")
            time.sleep(5)
            continue

        print(f"Processing batch of {len(tasks)} files...")

        for task_id, file_path in tasks:
            status = "PROCESSING"
            error_msg = None
            
            try:
                status, error_msg = process_file_content(file_path, embeddings, conn)
            except Exception as e:
                status = "FAILED"
                error_msg = f"Unexpected error: {traceback.format_exc()}"
            
            # Update queue status
            with conn.cursor() as cur:
                cur.execute("""
                    UPDATE ingestion_queue
                    SET status = %s, last_error = %s, updated_at = NOW()
                    WHERE id = %s
                """, (status, error_msg, task_id))
                
            print(f"[{status}] {file_path}")
            
            # Throttle to prevent system freeze
            time.sleep(SLEEP_BETWEEN_FILES)
        
        # Throttle between batches
        time.sleep(SLEEP_BETWEEN_BATCHES)

if __name__ == "__main__":
    worker_loop()
