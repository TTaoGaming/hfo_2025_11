import asyncio
import json
import logging
import sys
import os
import nats
from nats.js.api import StreamConfig, RetentionPolicy

# Add root to path
sys.path.append(os.getcwd())

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("ResultReader")

async def read_results():
    nc = await nats.connect("nats://localhost:4225")
    js = nc.jetstream()
    
    logger.info("👂 Listening for results on HFO_INGEST...")
    
    # Create a consumer
    psub = await js.pull_subscribe("hfo.ingest.>", "result_reader")
    
    try:
        while True:
            msgs = await psub.fetch(1, timeout=5)
            for msg in msgs:
                data = json.loads(msg.data.decode())
                print("\n" + "="*50)
                print(f"TASK: {data.get('task_id')}")
                print(f"STATUS: {data.get('status')}")
                print("-" * 20)
                print(data.get('result'))
                print("="*50 + "\n")
                await msg.ack()
    except nats.errors.TimeoutError:
        logger.info("No more messages.")
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        await nc.close()

if __name__ == "__main__":
    asyncio.run(read_results())
