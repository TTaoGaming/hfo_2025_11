"""
---
holon:
  id: hfo-bridger-mcp
  type: server
  file: bridger_mcp.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_mcp_servers.md
---
"""
import asyncio
import json
from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

# Import the Bridger Core
# We use the sys.path hack again to ensure we can load the core
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir) # 01_bridger_nerves
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from bridger import bridger

# Initialize MCP Server
mcp = FastMCP("Obsidian Bridger")

@mcp.tool()
async def emit_pheromone(subject: str, payload: str) -> str:
    """
    Emit a Pheromone (Event) to the Hive Nervous System (NATS).
    Args:
        subject: The NATS subject (e.g., 'hfo.gen63.heartbeat')
        payload: The JSON payload as a string.
    """
    try:
        data = json.loads(payload)
        await bridger.publish(subject, data)
        return f"✅ Emitted to {subject}"
    except Exception as e:
        return f"❌ Failed to emit: {str(e)}"

@mcp.tool()
async def check_connection() -> str:
    """Check if the Bridger is connected to NATS."""
    try:
        await bridger.connect()
        return "✅ Bridger is Online and Connected to NATS."
    except Exception as e:
        return f"❌ Bridger is Offline: {str(e)}"

if __name__ == "__main__":
    mcp.run()
