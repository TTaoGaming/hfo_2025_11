import os

# Fix for OMP Error: Must be set before importing libraries that use OpenMP
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

from sentence_transformers import SentenceTransformer
import lancedb
import pyarrow as pa
import time
import json
from typing import Optional


class HFOStigmergyMemory:
    def __init__(self, db_path="memory/lancedb", embedding_model="all-MiniLM-L6-v2"):
        # Ensure the directory exists
        os.makedirs(db_path, exist_ok=True)
        self.db_path = os.path.abspath(db_path)
        self.db = lancedb.connect(db_path)
        self.table_name = "hfo_stigmergy"

        # Initialize embedding model
        print(f"Loading embedding model: {embedding_model}...")
        self.encoder = SentenceTransformer(embedding_model)
        print("Model loaded.")

        self.setup_table()

    def setup_table(self):
        schema = pa.schema(
            [
                pa.field("id", pa.string()),
                pa.field("section", pa.string()),
                pa.field("payload", pa.string()),
                pa.field("timestamp", pa.float64()),
                pa.field("privilege_level", pa.int32()),  # 0=Public/Agent, 8=Overmind
                # 384 dimensions for all-MiniLM-L6-v2
                pa.field("vector", pa.list_(pa.float32(), 384)),
            ]
        )

        try:
            self.table = self.db.create_table(
                self.table_name, schema=schema, exist_ok=True
            )
            print(f"Table {self.table_name} ready.")
        except Exception as e:
            print(f"Error creating table: {e}")
            self.table = self.db.open_table(self.table_name)

    def store(self, section: str, payload: dict, privilege_level: int = 0):
        # Generate embedding from the payload content
        # We'll serialize the whole payload to text for embedding
        text_to_embed = json.dumps(payload)
        vector = self.encoder.encode(text_to_embed).tolist()

        data = [
            {
                "id": payload.get("id", str(time.time())),
                "section": section,
                "payload": text_to_embed,
                "timestamp": time.time(),
                "privilege_level": privilege_level,
                "vector": vector,
            }
        ]
        self.table.add(data)
        print(f"Stored in LanceDB: {section} -> {payload} (Lvl {privilege_level})")

    def query(
        self,
        section: Optional[str] = None,
        limit: int = 10,
        query_text: Optional[str] = None,
        min_privilege: int = 0,
    ):
        query = self.table.search()

        if query_text:
            # Semantic search
            query_vector = self.encoder.encode(query_text).tolist()
            query = self.table.search(query_vector)

        if section:
            query = query.where(f"section = '{section}'")

        # Filter by privilege (Agents can only see up to their clearance, but here we filter *out* lower levels if needed?
        # Usually permissions mean "Show me everything I have access to".
        # If I am Lvl 0, I can see Lvl 0. If I am Lvl 8, I can see Lvl 0-8.
        # For now, let's just return the privilege_level column so the caller can filter.

        return query.limit(limit).to_pandas()


# Example usage
if __name__ == "__main__":
    mem = HFOStigmergyMemory()
    mem.store("ontos", {"id": "test-1", "msg": "I am"})
    print(mem.query("ontos"))
