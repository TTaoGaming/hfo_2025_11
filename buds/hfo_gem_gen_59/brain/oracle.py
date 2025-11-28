import logging
import pandas as pd
from typing import List, Dict, Any
from ..memory.lancedb_store import VectorMirror
from ..brain.assimilator import EmbeddingMotor

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Oracle")

class Oracle:
    """
    The Oracle.
    The Query Interface for the HFO Memory System.
    """
    def __init__(self, lancedb_path: str = "buds/hfo_gem_gen_59/memory/hfo_gen_59_lancedb"):
        self.mirror = VectorMirror(db_path=lancedb_path)
        self.motor = EmbeddingMotor(model_name="nomic-embed-text")

    def ask(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Ask the Oracle a question.
        Returns a list of relevant memory items.
        """
        logger.info(f"🔮 Oracle received query: '{query}'")
        
        # 1. Embed the query
        try:
            query_vec = self.motor.embed([query])[0]
        except Exception as e:
            logger.error(f"Failed to embed query: {e}")
            return []

        # 2. Search LanceDB
        results_df = self.mirror.search(query_vec, limit=limit)
        
        if results_df.empty:
            logger.info("🔮 Oracle found nothing.")
            return []

        # 3. Format results
        answers = []
        for _, row in results_df.iterrows():
            answers.append({
                "text": row['text'],
                "source": row.get('source_path', 'unknown'),
                "category": row.get('category', 'unknown'),
                "score": 1.0 - row.get('_distance', 0.0) # LanceDB returns distance, so 1-distance is similarity (roughly)
            })
            
        logger.info(f"🔮 Oracle found {len(answers)} answers.")
        return answers

if __name__ == "__main__":
    # Simple CLI test
    oracle = Oracle()
    while True:
        q = input("\n🔮 Ask the Oracle (or 'exit'): ")
        if q.lower() == 'exit':
            break
        results = oracle.ask(q)
        for i, res in enumerate(results):
            print(f"\n--- Result {i+1} (Score: {res['score']:.4f}) ---")
            print(f"Source: {res['source']}")
            print(f"Text: {res['text'][:200]}...")
