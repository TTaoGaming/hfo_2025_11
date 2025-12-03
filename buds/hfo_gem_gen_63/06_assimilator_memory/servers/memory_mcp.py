"""
---
holon:
  id: hfo-memory-mcp
  type: server
  file: memory_mcp.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_mcp_servers.md
---
"""
import lancedb
from lancedb.pydantic import LanceModel, Vector
from lancedb.embeddings import get_registry
from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any

# Import Config via Proxy
import sys
import os
# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
from src.config import settings

# Initialize MCP Server
mcp = FastMCP("Obsidian Memory")

# --- Embedding Setup ---
# FIX: Enforce Local Ollama Embeddings (Phoenix Protocol)
# We use the 'ollama' registry to ensure we use the local model (e.g., nomic-embed-text)
# defined in settings.MODEL_EMBEDDING.
embedding_func = get_registry().get("ollama").create(
    name=settings.MODEL_EMBEDDING,
)

class MemoryItem(LanceModel):
    text: str = embedding_func.SourceField()
    vector: Vector(embedding_func.ndims()) = embedding_func.VectorField()
    category: str
    timestamp: str

# Connect to DB
db = lancedb.connect(settings.LANCEDB_PATH)
TABLE_NAME = "memories" # Correct table name for Gen 63

def get_table():
    if TABLE_NAME not in db.table_names():
        # Create table with schema
        return db.create_table(TABLE_NAME, schema=MemoryItem)
    return db.open_table(TABLE_NAME)

@mcp.tool()
def recall(query: str, limit: int = 5) -> str:
    """
    Recall memories from the Hive's Long-Term Memory (LanceDB).
    Args:
        query: The semantic search query.
        limit: Number of results to return.
    """
    try:
        tbl = get_table()
        
        # Perform semantic search
        # LanceDB handles the embedding of 'query' automatically via the registered function
        results = tbl.search(query).limit(limit).to_pandas()
        
        if results.empty:
            return f"No memories found for '{query}'."
            
        response = f"🔍 Found {len(results)} memories for '{query}':\n"
        for _, row in results.iterrows():
            score = row.get('_distance', 0.0)
            text = row.get('text', '???')
            cat = row.get('category', 'general')
            response += f"- [{cat}] (dist: {score:.3f}) {text[:200]}...\n"
            
        return response
    except Exception as e:
        return f"❌ Recall failed: {str(e)}"

@mcp.tool()
def remember(text: str, category: str = "general") -> str:
    """
    Save a new memory to the Hive.
    """
    try:
        tbl = get_table()
        from datetime import datetime
        
        item = MemoryItem(
            text=text,
            category=category,
            timestamp=datetime.now().isoformat()
        )
        
        tbl.add([item])
        return f"💾 Saved to {TABLE_NAME}: [{category}] {text[:50]}..."
    except Exception as e:
        return f"❌ Remember failed: {str(e)}"

if __name__ == "__main__":
    mcp.run()
