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
