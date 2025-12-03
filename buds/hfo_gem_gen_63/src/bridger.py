"""
---
holon:
  id: hfo-c41371e4
  type: implementation
  file: bridger.py
  status: active
---
"""
import sys
import os
import importlib.util

# Proxy to 01_bridger_nerves/bridger.py
# We use importlib to avoid name collision and handle numbered directory

current_dir = os.path.dirname(os.path.abspath(__file__))
bud_root = os.path.dirname(current_dir) # buds/hfo_gem_gen_63
target_path = os.path.join(bud_root, "01_bridger_nerves", "bridger.py")

if not os.path.exists(target_path):
    raise ImportError(f"Target file not found: {target_path}")

spec = importlib.util.spec_from_file_location("bridger_nerves_bridger", target_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Bridger = module.Bridger
bridger = module.bridger
