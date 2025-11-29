import sys
import os
import logging
from typing import Dict, Any

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.blood.schema import MemoryItem
from buds.hfo_gem_gen_60.memory.database import IronLedger

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("TheScribe")

class Scribe:
    """
    The Scribe (Gatekeeper).
    The ONLY entity allowed to write to the Iron Ledger.
    It accepts raw data, validates it against the Schema, and commits it.
    """
    def __init__(self):
        self.ledger = IronLedger(db_path="buds/hfo_gem_gen_60/memory/hfo_gen_60_memory.db")

    def ingest(self, raw_data: Dict[str, Any]):
        """
        The Public Interface.
        Agents call this. They do NOT touch the DB.
        """
        try:
            # 1. Validate (Pydantic)
            # This will raise ValidationError if the AI sends "slop"
            item = MemoryItem(**raw_data)
            
            # 2. Compute Integrity Hash
            item.compute_hash()
            
            # 3. Write to Ledger
            row_id = self.ledger.insert(item)
            
            return {"status": "success", "id": row_id, "hash": item.content_hash}
            
        except Exception as e:
            logger.error(f"🛑 REJECTED: {e}")
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # Simple Test
    scribe = Scribe()
    test_data = {
        "source_path": "test/doc.md",
        "content": "# Hello World\nThis is a test.",
        "generation": 58,
        "category": "test",
        "tags": ["sanity_check"]
    }
    print(scribe.ingest(test_data))
