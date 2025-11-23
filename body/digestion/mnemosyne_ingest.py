"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 56c965ee-b8c2-412b-9e2a-150073bf12f2
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.440062+00:00'
    generation: 51
  topos:
    address: body/digestion/mnemosyne_ingest.py
    links: []
  telos:
    viral_factor: 0.0
    meme: mnemosyne_ingest.py
"""

import re
from pathlib import Path
from typing import Optional

# 🧠 MNEMOSYNE INGESTION PROTOCOL
# Purpose: Bulk ingest historical HFO Gems (Gen 1-50) and refine them into Semantic Memory.

SOURCE_DIRS = [
    Path("memory/procedural/gen_1_50_codebase/HiveFleetObsidian_hfo_gem"),
    Path("memory/procedural/gen_1_50_codebase/HFO_2025_11_19/hfo_gem"),
]
DEST_DIR = Path("memory/semantic/library/evolutionary")


def ensure_dest():
    DEST_DIR.mkdir(parents=True, exist_ok=True)


def find_gem_file(gen_dir: Path) -> Optional[Path]:
    """Finds the primary gem file in a generation directory."""
    # Prioritize specific filenames
    candidates = [
        "HFO_GENE_SEED_GEN43.md",  # Gen 43 specific
        "original_gem.md",
        "summary.md",
        "README.md",
        "deep_dive.md",
    ]
    for cand in candidates:
        f = gen_dir / cand
        if f.exists():
            return f
    # Fallback: look for any .md file
    mds = list(gen_dir.glob("*.md"))
    if mds:
        # Sort by size (largest likely contains the most info) or name
        mds.sort(key=lambda x: x.stat().st_size, reverse=True)
        return mds[0]
    return None


def extract_bluf(content: str) -> str:
    """Extracts the BLUF or first paragraph."""
    match = re.search(r"(?i)##\s*BLUF(.*?)(##|$)", content, re.DOTALL)
    if match:
        return match.group(1).strip()

    # Fallback to first non-header paragraph
    lines = content.split("\n")
    for line in lines:
        if line.strip() and not line.startswith("#") and not line.startswith("---"):
            return line.strip()
    return "No summary available."


def refine_gem(gen_num: int, source_file: Path):
    """Refines a raw gem into a Semantic Crystal."""
    content = source_file.read_text(encoding="utf-8")
    bluf = extract_bluf(content)

    # Create Standardized Header
    refined_content = f"""---
title: "Evolutionary Gem: Generation {gen_num}"
status: Archived
type: Evolutionary Memory
tags:
  - evolution
  - generation_{gen_num}
  - history
  - gem
source_file: "{source_file.relative_to(Path.cwd())}"
---

# 💎 Generation {gen_num}: Refined Memory

## ⚡ BLUF (Summary)
{bluf}

## 📜 Original Artifact
> *Ingested from {source_file.name}*

---
{content}
"""

    dest_file = DEST_DIR / f"gen_{gen_num:02d}_refined.md"
    dest_file.write_text(refined_content, encoding="utf-8")
    print(f"✨ Refined Gen {gen_num} -> {dest_file}")


def run_ingestion():
    print("🦁 Mnemosyne: Awakening...")
    ensure_dest()

    found_gens = {}  # Map gen_num -> source_path (to handle duplicates/overwrites)

    for source_dir in SOURCE_DIRS:
        if not source_dir.exists():
            print(f"⚠️ Source directory not found: {source_dir}")
            continue

        print(f"📂 Scanning {source_dir}...")
        # Scan for Gen folders
        gen_dirs = sorted(
            [
                d
                for d in source_dir.iterdir()
                if d.is_dir() and d.name.startswith("gen_")
            ]
        )

        for d in gen_dirs:
            try:
                # Extract number
                # Handle gen_33.1 case by taking just the integer part for now, or float?
                # The user asked for 1-50, let's stick to integers for the main sequence
                num_part = d.name.replace("gen_", "")
                if "." in num_part:
                    # Handle sub-versions if needed, for now let's skip or map to int
                    # gen_33.1 -> 33 (might overwrite 33)
                    gen_num = int(float(num_part))
                else:
                    gen_num = int(num_part)

                gem_file = find_gem_file(d)
                if gem_file:
                    # If we already found this gen, we overwrite if this one seems "better" or just last one wins
                    # Since HFO_2025_11_19 is likely newer, it comes second in the list and will overwrite
                    found_gens[gen_num] = gem_file
                    refine_gem(gen_num, gem_file)
                else:
                    print(f"⚠️  Gen {gen_num} in {d.name}: No markdown crystal found.")

            except ValueError:
                continue

    print("\n📊 Ingestion Report")
    print(f"✅ Processed {len(found_gens)} unique generations.")

    # Gap Analysis
    all_gens = set(found_gens.keys())
    missing = []
    for i in range(1, 51):
        if i not in all_gens:
            missing.append(i)

    if missing:
        print(f"❌ Missing Generations: {missing}")
    else:
        print("✅ All Generations 1-50 present.")


if __name__ == "__main__":
    run_ingestion()
