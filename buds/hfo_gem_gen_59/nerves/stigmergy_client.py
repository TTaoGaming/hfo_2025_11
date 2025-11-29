import asyncio
import json
import logging
import nats
from nats.js.api import StreamConfig, RetentionPolicy

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("StigmergyClient")

class StigmergyClient:
    """
    The Nervous System (NATS JetStream).
    Handles Hot Stigmergy (Event Bus).
    """
    def __init__(self, nats_url: str = "nats://localhost:4225"):
        self.nats_url = nats_url
        self.nc = None
        self.js = None

    async def connect(self):
        """Connect to NATS and init JetStream."""
        try:
            self.nc = await nats.connect(self.nats_url)
            self.js = self.nc.jetstream()
            logger.info(f"⚡ Connected to NATS at {self.nats_url}")
            await self._init_streams()
        except Exception as e:
            logger.error(f"❌ NATS Connection Failed: {e}")
            raise

    async def _init_streams(self):
        """Initialize the HFO Streams."""
        # Ingest Stream: For raw memory items waiting to be processed
        try:
            await self.js.add_stream(name="HFO_INGEST", subjects=["hfo.ingest.>"], config=StreamConfig(
                retention=RetentionPolicy.WORK_QUEUE # Remove after ack
            ))
            logger.info("🌊 Stream 'HFO_INGEST' ready.")
        except Exception as e:
            # Stream might already exist
            pass

        # Artifact Stream: For completed artifacts (Level 0, 1, 2)
        try:
            await self.js.add_stream(name="HFO_ARTIFACTS", subjects=["hfo.artifacts.>"])
            logger.info("🌊 Stream 'HFO_ARTIFACTS' ready.")
        except Exception as e:
            pass

    async def publish_ingest(self, item_json: str):
        """Publish a raw item to the Ingest Queue."""
        if not self.js:
            await self.connect()
        
        ack = await self.js.publish("hfo.ingest.raw", item_json.encode())
        return ack

    async def subscribe(self, subject: str, callback):
        """Subscribe to a subject."""
        if not self.nc:
            await self.connect()
        
        await self.nc.subscribe(subject, cb=callback)

    async def close(self):
        if self.nc:
            await self.nc.close()
            self.nc = None
            self.js = None
