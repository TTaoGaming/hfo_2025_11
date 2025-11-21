import os
import sys
import time
from datetime import datetime
from typing import List, Dict
import psycopg2
from psycopg2.extras import execute_values, Json
from tqdm import tqdm

# Add HiveFleetObsidian to path to use existing config and embeddings
sys.path.append(os.path.join(os.getcwd(), "HiveFleetObsidian"))

try:
    from hfo_sdk.config import get_config
    from langchain_openai import OpenAIEmbeddings
except ImportError:
    print(
        "Could not import hfo_sdk. Make sure you are running this from the workspace root."
    )
    sys.exit(1)

# Configuration
IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    "env",
    ".vscode",
    ".idea",
    "dist",
    "build",
    "coverage",
}
IGNORE_EXTENSIONS = {
    ".pyc",
    ".pyo",
    ".pyd",
    ".so",
    ".dll",
    ".class",
    ".exe",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".ico",
    ".svg",
    ".zip",
    ".tar",
    ".gz",
    ".7z",
    ".deb",
    ".rpm",
    ".apk",
    ".iso",
    ".img",
    ".bin",
    ".lock",
    ".log",
    ".jsonl",
}
MAX_FILE_SIZE_BYTES = 1024 * 1024  # 1MB limit for text files
MAX_CHUNK_SIZE = 2000
OVERLAP = 200


def get_db_connection():
    config = get_config()
    return psycopg2.connect(config.database.url)


def get_embeddings_model():
    # Re-instantiate to avoid potential memory leaks in long runs
    return OpenAIEmbeddings(model="text-embedding-3-small")


def chunk_text(
    text: str, chunk_size: int = MAX_CHUNK_SIZE, overlap: int = OVERLAP
) -> List[str]:
    """Simple overlapping chunker."""
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


def determine_metadata(file_path: str, content: str) -> Dict:
    """
    Infer metadata based on file path and content.
    Enforces the user's rules:
    - Max confidence: 0.9
    - Level: hfo_lvl0 (default) or hfo_lvl1 (if it looks like a consensus result)
    """
    meta = {
        "confidence": 0.9,  # Capped as requested
        "level": "hfo_lvl0",  # Default to single agent/unverified
        "file_type": os.path.splitext(file_path)[1],
        "ingest_timestamp": time.time(),
    }

    # Capture original file timestamp for time filtering
    try:
        mtime = os.path.getmtime(file_path)
        meta["original_timestamp"] = mtime
        meta["original_date"] = datetime.fromtimestamp(mtime).isoformat()
    except Exception:
        pass

    # Detect Generation
    path_parts = file_path.split(os.sep)
    for part in path_parts:
        if part.startswith("gen_") and part[4:].isdigit():
            meta["generation"] = int(part[4:])
            break

    # Detect "Consensus" or "Swarm" results for slightly higher level (still capped at lvl1)
    lower_path = file_path.lower()
    if (
        "swarm_results" in lower_path
        or "consensus" in lower_path
        or "hfo_crew_ai" in lower_path
    ):
        meta["level"] = "hfo_lvl1"

    return meta


def process_file(file_path: str, embeddings_model, cursor):
    try:
        # Skip large files
        if os.path.getsize(file_path) > MAX_FILE_SIZE_BYTES:
            return

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # Check if file already exists to avoid re-ingesting on re-runs
        cursor.execute(
            "SELECT id FROM knowledge_bank WHERE source_path = %s LIMIT 1", (file_path,)
        )
        if cursor.fetchone():
            return

        chunks = chunk_text(content)
        if not chunks:
            return

        # Batch embed chunks
        try:
            vectors = embeddings_model.embed_documents(chunks)
        except Exception as e:
            print(f"Error embedding {file_path}: {e}")
            return

        metadata = determine_metadata(file_path, content)

        # Prepare rows
        rows = []
        for chunk, vector in zip(chunks, vectors):
            rows.append((file_path, chunk, vector, Json(metadata)))

        execute_values(
            cursor,
            """
            INSERT INTO knowledge_bank (source_path, content, embedding, metadata)
            VALUES %s
        """,
            rows,
        )

    except Exception as e:
        print(f"Skipping {file_path}: {e}")


def main():
    print("Starting Universal Ingestion...")

    conn = get_db_connection()
    conn.autocommit = True
    cur = conn.cursor()

    embeddings = get_embeddings_model()

    root_dir = os.getcwd()
    files_to_process = []

    # 1. Scan for files
    print("Scanning workspace...")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filter directories
        dirnames[:] = [
            d for d in dirnames if d not in IGNORE_DIRS and not d.startswith(".")
        ]

        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in IGNORE_EXTENSIONS:
                continue

            full_path = os.path.join(dirpath, f)
            files_to_process.append(full_path)

    print(f"Found {len(files_to_process)} files to ingest.")

    # 2. Process files
    # We'll process in batches to be safe, but the loop handles one file at a time for simplicity
    # The embedding call is the bottleneck.

    # Re-instantiate embeddings every N files to prevent memory leaks
    BATCH_SIZE = 100

    for i, file_path in enumerate(tqdm(files_to_process)):
        if i % BATCH_SIZE == 0:
            embeddings = get_embeddings_model()

        process_file(file_path, embeddings, cur)

    print("Ingestion complete.")
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
