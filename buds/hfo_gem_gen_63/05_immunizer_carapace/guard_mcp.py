"""
---
holon:
  id: hfo-guard-mcp
  type: guard
  file: guard_mcp.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_mcp_servers.md
---
"""
import os
import ast
from typing import List

class MCPGuard:
    """
    The Immunizer Guard for MCP Compliance.
    Scans the codebase to ensure Agents are using MCP tools
    instead of direct library calls where prohibited.
    """
    def __init__(self, root_path: str):
        self.root_path = root_path
        self.violations = []

    def scan(self):
        """Scan the bud for violations."""
        print("🛡️ [GUARD] Scanning for MCP Compliance...")
        
        for root, _, files in os.walk(self.root_path):
            for file in files:
                if file.endswith(".py") and "test" not in file:
                    self._check_file(os.path.join(root, file))
        
        if self.violations:
            print(f"❌ Found {len(self.violations)} MCP Violations!")
            for v in self.violations:
                print(f"  - {v}")
        else:
            print("✅ No MCP Violations found.")

    def _check_file(self, filepath: str):
        """Check a single file for banned imports."""
        with open(filepath, "r") as f:
            try:
                tree = ast.parse(f.read())
            except SyntaxError:
                return # Skip invalid python files

        for node in ast.walk(tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                # Rule: Agents (Brain) should not import LanceDB directly.
                # They should use the Memory MCP (or the Bridger abstraction).
                if "07_navigator_brain" in filepath:
                    self._check_import(node, "lancedb", filepath, "Navigator should not access LanceDB directly. Use Memory MCP.")
                    self._check_import(node, "sqlite3", filepath, "Navigator should not access SQLite directly. Use Memory MCP.")

    def _check_import(self, node, banned_module, filepath, message):
        """Helper to check imports."""
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == banned_module:
                    self.violations.append(f"{filepath}: {message}")
        elif isinstance(node, ast.ImportFrom):
            if node.module == banned_module:
                self.violations.append(f"{filepath}: {message}")

if __name__ == "__main__":
    # Run scan on the current bud
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bud_root = os.path.dirname(current_dir) # buds/hfo_gem_gen_63
    guard = MCPGuard(bud_root)
    guard.scan()
