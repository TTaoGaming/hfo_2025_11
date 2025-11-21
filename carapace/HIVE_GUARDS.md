# 🛡️ Carapace Hive Guards

> **Status**: Active
> **Role**: Automated Defense System
> **Tools**: Pre-commit, Ruff, Black, Mypy, Venom

## 🧬 Overview
The **Hive Guards** are the automated immune system of Hive Fleet Obsidian. They run before every commit to ensure code quality, consistency, and stability.

## 🛡️ The Guard Layers

### 1. 🧹 Hygiene (Pre-Commit Hooks)
*   **Trailing Whitespace**: Removes useless whitespace.
*   **End of File Fixer**: Ensures files end with a newline.
*   **Check YAML**: Validates YAML syntax (critical for `models.yaml` and `registry.yaml`).
*   **Large Files**: Prevents accidental commit of large binaries (>1MB).

### 2. ⚡ Static Analysis (Linting)
*   **Ruff**: Extremely fast Python linter. Replaces Flake8, isort, etc.
    *   *Action*: Auto-fixes import sorting and common errors.
*   **Black**: The uncompromising code formatter.
    *   *Action*: Enforces consistent style (PEP 8).
*   **Mypy**: Static type checker.
    *   *Action*: Enforces type safety (Pydantic compatibility).

### 3. 🧪 Venom Injection (Smoke Tests)
*   **Venom Smoke Tests**: Runs `python genesis.py --venom` before every commit.
    *   *Action*: Verifies that the core anatomy (Brain, Body, Nerves) is functional.
    *   *Policy*: If the anatomy is broken, the commit is rejected.

### 4. 🔒 Security Guard (Secrets)
*   **Detect Secrets**: Scans for hardcoded API keys, passwords, and model names.
    *   *Action*: Prevents committing secrets to the repo.
    *   *Policy*: Use environment variables (`.env`) for all sensitive data.

### 5. 🧠 Brain Integrity Guard (Registry)
*   **Concept Validation**: Enforces the "Intent-Based Engineering" structure in `brain/`.
*   **Rule**: Every concept must have:
    1.  **Gherkin Feature** (`.feature`): Defines behavior and requirements.
    2.  **Executive Summary** (`.md`): Contains high-level overview and **Mermaid** visualization.
*   **Registry**: Validates against `brain/concepts.yaml`.
*   **Slop Detection**: Flags any file in `brain/` that is not registered.
*   **Command**: `./carapace/hive_guards/guard_brain.py`

### 6. 🧜‍♀️ Mermaid Guard (Visualization)
*   **Syntax Validation**: Scans `brain/*.md` for `mermaid` code blocks.
*   **Type Check**: Ensures diagrams start with valid types (e.g., `graph`, `sequenceDiagram`).
*   **Empty Check**: Flags empty diagram blocks.
*   **Command**: `./carapace/hive_guards/guard_mermaid.py`

## 🔮 Future Guards & Immunizers (Roadmap)
*Based on HFO Gem Evolution Pain Points*

### 1. 🌀 Hallucination Death Spiral Immunizer
*   **Pain Point**: Agents getting stuck in loops, repeating the same error or outputting infinite text.
*   **Solution**: Runtime monitor (Immunizer) that tracks:
    *   **Repetition Rate**: N-gram overlap with previous outputs.
    *   **Cyclic Tool Calls**: Repeating the same tool with same args > 3 times.
    *   **Action**: Circuit breaker that kills the agent and triggers a "Reflexion" step.

### 2. 🕸️ Link Rot Guard
*   **Pain Point**: Markdown files referencing non-existent files or anchors.
*   **Solution**: Static analysis that parses `[Link](path)` and verifies `path` exists.

### 3. 🐍 Code Block Validator
*   **Pain Point**: Python code snippets in Markdown that are syntactically invalid.
*   **Solution**: Extract `python` blocks from `.md` and run `ast.parse()` on them.

### 4. 📄 Gherkin-Code Parity Guard
*   **Pain Point**: Implementation drifting away from Intent.
*   **Solution**: Check that every `Feature` in `brain/` has a corresponding `Test` in `venom/` or `Implementation` in `body/`.

## 🛠️ Usage

### Installation
```bash
pip install pre-commit
pre-commit install
```

### Manual Run
To run the guards on all files without committing:
```bash
pre-commit run --all-files
```

### Bypass (Emergency Only)
If you must bypass the guards (e.g., for a WIP save):
```bash
git commit -m "wip" --no-verify
```
**Warning**: Bypassing guards weakens the Hive. Use sparingly.
