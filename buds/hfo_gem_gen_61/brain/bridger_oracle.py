import logging
import pandas as pd
import sys
import os
from typing import List, Dict, Any

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_61.memory.lancedb_store import VectorMirror
from buds.hfo_gem_gen_61.brain.assimilator import EmbeddingMotor

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("BridgerOracle")

class BridgerOracle:
    """
    The Bridger Oracle (Subrole).
    The Query Interface for the HFO Memory System.
    Operates under the Bridger (Communicator) Role.
    """
    def __init__(self, lancedb_path: str = "buds/hfo_gem_gen_61/memory/hfo_gen_61_lancedb"):
        self.mirror = VectorMirror(db_path=lancedb_path)
        self.motor = EmbeddingMotor(model_name="nomic-embed-text")

    def ask(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """
        Ask the Oracle a question.
        Returns a list of relevant memory items.
        """
        logger.info(f"🔮 Bridger Oracle received query: '{query}'")
        
        # 1. Embed the query
        try:
            query_vec = self.motor.embed([query])[0]
        except Exception as e:
            logger.error(f"Failed to embed query: {e}")
            return []

        # 2. Search LanceDB
        results_df = self.mirror.search(query_vec, limit=limit)
        
        if results_df.empty:
            logger.info("🔮 Bridger Oracle found nothing.")
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
            
        logger.info(f"🔮 Bridger Oracle found {len(answers)} answers.")
        return answers

if __name__ == "__main__":
    # Simple CLI test
    import sys
    oracle = BridgerOracle()
    
    if len(sys.argv) > 1:
        q = sys.argv[1]
        results = oracle.ask(q)
        for i, res in enumerate(results):
            print(f"\n--- Result {i+1} (Score: {res['score']:.4f}) ---")
            print(f"Source: {res['source']}")
            print(f"Content: {res['text'][:500]}...")
    else:
        while True:
            try:
                q = input("\n🔮 Ask the Bridger Oracle (or 'exit'): ")
                if q.lower() == 'exit':
                    break
                results = oracle.ask(q)
                for i, res in enumerate(results):
                    print(f"\n--- Result {i+1} (Score: {res['score']:.4f}) ---")
                    print(f"Source: {res['source']}")
                    print(f"Content: {res['text'][:500]}...")
            except KeyboardInterrupt:
                break
            print(f"Source: {res['source']}")
            print(f"Text: {res['text'][:200]}...")
