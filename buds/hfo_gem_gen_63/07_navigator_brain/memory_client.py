"""
---
holon:
  id: hfo-navigator-memory-client
  type: client
  file: memory_client.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_navigator_temporal.md
---
"""
import lancedb
from lancedb.embeddings import get_registry
import os
import sys
import logging

# Import Config via Proxy
# We need to add the root to path to find src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.config import settings

logger = logging.getLogger("MemoryClient")

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def get_embedding_function():
    """Get the embedding function used for the memory table."""
    # FIX: Use Ollama/Nomic
    return get_registry().get("ollama").create(
        name=settings.MODEL_EMBEDDING
    )

def search_memory_direct(query: str, limit: int = 5) -> str:
    """
    Directly query the LanceDB memory table.
    Bypasses MCP/NATS for immediate access (Gen 63 Stabilization).
    """
    try:
        db_path = settings.LANCEDB_PATH
        if not os.path.exists(db_path):
            return f"[MEMORY ERROR] DB Path not found: {db_path}"

        db = lancedb.connect(db_path)
        
        # Check for table
        table_name = "memories" # Found via inspection
        if table_name not in db.table_names():
             # Fallback to memories_gen63 if it exists
            if "memories_gen63" in db.table_names():
                table_name = "memories_gen63"
            else:
                return f"[MEMORY] No memory tables found. (Tables: {db.table_names()})"

        tbl = db.open_table(table_name)
        
        # Perform semantic search
        # We explicitly embed the query to avoid metadata issues
        func = get_embedding_function()
        # Ollama embedding function returns a list of embeddings
        # We assume single query
        vectors = func.compute_query_embeddings([query])
        if not vectors:
             return f"[MEMORY ERROR] Failed to embed query."
        query_vec = vectors[0]
        
        results = tbl.search(query_vec).limit(limit).to_pandas()
        
        if results.empty:
            return f"[MEMORY] No records found for '{query}'."
            
        response = f"🔍 [MEMORY] Found {len(results)} records:\n"
        for _, row in results.iterrows():
            score = row.get('_distance', 0.0)
            text = row.get('text', '???')
            cat = row.get('category', 'general')
            # Invert score for display if needed (lower is better for L2/Cosine distance usually)
            response += f"- [{cat}] (dist: {score:.3f}) {text[:300]}...\n"
            
        return response

    except Exception as e:
        logger.error(f"Memory Search Failed: {e}")
        return f"[MEMORY ERROR] {str(e)}"
