#!/usr/bin/env python3
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 694892bf-13a2-4d47-9669-d1c38ac74567
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.566690+00:00'
  topos:
    address: carapace/hive_guards/guard_hardcoded_values.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_hardcoded_values.py

🛡️ Hive Guard: Hardcoded Values & Magic Numbers
Scans for hardcoded model names and configuration bypasses.
Warns if detected, encouraging use of `body/swarm_config.yaml`.
"""

import re
import sys
from pathlib import Path

# Patterns that look like model names
MODEL_PATTERNS = [
    r"[\"']gpt-\d",
    r"[\"']claude-\d",
    r"[\"']gemini-",
    r"[\"']x-ai/",
    r"[\"']meta-llama/",
    r"[\"']mistral",
    r"[\"']anthropic/",
    r"[\"']google/",
    r"[\"']openai/",
]

# Patterns that look like hardcoded config keys (Magic Numbers)
# We look for assignments like `timeout = 60` or `max_rounds = 2`
MAGIC_NUMBER_PATTERNS = [
    r"timeout\s*=\s*\d+",
    r"max_rounds\s*=\s*\d+",
    r"squad_size\s*=\s*\d+",
    r"quorum_threshold\s*=\s*\d+",
]


def check_hardcoded_values():
    print("🛡️  Scanning for Hardcoded Models & Magic Numbers...")

    root_dir = Path(__file__).parent.parent.parent
    hands_dir = root_dir / "body" / "hands"

    # Files to exclude (tests, config loaders)
    exclusions = ["__init__.py", "swarm_config.py"]

    files = list(hands_dir.glob("*.py"))
    warnings = []

    for file_path in files:
        if file_path.name in exclusions:
            continue

        # Skip tests
        if file_path.name.startswith("test_"):
            continue

        content = file_path.read_text()
        lines = content.splitlines()

        for i, line in enumerate(lines):
            # Skip comments
            if line.strip().startswith("#"):
                continue

            # Check for Model Names
            for pattern in MODEL_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    # Allow if it looks like a config lookup or log
                    if "SWARM_CFG" in line or "os.getenv" in line or "logger." in line:
                        continue

                    msg = f"   ⚠️  {file_path.name}:{i+1} -> Potential Hardcoded Model: {line.strip()}"
                    print(msg)
                    warnings.append(msg)

            # Check for Magic Numbers
            for pattern in MAGIC_NUMBER_PATTERNS:
                if re.search(pattern, line):
                    # Allow if it looks like a default value in .get()
                    if ".get(" in line:
                        continue

                    msg = f"   ⚠️  {file_path.name}:{i+1} -> Potential Magic Number: {line.strip()}"
                    print(msg)
                    warnings.append(msg)

    if warnings:
        print(f"\n⚠️  Found {len(warnings)} potential violations.")
        print("   Recommendation: Move these values to `body/swarm_config.yaml`.")
        # User requested "just warn and not stop", so we exit 0
        sys.exit(0)
    else:
        print("✨ No hardcoded values detected.")
        sys.exit(0)


if __name__ == "__main__":
    check_hardcoded_values()
