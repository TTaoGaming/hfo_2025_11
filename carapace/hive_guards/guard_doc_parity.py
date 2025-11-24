#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: guard-doc-parity
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.8
    decay: 0.1
    created: '2025-11-23T12:10:00+00:00'
    generation: 51
  topos:
    address: carapace/hive_guards/guard_doc_parity.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_doc_parity.py
"""

import sys
import yaml
from pathlib import Path


def extract_header(content):
    """Extracts the Hexagon YAML dictionary from MD file content."""
    try:
        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 2:
                data = yaml.safe_load(parts[1])
                if data and "hexagon" in data:
                    return data["hexagon"]
    except Exception:
        pass
    return None


def check_doc_parity():
    print("🛡️  Scanning Documentation <-> Intent Parity...")

    root_dir = Path(__file__).parent.parent.parent
    brain_dir = root_dir / "brain"

    # 1. Find all Intent (Feature) files
    feature_files = list(brain_dir.rglob("*.feature"))
    feature_map = {f.name: f for f in feature_files}

    if not feature_files:
        print("⚠️  No feature files found in brain/")
        return True

    print(f"   Found {len(feature_files)} Intent Definitions (.feature)")

    # 2. Find all Documentation (Markdown) files
    md_files = list(root_dir.rglob("*.md"))
    # Exclude some dirs
    md_files = [
        f for f in md_files if "node_modules" not in str(f) and "venv" not in str(f)
    ]

    print(f"   Found {len(md_files)} Documentation Files (.md)")

    # 3. Build Linkage Graph
    linked_features = set()
    broken_links = []

    for md_file in md_files:
        try:
            content = md_file.read_text()
            header = extract_header(content)

            if header and "topos" in header and "links" in header["topos"]:
                links = header["topos"]["links"]
                if not links:
                    continue

                for link in links:
                    # Link might be a path "brain/identity_core.feature" or just filename
                    link_name = Path(link).name

                    if link_name.endswith(".feature"):
                        if link_name in feature_map:
                            linked_features.add(link_name)
                            # print(f"   🔗 {md_file.name} -> {link_name}")
                        else:
                            broken_links.append((md_file.name, link))
        except Exception:
            # print(f"   ⚠️ Error parsing {md_file.name}: {e}")
            pass

    # 4. Report Results
    print("\n   --- Parity Report ---")

    # Check for Broken Links
    if broken_links:
        print(f"   ❌ Found {len(broken_links)} Broken Links in Documentation:")
        for md, link in broken_links:
            print(f"      - {md} links to missing '{link}'")
    else:
        print("   ✅ No broken links found.")

    # Check for Orphaned Features
    orphans = []
    for fname in feature_map:
        if fname not in linked_features:
            orphans.append(fname)

    if orphans:
        print(f"   ❌ Found {len(orphans)} Orphaned Intents (Not linked by any MD):")
        for orphan in orphans:
            print(f"      - {orphan}")
        return False
    else:
        print("   ✅ All Intents are Documented.")
        return True


if __name__ == "__main__":
    success = check_doc_parity()
    sys.exit(0 if success else 1)
