"""
# ==================================================================
# 🧪 VENOM: Live Heartbeat Verification
# ==================================================================
# Purpose: Connect to the LIVE NATS JetStream and verify that
#          the background agent is successfully publishing heartbeats.
# ==================================================================
"""

import sys
import os
import asyncio
import logging
import json

# Add project root to sys.path
sys.path.append(os.path.abspath("."))

from body.hfo_sdk.stigmergy import StigmergyClient

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("VenomLiveVerify")

import uuid
from nats.js.api import ConsumerConfig, DeliverPolicy


async def verify_live_stream():
    logger.info("🐍 Venom: Connecting to LIVE Stigmergy Layer...")

    client = StigmergyClient()
    try:
        await client.connect()
    except Exception as e:
        logger.error(f"❌ Failed to connect: {e}")
        return

    subject = "hfo.heartbeat.>"
    logger.info(f"🔍 Fetching history for subject: {subject}")

    # Manually create a consumer to ensure we get ALL history
    js = client.js
    unique_consumer = f"venom_verifier_{uuid.uuid4().hex[:8]}"

    try:
        sub = await js.pull_subscribe(
            subject,
            durable=unique_consumer,
            config=ConsumerConfig(deliver_policy=DeliverPolicy.ALL),
        )

        msgs = []
        try:
            fetched = await sub.fetch(10, timeout=2)
            for msg in fetched:
                msgs.append(json.loads(msg.data.decode()))
                await msg.ack()
        except Exception:
            pass  # Timeout

        history = msgs

        if not history:
            logger.warning("⚠️ No heartbeats found in the stream yet.")
        else:
            logger.info(f"✅ Found {len(history)} heartbeats in the stream!")
            for i, msg in enumerate(history):
                # Try to parse the content
                try:
                    content = msg.get("content", "No Content")
                    phase = msg.get("phase", "Unknown")
                    delta = msg.get("delta_seconds", -1.0)
                    mantra_hash = msg.get("mantra_hash", "Missing")

                    logger.info(f"\n--- Signal {i+1} ---")
                    logger.info(f"   Phase: {phase}")
                    logger.info(f"   Delta: {delta:.4f}s")
                    logger.info(f"   Hash:  {mantra_hash[:8]}...")
                    logger.info(f"   Content: {content[:60]}...")
                except Exception as e:
                    logger.error(f"Error parsing message: {e}")

    except Exception as e:
        logger.error(f"Subscription error: {e}")

    await client.close()


if __name__ == "__main__":
    asyncio.run(verify_live_stream())
