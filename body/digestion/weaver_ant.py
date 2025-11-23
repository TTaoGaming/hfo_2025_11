"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: c9ed7ce7-f851-4a97-8552-6f6d53c65063
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.436761+00:00'
  topos:
    address: body/digestion/weaver_ant.py
    links: []
  telos:
    viral_factor: 0.0
    meme: weaver_ant.py
"""

import json
import re
import yaml
import networkx as nx
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


# 🐜 THE WEAVER ANT
# Role: Assimilator / Graph Builder
# Mission: Weave individual crystals into a cohesive Knowledge Graph.

LIBRARY_PATH = Path("memory/semantic/library")
SEARCH_PATHS = [
    Path("brain"),
    Path("memory"),
    Path("eyes"),
    Path("body"),
    Path("."),  # Root for AGENTS.md, README.md
]
EXCLUDE_DIRS = {
    "venv",
    ".git",
    "__pycache__",
    "node_modules",
    "site-packages",
    ".pytest_cache",
}

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
    files = []
    for root_path in SEARCH_PATHS:
        if root_path == Path("."):
            # Just pick specific root files
            for f in [Path("AGENTS.md"), Path("README.md")]:
                if f.exists():
                    files.append(f)
            continue

        if not root_path.exists():
            continue

        for path in root_path.rglob("*.md"):
            # Check exclusions
            if any(part in EXCLUDE_DIRS for part in path.parts):
                continue
            files.append(path)

    print(f"🕷️  Scanning {len(files)} crystals across the Hive...")

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

            # Heuristic: Extract "Cognitive Symbiote" definition
            if "cognitive symbiote" in content.lower():
                if "concepts" not in frontmatter:
                    frontmatter["concepts"] = []
                if isinstance(frontmatter["concepts"], list):
                    if "Cognitive Symbiote" not in frontmatter["concepts"]:
                        frontmatter["concepts"].append("Cognitive Symbiote")

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
    OUTPUT_GRAPH.write_text(json.dumps(data, indent=2, cls=DateTimeEncoder))
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
