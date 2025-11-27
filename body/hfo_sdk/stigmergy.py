"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: c908a368-059e-42af-90fe-dcab8f582ed4
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.427596+00:00'
    generation: 51
  topos:
    address: body/hfo_sdk/stigmergy.py
    links: []
  telos:
    viral_factor: 0.0
    meme: stigmergy.py
"""

import json
import logging
import nats
from nats.js.api import StreamConfig, RetentionPolicy
from typing import List, Dict, Any
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from body.config import Config

logger = logging.getLogger("StigmergyClient")


class StigmergyClient:
    """
    Client for the NATS JetStream Stigmergy Layer.
    Allows agents to Publish (Write) and Subscribe (Read) to the Hive Mind.
    """

    def __init__(self, nats_url: str = Config.NATS_URL):
        self.nats_url = nats_url
        self.nc = None
        self.js = None
        self.stream_name = "HIVE_MIND"

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),
        reraise=True,
    )
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
                    subjects=["hfo.mission.>", "hfo.heartbeat.>"],
                    config=StreamConfig(
                        retention=RetentionPolicy.LIMITS,
                        max_age=3600 * 24,  # 24 Hour TTL for Heartbeats
                        storage="file",
                    ),
                )
            except Exception:
                # Update existing stream config if needed
                try:
                    await self.js.update_stream(
                        name=self.stream_name,
                        subjects=["hfo.mission.>", "hfo.heartbeat.>"],
                        config=StreamConfig(
                            retention=RetentionPolicy.LIMITS,
                            max_age=3600 * 24,
                            storage="file",
                        ),
                    )
                except Exception as e:
                    logger.warning(f"Stream update failed (might be unchanged): {e}")

            logger.info(f"✅ Connected to Stigmergy Layer at {self.nats_url}")
        except Exception as e:
            logger.error(f"❌ Failed to connect to NATS: {e}")
            raise e

    async def publish(self, subject: str, data: Dict[str, Any]):
        """Publishes a signal to the Hive Mind."""
        if not self.js:
            await self.connect()

        if not self.js:
            raise ConnectionError("Failed to connect to NATS JetStream")

        payload = json.dumps(data).encode()
        ack = await self.js.publish(subject, payload)
        return ack

    async def fetch_history(
        self, subject: str, limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Fetches recent signals from a subject."""
        if not self.js:
            await self.connect()

        if not self.js:
            return []

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
