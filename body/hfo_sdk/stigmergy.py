import json
import logging
import nats
from nats.js.api import StreamConfig, RetentionPolicy
from typing import List, Dict, Any

logger = logging.getLogger("StigmergyClient")


class StigmergyClient:
    """
    Client for the NATS JetStream Stigmergy Layer.
    Allows agents to Publish (Write) and Subscribe (Read) to the Hive Mind.
    """

    def __init__(self, nats_url: str = "nats://localhost:4222"):
        self.nats_url = nats_url
        self.nc = None
        self.js = None
        self.stream_name = "HIVE_MIND"

    async def connect(self):
        """Connects to NATS and ensures the JetStream exists."""
        if self.nc and self.nc.is_connected:
            return

        try:
            self.nc = await nats.connect(self.nats_url)
            self.js = self.nc.jetstream()

            # Ensure Stream Exists
            try:
                await self.js.add_stream(
                    name=self.stream_name,
                    subjects=["hfo.mission.>"],
                    config=StreamConfig(
                        retention=RetentionPolicy.LIMITS,
                        max_age=3600,  # 1 Hour TTL (Evaporating Blackboard)
                        storage="file",
                    ),
                )
            except Exception:
                pass  # Stream likely exists

            logger.info(f"✅ Connected to Stigmergy Layer at {self.nats_url}")
        except Exception as e:
            logger.error(f"❌ Failed to connect to NATS: {e}")
            raise e

    async def publish(self, subject: str, data: Dict[str, Any]):
        """Publishes a signal to the Hive Mind."""
        if not self.js:
            await self.connect()

        payload = json.dumps(data).encode()
        ack = await self.js.publish(subject, payload)
        return ack

    async def fetch_history(
        self, subject: str, limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Fetches recent signals from a subject."""
        if not self.js:
            await self.connect()

        # Create a temporary ephemeral consumer to read the stream
        sub = await self.js.pull_subscribe(subject, "temp_history_reader")
        msgs = []
        try:
            fetched = await sub.fetch(limit, timeout=2)
            for msg in fetched:
                msgs.append(json.loads(msg.data.decode()))
                await msg.ack()
        except Exception:
            pass  # Timeout or no messages

        return msgs

    async def close(self):
        if self.nc:
            await self.nc.close()
