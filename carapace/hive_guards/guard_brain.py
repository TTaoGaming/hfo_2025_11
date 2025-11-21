#!/usr/bin/env python3
import yaml
from pathlib import Path
from typing import List, Dict

# Configuration
BRAIN_DIR = Path("brain")
REGISTRY_FILE = BRAIN_DIR / "concepts.yaml"


def load_registry() -> Dict:
    if not REGISTRY_FILE.exists():
        print(f"❌ Registry not found: {REGISTRY_FILE}")
        return {"concepts": []}
    with open(REGISTRY_FILE, "r") as f:
        return yaml.safe_load(f)


def check_concept_integrity(concept: Dict) -> List[str]:
    issues = []
    name = concept.get("name", "Unknown")
    feature_file = BRAIN_DIR / concept.get("feature", "")
    summary_file = BRAIN_DIR / concept.get("summary", "")
    # status = concept.get("status", "Draft") # Unused

    # 1. Check Feature File
    if not feature_file.name:
        issues.append(f"[{name}] Missing 'feature' field in registry.")
    elif not feature_file.exists():
        issues.append(f"[{name}] Feature file missing: {feature_file}")

    # 2. Check Summary File
    if not summary_file.name:
        issues.append(f"[{name}] Missing 'summary' field in registry.")
    elif not summary_file.exists():
        issues.append(f"[{name}] Summary file missing: {summary_file}")
    elif summary_file.suffix != ".md":
        issues.append(
            f"[{name}] Summary file must be Markdown (.md), found: {summary_file.suffix}"
        )
    else:
        # 3. Check for Mermaid in Summary
        try:
            content = summary_file.read_text()
            if "mermaid" not in content.lower():
                issues.append(
                    f"[{name}] Summary file missing Mermaid diagram: {summary_file}"
                )
        except Exception as e:
            issues.append(f"[{name}] Error reading summary file: {e}")

    return issues


def find_slop(registry: Dict) -> List[str]:
    registered_files = {
        REGISTRY_FILE.name,
        "README.md",
        "registry.yaml",
        "file_structure_governance.md",
    }
    for concept in registry.get("concepts", []):
        if concept.get("feature"):
            registered_files.add(concept["feature"])
        if concept.get("summary"):
            registered_files.add(concept["summary"])

    # Allow subdirectories for now, just check root files
    all_files = [f.name for f in BRAIN_DIR.glob("*") if f.is_file()]

    slop = []
    for f in all_files:
        if f not in registered_files:
            slop.append(f)

    return slop


def main():
    print("🛡️  HIVE GUARD: Brain Integrity Check")
    print("=====================================")

    registry = load_registry()
    concepts = registry.get("concepts", [])
    print(f"🔍 Found {len(concepts)} concepts in registry.")

    all_issues = []
    for concept in concepts:
        issues = check_concept_integrity(concept)
        all_issues.extend(issues)

    if all_issues:
        print("\n❌ Integrity Violations:")
        for issue in all_issues:
            print(f"  - {issue}")
    else:
        print("\n✅ All registered concepts are valid.")

    print("\n🧹 Checking for AI Slop (Unregistered Files)...")
    slop = find_slop(registry)
    if slop:
        print(f"⚠️  Found {len(slop)} unregistered files in {BRAIN_DIR}:")
        for s in slop:
            print(f"  - {s}")
    else:
        print("✨ No slop found. Brain is clean.")

    if all_issues or slop:
        exit(1)
    else:
        exit(0)


if __name__ == "__main__":
    main()
