import duckdb
import json
from datetime import datetime

DB_PATH = "buds/hfo_gem_gen_55/memory/memory-duckdb/hfo_core.duckdb"
JSONL_PATH = "buds/hfo_gem_gen_55/memory/memory-duckdb/hfo_core_mirror.jsonl"


def init_db():
    """Initialize the DuckDB schema for Cold and Refined storage."""
    con = duckdb.connect(DB_PATH)

    # --- COLD STORAGE (The Raw Feed) ---
    # Stores raw signals, file contents, and observations.
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS cold_signals (
            id VARCHAR PRIMARY KEY,
            timestamp TIMESTAMP,
            source VARCHAR, -- e.g., 'file_system', 'nats_stream'
            type VARCHAR,   -- e.g., 'file_content', 'agent_log'
            payload JSON,   -- The raw data
            hash VARCHAR    -- For deduplication
        )
    """
    )

    # --- REFINED STORAGE (The Gem) ---
    # Stores synthesized knowledge, vectors, and relationships.
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS refined_artifacts (
            id VARCHAR PRIMARY KEY,
            cold_id VARCHAR, -- Link back to source
            level INTEGER,   -- Refinement Level (N)
            type VARCHAR,    -- e.g., 'summary', 'vector', 'graph_node'
            content JSON,    -- The refined knowledge
            embedding FLOAT[], -- Vector embedding
            created_at TIMESTAMP
        )
    """
    )

    con.close()
    print(f"✅ DuckDB initialized at {DB_PATH}")


def append_to_jsonl(table_name, data):
    """Mirror a write to the JSONL file for human readability."""
    entry = {"table": table_name, "timestamp": datetime.now().isoformat(), "data": data}
    with open(JSONL_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")


if __name__ == "__main__":
    init_db()
