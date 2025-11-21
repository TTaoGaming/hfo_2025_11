import os
import sys
import psycopg2
from tqdm import tqdm

# Add HiveFleetObsidian to path
sys.path.append(os.path.join(os.getcwd(), 'HiveFleetObsidian'))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print("Could not import hfo_sdk.")
    sys.exit(1)

# Configuration
IGNORE_DIRS = {
    '.git', '__pycache__', 'node_modules', '.venv', 'venv', 'env',
    '.vscode', '.idea', 'dist', 'build', 'coverage', 'site-packages',
    'miniconda3' # Explicitly ignore the python environment itself
}
IGNORE_EXTENSIONS = {
    '.pyc', '.pyo', '.pyd', '.so', '.dll', '.class', '.exe',
    '.jpg', '.jpeg', '.png', '.gif', '.ico', '.svg', '.zip', '.tar', '.gz', '.7z',
    '.deb', '.rpm', '.apk', '.iso', '.img', '.bin', '.lock', '.log', '.jsonl',
    '.map', '.wav', '.mp3', '.mp4', '.webm', '.ogg', '.flac', '.aac', '.wma', '.m4a',
    '.ttf', '.woff', '.woff2', '.eot'
}

def setup_queue_db():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    conn.autocommit = True
    cur = conn.cursor()

    print("Creating ingestion_queue table...")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS ingestion_queue (
            file_path TEXT PRIMARY KEY,
            status TEXT DEFAULT 'PENDING',
            error_message TEXT,
            attempts INT DEFAULT 0,
            created_at TIMESTAMP DEFAULT NOW(),
            updated_at TIMESTAMP DEFAULT NOW()
        );
    """)

    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_queue_status
        ON ingestion_queue(status);
    """)

    conn.close()
    print("Queue table ready.")

def populate_queue():
    config = get_config()
    conn = psycopg2.connect(config.database.url)
    conn.autocommit = True
    cur = conn.cursor()

    root_dir = os.getcwd()
    files_to_add = []

    print("Scanning workspace for files...")
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Filter directories in place
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS and not d.startswith('.')]

        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in IGNORE_EXTENSIONS:
                continue

            full_path = os.path.join(dirpath, f)

            # Skip if file is too large (fast check)
            try:
                if os.path.getsize(full_path) > 1024 * 1024: # 1MB
                    continue
            except OSError:
                continue

            files_to_add.append((full_path,))

    print(f"Found {len(files_to_add)} candidates.")

    print("Populating database (this handles deduplication)...")
    # Use INSERT ON CONFLICT DO NOTHING to avoid duplicates if run multiple times
    query = """
        INSERT INTO ingestion_queue (file_path)
        VALUES %s
        ON CONFLICT (file_path) DO NOTHING
    """

    # Batch insert
    batch_size = 1000
    total = 0
    for i in tqdm(range(0, len(files_to_add), batch_size)):
        batch = files_to_add[i:i + batch_size]
        psycopg2.extras.execute_values(cur, query, batch)
        total += len(batch)

    print(f"Queue population complete. Total items in manifest: {total}")
    conn.close()

if __name__ == "__main__":
    setup_queue_db()
    populate_queue()
