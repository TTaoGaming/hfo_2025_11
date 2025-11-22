import glob
import os


def check_intents():
    feature_files = glob.glob("brain/*.feature")
    venom_files = glob.glob("venom/test_*.py")

    print(f"Found {len(feature_files)} feature files in brain/")
    print(f"Found {len(venom_files)} test files in venom/")

    implemented_count = 0
    placeholder_count = 0
    missing_count = 0

    results = []

    for feature_path in feature_files:
        feature_name = os.path.basename(feature_path)
        slug = feature_name.replace(".feature", "").replace("-", "_")

        # Try to find matching test file
        # Common patterns: test_{slug}.py, test_{slug_without_prefix}.py

        matching_test = None
        for vf in venom_files:
            if slug in vf:
                matching_test = vf
                break

        # Special cases mapping if needed (based on my manual observation)
        if not matching_test:
            if "capability_external_tools" in slug:
                if "venom/test_external_tools.py" in venom_files:
                    matching_test = "venom/test_external_tools.py"
            elif "workflow_obsidian_hourglass" in slug:
                if "venom/test_strategy_obsidian_hourglass.py" in venom_files:
                    matching_test = "venom/test_strategy_obsidian_hourglass.py"

        status = "MISSING"
        # details = ""

        if matching_test:
            with open(matching_test, "r") as f:
                content = f.read()
                if '@pytest.mark.skip(reason="Placeholder")' in content:
                    status = "PLACEHOLDER"
                    placeholder_count += 1
                elif "TODO: Implement actual steps" in content:
                    status = "PLACEHOLDER"
                    placeholder_count += 1
                elif "TODO: Implement steps" in content:
                    status = "PLACEHOLDER"
                    placeholder_count += 1
                elif "def test_" in content:
                    status = "IMPLEMENTED"
                    implemented_count += 1
                else:
                    status = "UNCERTAIN"
                    # details = "File exists but structure unclear"
        else:
            missing_count += 1

        results.append((feature_name, status, matching_test))

    print("\n--- Intent Implementation Status ---")
    print(f"{'Feature File':<50} | {'Status':<20} | {'Test File'}")
    print("-" * 100)
    for name, status, test_file in sorted(results, key=lambda x: x[1]):
        print(f"{name:<50} | {status:<20} | {test_file if test_file else 'N/A'}")

    print("\nSummary:")
    print(f"Total Intents: {len(feature_files)}")
    print(f"Implemented: {implemented_count}")
    print(f"Placeholders: {placeholder_count}")
    print(f"Missing Tests: {missing_count}")


if __name__ == "__main__":
    check_intents()
