import asyncio
import json
import logging
import sys
import os
import signal
from nats.errors import TimeoutError

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.blood.schema import MemoryItem
from buds.hfo_gem_gen_60.brain.prey_swarm import PreySwarm
from buds.hfo_gem_gen_60.nerves.stigmergy_client import StigmergyClient

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("IngestWorker")

class IngestWorker:
    """
    The Digestive Enzyme.
    Consumes raw memory items from NATS and processes them via PreySwarm.
    """
    def __init__(self):
        self.swarm = PreySwarm()
        self.stigmergy = StigmergyClient()
        self.running = True

    async def start(self):
        logger.info("🦠 Ingest Worker Starting...")
        await self.stigmergy.connect()
        
        # Create a Pull Subscription
        # Durable consumer ensures we don't lose work if we crash
        # Try to delete existing consumer to clear 'filtered consumer not unique' error
        try:
            await self.stigmergy.js.delete_consumer("HFO_INGEST", "ingest_worker_1")
            logger.info("🗑️ Deleted existing consumer 'ingest_worker_1'")
        except Exception:
            pass

        psub = await self.stigmergy.js.pull_subscribe("hfo.ingest.raw", durable="ingest_worker_1")
        
        logger.info("👂 Listening for Ingest Tasks (Consumer: ingest_worker_1)...")
        
        while self.running:
            try:
                # Fetch 1 message at a time (to avoid overloading the swarm)
                msgs = await psub.fetch(1, timeout=5)
                for msg in msgs:
                    await self.process_message(msg)
            except TimeoutError:
                # No messages, just loop
                continue
            except Exception as e:
                logger.error(f"❌ Worker Loop Error: {e}")
                await asyncio.sleep(1)

        await self.stigmergy.close()
        logger.info("🛑 Worker Stopped.")

    async def process_message(self, msg):
        try:
            data = msg.data.decode()
            item_dict = json.loads(data)
            item = MemoryItem(**item_dict)
            
            logger.info(f"🍽️  Consuming: {item.source_path}")
            
            # Process with Swarm
            await self.swarm.process_item(item)
            
            # Ack the message (Work Complete)
            await msg.ack()
            logger.info(f"✅ Processed & Acked: {item.source_path}")
            
        except Exception as e:
            logger.error(f"❌ Failed to process message: {e}")
            # Nak to retry later? Or Term to kill it?
            # For now, let's Nak with delay
            await msg.nak(delay=10)

    def stop(self):
        self.running = False

async def main():
    worker = IngestWorker()
    
    # Handle Signals
    def signal_handler():
        logger.info("⚠️  Signal Received. Stopping...")
        worker.stop()

    loop = asyncio.get_running_loop()
    # loop.add_signal_handler(signal.SIGINT, signal_handler)
    # loop.add_signal_handler(signal.SIGTERM, signal_handler)
    
    await worker.start()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
