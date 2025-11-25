"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 0e2b3cf5-8d30-4595-a63e-989ce43b5535
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:34.835033Z'
    generation: 51
  topos:
    address: body/hybrid_memory.py
    links: []
  telos:
    viral_factor: 0.0
    meme: hybrid_memory.py
"""

import json
import logging
import os
import time
import uuid
from typing import Any, Dict, List, Optional

import asyncpg
from openai import AsyncOpenAI
from pydantic import BaseModel, Field

from body.config import Config

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HybridMemory")


class MemoryItem(BaseModel):
    """A single unit of memory."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    content: str
    metadata: Dict[str, Any] = Field(default_factory=dict)
    embedding: Optional[List[float]] = None
    created_at: float = Field(default_factory=time.time)


class HybridMemory:
    """
    🧠 The Tri-Brain Memory System.
    Integrates Postgres (pgvector) for Semantic Memory and NetworkX for Graph Memory.
    """

    def __init__(self, openai_client: Optional[AsyncOpenAI] = None):
        self.dsn = Config.PG_DSN
        self.pool = None

        # Configure Client with Fallback
        if openai_client:
            self.client = openai_client
        else:
            api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
            base_url = os.getenv("OPENAI_BASE_URL") or os.getenv("OPENROUTER_BASE_URL")
            self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)

        self.embedding_model = "text-embedding-3-small"  # Cost-effective

    async def initialize(self):
        """Connects to Postgres and ensures schema exists."""
        try:
            self.pool = await asyncpg.create_pool(self.dsn)
            async with self.pool.acquire() as conn:
                # Enable pgvector extension
                await conn.execute("CREATE EXTENSION IF NOT EXISTS vector;")

                # Create Memories Table
                # We use 1536 dimensions for text-embedding-3-small
                await conn.execute(
                    """
                    CREATE TABLE IF NOT EXISTS memories (
                        id UUID PRIMARY KEY,
                        content TEXT NOT NULL,
                        metadata JSONB,
                        embedding vector(1536),
                        created_at DOUBLE PRECISION
                    );
                    """
                )

                # Create Index for faster search
                await conn.execute(
                    """
                    CREATE INDEX IF NOT EXISTS memories_embedding_idx
                    ON memories USING hnsw (embedding vector_cosine_ops);
                    """
                )
            logger.info("✅ HybridMemory initialized (Postgres + pgvector).")
        except Exception as e:
            logger.error(f"❌ Failed to initialize HybridMemory: {e}")
            # Fallback or re-raise depending on strictness.
            # For now, we log and allow the system to limp along if DB is down.

    async def close(self):
        if self.pool:
            await self.pool.close()

    async def _get_embedding(self, text: str) -> List[float]:
        """Generates an embedding for the text."""
        try:
            response = await self.client.embeddings.create(
                input=text, model=self.embedding_model
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"⚠️ Embedding generation failed: {e}")
            return [0.0] * 1536  # Return zero vector on failure

    async def add_memory(self, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Adds a new memory to the store."""
        if not self.pool:
            logger.warning("⚠️ Memory not initialized. Call initialize() first.")
            return

        if metadata is None:
            metadata = {}

        embedding = await self._get_embedding(content)
        # Convert embedding list to string format for pgvector
        embedding_str = str(embedding)

        memory_id = str(uuid.uuid4())
        created_at = time.time()

        try:
            async with self.pool.acquire() as conn:
                await conn.execute(
                    """
                    INSERT INTO memories (id, content, metadata, embedding, created_at)
                    VALUES ($1, $2, $3, $4, $5)
                    """,
                    memory_id,
                    content,
                    json.dumps(metadata),
                    embedding_str,
                    created_at,
                )
            logger.info(f"💾 Memory stored: {memory_id}")
        except Exception as e:
            logger.error(f"❌ Failed to store memory: {e}")

    async def search_memory(self, query: str, limit: int = 5) -> List[MemoryItem]:
        """Semantic search for memories."""
        if not self.pool:
            return []

        embedding = await self._get_embedding(query)
        embedding_str = str(embedding)

        try:
            async with self.pool.acquire() as conn:
                rows = await conn.fetch(
                    """
                    SELECT id, content, metadata, created_at,
                           1 - (embedding <=> $1) as similarity
                    FROM memories
                    ORDER BY embedding <=> $1
                    LIMIT $2
                    """,
                    embedding_str,
                    limit,
                )

                results = []
                for row in rows:
                    results.append(
                        MemoryItem(
                            id=str(row["id"]),
                            content=row["content"],
                            metadata=json.loads(row["metadata"]),
                            created_at=row["created_at"],
                        )
                    )
                return results
        except Exception as e:
            logger.error(f"❌ Memory search failed: {e}")
            return []

    async def get_recent_memories(self, limit: int = 10) -> List[MemoryItem]:
        """Retrieves the most recent memories."""
        if not self.pool:
            return []

        try:
            async with self.pool.acquire() as conn:
                rows = await conn.fetch(
                    """
                    SELECT id, content, metadata, created_at
                    FROM memories
                    ORDER BY created_at DESC
                    LIMIT $1
                    """,
                    limit,
                )

                results = []
                for row in rows:
                    results.append(
                        MemoryItem(
                            id=str(row["id"]),
                            content=row["content"],
                            metadata=json.loads(row["metadata"]),
                            created_at=row["created_at"],
                        )
                    )
                return results
        except Exception as e:
            logger.error(f"❌ Failed to get recent memories: {e}")
            return []
