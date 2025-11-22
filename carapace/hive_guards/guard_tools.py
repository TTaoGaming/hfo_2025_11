#!/usr/bin/env python3
"""
🛡️ Hive Guard: Tool Integrity
Verifies that the Agent ToolSet is responsive and not freezing.
"""

import sys
import os
import time
import tempfile
from pathlib import Path

# Add root to path
sys.path.append(str(Path(__file__).parent.parent.parent))

from body.hands.tools import ToolSet  # noqa: E402


def check_tools():
    print("🛡️  Scanning ToolSet Integrity...")

    tools = ToolSet()
    errors = []

    # 1. Test File I/O
    try:
        start = time.time()
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:
            tmp_path = tmp.name

        # Write
        res_write = tools.write_file(tmp_path, "Hive Guard Test")
        if "Error" in res_write:
            errors.append(f"write_file failed: {res_write}")

        # Read
        res_read = tools.read_file(tmp_path)
        if res_read != "Hive Guard Test":
            errors.append(f"read_file mismatch: {res_read}")

        # Cleanup
        os.remove(tmp_path)

        duration = time.time() - start
        if duration > 1.0:
            errors.append(f"File I/O too slow: {duration:.4f}s")
        else:
            print(f"   ✅ File I/O Verified ({duration:.4f}s)")

    except Exception as e:
        errors.append(f"File I/O Exception: {e}")

    # 2. Test Directory Listing
    try:
        start = time.time()
        res_list = tools.list_directory(".")
        if "Error" in res_list:
            errors.append(f"list_directory failed: {res_list}")

        duration = time.time() - start
        if duration > 1.0:
            errors.append(f"list_directory too slow: {duration:.4f}s")
        else:
            print(f"   ✅ Directory Listing Verified ({duration:.4f}s)")

    except Exception as e:
        errors.append(f"Directory Listing Exception: {e}")

    # 3. Test Grep (Potential Freeze Point)
    try:
        start = time.time()
        # Search for a string known to be in this file
        res_grep = tools.grep_files(
            "Hive Guard: Tool Integrity", "carapace/hive_guards"
        )
        if "guard_tools.py" not in res_grep:
            errors.append(f"grep_files failed to find self: {res_grep}")

        duration = time.time() - start
        if duration > 2.0:
            errors.append(f"grep_files too slow: {duration:.4f}s")
        else:
            print(f"   ✅ Grep Search Verified ({duration:.4f}s)")

    except Exception as e:
        errors.append(f"Grep Exception: {e}")

    # Report
    if errors:
        print("\n🚫 Tool Integrity Check Failed!")
        for err in errors:
            print(f"   ❌ {err}")
        sys.exit(1)

    print("\n✅ All Tools Operational.")
    sys.exit(0)


if __name__ == "__main__":
    check_tools()
