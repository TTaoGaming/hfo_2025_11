import json
import logging
import os
from typing import Any, Dict, List
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
                    subjects=["hfo.mission.>"],
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
                    subjects=["hfo.mission.>"],  # Use > for recursive wildcard
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

    async def fetch_history(
        self, subject: str, limit: int = 100
    ) -> List[Dict[str, Any]]:
        """Fetches recent messages from a subject (simulating memory lookup)."""
        if not self.js:
            raise ConnectionError("Not connected to NATS JetStream")

        # Create a temporary consumer to read past messages
        # Note: This is a simplified 'fetch' pattern.
        # In production, we might use a durable consumer or KeyValue store.
        results = []
        try:
            # We use a durable name to potentially resume, but here we just want 'last N'
            # Actually, for 'fetch history', we might want to create an ephemeral consumer
            # that starts from the beginning or a specific point.
            # For simplicity in this demo, we'll assume we are just subscribing to get *new* stuff
            # OR we use a KeyValue bucket.
            # BUT, standard streams store history.

            # Let's try to create an ephemeral consumer that reads from start
            sub = await self.js.pull_subscribe(subject, "history_reader")
            msgs = await sub.fetch(limit, timeout=2)
            for msg in msgs:
                results.append(json.loads(msg.data.decode()))
                await msg.ack()
        except Exception:
            # Timeout is expected if no messages
            pass

        return results
