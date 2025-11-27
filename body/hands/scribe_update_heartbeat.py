import asyncio
import logging
import time
import lancedb
from lancedb.pydantic import LanceModel, Vector
from pydantic import Field

# --- Configuration ---
LANCE_DB_PATH = "memory/lancedb"
TABLE_NAME = "hfo_memory"

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("MemoryScribe")

# --- LanceDB Schema (Must match existing) ---
class MemoryGem(LanceModel):
    id: str = Field(..., description="Unique ID (UUID)")
    content: str = Field(..., description="The text content of the memory")
    vector: Vector(270) = Field(..., description="Embedding Vector (Mock 270 dim for gemma3:270m)")
    agent_id: str = Field(..., description="Who created this memory")
    timestamp: float = Field(..., description="Unix timestamp")
    tags: str = Field(..., description="Comma-separated tags")

class MemoryScribe:
    def __init__(self):
        self.db = lancedb.connect(LANCE_DB_PATH)
        self.table = self._get_or_create_table()

    def _get_or_create_table(self):
        try:
            return self.db.create_table(TABLE_NAME, schema=MemoryGem, exist_ok=True)
        except Exception as e:
            logger.error(f"Failed to create table: {e}")
            return None

    def ingest_note(self, note: str, agent_id: str = "Swarmlord"):
        """Ingests a note into the Long-Term Memory."""
        mock_vector = [0.1] * 270 
        
        gem = MemoryGem(
            id=f"mem_{int(time.time())}",
            content=note,
            vector=mock_vector,
            agent_id=agent_id,
            timestamp=time.time(),
            tags="guard,heartbeat,hfo,update"
        )
        
        self.table.add([gem])
        logger.info(f"💎 Ingested Note: {note[:50]}...")

async def main():
    scribe = MemoryScribe()
    
    note = """
    SYSTEM UPDATE (Nov 26, 2025):
    Implemented 'Hive Guard' for Heartbeat Integrity.
    - Script: body/hands/guard_heartbeat.py
    - Checks: Mantra Hash, 8 Pillars (Ontos-Techne), Time Regression.
    - Status: Active & Monitoring 'hfo.heartbeat.>'.
    - Makefile: Added 'make heartbeat' and 'make guard-heartbeat'.
    The Octarchy is now monitored for structural and temporal integrity.
    """
    
    scribe.ingest_note(note)
    logger.info("✅ Guard Note Saved to LanceDB.")

if __name__ == "__main__":
    asyncio.run(main())
