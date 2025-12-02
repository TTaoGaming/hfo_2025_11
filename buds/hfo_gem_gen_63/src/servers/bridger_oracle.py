"""
---
holon:
  id: hfo-fc88fb6f
  type: implementation
  file: bridger_oracle.py
  status: active
---
"""
import sqlite3
import lancedb
import json
from typing import List, Dict, Any
from mcp.server.fastmcp import FastMCP

# Initialize the MCP Server
mcp = FastMCP("Bridger Oracle")

# Configuration
DB_PATH = "buds/hfo_gem_gen_63/memory/iron_ledger.db"
LANCEDB_PATH = "buds/hfo_gem_gen_63/memory/lancedb"

@mcp.tool()
def query_iron_ledger(query: str, params: List[Any] = None) -> List[Dict[str, Any]]:
    """
    Executes a SQL query against the Iron Ledger (SQLite).
    Use this for transactional data, logs, and structured facts.
    """
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params or [])
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
    except Exception as e:
        return [{"error": str(e)}]

@mcp.tool()
def query_semantic_memory(text: str, limit: int = 5) -> List[Dict[str, Any]]:
    """
    Searches the LanceDB vector store for semantically similar content.
    Use this for retrieving concepts, documentation, and "fuzzy" knowledge.
    """
    try:
        db = lancedb.connect(LANCEDB_PATH)
        # Assuming a default table name 'knowledge' - adjust as needed
        table = db.open_table("knowledge") 
        results = table.search(text).limit(limit).to_list()
        return results
    except Exception as e:
        return [{"error": str(e)}]

@mcp.tool()
def get_holon_metadata(holon_id: str) -> Dict[str, Any]:
    """
    Retrieves the Stigmergic Metadata (YAML Header info) for a specific Holon ID.
    """
    # This would typically query a specific table or index
    return query_iron_ledger("SELECT * FROM holon_registry WHERE id = ?", [holon_id])

if __name__ == "__main__":
    mcp.run()
