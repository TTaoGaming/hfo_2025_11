"""
---
holon:
  id: hfo-c29a352b
  type: unknown
  file: stigmergy_loop.py
  status: active
---
"""
import asyncio
import logging
import sys
import os

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings
from src.adapters.nats_adapter import NatsAdapter
from src.adapters.fs_adapter import LocalFileSystemAdapter

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("StigmergyLoop")

async def run_loop():
    """
    The Hello World Stigmergic Loop.
    1. Navigator (Publisher) -> Sends Intent.
    2. Shaper (Worker) -> Receives Intent, Acts (Writes File), Reports.
    3. Navigator (Publisher) -> Receives Report, Exits.
    """
    
    # 1. Initialize Ports
    bus = NatsAdapter(settings.NATS_URL)
    fs = LocalFileSystemAdapter(base_path="buds/hfo_gem_gen_63/sandbox")
    
    await bus.connect()
    
    # Shared State for the Test
    loop_complete = asyncio.Future()

    # --- The Shaper (Worker) ---
    async def shaper_callback(msg: dict):
        if msg.get("type") == "INTENT":
            logger.info(f"🛠️ Shaper received intent: {msg['payload']}")
            path = msg['payload']['path']
            content = msg['payload']['content']
            
            # Act
            await fs.write_file(path, content)
            
            # Report
            await bus.publish("hfo.gen63.report", {
                "type": "REPORT",
                "status": "SUCCESS",
                "file": path
            })

    # --- The Navigator (Observer) ---
    async def navigator_callback(msg: dict):
        if msg.get("type") == "REPORT":
            logger.info(f"🧭 Navigator received report: {msg}")
            if msg['status'] == "SUCCESS":
                loop_complete.set_result(True)

    # Subscribe
    await bus.subscribe("hfo.gen63.intent", shaper_callback)
    await bus.subscribe("hfo.gen63.report", navigator_callback)
    
    # --- Trigger the Loop ---
    logger.info("🚀 Triggering Stigmergic Loop...")
    await bus.publish("hfo.gen63.intent", {
        "type": "INTENT",
        "payload": {
            "path": "hello_stigmergy.txt",
            "content": "The Swarm is One. The Loop is Closed."
        }
    })
    
    # Wait for completion
    try:
        await asyncio.wait_for(loop_complete, timeout=5.0)
        logger.info("✅ Stigmergic Loop Completed Successfully.")
    except asyncio.TimeoutError:
        logger.error("❌ Stigmergic Loop Timed Out.")
    
    await bus.close()

if __name__ == "__main__":
    asyncio.run(run_loop())
