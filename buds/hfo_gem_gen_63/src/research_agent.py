"""
---
holon:
  id: hfo-c8800e51
  type: implementation
  file: research_agent.py
  status: active
---
"""
import sys
import os
import importlib.util

# Proxy to 07_navigator_brain/research_agent.py
# We use importlib to avoid name collision with this file itself (research_agent.py)

current_dir = os.path.dirname(os.path.abspath(__file__))
bud_root = os.path.dirname(current_dir) # buds/hfo_gem_gen_63
target_path = os.path.join(bud_root, "07_navigator_brain", "research_agent.py")

if not os.path.exists(target_path):
    raise ImportError(f"Target file not found: {target_path}")

spec = importlib.util.spec_from_file_location("navigator_brain_research_agent", target_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

ResearchAgent = module.ResearchAgent
