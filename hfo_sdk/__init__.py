"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 4ae08631-f173-47cd-85a6-4606c19c0ef9
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.607182+00:00'
    generation: 51
  topos:
    address: hfo_sdk/__init__.py
    links: []
  telos:
    viral_factor: 0.0
    meme: __init__.py
"""

from .swarm import SwarmController, SwarmConfig
from .models import MissionIntent
from .stigmergy import StigmergyClient

# Expose GraphRAG tools for easy import
try:
    from body.digestion.weaver_ant import weave
    from body.digestion.consensus_council import convene_council
    from body.digestion.graph_gardener import garden
except ImportError:
    # Allow SDK to load even if body/ isn't fully set up (e.g. during bootstrap)
    pass

__all__ = [
    "SwarmController",
    "SwarmConfig",
    "MissionIntent",
    "StigmergyClient",
    "weave",
    "convene_council",
    "garden",
]
