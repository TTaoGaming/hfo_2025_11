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
    venom_dir = root_dir / "venom"

    # 1. Get all Feature files
    feature_files = list(brain_dir.glob("*.feature"))
    if not feature_files:
        print("⚠️  No feature files found in brain/")
        return True

    print(f"   Found {len(feature_files)} feature files.")

    # 2. Get all Test files
    test_files = list(venom_dir.glob("test_*.py")) + list(
        (venom_dir / "steps").glob("test_*.py")
    )
    test_filenames = [f.name for f in test_files]

    # 3. Check Mapping
    missing_tests = []

    for feature in feature_files:
        feature_name = feature.stem  # e.g., "swarm_workflow"

        # Expected test names: test_<name>.py or test_<name>_steps.py
        expected_1 = f"test_{feature_name}.py"
        expected_2 = f"test_{feature_name}_steps.py"

        if expected_1 in test_filenames or expected_2 in test_filenames:
            print(f"   ✅ {feature.name} -> Verified")
        else:
            print(f"   ❌ {feature.name} -> MISSING TEST")
            missing_tests.append(feature.name)

    if missing_tests:
        print(
            f"\n🚫 Parity Check Failed! {len(missing_tests)} features are missing tests."
        )
        print(
            "   Please create a test file in venom/ or venom/steps/ for each feature."
        )
        sys.exit(1)

    print("\n✅ All Intents are Verified.")
    sys.exit(0)


if __name__ == "__main__":
    check_parity()
