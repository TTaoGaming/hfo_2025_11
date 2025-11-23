"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 084c56a9-3e19-4092-b25d-68ed13897705
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.310701+00:00'
  topos:
    address: venom/guard_static_analysis.py
    links: []
  telos:
    viral_factor: 0.0
    meme: guard_static_analysis.py
"""

import os
import re
from rich.console import Console
from rich.table import Table

console = Console()

# --- Configuration ---
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {
    ".git",
    "__pycache__",
    "venv",
    ".venv",
    "node_modules",
    ".pytest_cache",
    "venom",
    "eyes/archive",
    "memory/episodic",
}
SKIP_FILES = {"guard_static_analysis.py", "swarm_config.yaml", "requirements.txt"}

# Regex for potential model names (e.g., "gpt-4", "claude-3", "gemini-", "x-ai/")
MODEL_REGEX = re.compile(
    r"['\"](gpt-|claude-|gemini-|x-ai/|text-embedding-)[a-zA-Z0-9\-\.]*['\"]"
)


def is_yaml_header_present(content: str) -> bool:
    """Checks if the file starts with a YAML frontmatter block."""
    return content.strip().startswith("---")


def scan_file_for_hardcoded_models(file_path: str, content: str) -> list:
    """Scans a file for hardcoded model strings."""
    warnings = []
    lines = content.splitlines()
    for i, line in enumerate(lines):
        # Skip comments
        if line.strip().startswith("#"):
            continue

        matches = MODEL_REGEX.findall(line)
        for match in matches:
            # Allow if it's in a config file or specifically exempted
            if "config" in file_path.lower() or "test" in file_path.lower():
                continue
            warnings.append((i + 1, match))
    return warnings


def run_static_analysis():
    console.print("[bold blue]🛡️  Hive Guard: Static Analysis[/bold blue]")

    model_warnings = []
    header_warnings = []

    for root, dirs, files in os.walk(ROOT_DIR):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]

        for file in files:
            if file in SKIP_FILES:
                continue

            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, ROOT_DIR)

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue  # Skip binary or unreadable files

            # 1. Check for Hardcoded Models (Python only)
            if file.endswith(".py"):
                warnings = scan_file_for_hardcoded_models(rel_path, content)
                for line_num, model in warnings:
                    model_warnings.append((rel_path, line_num, model))

            # 2. Check for Stigmergy Headers (Markdown & Python)
            # For Python, we look for a module docstring or a comment block at the top?
            # The user said "yaml header on top of pretty much every single file".
            # For MD it's standard frontmatter. For Py it might be a comment block.
            # Let's stick to MD for now as it's the primary documentation/intent source.
            if (
                file.endswith(".md") and not file.upper() == "README.MD"
            ):  # READMEs often don't have them
                if not is_yaml_header_present(content):
                    header_warnings.append(rel_path)

    # --- Report: Hardcoded Models ---
    if model_warnings:
        table = Table(title="⚠️  Hardcoded Model Warnings")
        table.add_column("File", style="cyan")
        table.add_column("Line", style="yellow")
        table.add_column("Detected Model", style="red")

        for path, line, model in model_warnings:
            table.add_row(path, str(line), model)

        console.print(table)
    else:
        console.print("[green]✅ No hardcoded models detected.[/green]")

    # --- Report: Missing Headers ---
    if header_warnings:
        table = Table(title="⚠️  Missing Stigmergy Headers (Markdown)")
        table.add_column("File", style="cyan")

        for path in header_warnings:
            table.add_row(path)

        console.print(table)
    else:
        console.print("[green]✅ All Markdown files have Stigmergy Headers.[/green]")


if __name__ == "__main__":
    run_static_analysis()
