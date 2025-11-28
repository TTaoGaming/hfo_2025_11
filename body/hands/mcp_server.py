"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: hfo-mcp-server-001
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T14:45:00Z'
    generation: 51
  topos:
    address: body/hands/mcp_server.py
    links: []
  telos:
    viral_factor: 1.0
    meme: mcp_server.py
"""

import logging
import os
from typing import Optional

from mcp.server.fastmcp import FastMCP

# Import HFO Components
from body.hybrid_memory import HybridMemory
from body.models.stigmergy import (
    StigmergySignal,
    RichMetadata,
    ArtifactType,
    ClaimCheck,
)
from nats.aio.client import Client as NATS

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HFO_MCP")

# Initialize FastMCP
mcp = FastMCP("Hive Fleet Obsidian")

# Global State
memory: Optional[HybridMemory] = None
nats_client: Optional[NATS] = None


@mcp.resource("obsidian://memory/recent")
async def get_recent_memories() -> str:
    """Returns the most recent memories from the Hive Mind."""
    global memory
    if not memory:
        memory = HybridMemory()
        await memory.initialize()

    items = await memory.get_recent_memories(limit=10)
    return "\n".join([f"- [{m.created_at}] {m.content}" for m in items])


@mcp.tool()
async def obsidian_memory_search(query: str) -> str:
    """
    Search the Hive Fleet Obsidian's Long-Term Memory (Postgres/Vector).
    Use this to recall past conversations, facts, or swarm artifacts.
    """
    global memory
    if not memory:
        memory = HybridMemory()
        await memory.initialize()

    results = await memory.search_memory(query, limit=5)
    if not results:
        return "No relevant memories found."

    return "\n".join(
        [
            f"- {m.content} (Score: {m.metadata.get('similarity', 'N/A')})"
            for m in results
        ]
    )


@mcp.tool()
async def obsidian_fs_read(path: str) -> str:
    """
    Read a file from the Hive Fleet Obsidian repository.
    Enforces security: can only read files within the repo.
    """
    # Security Check
    abs_path = os.path.abspath(path)
    repo_root = os.path.abspath(os.getcwd())  # Assuming running from repo root

    if not abs_path.startswith(repo_root):
        return "Error: Access Denied. Can only read files within the Hive."

    if not os.path.exists(abs_path):
        return "Error: File not found."

    try:
        with open(abs_path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"


@mcp.tool()
async def obsidian_hive_signal(channel: str, message: str, type: str = "log") -> str:
    """
    Publish a Stigmergic Signal to the Swarm (NATS).
    Use this to notify other agents or log an event.
    """
    global nats_client
    if not nats_client:
        nats_client = NATS()
        try:
            await nats_client.connect(os.getenv("NATS_URL", "nats://localhost:4225"))
        except Exception as e:
            return f"Error connecting to NATS: {e}"

    # Construct Signal
    signal = StigmergySignal(
        id=str(os.urandom(4).hex()),
        producer_id="mcp-copilot",
        claim_check=ClaimCheck(pointer="mcp-direct", storage="memory"),
        metadata=RichMetadata(type=ArtifactType(type)),
    )

    # Publish
    subject = f"hfo.signal.artifact.{channel}"
    payload = signal.model_dump_json().encode()

    try:
        await nats_client.publish(subject, payload)
        return f"Signal published to {subject}"
    except Exception as e:
        return f"Error publishing signal: {e}"


if __name__ == "__main__":
    # Run the MCP Server
    mcp.run()
