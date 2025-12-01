import aiofiles
import os
import logging
from ..core.ports import FileSystemPort

logger = logging.getLogger("FSAdapter")

class LocalFileSystemAdapter(FileSystemPort):
    """
    Local File System Adapter.
    """
    def __init__(self, base_path: str = "."):
        self.base_path = base_path

    async def write_file(self, path: str, content: str):
        full_path = os.path.join(self.base_path, path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        async with aiofiles.open(full_path, mode='w') as f:
            await f.write(content)
        logger.info(f"💾 Wrote file: {full_path}")

    async def read_file(self, path: str) -> str:
        full_path = os.path.join(self.base_path, path)
        async with aiofiles.open(full_path, mode='r') as f:
            content = await f.read()
        logger.info(f"📖 Read file: {full_path}")
        return content
