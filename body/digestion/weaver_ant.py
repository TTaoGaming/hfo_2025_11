import json
import re
import yaml
import networkx as nx
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime

# 🐜 THE WEAVER ANT
# Role: Assimilator / Graph Builder
# Mission: Weave individual crystals into a cohesive Knowledge Graph.

LIBRARY_PATH = Path("memory/semantic/library")
OUTPUT_GRAPH = Path("memory/semantic/knowledge_graph.json")
AUDIT_REPORT = Path("venom/audit_report.md")


def parse_frontmatter(content: str) -> Dict[str, Any]:
    """Extracts YAML frontmatter from Markdown."""
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if match:
        try:
            data = yaml.safe_load(match.group(1))
            if isinstance(data, dict):
                return data
            elif isinstance(data, list):
                # Handle case where YAML is a list (rare but possible)
                return {"_raw_list": data}
            else:
                return {}
        except yaml.YAMLError:
            return {}
    return {}


def extract_wikilinks(content: str) -> List[str]:
    """Extracts [[WikiLinks]] from content."""
    # Matches [[Target]] or [[Target|Label]]
    return re.findall(r"\[\[(.*?)(?:\|.*?)?\]\]", content)


def weave():
    print("🕷️  Weaver Ant: Awakening...")
    G = nx.DiGraph()

    # 1. Scan & Build Nodes
    files = list(LIBRARY_PATH.rglob("*.md"))
    print(f"🕷️  Scanning {len(files)} crystals...")

    node_map = {}  # Filename -> Path

    for file_path in files:
        try:
            content = file_path.read_text(encoding="utf-8")
            frontmatter = parse_frontmatter(content)

            # Extract links from content
            links = extract_wikilinks(content)

            # Extract links from YAML 'related_files' or 'concepts'
            if "related_files" in frontmatter and isinstance(
                frontmatter["related_files"], list
            ):
                links.extend([str(f) for f in frontmatter["related_files"]])

            # Use filename (without extension) as ID
            node_id = file_path.stem
            node_map[node_id] = str(file_path)

            G.add_node(node_id, **frontmatter, filepath=str(file_path))

            # Store raw links for edge building
            G.nodes[node_id]["_raw_links"] = links

        except Exception as e:
            print(f"⚠️  Error reading {file_path}: {e}")

    # 2. Build Edges
    print("🕸️  Weaving connections...")
    broken_links = []

    # Create a lookup map for fuzzy matching (filename -> node_id)
    # This handles cases where links include paths or extensions
    # lookup_map = {nid: nid for nid in G.nodes}

    for node_id in G.nodes:
        raw_links = G.nodes[node_id].get("_raw_links", [])
        for link in raw_links:
            # Clean the link
            target_raw = link.split("|")[0].strip()

            # Strategy 1: Exact Match
            if target_raw in G.nodes:
                G.add_edge(node_id, target_raw)
                continue

            # Strategy 2: Path/Extension Stripping
            # e.g. "hfo_gem/gen_30/HIVE_GUARDS_SPEC.md" -> "HIVE_GUARDS_SPEC"
            target_stem = Path(target_raw).stem
            if target_stem in G.nodes:
                G.add_edge(node_id, target_stem)
                continue

            # Strategy 3: Failed
            broken_links.append({"source": node_id, "target": target_raw})

    # 3. Analyze
    orphans = [n for n, d in G.degree() if d == 0]
    density = nx.density(G)
    components = nx.number_weakly_connected_components(G)

    print(f"📊 Graph Stats: {G.number_of_nodes()} Nodes, {G.number_of_edges()} Edges")
    print(f"🕸️  Density: {density:.4f}")
    print(f"🏝️  Orphans: {len(orphans)}")
    print(f"🔗 Broken Links: {len(broken_links)}")

    # 4. Save Graph
    data = nx.node_link_data(G)
    OUTPUT_GRAPH.write_text(json.dumps(data, indent=2))
    print(f"💾 Graph saved to {OUTPUT_GRAPH}")

    # 5. Generate Audit Report
    report = f"""# 🕷️ Weaver Audit Report
**Date**: {datetime.now().isoformat()}
**Status**: {"🟢 Healthy" if density > 0.1 else "🟡 Fragmented"}

## 📊 Statistics
*   **Nodes**: {G.number_of_nodes()}
*   **Edges**: {G.number_of_edges()}
*   **Density**: {density:.4f}
*   **Components**: {components}

## 🏝️ Orphan Nodes ({len(orphans)})
*(Nodes with no incoming or outgoing connections)*
"""
    for orphan in orphans[:20]:
        report += f"*   `{orphan}`\n"
    if len(orphans) > 20:
        report += f"*   ... and {len(orphans) - 20} more.\n"

    report += f"\n## 🔗 Broken Links ({len(broken_links)})\n*(Links pointing to non-existent nodes)*\n"
    for link in broken_links[:20]:
        report += f"*   `{link['source']}` -> `{link['target']}`\n"
    if len(broken_links) > 20:
        report += f"*   ... and {len(broken_links) - 20} more.\n"

    AUDIT_REPORT.write_text(report)
    print(f"📝 Audit Report saved to {AUDIT_REPORT}")


if __name__ == "__main__":
    weave()
