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
