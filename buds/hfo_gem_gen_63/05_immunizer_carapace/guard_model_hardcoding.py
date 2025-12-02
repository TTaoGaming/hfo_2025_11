"""
---
holon:
  id: hfo-a7486b1b
  type: unknown
  file: guard_model_hardcoding.py
  status: active
---
"""
import os
import sys
from pathlib import Path
from typing import List, Tuple

# Forbidden strings that indicate hardcoding
FORBIDDEN_MODELS = [
    "gpt-4",
    "gpt-3.5",
    "claude-3",
    "claude-2",
    "gemini-",
    "llama-3",
    "nomic-embed",
    "text-embedding-3"
]

# Files allowed to contain these strings (Configuration files)
ALLOWLIST = [
    "config.py",
    "guard_model_hardcoding.py",
    "REGISTRY.yaml"
]

def scan_file(file_path: Path) -> List[Tuple[int, str, str]]:
    """
    Scans a file for forbidden model strings.
    Returns a list of (line_number, line_content, matched_forbidden_string).
    """
    violations = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                for forbidden in FORBIDDEN_MODELS:
                    if forbidden in line and "REGISTRY" not in line: # Allow comments referencing registry
                        violations.append((i + 1, line.strip(), forbidden))
    except Exception as e:
        print(f"⚠️ Could not read {file_path}: {e}")
    return violations

def main():
    print("🛡️  HFO Gen 63 Guard: Checking for Hardcoded AI Models...")
    
    root_dir = Path("buds/hfo_gem_gen_63")
    src_dir = root_dir / "src"
    
    if not src_dir.exists():
        print(f"❌ Source directory not found: {src_dir}")
        sys.exit(1)
        
    all_violations = {}
    
    for file_path in src_dir.rglob("*.py"):
        if file_path.name in ALLOWLIST:
            continue
            
        violations = scan_file(file_path)
        if violations:
            all_violations[str(file_path)] = violations

    if all_violations:
        print("\n🚨 HARDCODED MODELS DETECTED! 🚨")
        print("The following files contain hardcoded model names. Use `settings.MODEL_*` instead.")
        print("-" * 60)
        for file, viols in all_violations.items():
            print(f"\n📄 {file}:")
            for line_num, content, forbidden in viols:
                print(f"  Line {line_num}: [{forbidden}] -> {content}")
        print("-" * 60)
        sys.exit(1)
    else:
        print("\n✅ No hardcoded models found. The Hive is pure.")
        sys.exit(0)

if __name__ == "__main__":
    main()
