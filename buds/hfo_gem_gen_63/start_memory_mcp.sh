#!/bin/bash
# Start the Obsidian Memory MCP Server
# Usage: ./start_memory_mcp.sh

# Ensure we are in the root of the workspace
cd "$(dirname "$0")/../.."

# Set PYTHONPATH to include the root and the bud
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/buds/hfo_gem_gen_63

# Fix for OMP Error
export KMP_DUPLICATE_LIB_OK=TRUE

echo "🕷️ Starting Obsidian Memory MCP Server..."
echo "🧠 Model: nomic-embed-text (Ollama)"
echo "📂 DB: buds/hfo_gem_gen_63/06_assimilator_memory/lancedb"

# Run the server
python3 buds/hfo_gem_gen_63/06_assimilator_memory/servers/memory_mcp.py
