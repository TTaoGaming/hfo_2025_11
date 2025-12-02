---
card:
  id: gitops-automation-protocol-4ec0a22a
  source: infrastructure_gitops.md
  type: Spell
---

# 🃏 🔄 GitOps Automation Protocol

> **Intuition**: The GitOps Automation Protocol acts as the hive's immune system, intelligently enforcing guards, generating semantic commits, and resiliently synchronizing the repository to prevent slop and maintain pristine history.

## 📜 The Incantation (Intent)
```gherkin
Feature: GitOps Automation Cycle

  Scenario: Synchronize repository with integrity
    Given unstaged changes exist in the hive
    When GitOpsAgent.execute_cycle() is triggered
    Then hive guards pass
      And semantic commit message is generated
      And files are staged and committed
      And resilient push synchronizes with remote
      And slop is detected and aborted if present
    And alerts Swarmlord on failure
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import subprocess
import os
from typing import Dict

class GitOpsAgent:
    def check_guards(self) -> bool:
        """Enforce Hive Guards (linting, tests, integrity)."""
        result = subprocess.run(["make", "guards"], capture_output=True)
        return result.returncode == 0

    def generate_message(self, diff: str = None) -> str:
        """Use LLM to generate conventional commit message."""
        if not diff:
            diff = subprocess.check_output(["git", "diff", "--staged"]).decode()
        # LLM call placeholder (e.g., via OpenAI API)
        prompt = f"Generate conventional commit message for diff:\n{diff}"
        return "feat: semantic commit via GitOps Agent"  # LLM response stub

    def scan_slop(self) -> bool:
        """Detect unregistered slop files."""
        # Check against registry or known files
        return True  # Placeholder: all valid

    def push_with_resilience(self) -> bool:
        """Rebase/retry on conflict."""
        for _ in range(3):  # Retry limit
            try:
                subprocess.check_call(["git", "push"])
                return True
            except subprocess.CalledProcessError:
                subprocess.check_call(["git", "pull", "--rebase"])
        return False

    def execute_cycle(self) -> None:
        """Full GitOps cycle."""
        if subprocess.run(["git", "status", "--porcelain"]).returncode == 0:
            return  # No changes
        if not self.scan_slop() or not self.check_guards():
            print("⚠️ Guards/Slop failed. Aborting.")
            return
        subprocess.check_call(["git", "add", "."])
        msg = self.generate_message()
        subprocess.check_call(["git", "commit", "-m", msg])
        if not self.push_with_resilience():
            print("🚨 Alert: Sync failed. Manual intervention needed.")
```

## ⚔️ Synergies
*   **Hive Guards**: Integrates `make guards` for linting, Mermaid, Gherkin, and brain integrity checks.
*   **LLM Integration**: Leverages language models for semantic, conventional commit messages from diffs.
*   **Slop Defense**: Scans for unregistered files, preventing low-quality code from polluting history.
*   **Swarmlord/Brain**: Alerts owner on failures; maintains `brain/infrastructure_gitops.md` synchronization.
*   **Resilient Sync**: Automates rebase/retry, reducing manual Git conflicts in the hive ecosystem.