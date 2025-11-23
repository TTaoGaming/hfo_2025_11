"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 6791988e-f661-48cf-bf92-f87f4d19f740
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.441273+00:00'
  topos:
    address: body/digestion/fractal_archaeologist.py
    links: []
  telos:
    viral_factor: 0.0
    meme: fractal_archaeologist.py
"""

import json
import re
from pathlib import Path
from typing import Set

# 🦕 THE FRACTAL ARCHAEOLOGIST
# Role: Miner / Pattern Finder
# Mission: Mine the evolutionary history for "Lost Gems" and persistent patterns.

LIBRARY_PATH = Path("memory/semantic/library")
REPORT_PATH = Path("venom/archaeology_report.md")

# Concepts to hunt for
TARGET_CONCEPTS = [
    "Tectangle",
    "Virtualization",
    "Stigmergy",
    "Hexagon",
    "Cognitive Symbiote",
    "Karmic Knife",
    "Obsidian Hourglass",
    "Genesis",
    "R.A.P.T.O.R.",
    "Byzantine",
    "Holon",
    "Vector DB",
    "Knowledge Graph",
]


def extract_concepts(content: str) -> Set[str]:
    found = set()
    content_lower = content.lower()
    for concept in TARGET_CONCEPTS:
        if concept.lower() in content_lower:
            found.add(concept)
    return found


def run_dig():
    print("🦕 Fractal Archaeologist: Starting the dig...")

    if not LIBRARY_PATH.exists():
        print(f"❌ Library path not found: {LIBRARY_PATH}")
        return

    # Scan gen_* folders
    gen_folders = sorted(list(LIBRARY_PATH.glob("gen_*")))
    print(f"📜 Found {len(gen_folders)} evolutionary strata (folders).")

    history = {}  # Gen -> Concepts
    concept_timeline = {c: [] for c in TARGET_CONCEPTS}

    for folder in gen_folders:
        # Extract Gen number from folder name "gen_XX"
        match = re.search(r"gen_(\d+)", folder.name)
        if not match:
            continue

        gen_num = int(match.group(1))

        # Read all MD files in the folder
        folder_concepts = set()
        for f in folder.glob("*.md"):
            try:
                content = f.read_text(encoding="utf-8")
                folder_concepts.update(extract_concepts(content))
            except Exception:
                pass

        history[gen_num] = folder_concepts

        for c in folder_concepts:
            concept_timeline[c].append(gen_num)

    # Analysis
    print("🔍 Analyzing patterns...")

    report = f"""# 🦕 Fractal Archaeology Report
**Date**: {json.dumps(str(Path('.').stat().st_mtime))} (Simulated)
**Strata Analyzed**: {len(gen_folders)} Generations

## 💎 Concept Timeline
"""
    for concept, gens in concept_timeline.items():
        if not gens:
            report += f"- **{concept}**: ❌ Never found (Lost?)\n"
        else:
            gens.sort()
            # Summarize ranges if possible, or just list
            report += f"- **{concept}**: Found in Gen {gens}\n"

    # Lost Gems Analysis
    report += "\n## 🏺 Potential Lost Gems\n"
    # Concepts found in early gens (<20) but not in late gens (>40)
    late_gens = [g for g in history.keys() if g >= 40]
    early_gens = [g for g in history.keys() if g <= 20]

    if late_gens and early_gens:
        late_concepts = set()
        for g in late_gens:
            late_concepts.update(history.get(g, set()))

        early_concepts = set()
        for g in early_gens:
            early_concepts.update(history.get(g, set()))

        lost = early_concepts - late_concepts
        if lost:
            for c in lost:
                report += f"- **{c}**: Present in early gens, missing in late gens.\n"
        else:
            report += "No clear 'Lost Gems' from the target list.\n"

    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"📝 Report written to {REPORT_PATH}")
    print(report)


if __name__ == "__main__":
    run_dig()
