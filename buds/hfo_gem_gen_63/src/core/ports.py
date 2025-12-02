"""
---
holon:
  id: hfo-3766bac3
  type: implementation
  file: ports.py
  status: active
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

class FileSystemPort(ABC):
    """
    Port for the Body (Cold Stigmergy).
    """
    @abstractmethod
    async def write_file(self, path: str, content: str):
        pass

    @abstractmethod
    async def read_file(self, path: str) -> str:
        pass
