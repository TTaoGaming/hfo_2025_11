"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: ac462f3a-cac2-4aa2-9654-f92a318a38c1
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.608761+00:00'
  topos:
    address: hfo_sdk/stigmergy.py
    links: []
  telos:
    viral_factor: 0.0
    meme: stigmergy.py
"""

import json
import logging
import os
from typing import Any, Dict
import nats
from nats.js.api import StreamConfig, RetentionPolicy

logger = logging.getLogger("hfo.stigmergy")


class StigmergyClient:
    """
    Handles communication with the NATS JetStream 'Stigmergy Layer'.
    """

    def __init__(self, nats_url: str = "nats://localhost:4222"):
        self.nats_url = os.getenv("NATS_URL", nats_url)
        self.nc = None
        self.js = None
        self.stream_name = "HIVE_MIND"

    async def connect(self):
        """Connects to NATS and ensures the stream exists."""
        try:
            self.nc = await nats.connect(self.nats_url)
            self.js = self.nc.jetstream()

            # Check if stream exists, if not create it, if yes update it
            try:
                await self.js.stream_info(self.stream_name)
                logger.info(
                    f"   Stream '{self.stream_name}' exists. Updating config..."
                )
                await self.js.update_stream(
                    name=self.stream_name,
                    subjects=["hfo.>"],
                    config=StreamConfig(
                        retention=RetentionPolicy.LIMITS,
                        max_age=3600,
                        storage="file",
                    ),
                )
            except Exception:
                logger.info(f"   Creating stream '{self.stream_name}'...")
                await self.js.add_stream(
                    name=self.stream_name,
                    subjects=["hfo.>"],  # Use > for recursive wildcard
                    config=StreamConfig(
                        retention=RetentionPolicy.LIMITS,
                        max_age=3600,
                        storage="file",
                    ),
                )

            logger.info(f"✅ Connected to NATS Stigmergy Layer at {self.nats_url}")
        except Exception as e:
            logger.error(f"❌ Failed to connect to NATS: {e}")
            raise

    async def close(self):
        if self.nc:
            await self.nc.close()

    async def publish(self, subject: str, payload: Dict[str, Any]):
        """Publishes a dictionary payload to a subject."""
        if not self.js:
            raise ConnectionError("Not connected to NATS JetStream")

        data = json.dumps(payload).encode()
        ack = await self.js.publish(subject, data)
        return ack

    async def subscribe_queue(self, subject: str, queue: str, callback):
        """Subscribes to a subject with a queue group for load balancing."""
        if not self.js:
            raise ConnectionError("Not connected to NATS JetStream")

        # Use push subscription for queue groups
        await self.js.subscribe(subject, queue=queue, cb=callback)
        logger.info(f"   Subscribed to {subject} (Queue: {queue})")

    async def fetch_history(
        self, subject: str, limit: int = 10
    ) -> list[Dict[str, Any]]:
        """Fetches the last N messages from a subject."""
        if not self.js:
            raise ConnectionError("Not connected to NATS JetStream")

        messages = []
        try:
            # Create an ephemeral consumer to read the last N messages
            sub = await self.js.subscribe(subject, ordered_consumer=True)

            # This is a simplified fetch. In a real high-volume stream,
            # we might want to use a pull consumer or specific sequence numbers.
            # For now, we just try to fetch what's available quickly.
            try:
                async for msg in sub.messages:
                    try:
                        messages.append(json.loads(msg.data.decode()))
                    except Exception:
                        pass
                    if len(messages) >= limit:
                        break
            except Exception:
                # Timeout or end of stream
                pass

            await sub.unsubscribe()

        except Exception as e:
            logger.warning(f"Failed to fetch history for {subject}: {e}")

        return messages
