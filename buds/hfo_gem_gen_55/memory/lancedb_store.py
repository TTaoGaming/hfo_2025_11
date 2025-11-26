import lancedb
import pyarrow as pa
import time
import json
import os
from typing import Optional


class HFOStigmergyMemory:
    def __init__(self, db_path="memory/lancedb"):
        # Ensure the directory exists
        os.makedirs(db_path, exist_ok=True)
        self.db_path = os.path.abspath(db_path)
        self.db = lancedb.connect(db_path)
        self.table_name = "hfo_stigmergy"
        self.setup_table()

    def setup_table(self):
        schema = pa.schema(
            [
                pa.field("id", pa.string()),
                pa.field("section", pa.string()),
                pa.field("payload", pa.string()),
                pa.field("timestamp", pa.float64()),
                # Vector field is optional for now, but good to have for future
                # pa.field("vector", pa.list_(pa.float32(), 1536))
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

    def store(self, section: str, payload: dict):
        data = [
            {
                "id": payload.get("id", str(time.time())),
                "section": section,
                "payload": json.dumps(payload),
                "timestamp": time.time(),
            }
        ]
        self.table.add(data)
        print(f"Stored in LanceDB: {section} -> {payload}")

    def query(self, section: Optional[str] = None, limit: int = 10):
        query = self.table.search()
        if section:
            query = query.where(f"section = '{section}'")
        return query.limit(limit).to_pandas()


# Example usage
if __name__ == "__main__":
    mem = HFOStigmergyMemory()
    mem.store("ontos", {"id": "test-1", "msg": "I am"})
    print(mem.query("ontos"))
