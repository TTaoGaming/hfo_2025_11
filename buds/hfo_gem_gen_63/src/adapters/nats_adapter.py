import nats
import json
import logging
from typing import Any, Dict, Callable, Awaitable
from ..core.ports import EventBusPort

logger = logging.getLogger("NatsAdapter")

class NatsAdapter(EventBusPort):
    """
    NATS JetStream Adapter.
    """
    def __init__(self, url: str):
        self.url = url
        self.nc = None
        self.js = None

    async def connect(self):
        try:
            self.nc = await nats.connect(self.url)
            self.js = self.nc.jetstream()
            logger.info(f"🔌 Connected to NATS at {self.url}")
        except Exception as e:
            logger.error(f"❌ NATS Connection Failed: {e}")
            raise

    async def publish(self, subject: str, payload: Dict[str, Any]):
        if not self.nc:
            raise ConnectionError("Not connected to NATS")
        
        data = json.dumps(payload).encode()
        await self.nc.publish(subject, data)
        logger.debug(f"📤 Published to {subject}: {payload}")

    async def subscribe(self, subject: str, callback: Callable[[Dict[str, Any]], Awaitable[None]]):
        if not self.nc:
            raise ConnectionError("Not connected to NATS")

        async def wrapped_callback(msg):
            try:
                data = json.loads(msg.data.decode())
                logger.debug(f"📥 Received on {subject}: {data}")
                await callback(data)
            except Exception as e:
                logger.error(f"Error processing message: {e}")

        await self.nc.subscribe(subject, cb=wrapped_callback)
        logger.info(f"👂 Subscribed to {subject}")

    async def close(self):
        if self.nc:
            await self.nc.close()
            logger.info("🔌 NATS Connection Closed")
