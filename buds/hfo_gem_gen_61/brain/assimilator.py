import time
import logging
import requests
import json
import sys
import os
import asyncio
import argparse
from typing import List

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_61.nerves.stigmergy_client import StigmergyClient
from buds.hfo_gem_gen_61.memory.database import IronLedger
from buds.hfo_gem_gen_61.memory.lancedb_store import VectorMirror

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
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
        total = len(texts)
        for i, text in enumerate(texts):
            if i % 5 == 0:
                logger.info(f"Embedding chunk {i+1}/{total}...")
            try:
                response = requests.post(
                    f"{self.base_url}/api/embeddings",
                    json={"model": self.model_name, "prompt": text}
                )
                if response.status_code == 200:
                    embeddings.append(response.json()['embedding'])
                else:
                    logger.error(f"Ollama Error: {response.text}")
                    raise Exception(f"Ollama Error: {response.text}")
            except Exception as e:
                logger.error(f"Embedding Failed: {e}")
                raise
        return embeddings

class Chunker:
    """
    Splits text into manageable chunks for embedding.
    """
    def __init__(self, chunk_size: int = 1000, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str) -> List[str]:
        if not text:
            return []
        
        chunks = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunk_size - self.overlap
        
        return chunks

class Assimilator:
    """
    The Synapse Link.
    Syncs IronLedger (SQLite) to VectorMirror (LanceDB).
    """
    def __init__(self, db_path: str = "buds/hfo_gem_gen_61/memory/hfo_gen_61_memory.db", lancedb_path: str = "buds/hfo_gem_gen_61/memory/hfo_gen_61_lancedb"):
        self.ledger = IronLedger(db_path=db_path)
        self.mirror = VectorMirror(db_path=lancedb_path)
        self.motor = EmbeddingMotor(model_name="nomic-embed-text")
        self.chunker = Chunker(chunk_size=1000, overlap=100)

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

        for item_id, content, source_path, category in items:
            logger.info(f"Processing Item ID {item_id} ({source_path})...")
            
            # CHUNK THE CONTENT
            chunks = self.chunker.chunk_text(content)
            if not chunks:
                logger.warning(f"No chunks for Item {item_id}. Marking done.")
                self.ledger.mark_vectorized(item_id)
                continue

            metadatas = []
            for i, chunk in enumerate(chunks):
                metadatas.append({
                    "source_path": source_path,
                    "category": category,
                    "memory_id": item_id,
                    "chunk_index": i,
                    "total_chunks": len(chunks)
                })

            # Generate Embeddings for this item
            try:
                embeddings = self.motor.embed(chunks)
                # Store in LanceDB
                self.mirror.add_texts(chunks, metadatas, embeddings)
                # Mark as Vectorized
                self.ledger.mark_vectorized(item_id)
                logger.info(f"✅ Item {item_id} assimilated ({len(chunks)} chunks).")
            except Exception as e:
                logger.error(f"❌ Failed to assimilate Item {item_id}: {e}")
                # Continue to next item instead of aborting everything
                continue

        logger.info("Batch complete.")

    async def listen_to_heartbeat(self):
        """
        Listens for the 1-Minute Pulse to trigger assimilation.
        """
        self.stigmergy = StigmergyClient()
        await self.stigmergy.connect()
        
        async def callback(msg):
            try:
                data = json.loads(msg.data.decode())
                logger.info(f"💓 Pulse Received: {data.get('chant_line', 'Unknown')}")
                # Run sync cycle in a thread to not block the async loop
                loop = asyncio.get_running_loop()
                await loop.run_in_executor(None, self.run_sync_cycle, 10)
            except Exception as e:
                logger.error(f"Error processing pulse: {e}")

        await self.stigmergy.subscribe("hfo.pulse.1min", callback)
        logger.info("👂 Listening for hfo.pulse.1min...")
        
        # Keep alive
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HFO Assimilator")
    parser.add_argument("--daemon", action="store_true", help="Run in daemon mode listening to heartbeat")
    parser.add_argument("--batch-size", type=int, default=10, help="Batch size for assimilation")
    args = parser.parse_args()

    assimilator = Assimilator()
    
    if args.daemon:
        try:
            asyncio.run(assimilator.listen_to_heartbeat())
        except KeyboardInterrupt:
            logger.info("Assimilator Stopped.")
    else:
        # Run a few cycles to catch up
        while True:
            assimilator.run_sync_cycle(batch_size=args.batch_size)
            time.sleep(1) # Small pause between batches
            if not assimilator.ledger.get_unvectorized_items(limit=1):
                break
        logger.info("Assimilation Complete.")
