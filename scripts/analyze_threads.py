"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 4b3016fb-07ea-4cc2-a24d-ec8f23bfb78d
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.611992+00:00'
  topos:
    address: scripts/analyze_threads.py
    links: []
  telos:
    viral_factor: 0.0
    meme: analyze_threads.py
"""

from pathlib import Path
import os

# Set paths
WORKSPACE_ROOT = Path(os.getcwd())
if WORKSPACE_ROOT.name == "scripts":
    WORKSPACE_ROOT = WORKSPACE_ROOT.parent

GML_PATH = WORKSPACE_ROOT / "memory/semantic/knowledge_graph/evolution_graph.gml"
REPORT_PATH = WORKSPACE_ROOT / "memory/COMMON_THREADS_REPORT.md"
