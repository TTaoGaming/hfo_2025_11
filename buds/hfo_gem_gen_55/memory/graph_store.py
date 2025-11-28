"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: graph-store-portable-001
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.8
    decay: 0.1
    created: '2025-11-26T12:05:00+00:00'
    generation: 55
  topos:
    address: memory/graph_store.py
    links: []
  telos:
    viral_factor: 0.0
    meme: graph_store.py
"""

import networkx as nx
import json
from pathlib import Path
from typing import Dict, Any, List, Optional


class PortableGraphStore:
    """
    🕸️ A Portable Knowledge Graph backed by NetworkX and JSON.
    No database required. Pure Python.
    """

    def __init__(self, storage_path: str = "memory/semantic/knowledge_graph.json"):
        self.storage_path = Path(storage_path)
        self.graph = nx.DiGraph()
        self._ensure_directory()
        self.load()

    def _ensure_directory(self):
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)

    def load(self):
        """Loads the graph from disk."""
        if self.storage_path.exists():
            try:
                data = json.loads(self.storage_path.read_text())
                self.graph = nx.node_link_graph(data)
                print(
                    f"🕸️ Loaded graph with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges."
                )
            except Exception as e:
                print(f"⚠️ Failed to load graph: {e}. Starting fresh.")
                self.graph = nx.DiGraph()
        else:
            print("🕸️ No existing graph found. Starting fresh.")

    def save(self):
        """Saves the graph to disk."""
        data = nx.node_link_data(self.graph)
        self.storage_path.write_text(json.dumps(data, indent=2))
        print(f"💾 Saved graph to {self.storage_path}")

    def add_node(self, node_id: str, **attributes):
        """Adds a node with attributes."""
        self.graph.add_node(node_id, **attributes)
        self.save()

    def add_edge(
        self, source: str, target: str, relation: str = "related_to", **attributes
    ):
        """Adds a directed edge."""
        self.graph.add_edge(source, target, relation=relation, **attributes)
        self.save()

    def get_node(self, node_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves node attributes."""
        if self.graph.has_node(node_id):
            return self.graph.nodes[node_id]
        return None

    def get_neighbors(self, node_id: str) -> List[str]:
        """Returns a list of neighbor IDs."""
        if self.graph.has_node(node_id):
            return list(self.graph.neighbors(node_id))
        return []

    def find_path(self, source: str, target: str) -> List[str]:
        """Finds the shortest path between two nodes."""
        try:
            return nx.shortest_path(self.graph, source, target)
        except nx.NetworkXNoPath:
            return []
        except nx.NodeNotFound:
            return []


# Example Usage
if __name__ == "__main__":
    store = PortableGraphStore(storage_path="memory/semantic/test_graph.json")
    store.add_node("Concept A", type="idea")
    store.add_node("Concept B", type="implementation")
    store.add_edge("Concept A", "Concept B", relation="inspires")
    print(store.find_path("Concept A", "Concept B"))
