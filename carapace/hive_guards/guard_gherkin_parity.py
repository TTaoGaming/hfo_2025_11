#!/usr/bin/env python3
"""
🛡️ Hive Guard: Gherkin-Code Parity
Ensures that every Intent (.feature) has a corresponding Verification (.py).
"""

import sys
from pathlib import Path


def check_parity():
    print("🛡️  Scanning Brain for Intent (Gherkin)...")

    root_dir = Path(__file__).parent.parent.parent
    brain_dir = root_dir / "brain"
    # We now check body/hands for the generated implementation/tests
    hands_dir = root_dir / "body" / "hands"

    # 1. Get all Feature files
    feature_files = list(brain_dir.glob("*.feature"))
    if not feature_files:
        print("⚠️  No feature files found in brain/")
        return True

    print(f"   Found {len(feature_files)} feature files.")

    # 2. Get all Implementation files in body/hands
    # Genesis generates them as <feature_slug>.py
    hand_files = list(hands_dir.glob("*.py"))
    hand_filenames = [f.name for f in hand_files]

    # 3. Check Mapping
    missing_impls = []

    for feature in feature_files:
        feature_slug = feature.stem.lower().replace(" ", "_")
        expected_file = f"{feature_slug}.py"

        if expected_file in hand_filenames:
            print(f"   ✅ {feature.name} -> {expected_file}")
        else:
            print(f"   ❌ {feature.name} -> MISSING IMPLEMENTATION ({expected_file})")
            missing_impls.append(feature.name)

    if missing_impls:
        print(
            f"\n🚫 Parity Check Failed! {len(missing_impls)} features are missing implementations."
        )
        print("   Run 'python genesis.py evolve' to generate missing bodies.")
        sys.exit(1)

    print("\n✅ All Intents are Verified.")
    sys.exit(0)


if __name__ == "__main__":
    check_parity()
