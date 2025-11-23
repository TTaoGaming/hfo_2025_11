"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 2e456cf7-c397-41b7-a137-c94515239437
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.559126+00:00'
  topos:
    address: carapace/hive_guards/guard_brain.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_brain.py
"""

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
        # 3. Check Content Format (Swarmlord of Webs)
        try:
            content = summary_file.read_text(encoding="utf-8")

            # A. YAML Header
            if not content.startswith("---"):
                issues.append(
                    f"[{name}] Missing YAML Frontmatter (must start with ---)"
                )

            # B. BLUF
            if "BLUF" not in content and "Bottom Line Up Front" not in content:
                issues.append(f"[{name}] Missing BLUF (Bottom Line Up Front) section")

            # C. Matrix Table
            if "|" not in content:
                issues.append(f"[{name}] Missing Matrix Table (Markdown table syntax)")

            # D. Mermaid Diagrams (3+)
            mermaid_count = content.count("```mermaid")
            if mermaid_count < 3:
                issues.append(
                    f"[{name}] Insufficient Visuals: Found {mermaid_count} Mermaid diagrams, required 3+"
                )

        except Exception as e:
            issues.append(f"[{name}] Error reading summary file: {e}")

    return issues


def find_slop(registry: Dict) -> List[str]:
    # Load the main registry to get the allowlist
    main_registry_path = BRAIN_DIR / "registry.yaml"
    allowlist = []
    if main_registry_path.exists():
        with open(main_registry_path, "r") as reg_file:
            main_reg = yaml.safe_load(reg_file)
            # Navigate to organs.brain.allowlist
            try:
                allowlist = (
                    main_reg.get("organs", {}).get("brain", {}).get("allowlist", [])
                )
            except AttributeError:
                pass

    registered_files = {
        REGISTRY_FILE.name,
        "README.md",
        "registry.yaml",
        "file_structure_governance.md",
        "BRAIN_AUDIT_LOG.md",
        "holonic_stigmergy_architecture.md",
        "configuration_ssot.yaml",
    }
    # Add allowlisted files
    for filename in allowlist:
        registered_files.add(str(filename))

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
