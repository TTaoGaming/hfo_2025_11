"""
---
holon:
  id: hfo-09be58b6
  type: unknown
  file: assimilator.py
  status: active
---
"""
import os
import logging
import sys
from typing import List

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.bridger import Bridger

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Assimilator")

class Chunker:
    """
    Splits text into manageable chunks for embedding.
    """
    def __init__(self, chunk_size: int = 1000, overlap: int = 100):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk_text(self, text: str) -> List[str]:
        if not text:
            return []
        
        chunks = []
        start = 0
        text_len = len(text)

        while start < text_len:
            end = start + self.chunk_size
            chunk = text[start:end]
            chunks.append(chunk)
            start += self.chunk_size - self.overlap
        
        return chunks

class Assimilator:
    """
    The Assimilator (Gen 63).
    Digests raw information (Files) into Wisdom (Vector Memory).
    """
    def __init__(self):
        self.bridger = Bridger()
        self.chunker = Chunker()

    def ingest_file(self, file_path: str):
        """
        Reads a file, chunks it, and memorizes it via the Bridger.
        """
        if not os.path.exists(file_path):
            logger.error(f"File not found: {file_path}")
            return

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic metadata
            filename = os.path.basename(file_path)
            extension = os.path.splitext(filename)[1]
            category = "code" if extension in ['.py', '.js', '.sh'] else "doc"
            
            chunks = self.chunker.chunk_text(content)
            logger.info(f"Ingesting {filename}: {len(chunks)} chunks.")
            
            for i, chunk in enumerate(chunks):
                # Add context to the chunk
                contextualized_chunk = f"File: {filename}\nPath: {file_path}\nPart: {i+1}/{len(chunks)}\n\n{chunk}"
                self.bridger.memorize(
                    text=contextualized_chunk,
                    source=file_path,
                    category=category
                )
                
        except Exception as e:
            logger.error(f"Failed to ingest {file_path}: {e}")

    def ingest_directory(self, dir_path: str, extensions: List[str] = ['.md', '.py'], exclude_dirs: List[str] = []):
        """
        Recursively ingests a directory.
        """
        logger.info(f"Scanning directory: {dir_path}")
        for root, dirs, files in os.walk(dir_path):
            # Modify dirs in-place to skip excluded directories
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs and d not in exclude_dirs]
            
            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    full_path = os.path.join(root, file)
                    # Double check we aren't in an excluded path (for safety)
                    if any(ex in full_path for ex in exclude_dirs):
                        continue
                        
                    self.ingest_file(full_path)

if __name__ == "__main__":
    assimilator = Assimilator()
    
    # Ingest the Gen 63 Brain and Src
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    brain_path = os.path.join(base_path, "brain")
    src_path = os.path.join(base_path, "src")
    
    print(f"🧠 Ingesting Brain: {brain_path}")
    assimilator.ingest_directory(brain_path)
    
    print(f"🧬 Ingesting Src: {src_path}")
    assimilator.ingest_directory(src_path)
