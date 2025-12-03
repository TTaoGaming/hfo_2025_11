"""
---
holon:
  id: hfo-bridger-nerves
  type: implementation
  file: bridger.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_bridger_nats.md
---
"""
import asyncio
import logging
from typing import Dict, Any, Callable, Awaitable, Optional

# Import Config via Proxy
from src.config import settings

# Import Adapter
# We use sys.path hack because of numeric folder names preventing relative imports
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from adapters.nats_adapter import NatsAdapter

logger = logging.getLogger("Bridger")

class Bridger:
    """
    The Bridger (Nerves/Logos).
    The Central Nervous System of the Hive.
    Wraps the NATS Adapter to provide a high-level Bus API.
    """
    def __init__(self):
        self.url = settings.NATS_URL
        self.adapter = NatsAdapter(self.url)
        self._connected = False

    async def connect(self):
        """Connect to the Nervous System."""
        if self._connected:
            return
        
        logger.info(f"🔌 Bridger connecting to {self.url}...")
        await self.adapter.connect()
        self._connected = True
        logger.info("✅ Bridger Connected.")

    async def publish(self, subject: str, payload: Dict[str, Any]):
        """Emit a Pheromone (Event)."""
        if not self._connected:
            await self.connect()
        
        await self.adapter.publish(subject, payload)

    async def subscribe(self, subject: str, callback: Callable[[Dict[str, Any]], Awaitable[None]]):
        """Listen for Pheromones."""
        if not self._connected:
            await self.connect()
            
        await self.adapter.subscribe(subject, callback)

    async def close(self):
        """Sever the connection."""
        if self._connected:
            await self.adapter.close()
            self._connected = False

# Singleton Instance
bridger = Bridger()
