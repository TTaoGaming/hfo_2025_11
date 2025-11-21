#!/usr/bin/env python3
import re
from pathlib import Path
import sys

# Configuration
BRAIN_DIR = Path("brain")
VALID_DIAGRAM_TYPES = {
    "graph",
    "flowchart",
    "sequenceDiagram",
    "classDiagram",
    "stateDiagram",
    "stateDiagram-v2",
    "erDiagram",
    "journey",
    "gantt",
    "pie",
    "requirementDiagram",
    "gitGraph",
    "c4Context",
    "mindmap",
    "timeline",
}


def check_mermaid_blocks(file_path: Path) -> list[str]:
    issues = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"Could not read file: {e}"]

    # Regex to find mermaid blocks
    # Matches ```mermaid ... ```
    mermaid_pattern = re.compile(r"```mermaid\s+(.*?)```", re.DOTALL)
    matches = mermaid_pattern.finditer(content)

    found_blocks = 0
    for match in matches:
        found_blocks += 1
        block_content = match.group(1).strip()

        if not block_content:
            issues.append("Empty mermaid block found.")
            continue

        # Check first line for diagram type
        lines = block_content.split("\n")
        # Remove comments from first line if any (%%)
        first_line = lines[0].strip()
        if "%%" in first_line:
            first_line = first_line.split("%%")[0].strip()

        # Handle "graph TD" or "direction TB" inside stateDiagram
        # We just want the first word
        first_word = first_line.split(" ")[0]

        if first_word not in VALID_DIAGRAM_TYPES:
            # Special case: sometimes people put comments or directives first
            # But strictly, mermaid usually starts with the type.
            # Let's be lenient if it starts with %%
            if not lines[0].strip().startswith("%%"):
                issues.append(
                    f"Unknown or missing diagram type: '{first_word}'. Valid types: {', '.join(sorted(list(VALID_DIAGRAM_TYPES)))}"
                )

    if found_blocks == 0 and file_path.suffix == ".md":
        # Not all MD files need mermaid, but if they are in brain/ and registered as summary, they might.
        # The guard_brain.py checks for *presence* of "mermaid" string.
        # This guard checks validity of blocks IF they exist.
        pass

    return issues


def main():
    print("🛡️  HIVE GUARD: Mermaid Syntax Check")
    print("====================================")

    md_files = list(BRAIN_DIR.glob("*.md"))
    print(f"🔍 Scanning {len(md_files)} Markdown files in {BRAIN_DIR}...")

    all_issues = []
    for md_file in md_files:
        issues = check_mermaid_blocks(md_file)
        if issues:
            for issue in issues:
                all_issues.append(f"{md_file.name}: {issue}")

    if all_issues:
        print("\n❌ Mermaid Validation Errors:")
        for issue in all_issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print("\n✅ All Mermaid diagrams appear valid (basic syntax).")
        sys.exit(0)


if __name__ == "__main__":
    main()
