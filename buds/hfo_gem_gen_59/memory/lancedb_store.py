import lancedb
import pyarrow as pa
from pathlib import Path
from typing import List, Dict, Any
import logging

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("VectorMirror")

class VectorMirror:
    """
    The Vector Mirror (LanceDB).
    Stores semantic embeddings of the Iron Ledger.
    """
    def __init__(self, db_path: str = "memory/lancedb"):
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.db = lancedb.connect(self.db_path)
        self._init_table()

    def _init_table(self):
        """Initialize the vector table."""
        # We'll use a dynamic schema or a fixed one. 
        # For now, let's assume a fixed schema for HFO.
        # 1536 dimensions for text-embedding-3-small, or 384 for all-minilm, 768 for nomic
        # LanceDB can infer schema from data.
        pass

    def add_texts(self, texts: List[str], metadatas: List[Dict[str, Any]], embeddings: List[List[float]], table_name: str = "hfo_vectors"):
        """
        Add vectors to the database.
        """
        if not texts:
            return

        data = []
        for t, m, e in zip(texts, metadatas, embeddings):
            row = {
                "vector": e,
                "text": t,
                **m
            }
            data.append(row)

        if table_name in self.db.table_names():
            tbl = self.db.open_table(table_name)
            tbl.add(data)
        else:
            # Table doesn't exist, create it
            self.db.create_table(table_name, data)
            logger.info(f"Created new table: {table_name}")

    def search(self, query_vector: List[float], limit: int = 5, table_name: str = "hfo_vectors"):
        """
        Search for similar vectors.
        """
        if table_name not in self.db.table_names():
            logger.warning(f"Table {table_name} not found.")
            import pandas as pd
            return pd.DataFrame()

        tbl = self.db.open_table(table_name)
        return tbl.search(query_vector).limit(limit).to_pandas()
