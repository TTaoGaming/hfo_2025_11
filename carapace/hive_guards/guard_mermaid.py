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


def check_balanced_brackets(content: str) -> list[str]:
    """Checks for balanced brackets in the mermaid block."""
    stack = []
    issues = []
    # Map of closing to opening brackets
    brackets = {")": "(", "]": "[", "}": "{"}
    # Reverse map for error messages
    names = {"(": "parentheses", "[": "square brackets", "{": "curly braces"}

    # We need to ignore brackets inside strings
    in_string = False
    string_char = None

    lines = content.split("\n")
    for line_idx, line in enumerate(lines, 1):
        # Ignore comments
        if line.strip().startswith("%%"):
            continue

        # Strip comments at end of line
        if "%%" in line:
            line = line.split("%%")[0]

        for char_idx, char in enumerate(line):
            if char in "\"'":
                if not in_string:
                    in_string = True
                    string_char = char
                elif char == string_char:
                    in_string = False
                continue

            if in_string:
                continue

            if char in "([{":
                # Special handling for Mermaid ER diagram arrows: |{, o{
                if char == "{" and char_idx > 0 and line[char_idx - 1] in "o|":
                    continue

                stack.append((char, line_idx, char_idx))
            elif char in ")]}":
                if not stack:
                    issues.append(
                        f"Line {line_idx}: Unmatched closing {names[brackets[char]]} '{char}'"
                    )
                else:
                    last_open, last_line, _ = stack.pop()
                    if last_open != brackets[char]:
                        issues.append(
                            f"Line {line_idx}: Mismatched closing '{char}' for opening '{last_open}' on line {last_line}"
                        )

    if stack:
        for char, line_idx, _ in stack:
            issues.append(f"Line {line_idx}: Unclosed {names[char]} '{char}'")

    return issues


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
        if not first_line:
            # Could happen if first line was just a comment
            # Find first non-empty non-comment line
            for line in lines:
                line = line.strip()
                if line and not line.startswith("%%"):
                    first_line = line
                    break

        first_word = first_line.split(" ")[0]

        if first_word not in VALID_DIAGRAM_TYPES:
            # Special case: sometimes people put comments or directives first
            # But strictly, mermaid usually starts with the type.
            # Let's be lenient if it starts with %%
            if not lines[0].strip().startswith("%%"):
                issues.append(
                    f"Unknown or missing diagram type: '{first_word}'. Valid types: {', '.join(sorted(list(VALID_DIAGRAM_TYPES)))}"
                )

        # Run deeper syntax checks
        bracket_issues = check_balanced_brackets(block_content)
        if bracket_issues:
            for issue in bracket_issues:
                issues.append(f"Syntax Error: {issue}")

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
