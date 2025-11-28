import asyncio
import os
import json
import uuid
import hashlib
from datetime import datetime
import duckdb

# Configuration
REPO_ROOT = "."
DB_PATH = "buds/hfo_gem_gen_55/memory/memory-duckdb/hfo_core.duckdb"
JSONL_PATH = "buds/hfo_gem_gen_55/memory/memory-duckdb/hfo_core_mirror.jsonl"
IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    "node_modules",
    "buds",
}  # Don't ingest the gem itself recursively


class Assimilator:
    def __init__(self):
        self.con = duckdb.connect(DB_PATH)

    def ingest_file(self, file_path: str):
        """Reads a file and stores it as a COLD signal."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            # Generate ID and Hash
            file_hash = hashlib.sha256(content.encode()).hexdigest()
            signal_id = str(uuid.uuid4())

            payload = {
                "path": file_path,
                "content": content,
                "size": len(content),
                "extension": os.path.splitext(file_path)[1],
            }

            # Write to DuckDB (Cold)
            self.con.execute(
                """
                INSERT INTO cold_signals (id, timestamp, source, type, payload, hash)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    signal_id,
                    datetime.now(),
                    "repo_scan",
                    "file_content",
                    json.dumps(payload),
                    file_hash,
                ),
            )

            # Mirror to JSONL
            self._mirror_jsonl(
                "cold_signals",
                {
                    "id": signal_id,
                    "path": file_path,
                    "type": "file_content",
                    "hash": file_hash,
                },
            )

            return True
        except Exception as e:
            print(f"❌ Failed to ingest {file_path}: {e}")
            return False

    def _mirror_jsonl(self, table, data):
        entry = {"table": table, "timestamp": datetime.now().isoformat(), "data": data}
        with open(JSONL_PATH, "a") as f:
            f.write(json.dumps(entry) + "\n")


async def swarm_scan():
    """Simulates the Swarm scanning the repo."""
    assimilator = Assimilator()
    count = 0

    print("🐜 Swarm activated. Scanning repository...")

    for root, dirs, files in os.walk(REPO_ROOT):
        # Filter ignored directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            file_path = os.path.join(root, file)
            # Skip the DB itself
            if "hfo_core.duckdb" in file_path:
                continue

            if assimilator.ingest_file(file_path):
                count += 1
                if count % 10 == 0:
                    print(f"✅ Ingested {count} files...")

    print(f"🏁 Mission Complete. Ingested {count} files into Cold Storage.")


if __name__ == "__main__":
    asyncio.run(swarm_scan())
