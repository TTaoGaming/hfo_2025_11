"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: f2b60506-deb8-49f2-9fef-2ca58e72ee08
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.594293+00:00'
    generation: 51
  topos:
    address: eyes/tools/visualize_concepts.py
    links: []
  telos:
    viral_factor: 0.0
    meme: visualize_concepts.py
"""

import matplotlib.pyplot as plt
import networkx as nx


def create_concept_map():
    # Concepts
    concepts = [
        "Hexagonal Architecture",
        "Swarm Intelligence",
        "Stigmergy",
        "Adversarial Co-evolution",
        "Holonic Topology",
        "Epistemic Uncertainty",
    ]

    # Create a graph
    G = nx.Graph()

    # Add central node
    G.add_node("HFO Core", size=3000, color="black")

    # Add concept nodes
    for concept in concepts:
        G.add_node(concept, size=1500, color="#1f77b4")
        G.add_edge("HFO Core", concept)

    # Add some "file" nodes to show how data connects (Mock Data)
    files = [
        "queue_worker.py",
        "inventory_scanner.py",
        "Gen_1_Evolution.md",
        "Blackboard_Protocol.json",
        "Critic_Agent.py",
        "Molt_Script.sh",
    ]

    connections = [
        ("queue_worker.py", "Swarm Intelligence"),
        ("queue_worker.py", "Stigmergy"),
        ("inventory_scanner.py", "Hexagonal Architecture"),
        ("Gen_1_Evolution.md", "Adversarial Co-evolution"),
        ("Blackboard_Protocol.json", "Stigmergy"),
        ("Critic_Agent.py", "Adversarial Co-evolution"),
        ("Critic_Agent.py", "Epistemic Uncertainty"),
        ("Molt_Script.sh", "Holonic Topology"),
    ]

    for f in files:
        G.add_node(f, size=500, color="#2ca02c")

    for f, c in connections:
        G.add_edge(f, c)

    # Layout
    pos = nx.spring_layout(G, seed=42)

    # Draw
    plt.figure(figsize=(12, 8))

    # Draw nodes
    node_sizes = [G.nodes[n].get("size", 1000) for n in G.nodes]
    node_colors = [G.nodes[n].get("color", "gray") for n in G.nodes]

    nx.draw_networkx_nodes(
        G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.8
    )
    nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

    plt.title("HFO Conceptual Topology (Visualization)", fontsize=15)
    plt.axis("off")

    # Save
    output_file = "hfo_concept_map.png"
    plt.savefig(output_file)
    print(f"Visualization saved to {output_file}")


if __name__ == "__main__":
    try:
        create_concept_map()
    except ImportError as e:
        print(
            "Missing libraries for visualization. Please install matplotlib and networkx."
        )
        print(f"Error: {e}")
