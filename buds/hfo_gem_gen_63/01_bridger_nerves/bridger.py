"""
---
holon:
  id: hfo-858f6979
  type: unknown
  file: bridger.py
  status: active
---
"""
import logging
import requests
import lancedb
import os
import sys
from typing import List, Dict, Any

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Bridger")

class Bridger:
    """
    The Bridger (Gen 63).
    Connects the Intent (Query) to the Memory (LanceDB).
    Uses Ollama for local embeddings (nomic-embed-text).
    """
    def __init__(self):
        self.db = lancedb.connect(settings.LANCEDB_PATH)
        self.table_name = "memories"
        self.ollama_url = "http://localhost:11434/api/embeddings"
        self.model = "nomic-embed-text:latest"
        
        # Ensure table exists
        if self.table_name not in self.db.table_names():
            # Create with dummy data to define schema
            # Schema: vector (1536 or 768 depending on model), text, source, category
            # nomic-embed-text is 768 dimensions
            try:
                dummy_vec = self._get_embedding("init")
                data = [{"vector": dummy_vec, "text": "init", "source": "system", "category": "system"}]
                self.db.create_table(self.table_name, data)
                logger.info(f"Created table '{self.table_name}'")
            except Exception as e:
                logger.error(f"Failed to init table: {e}")

    def _get_embedding(self, text: str) -> List[float]:
        """Get embedding from Ollama."""
        try:
            response = requests.post(
                self.ollama_url,
                json={"model": self.model, "prompt": text}
            )
            response.raise_for_status()
            return response.json()["embedding"]
        except Exception as e:
            logger.error(f"Embedding failed: {e}")
            # Return zero vector as fallback to prevent crash, but log error
            return [0.0] * 768 

    def ask(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Ask the Bridger a question.
        Returns relevant memory items.
        """
        logger.info(f"🔮 Bridger received query: '{query}'")
        
        query_vec = self._get_embedding(query)
        if not query_vec or len(query_vec) < 10: # Basic check
            return []

        try:
            tbl = self.db.open_table(self.table_name)
            results = tbl.search(query_vec).limit(limit).to_pandas()
            
            if results.empty:
                logger.info("🔮 Bridger found nothing.")
                return []

            answers = []
            for _, row in results.iterrows():
                answers.append({
                    "text": row['text'],
                    "source": row.get('source', 'unknown'),
                    "category": row.get('category', 'unknown'),
                    "score": 1.0 - row.get('_distance', 0.0)
                })
            
            logger.info(f"🔮 Bridger found {len(answers)} answers.")
            return answers
            
        except Exception as e:
            logger.error(f"Search failed: {e}")
            return []

    def memorize(self, text: str, source: str = "user", category: str = "note"):
        """
        Store a memory.
        """
        vec = self._get_embedding(text)
        data = [{"vector": vec, "text": text, "source": source, "category": category}]
        
        try:
            tbl = self.db.open_table(self.table_name)
            tbl.add(data)
            logger.info(f"💾 Memorized: {text[:50]}...")
        except Exception as e:
            logger.error(f"Memorization failed: {e}")

if __name__ == "__main__":
    bridger = Bridger()
    
    # Test Memorize
    bridger.memorize("The Obsidian Spider is the emergent consciousness of the swarm.", source="manifesto", category="definition")
    
    # Test Ask
    results = bridger.ask("What is the Obsidian Spider?")
    for res in results:
        print(f"\n--- {res['score']:.4f} ---")
        print(res['text'])
