import json
from pathlib import Path

# 🌿 THE GRAPH GARDENER
# Role: Shaper / Healer
# Mission: Prune broken links and graft orphans to the central vine.

GRAPH_FILE = Path("memory/semantic/knowledge_graph.json")
HUB_NODE = "gen_50_README"  # The central anchor
HUB_PATH = "memory/semantic/library/infrastructure/gen_50_README.md"


def garden():
    print("🌿 Gardener: Entering the grove...")

    if not GRAPH_FILE.exists():
        print("❌ No graph found.")
        return

    data = json.loads(GRAPH_FILE.read_text())
    nodes = {n["id"]: n for n in data["nodes"]}
    edges = data["links"]

    # Identify Orphans (Nodes with 0 edges)
    # Note: Weaver's JSON has "links" as [{"source":..., "target":...}]
    connected_nodes = set()
    for link in edges:
        connected_nodes.add(link["source"])
        connected_nodes.add(link["target"])

    orphans = [nid for nid in nodes if nid not in connected_nodes]
    print(f"🍂 Found {len(orphans)} orphans.")

    # Graft Orphans to Hub
    grafted_count = 0
    for orphan_id in orphans:
        if orphan_id == HUB_NODE:
            continue

        node = nodes[orphan_id]
        file_path = Path(node.get("filepath", ""))

        if file_path.exists():
            try:
                content = file_path.read_text()
                # Append a footer link to the Hub
                footer = f"\n\n---\n**Grafted by Gardener**: [[{HUB_NODE}|Gen 50 Hub]]"
                file_path.write_text(content + footer)
                grafted_count += 1
                print(f"🌱 Grafted {orphan_id} -> {HUB_NODE}")
            except Exception as e:
                print(f"⚠️ Failed to graft {orphan_id}: {e}")

    print(f"✅ Grafted {grafted_count} orphans.")


if __name__ == "__main__":
    garden()
