import os
import sys
import psycopg2

# Add HiveFleetObsidian to path to use existing config
sys.path.append(os.path.join(os.getcwd(), "HiveFleetObsidian"))

try:
    from hfo_sdk.config import get_config
except ImportError:
    print(
        "Could not import hfo_sdk. Make sure you are running this from the workspace root."
    )
    sys.exit(1)


def setup_database():
    config = get_config()
    db_url = config.database.url

    print("Connecting to database...")
    conn = psycopg2.connect(db_url)
    conn.autocommit = True
    cur = conn.cursor()

    print("Setting up 'knowledge_bank' table for unified storage...")

    # Enable pgvector if not exists
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")

    # Create the unified knowledge table
    # We use a generic structure to hold code, docs, and evolution notes
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS knowledge_bank (
            id SERIAL PRIMARY KEY,
            source_path TEXT NOT NULL,
            content TEXT NOT NULL,
            embedding vector(1536),
            metadata JSONB DEFAULT '{}'::jsonb,
            created_at TIMESTAMP DEFAULT NOW()
        );
    """
    )

    # Index for fast retrieval
    cur.execute(
        """
        CREATE INDEX IF NOT EXISTS knowledge_bank_embedding_idx
        ON knowledge_bank USING ivfflat (embedding vector_cosine_ops)
        WITH (lists = 100);
    """
    )

    # Index for metadata searching (e.g. finding all gen_1 files)
    cur.execute(
        """
        CREATE INDEX IF NOT EXISTS knowledge_bank_metadata_idx
        ON knowledge_bank USING gin (metadata);
    """
    )

    print("Database setup complete. Table 'knowledge_bank' is ready.")
    cur.close()
    conn.close()


if __name__ == "__main__":
    setup_database()
