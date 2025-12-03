import sys
import os
import importlib.util

# Add root to path
sys.path.append(os.getcwd())

# Load memory_client using importlib because of numeric folder
file_path = "buds/hfo_gem_gen_63/07_navigator_brain/memory_client.py"
spec = importlib.util.spec_from_file_location("memory_client", file_path)
if spec is None or spec.loader is None:
    raise ImportError(f"Could not load {file_path}")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

print("Testing Memory Client...")
result = module.search_memory_direct(
    "What are the multiple layers of meaning for Obsidian?"
)
print(result)
