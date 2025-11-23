"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 8308d916-f17b-46bd-a34a-578eade0a1ea
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.444237+00:00'
    generation: 51
  topos:
    address: body/digestion/import_gen43.py
    links: []
  telos:
    viral_factor: 0.0
    meme: import_gen43.py
"""

import json
import networkx as nx
from pathlib import Path

# 🐜 GEN 43 IMPORTER
# Role: Assimilator
# Mission: Import Gen 43 database into the collective memory.

DB_PATH = Path(
    "memory/procedural/gen_1_50_codebase/HFO_2025_11_19/hfo_gem/gen_43/hfo_memory_backup.json"
)
GRAPH_PATH = Path("memory/semantic/knowledge_graph.json")
VECTOR_STORE_PATH = Path("memory/semantic/gen43_vector_store.ndjson")


def load_graph() -> nx.DiGraph:
    if GRAPH_PATH.exists():
        with open(GRAPH_PATH, "r") as f:
            data = json.load(f)
            return nx.node_link_graph(data)
    return nx.DiGraph()


def save_graph(G: nx.DiGraph):
    data = nx.node_link_data(G)
    with open(GRAPH_PATH, "w") as f:
        json.dump(data, f, indent=2)
    print(f"💾 Graph saved to {GRAPH_PATH} with {len(G.nodes)} nodes.")


def import_db():
    print(f"🐜 Importing Gen 43 from {DB_PATH}...")

    if not DB_PATH.exists():
        print(f"❌ Database not found: {DB_PATH}")
        return

    G = load_graph()
    # initial_node_count = len(G.nodes)

    knowledge_items = []
    imported_nodes = 0

    with open(DB_PATH, "r", encoding="utf-8") as f:
        # Check format again (NDJSON vs List)
        first_char = f.read(1)
        f.seek(0)

        iterator = []
        if first_char == "[":
            print("📦 Loading JSON List...")
            iterator = json.load(f)
        else:
            print("📦 Streaming NDJSON...")
            iterator = (json.loads(line) for line in f if line.strip())

        for item in iterator:
            mem_type = item.get("memory_type", "unknown")

            if mem_type in ["digest", "mission"]:
                # Import as Node
                node_id = f"gen43_{item.get('id')}"

                # Map attributes
                attrs = {
                    "id": node_id,
                    "type": f"gen43_{mem_type}",
                    "source_id": item.get("source_id"),
                    "content": item.get("content"),
                    "trust_level": item.get("trust_level"),
                    "created_at": item.get("created_at"),
                    "source": "gen43_backup",
                    "title": f"Gen 43 {mem_type.capitalize()} {item.get('id')}",
                }

                # Add to graph
                G.add_node(node_id, **attrs)
                imported_nodes += 1

            elif mem_type == "knowledge":
                # Save to Vector Store
                knowledge_items.append(item)

    # Save Graph
    if imported_nodes > 0:
        print(f"✅ Imported {imported_nodes} nodes (Digests/Missions).")
        save_graph(G)
    else:
        print("⚠️ No new nodes imported.")

    # Save Vector Store
    if knowledge_items:
        print(
            f"💾 Saving {len(knowledge_items)} knowledge chunks to {VECTOR_STORE_PATH}..."
        )
        with open(VECTOR_STORE_PATH, "w", encoding="utf-8") as f:
            for item in knowledge_items:
                f.write(json.dumps(item) + "\n")
        print("✅ Vector Store saved.")


if __name__ == "__main__":
    import_db()
