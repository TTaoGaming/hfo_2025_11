"""
# ==================================================================
# 🧪 VENOM: Live Monitor (Polling)
# ==================================================================
# Purpose: Poll the NATS stream every 2 seconds to show the
#          heartbeat intervals in real-time.
# ==================================================================
"""

import sys
import os
import asyncio
import logging
import json
import time
from nats.js.api import ConsumerConfig, DeliverPolicy

# Add project root to sys.path
sys.path.append(os.path.abspath("."))

from body.hfo_sdk.stigmergy import StigmergyClient

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("VenomMonitor")

async def monitor_stream():
    logger.info("🐍 Venom: Monitoring Heartbeat Stream (Ctrl+C to stop)...")
    
    client = StigmergyClient()
    try:
        await client.connect()
    except Exception as e:
        logger.error(f"❌ Failed to connect: {e}")
        return

    subject = "hfo.heartbeat.>"
    js = client.js
    
    # Use a durable consumer to track what we've seen
    # But for monitoring, we just want "new" stuff or "last N"
    # Let's just fetch the last message repeatedly and check if it's new
    
    last_seen_id = None
    
    while True:
        try:
            # Fetch last 1 message
            sub = await js.pull_subscribe(
                subject, 
                durable="venom_monitor_last",
                config=ConsumerConfig(
                    deliver_policy=DeliverPolicy.LAST
                )
            )
            
            msgs = []
            try:
                fetched = await sub.fetch(1, timeout=1)
                for msg in fetched:
                    msgs.append(json.loads(msg.data.decode()))
                    await msg.ack()
            except Exception:
                pass

            if msgs:
                msg = msgs[0]
                msg_id = msg.get("id")
                
                if msg_id != last_seen_id:
                    last_seen_id = msg_id
                    
                    phase = msg.get("phase", "Unknown")
                    delta = msg.get("delta_seconds", -1.0)
                    timestamp = msg.get("timestamp", "")
                    
                    logger.info(f"💓 [{timestamp}] Phase: {phase} | Delta: {delta:.2f}s")
            
            await asyncio.sleep(1)
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"Monitor error: {e}")
            await asyncio.sleep(1)

    await client.close()

if __name__ == "__main__":
    asyncio.run(monitor_stream())
