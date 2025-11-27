#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: guard-cynefin-c5
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.8
    decay: 0.1
    created: '2025-11-26T12:00:00Z'
    generation: 55
  topos:
    address: carapace/hive_guards/guard_cynefin_c5.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_cynefin_c5.py
"""

import sys
from pathlib import Path

VALID_C5 = {"Clear", "Complicated", "Complex", "Chaotic", "Confused"}


def check_file(path: Path) -> bool:
    content = path.read_text()

    # Look for Cynefin assignments or definitions
    # This is a heuristic check
    if "Cynefin" in content:
        # Check if any valid C5 term is present in the file if Cynefin is mentioned
        found_valid = any(term in content for term in VALID_C5)
        if not found_valid:
            print(f"❌ {path}: Mentions 'Cynefin' but no valid C5 term found {VALID_C5}")
            return False

        # Specific check for Pydantic fields if possible
        # e.g. cynefin_state: ... default="Simple" -> Should be "Clear"
        if 'default="Simple"' in content and "cynefin" in content.lower():
            print(f"❌ {path}: Uses deprecated 'Simple' state. Use 'Clear'.")
            return False

    return True


def main():
    print("🛡️  Running Cynefin C5 Guard...")
    root = Path(".")
    failed = False

    for path in root.rglob("*.py"):
        if (
            "venv" in str(path)
            or "archive" in str(path)
            or path.name == "guard_cynefin_c5.py"
        ):
            continue

        if not check_file(path):
            failed = True

    if failed:
        sys.exit(1)
    else:
        print("✅ Cynefin C5 Compliance Verified.")


if __name__ == "__main__":
    main()
