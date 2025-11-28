import time
import logging
import requests
import json
from typing import List
from ..memory.database import IronLedger
from ..memory.lancedb_store import VectorMirror

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Assimilator")

class EmbeddingMotor:
    """
    Wraps the embedding model (Ollama).
    """
    def __init__(self, model_name: str = "nomic-embed-text", base_url: str = "http://localhost:11434"):
        self.model_name = model_name
        self.base_url = base_url
        logger.info(f"Connecting to Ollama Embedding Model: {model_name}...")
        # Simple check
        try:
            requests.get(f"{self.base_url}/api/tags")
            logger.info("Ollama Connected.")
        except Exception as e:
            logger.error(f"Could not connect to Ollama: {e}")

    def embed(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for text in texts:
            try:
                response = requests.post(
                    f"{self.base_url}/api/embeddings",
                    json={"model": self.model_name, "prompt": text}
                )
                if response.status_code == 200:
                    embeddings.append(response.json()['embedding'])
                else:
                    logger.error(f"Ollama Error: {response.text}")
                    # Append empty or zero vector? Better to skip or fail.
                    # For now, let's raise to stop the sync.
                    raise Exception(f"Ollama Error: {response.text}")
            except Exception as e:
                logger.error(f"Embedding Failed: {e}")
                raise
        return embeddings

class Assimilator:
    """
    The Synapse Link.
    Syncs IronLedger (SQLite) to VectorMirror (LanceDB).
    """
    def __init__(self, db_path: str = "buds/hfo_gem_gen_59/memory/hfo_gen_59_memory.db", lancedb_path: str = "buds/hfo_gem_gen_59/memory/hfo_gen_59_lancedb"):
        self.ledger = IronLedger(db_path=db_path)
        self.mirror = VectorMirror(db_path=lancedb_path)
        self.motor = EmbeddingMotor(model_name="nomic-embed-text")

    def run_sync_cycle(self, batch_size: int = 10):
        """
        Runs one cycle of synchronization.
        """
        logger.info("Checking for unvectorized memories...")
        items = self.ledger.get_unvectorized_items(limit=batch_size)

        if not items:
            logger.info("No new memories to assimilate.")
            return

        logger.info(f"Found {len(items)} items. Assimilating...")

        ids = []
        texts = []
        metadatas = []

        for item_id, content, source_path, category in items:
            ids.append(item_id)
            texts.append(content)
            metadatas.append({
                "source_path": source_path,
                "category": category,
                "memory_id": item_id
            })

        # Generate Embeddings
        try:
            embeddings = self.motor.embed(texts)
        except Exception as e:
            logger.error(f"Aborting sync cycle due to embedding error: {e}")
            return

        # Store in LanceDB
        self.mirror.add_texts(texts, metadatas, embeddings)

        # Mark as Vectorized
        for item_id in ids:
            self.ledger.mark_vectorized(item_id)

        logger.info(f"Successfully assimilated {len(items)} items.")

if __name__ == "__main__":
    assimilator = Assimilator()
    # Run a few cycles to catch up
    while True:
        assimilator.run_sync_cycle()
        time.sleep(1) # Small pause between batches
        # Break if no more items? For now, let's just run it once or loop until empty.
        if not assimilator.ledger.get_unvectorized_items(limit=1):
            break
    logger.info("Assimilation Complete.")
