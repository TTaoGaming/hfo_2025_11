import json
import os
from pathlib import Path
from typing import List, Dict

# Define the target memory file
MEMORY_PATH = "memory/evolutionary/prompt_genes.json"
LIBRARY_PATH = "memory/semantic/library"


def load_existing_genes() -> List[Dict]:
    if os.path.exists(MEMORY_PATH):
        with open(MEMORY_PATH, "r") as f:
            return json.load(f)
    return []


def save_genes(genes: List[Dict]):
    os.makedirs(os.path.dirname(MEMORY_PATH), exist_ok=True)
    with open(MEMORY_PATH, "w") as f:
        json.dump(genes, f, indent=2)


def extract_genes_from_library():
    print("🧬 Extracting Evolutionary Genes from Ancestral Memory...")

    genes = load_existing_genes()
    existing_names = {g["strategy_name"] for g in genes}

    # Heuristic Rules for Extraction
    # 1. Look for "Playbook" files -> Extract "Navigator" strategies
    # 2. Look for "Pattern" files -> Extract "Workflow" strategies

    library = Path(LIBRARY_PATH)

    # Scan for Playbooks
    for file_path in library.rglob("*Playbook.md"):
        print(f"   📖 Found Playbook: {file_path.name}")
        content = file_path.read_text()

        # Simple extraction: Use the first paragraph as the instruction
        instruction = content.split("\n\n")[1] if "\n\n" in content else content[:200]
        name = file_path.stem.replace("_", " ")

        if name not in existing_names:
            genes.append(
                {
                    "strategy_name": name,
                    "instruction": f"Follow the {name} protocol: {instruction[:300]}...",
                    "success_rate": 0.6,  # Give it a slight boost as it's a playbook
                    "usage_count": 0,
                }
            )
            existing_names.add(name)
            print(f"      + Added Gene: {name}")

    # Scan for Patterns
    for file_path in library.rglob("*PATTERN*.md"):
        print(f"   🧩 Found Pattern: {file_path.name}")
        content = file_path.read_text()

        name = file_path.stem.replace("_", " ")
        if name not in existing_names:
            genes.append(
                {
                    "strategy_name": name,
                    "instruction": f"Apply the {name} pattern. Focus on structure and repeatability.",
                    "success_rate": 0.55,
                    "usage_count": 0,
                }
            )
            existing_names.add(name)
            print(f"      + Added Gene: {name}")

    # Scan for "Spiral Quorum" (Specific HFO Strategy)
    for file_path in library.rglob("*SPIRAL_QUORUM*.md"):
        print(f"   🌀 Found Spiral Quorum: {file_path.name}")
        genes.append(
            {
                "strategy_name": "Spiral Quorum",
                "instruction": "Execute a Spiral Quorum: Start with 1 agent, expand to 3, then 10. Validate consensus at each turn.",
                "success_rate": 0.8,  # High confidence in this core strategy
                "usage_count": 0,
            }
        )
        print("      + Added Gene: Spiral Quorum")

    save_genes(genes)
    print(f"✅ Extraction Complete. Total Genes: {len(genes)}")


if __name__ == "__main__":
    extract_genes_from_library()
