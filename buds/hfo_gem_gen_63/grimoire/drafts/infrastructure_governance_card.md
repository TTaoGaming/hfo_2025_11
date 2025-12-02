---
card:
  id: c69a9939-4b2f-4e27-9a5f-bf6ca20f1545
  source: infrastructure_governance.md
  type: Concept
---

# 🃏 Holonic File Governance

> **Intuition**: In the Hive, cosmic order manifests through ruthless enforcement—the Holocron's registry is divine law, purging unregistered "slop" to forge a brain of crystalline intent and visualization.

## 📜 The Incantation (Intent)
```gherkin
Feature: Enforce Holonic File Governance in the Hive Brain

  Scenario: Guard rejects invalid brain concept commits
    Given a developer commits a file to "brain/"
    When "guard_brain.py" validates the concept
    Then it must exist in "registry.yaml" or "concepts.yaml"
    And it must have a companion ".feature" file for intent
    And its ".md" must include YAML frontmatter, BLUF, governance matrix, and 3+ Mermaid diagrams
    And if invalid, the commit is blocked and flagged as "Slop"
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Core validation logic from guard_brain.py
import yaml
import re
import os
from pathlib import Path

def enforce_holonic_governance(file_path: str, registry_path: str = "brain/registry.yaml") -> bool:
    """Validate file against Holocron law: registry + Swarmlord format."""
    path = Path(file_path)
    
    # Check 1: Registry presence
    with open(registry_path, 'r') as f:
        registry = yaml.safe_load(f)
    if path.name not in registry.get('files', []) and path.name not in registry.get('concepts', []):
        raise ValueError(f"{path.name} not in Holocron registry - marked as Slop!")
    
    # Check 2: Intent (.feature) exists
    feature_path = path.with_suffix('.feature')
    if not feature_path.exists():
        raise ValueError("Missing .feature for intent declaration")
    
    # Check 3: Rich .md with YAML, Matrix, 3x Mermaid
    if path.suffix != '.md':
        raise ValueError("Brain concepts require .md visualization")
    
    with open(path, 'r') as f:
        content = f.read()
    
    if not re.search(r'---\n.*---', content, re.DOTALL):  # YAML frontmatter
        raise ValueError("Missing YAML frontmatter")
    if 'BLUF' not in content or '|' not in content:  # Matrix proxy
        raise ValueError("Missing BLUF or Governance Matrix")
    mermaid_count = len(re.findall(r'```mermaid', content))
    if mermaid_count < 3:
        raise ValueError(f"Insufficient Mermaid diagrams: {mermaid_count}/3")
    
    return True  # Passes Holonic governance
```

## ⚔️ Synergies
*   **Holocron Registry**: `brain/registry.yaml` & `concepts.yaml` as the unyielding DNA—core dependency for all validations.
*   **Hive Guard**: Integrates directly with `guard_brain.py` Git hooks for pre-commit enforcement by the Immunizer.
*   **Swarmlord of Webs**: Mandates Gherkin `.feature` + Markdown with 3x Mermaid (Conceptual/Logical/Physical views).
*   **Organs Hierarchy**: Applies to `brain/` (Intent), `body/` (Execution), `memory/` (Knowledge)—ensures holonic purity across the Hive.
*   **Intent-Based Engineering**: Fuels Gen 51's viral meme propagation by rejecting low-density text for diagram-rich artifacts.