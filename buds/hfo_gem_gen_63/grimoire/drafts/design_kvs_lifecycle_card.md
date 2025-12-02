---
card:
  id: kvs-lifecycle-v6
  source: design_kvs_lifecycle.md
  type: Concept
---

# 🃏 KVS v6: Hybrid Holarchy

> **Intuition**: Knowledge mimics organic growth, demanding a brain-like holarchy to shepherd ideas from ephemeral seeds through maturation into archived timber.

## 📜 The Incantation (Intent)
```gherkin
Feature: Knowledge Versioning System Lifecycle Management

  Scenario: Promoting a draft from active memory to long-term canonical truth
    Given a draft file in "brain/active_memory/" with implicit "status: draft"
    When the draft is reviewed, approved, and crystallized
    Then move the file to "brain/long_term_memory/" under appropriate Diátaxis category
      And set frontmatter "status: stable"
      And archive prior versions to "brain/episodic_memory/"
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Enforce KVS promotion with folder/status validation
import os
import yaml
from pathlib import Path

def promote_knowledge(source_path: str, diataxis_category: str, version: str = "1.0"):
    """Promote draft to canonical, enforcing Hybrid Holarchy."""
    src = Path(source_path)
    if not src.exists() or "active_memory" not in src.parts:
        raise ValueError("Source must be in active_memory/")
    
    dest_dir = Path("brain/long_term_memory") / diataxis_category
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / f"{src.stem}_{version}.md"
    
    # Update frontmatter
    with open(src, 'r') as f:
        content = f.read()
    frontmatter_match = content.split('---', 2)
    if len(frontmatter_match) > 1:
        fm = yaml.safe_load(frontmatter_match[1]) or {}
        fm['status'] = 'stable'
        fm['version'] = version
        new_fm = yaml.dump(fm)
        content = f"---\n{new_fm}---\n{frontmatter_match[2]}"
    
    # Move and archive original if needed
    src.rename(dest_path)
    archive_path = Path("brain/episodic_memory/archive") / src.name
    archive_path.parent.mkdir(parents=True, exist_ok=True)
    if src.exists():  # Backup if not moved
        src.rename(archive_path)
    
    print(f"Promoted: {dest_path}")
```

## ⚔️ Synergies
*   **Diátaxis Integration**: `long_term_memory/` hosts Tutorials/Guides/Reference/Explanation as crystallized truth.
*   **Git Workflows**: Complements branch-based drafts (Option 2) via `active_memory/` as staging.
*   **Frontmatter Enforcement**: Builds on metadata states (Option 3) for searchability and emojis (e.g., 🚧 vs ✅).
*   **Biological HFO Metaphor**: Maps to human memory (working/long-term/episodic), enabling organic evolution.
*   **Industry Alignment**: Echoes GitLab drafts, Rust RFCs, and Obsidian Inbox/Zettelkasten patterns.