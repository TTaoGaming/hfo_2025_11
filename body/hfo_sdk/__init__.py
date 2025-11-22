"""
Hive Fleet Obsidian SDK
The unified entry point for the HFO R.A.P.T.O.R. stack.
"""

from .client import HFOClient
from body.hands.research_swarm import build_swarm_graph

__all__ = ["HFOClient", "build_swarm_graph"]
