"""
Intent: Implement the Mountain & Web Stigmergy System.
"""

from typing import List, Dict
from datetime import datetime


class ObsidianFacet:
    """
    The Unified Metadata Schema for the Mountain.
    """

    def __init__(self, id: str, type: str, urgency: float = 0.5):
        self.id = id
        self.type = type
        self.created = datetime.utcnow()
        self.last_touched = datetime.utcnow()
        self.urgency = urgency
        self.decay_rate = 0.1
        self.links: List[Dict[str, str]] = []

    @property
    def stigmergy_score(self) -> float:
        """
        Calculate the current Stigmergy Score.
        Score = Urgency / (TimeDelta * Decay)
        """
        delta = (datetime.utcnow() - self.last_touched).total_seconds()
        if delta < 1:
            delta = 1.0
        return self.urgency / (delta * self.decay_rate)


class SherpaAgent:
    """
    The Retrieval Holon.
    """

    def scan_mountain(self, files: List[ObsidianFacet]) -> List[ObsidianFacet]:
        """Find forgotten gems."""
        gems = []
        for f in files:
            if f.urgency > 0.7:
                gems.append(f)
        return gems


class GardenerAgent:
    """
    The Pruning Holon.
    """

    def prune_mountain(self, files: List[ObsidianFacet]) -> List[ObsidianFacet]:
        """Find dead weight."""
        compost = []
        for f in files:
            if f.stigmergy_score < 10.0:
                compost.append(f)
        return compost


class WeaverAgent:
    """
    The Synthesis Holon.
    """

    def weave(self, source: ObsidianFacet, target: ObsidianFacet, relation: str):
        """Add a link."""
        source.links.append({target.id: relation})
