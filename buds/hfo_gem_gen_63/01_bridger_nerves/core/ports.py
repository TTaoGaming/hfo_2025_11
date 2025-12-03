"""
---
holon:
  id: hfo-ports-core
  type: interface
  file: ports.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_bridger_nats.md
---
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, Callable, Awaitable

class EventBusPort(ABC):
    """
    Port for the Nervous System (Hot Stigmergy).
    """
    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def publish(self, subject: str, payload: Dict[str, Any]):
        pass

    @abstractmethod
    async def subscribe(self, subject: str, callback: Callable[[Dict[str, Any]], Awaitable[None]]):
        pass
    
    @abstractmethod
    async def close(self):
        pass
