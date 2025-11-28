"""
# ==================================================================
# 🛡️ HFO OCTET GUARD (The Enforcer)
# ==================================================================
# Enforces the Law of the Octet on all files.
# 1. Checks for Stigmergy Header.
# 2. Verifies all 8 Pillars.
# 3. Flags non-Power-of-Eight structures.
"""

import os
import yaml
import re
import math

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

OCTET_PILLARS = {
    "ontos", "logos", "techne", "chronos", 
    "pathos", "ethos", "topos", "telos"
}

def is_power_of_eight(n):
    if n == 0: return False
    # Check if log8(n) is an integer
    # log8(n) = log2(n) / 3
    # So n must be a power of 2, and the exponent must be divisible by 3?
    # No, 8^x. 8^0=1, 8^1=8, 8^2=64.
    # So n must be 1, 8, 64, 512...
    if n == 1: return True
    if n < 8: return False
    while n > 1:
        if n % 8 != 0:
            return False
        n //= 8
    return True

def extract_header(content):
    # Look for YAML frontmatter between ---
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if match:
        return yaml.safe_load(match.group(1))
    
    # Look for Python docstring header
    match_py = re.search(r'"""\n(.*?)\n"""', content, re.DOTALL)
    if match_py:
        try:
            # Try to find the hexagon/octagon block
            yaml_block = re.search(r"(hexagon|octagon):.*", match_py.group(1), re.DOTALL)
            if yaml_block:
                return yaml.safe_load(yaml_block.group(0))
        except:
            pass
    return None

def scan_files():
    print(f"🛡️ Scanning {ROOT_DIR} for Octet Compliance...")
    violations = []
    
    for root, dirs, files in os.walk(ROOT_DIR):
        if "memory/lancedb" in root: continue # Skip binary DB
        if "__pycache__" in root: continue
        
        for file in files:
            if not file.endswith((".py", ".md")): continue
            
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            header = extract_header(content)
            
            if not header:
                violations.append(f"❌ [MISSING HEADER] {file}")
                continue
            
            # Normalize header root (hexagon or octagon)
            root_key = "octagon" if "octagon" in header else "hexagon"
            if root_key not in header:
                violations.append(f"❌ [MALFORMED HEADER] {file} (No root key)")
                continue
                
            pillars = header[root_key]
            present_pillars = set(pillars.keys())
            missing = OCTET_PILLARS - present_pillars
            
            if missing:
                violations.append(f"❌ [BROKEN OCTET] {file} (Missing: {missing})")
            
            # Check Power of Eight in Lists
            for pillar, data in pillars.items():
                if isinstance(data, dict):
                    for k, v in data.items():
                        if isinstance(v, list):
                            if not is_power_of_eight(len(v)) and len(v) != 0:
                                violations.append(f"⚠️ [NON-OCTAL LIST] {file} -> {pillar}.{k} has {len(v)} items")

    if violations:
        print("\n🚨 VIOLATIONS FOUND:")
        for v in violations:
            print(v)
        print(f"\nTotal Violations: {len(violations)}")
        exit(1)
    else:
        print("\n✅ All files comply with the Law of the Octet.")
        exit(0)

if __name__ == "__main__":
    scan_files()
