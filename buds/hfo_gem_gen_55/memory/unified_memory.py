import asyncio
import json
import logging
import sys
import os

# Add workspace root to path to allow imports
# This assumes the file is located at buds/hfo_gem_gen_55/memory/unified_memory.py
# We need to go up 3 levels: memory -> hfo_gem_gen_55 -> buds -> root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from hfo_sdk.stigmergy import StigmergyClient
from buds.hfo_gem_gen_55.memory.lancedb_store import HFOStigmergyMemory

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hfo.unified_memory")

class UnifiedMemorySystem:
    """
    The Unified Memory System for HFO Gen 55.
    Combines NATS JetStream (Hot/Stigmergy) and LanceDB (Cold/Semantic).
    """
    def __init__(self, nats_url="nats://localhost:4225", lancedb_path="buds/hfo_gem_gen_55/memory/lancedb"):
        self.hot = StigmergyClient(nats_url=nats_url)
        # Ensure absolute path for LanceDB to avoid confusion
        abs_db_path = os.path.abspath(lancedb_path)
        self.cold = HFOStigmergyMemory(db_path=abs_db_path)
        self.running = False

    async def start(self):
        """Initialize connections."""
        await self.hot.connect()
        self.running = True
        logger.info("✅ Unified Memory System Started (Hot+Cold)")

    async def stop(self):
        """Close connections."""
        await self.hot.close()
        self.running = False
        logger.info("🛑 Unified Memory System Stopped")

    async def write_hot(self, subject: str, payload: dict):
        """
        Writes to NATS (Hot Memory).
        This is for rapid, ephemeral signaling and coordination.
        """
        ack = await self.hot.publish(subject, payload)
        logger.debug(f"🔥 Hot Write: {subject} (Seq: {ack.seq})")
        return ack

    def write_cold(self, section: str, payload: dict, privilege_level: int = 0):
        """
        Writes to LanceDB (Cold Memory).
        This is for long-term semantic storage and retrieval.
        """
        self.cold.store(section, payload, privilege_level)
        logger.debug(f"🧊 Cold Write: {section}")

    async def query_cold(self, query_text: str, limit: int = 5):
        """Semantic search on Cold Memory."""
        return self.cold.query(query_text=query_text, limit=limit)

    async def run_assimilator(self, subject_pattern: str = "hfo.>", durable_name: str = "hfo_assimilator_main"):
        """
        The 'Cooling' Process: Listens to Hot stream and persists to Cold storage.
        This runs as a continuous loop.
        """
        if not self.hot.js:
            raise ConnectionError("Hot memory not connected")

        logger.info(f"❄️ Starting Assimilator on {subject_pattern}...")

        async def msg_handler(msg):
            try:
                subject = msg.subject
                data = json.loads(msg.data.decode())
                
                # Convert NATS subject to LanceDB section
                # e.g. hfo.agents.swarmlord -> agents.swarmlord
                section = subject.replace("hfo.", "", 1)
                
                logger.info(f"❄️ Assimilating: {subject} -> LanceDB")
                
                # Run blocking DB write in executor to avoid blocking async loop
                loop = asyncio.get_event_loop()
                await loop.run_in_executor(None, self.write_cold, section, data)
                
                await msg.ack()
            except Exception as e:
                logger.error(f"❌ Failed to assimilate message: {e}")
                # Optionally nak, but be careful of poison pills
                # await msg.nak()

        # Create a durable consumer for assimilation
        # We use a queue group to ensure only one assimilator processes each message if we scale up
        await self.hot.js.subscribe(
            subject_pattern, 
            durable=durable_name, 
            cb=msg_handler
        )
        
        # Keep running until stopped
        while self.running:
            await asyncio.sleep(1)

# Example usage
if __name__ == "__main__":
    async def main():
        ums = UnifiedMemorySystem()
        await ums.start()
        
        # Test Hot Write
        await ums.write_hot("hfo.test.unification", {"msg": "Hello Unified World", "timestamp": "now"})
        
        # Give it a moment
        await asyncio.sleep(1)
        
        # In a real scenario, we'd run the assimilator. 
        # For this test, we'll just write cold directly to verify.
        ums.write_cold("test.direct", {"msg": "Direct Cold Write"})
        
        results = await ums.query_cold("Unified World")
        print("\nQuery Results:")
        print(results)
        
        await ums.stop()

    asyncio.run(main())
