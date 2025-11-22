import sys
import subprocess

# Install dependencies if not present
try:
    import networkx
    import matplotlib
    import pandas
    import pyvis
    import sklearn
except ImportError:
    print("Installing dependencies...")
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "pip",
            "install",
            "networkx",
            "matplotlib",
            "pandas",
            "pyvis",
            "scikit-learn",
        ]
    )

import networkx as nx
import pandas as pd
import json
import os
from pathlib import Path
from pyvis.network import Network

# Set paths
# Assuming script is run from workspace root or scripts/
WORKSPACE_ROOT = Path(os.getcwd())
if WORKSPACE_ROOT.name == "scripts":
    WORKSPACE_ROOT = WORKSPACE_ROOT.parent

GML_PATH = WORKSPACE_ROOT / "memory/semantic/knowledge_graph/evolution_graph.gml"
JSON_PATH = WORKSPACE_ROOT / "memory/semantic/knowledge_graph.json"
OUTPUT_HTML = WORKSPACE_ROOT / "knowledge_graph_interactive.html"
OUTPUT_MERMAID = WORKSPACE_ROOT / "core_memory.mmd"

print(f"Working directory: {os.getcwd()}")
print(f"Looking for GML at: {GML_PATH}")

# 1. Load Data
G = None
if GML_PATH.exists():
    try:
        print(f"Loading GML from {GML_PATH}...")
        G = nx.read_gml(GML_PATH)
        print(f"Successfully loaded GML. Nodes: {len(G.nodes)}, Edges: {len(G.edges)}")
    except Exception as e:
        print(f"Error loading GML: {e}")

if G is None and JSON_PATH.exists():
    try:
        print(f"Loading JSON from {JSON_PATH}...")
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
        G = nx.node_link_graph(data)
        print(f"Successfully loaded JSON. Nodes: {len(G.nodes)}, Edges: {len(G.edges)}")
    except Exception as e:
        print(f"Error loading JSON: {e}")

if G is None:
    print("No graph data found. Creating a sample graph.")
    G = nx.gnm_random_graph(20, 30, directed=True)
    for i in G.nodes:
        G.nodes[i]["label"] = f"Node_{i}"

# 2. Detect Hallucinations (Islands)
print("\n--- Hallucination Detection ---")
if nx.is_directed(G):
    components = list(nx.weakly_connected_components(G))
else:
    components = list(nx.connected_components(G))

components.sort(key=len, reverse=True)
main_component = components[0]
islands = components[1:]

print(f"Main Knowledge Base Size: {len(main_component)} nodes")
print(f"Disconnected Islands (Potential Hallucinations): {len(islands)}")

if islands:
    print("Top 5 Largest Islands:")
    for i, comp in enumerate(islands[:5]):
        labels = [G.nodes[n].get("label", n) for n in list(comp)[:3]]
        print(f"  Island {i+1} ({len(comp)} nodes): {labels}...")

# 3. Generate Interactive HTML (PyVis)
print(f"\n--- Generating Interactive Map ({OUTPUT_HTML}) ---")
net = Network(
    height="900px",
    width="100%",
    bgcolor="#1a1a1a",
    font_color="white",
    select_menu=True,
    filter_menu=True,
)

# Custom Physics options for better stability
net.set_options(
    """
var options = {
  "nodes": {
    "font": {
      "size": 16,
      "face": "tahoma"
    },
    "scaling": {
      "min": 10,
      "max": 30
    }
  },
  "edges": {
    "color": {
      "inherit": true
    },
    "smooth": {
      "type": "continuous"
    }
  },
  "physics": {
    "forceAtlas2Based": {
      "gravitationalConstant": -50,
      "centralGravity": 0.01,
      "springLength": 100,
      "springConstant": 0.08
    },
    "maxVelocity": 50,
    "solver": "forceAtlas2Based",
    "timestep": 0.35,
    "stabilization": {
      "enabled": true,
      "iterations": 1000
    }
  }
}
"""
)

# Visualize Main Component + Top Islands (limit to avoid browser crash)
nodes_to_viz = set(list(main_component)[:600])
for comp in islands[:30]:
    nodes_to_viz.update(comp)

subgraph = G.subgraph(nodes_to_viz).copy()  # Create a copy to modify attributes

# Calculate centrality for sizing
centrality = nx.degree_centrality(subgraph)

# Enhance Nodes with Visuals (Colors, Tooltips, Sizes)
for node_id in subgraph.nodes:
    node = subgraph.nodes[node_id]

    # 1. Tooltip (Title)
    # Extract attributes safely
    label = node.get("label", str(node_id))
    concept = node.get("concept", "N/A")
    gen = node.get("gen", "N/A")
    filename = node.get("filename", "N/A")

    tooltip_html = f"""
    <div style='font-family: sans-serif; padding: 10px; background: white; color: black; border-radius: 5px;'>
        <b>ID:</b> {node_id}<br>
        <b>Label:</b> {label}<br>
        <hr>
        <b>Concept:</b> {concept}<br>
        <b>Generation:</b> {gen}<br>
        <b>File:</b> {filename}
    </div>
    """
    node["title"] = tooltip_html

    # 2. Size (based on centrality)
    # Base size 10, max additional 40 based on centrality
    node["value"] = 10 + (centrality.get(node_id, 0) * 100)

    # 3. Color (Main vs Island)
    if node_id in main_component:
        node["group"] = "Main Memory"
        node["color"] = "#4da6ff"  # Blue
    else:
        node["group"] = "Fragmented/Hallucination"
        node["color"] = "#ff6b6b"  # Red

net.from_nx(subgraph)

# Add legend-like data (PyVis doesn't have a native legend, but groups help)
# The 'select_menu' and 'filter_menu' will use the groups we assigned.

try:
    net.save_graph(str(OUTPUT_HTML))
    print(f"✅ Interactive graph saved to: {OUTPUT_HTML}")
except Exception as e:
    print(f"Error saving HTML: {e}")

# 4. Export Mermaid & Generate Dashboard
print("\n--- Exporting Mermaid & Dashboard ---")
DASHBOARD_PATH = WORKSPACE_ROOT / "memory/VISUALIZATION_DASHBOARD.md"

try:
    # Generate Mermaid Content
    centrality = nx.degree_centrality(G)
    # Get top 15 nodes
    top_nodes = sorted(centrality, key=centrality.get, reverse=True)[:15]

    # Get subgraph of top nodes + their immediate neighbors to ensure connections
    core_nodes = set(top_nodes)
    for n in top_nodes:
        core_nodes.update(list(G.neighbors(n)))

    # Limit to reasonable size for Mermaid (max 50 nodes)
    if len(core_nodes) > 50:
        core_nodes = list(core_nodes)[:50]

    subgraph_core = G.subgraph(core_nodes)

    mermaid_lines = ["graph TD"]

    def sanitize(text):
        return (
            str(text)
            .replace(" ", "_")
            .replace(".", "_")
            .replace("/", "_")
            .replace("-", "_")
            .replace(":", "_")
            .replace("(", "")
            .replace(")", "")
        )

    # Add edges
    for u, v in subgraph_core.edges():
        u_safe = sanitize(u)
        v_safe = sanitize(v)
        u_label = str(G.nodes[u].get("label", u)).replace('"', "'")[
            :20
        ]  # Truncate labels
        v_label = str(G.nodes[v].get("label", v)).replace('"', "'")[:20]
        mermaid_lines.append(f'    {u_safe}["{u_label}"] --> {v_safe}["{v_label}"]')

    mermaid_content = "\n".join(mermaid_lines)

    # Save raw mermaid
    with open(OUTPUT_MERMAID, "w") as f:
        f.write(mermaid_content)

    # Generate Dashboard Markdown
    dashboard_content = f"""# 🧠 Memory Visualization Dashboard
> **Status**: {"🔴 Fragmented" if len(islands) > 10 else "🟢 Healthy"}
> **Generated**: {pd.Timestamp.now()}
> **Nodes**: {len(G.nodes)} | **Edges**: {len(G.edges)} | **Islands**: {len(islands)}

## 🗺️ Navigation
*   **[Launch Tactical Holomap (Interactive HTML)](../knowledge_graph_interactive.html)**
    *   *Use this for deep dives, zooming, and exploring specific clusters.*

## 💎 Strategic Core (Top Concepts)
*This map shows the central nervous system of the Hive.*

```mermaid
{mermaid_content}
```

## 🏝️ Hallucination Report (Disconnected Islands)
*These subgraphs are isolated from the main memory. They are likely hallucinations or stale backups.*

"""
    for i, comp in enumerate(islands[:10]):
        labels = [str(G.nodes[n].get("label", n)) for n in list(comp)[:3]]
        dashboard_content += f"### 🔴 Island {i+1} ({len(comp)} nodes)\n"
        dashboard_content += f"*   **Sample Nodes**: {', '.join(labels)}...\n"
        dashboard_content += (
            "*   **Action**: `Assimilator` should weave or prune these.\n\n"
        )

    if len(islands) > 10:
        dashboard_content += f"*...and {len(islands) - 10} more islands.*"

    with open(DASHBOARD_PATH, "w") as f:
        f.write(dashboard_content)

    print(f"✅ Dashboard saved to: {DASHBOARD_PATH}")
    print(f"✅ Mermaid saved to: {OUTPUT_MERMAID}")

except Exception as e:
    print(f"Error exporting Mermaid/Dashboard: {e}")
    import traceback

    traceback.print_exc()

print("\nDone! Open 'memory/VISUALIZATION_DASHBOARD.md' to view the report.")
