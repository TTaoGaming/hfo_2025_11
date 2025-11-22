import os
import yaml
import sys
import glob


def load_ssot():
    """Loads the Single Source of Truth configuration."""
    config_path = os.path.join("brain", "configuration_ssot.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def scan_files(forbidden_patterns):
    """Scans the body/ directory for forbidden patterns."""
    violations = []
    # Scan all python files in body/ recursively
    files = glob.glob("body/**/*.py", recursive=True)

    for file_path in files:
        with open(file_path, "r") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                for pattern_def in forbidden_patterns:
                    pattern = pattern_def["pattern"]
                    reason = pattern_def["reason"]
                    if (
                        pattern in line and "configuration_ssot" not in line
                    ):  # Ignore references to the config itself
                        violations.append(
                            {
                                "file": file_path,
                                "line": i + 1,
                                "content": line.strip(),
                                "pattern": pattern,
                                "reason": reason,
                            }
                        )
    return violations


def main():
    print("🛡️  Hive Guard: Configuration Drift Scanner")
    print("=========================================")

    try:
        config = load_ssot()
        forbidden = config["guards"]["forbidden_patterns"]
        print(f"🔍 Loaded {len(forbidden)} forbidden patterns from SSOT.")
    except Exception as e:
        print(f"❌ Failed to load SSOT: {e}")
        sys.exit(1)

    violations = scan_files(forbidden)

    if violations:
        print(f"\n🚨 FOUND {len(violations)} CONFIGURATION VIOLATIONS:")
        for v in violations:
            print(f"  ❌ {v['file']}:{v['line']}")
            print(f"     Pattern: '{v['pattern']}' -> {v['reason']}")
            print(f"     Code:    {v['content']}")
            print("")
        print(
            "❌ DRIFT DETECTED. Please refactor code to use brain/configuration_ssot.yaml or os.getenv()."
        )
        sys.exit(1)
    else:
        print("\n✅ No configuration drift detected. System is aligned with SSOT.")
        sys.exit(0)


if __name__ == "__main__":
    main()
