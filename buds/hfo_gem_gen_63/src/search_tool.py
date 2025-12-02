import sys
import os
import importlib.util

# Proxy to 00_observer_eyes/search_mcp.py

current_dir = os.path.dirname(os.path.abspath(__file__))
bud_root = os.path.dirname(current_dir) # buds/hfo_gem_gen_63
target_path = os.path.join(bud_root, "00_observer_eyes", "search_mcp.py")

if not os.path.exists(target_path):
    raise ImportError(f"Target file not found: {target_path}")

spec = importlib.util.spec_from_file_location("observer_eyes_search_mcp", target_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

search_web = module.search_web
