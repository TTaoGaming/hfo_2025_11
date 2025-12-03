"""
---
holon:
  id: hfo-proxy-config
  type: proxy
  file: config.py
  status: active
  target: buds/hfo_gem_gen_63/05_immunizer_carapace/config.py
---
"""
import sys
import os
import importlib.util

# Proxy to 05_immunizer_carapace/config.py
# This file exists ONLY to bridge the gap between Python's import system
# and the HFO Octree (Numeric Folders).
# Logic MUST reside in the Immunizer.

current_dir = os.path.dirname(os.path.abspath(__file__))
bud_root = os.path.dirname(current_dir) # buds/hfo_gem_gen_63
target_path = os.path.join(bud_root, "05_immunizer_carapace", "config.py")

if not os.path.exists(target_path):
    raise ImportError(f"Target file not found: {target_path}")

spec = importlib.util.spec_from_file_location("immunizer_carapace_config", target_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Re-export the symbols
Settings = module.Settings
settings = module.settings

if __name__ == "__main__":
    print(f"Loaded Settings for HFO Gen {settings.GENERATION} in {settings.ENV} mode.")
    print(f"Champion (Reasoning): {settings.MODEL_REASONING}")
