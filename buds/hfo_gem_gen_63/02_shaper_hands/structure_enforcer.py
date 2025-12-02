"""
---
holon:
  id: hfo-tool-structure-enforcer
  type: tool
  layer: forge
  intent: buds/hfo_gem_gen_63/brain/feature_structure_registry.feature
---
"""

import os
import yaml
import sys
from pathlib import Path

# Define the root of the Bud
BUD_ROOT = Path(__file__).parent.parent
REGISTRY_PATH = BUD_ROOT / "REGISTRY.yaml"

def load_registry():
    if not REGISTRY_PATH.exists():
        print(f"❌ REGISTRY.yaml not found at {REGISTRY_PATH}")
        sys.exit(1)
    
    with open(REGISTRY_PATH, "r") as f:
        return yaml.safe_load(f)

def check_structure(registry):
    print(f"🔍 Checking Structure for Bud: {BUD_ROOT.name}")
    print("-" * 40)
    
    organs = registry.get("organs", {})
    all_good = True
    
    # 1. Check Organs exist
    for organ_name, organ_data in organs.items():
        organ_path = BUD_ROOT / organ_data["path"]
        if not organ_path.exists():
            print(f"❌ Missing Organ: {organ_name} ({organ_path})")
            print(f"   ✨ Creating {organ_name}...")
            os.makedirs(organ_path, exist_ok=True)
            all_good = False # It was missing, but we fixed it.
        else:
            print(f"✅ Organ Found: {organ_name}")

    # 2. Check for Misplaced Files (e.g., in src/)
    src_path = BUD_ROOT / "src"
    if src_path.exists():
        print("\n⚠️  'src/' directory detected! This is deprecated in Gen 63.")
        files = list(src_path.glob("**/*"))
        if files:
            print(f"   Found {len(files)} files in src/ that need migration:")
            # for f in files:
            #     if f.is_file():
            #         print(f"   - {f.relative_to(BUD_ROOT)}")
            all_good = False
        else:
            print("   (src/ is empty, you can delete it)")

    # 3. Check Root Clutter
    print("\n🔍 Checking Root Clutter...")
    allowed_root_files = ["REGISTRY.yaml", "README.md", "AGENTS.md", "heartbeat_artifact.json"]
    for item in BUD_ROOT.iterdir():
        if item.is_file():
            if item.name not in allowed_root_files:
                print(f"⚠️  Unknown Root File: {item.name}")
                # all_good = False # Warning only

    print("-" * 40)
    if all_good:
        print("✨ Structure is Clean & Compliant.")
    else:
        print("🔧 Structure needs attention (Migration Required).")

if __name__ == "__main__":
    registry = load_registry()
    check_structure(registry)
