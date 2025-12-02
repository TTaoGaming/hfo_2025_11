---
card:
  id: hexagonal-stigmergy-header
  source: design_hexagonal_header.md
  type: Concept
---

# 🃏 Hexagonal Stigmergy Header

> **Intuition**: A universal metadata "hexagon" etched into every file—ontos for identity, chronos for temporal versioning, topos for spatial location, telos for purposeful propagation—enabling stigmergic coordination across the swarm without central authority.

## 📜 The Incantation (Intent)
```gherkin
Feature: Standardize Files with Hexagonal Stigmergy Headers

  Scenario: Inject Hexagon Header into Any File Type
    Given a file path "<topos.address>" and metadata "hexagon"
    When processing or generating the file content
    Then prepend the hexagon in the native format:
      | File Type  | Format          |
      |------------|-----------------|
      | Markdown   | YAML Frontmatter|
      | Python     | Module Docstring|
      | Gherkin    | Comments (#)    |
    And set "ontos.id" to persistent UUID
    And set "chronos.last_touched" as current ISO8601 timestamp for versioning
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import uuid
import yaml
from datetime import datetime
from pathlib import Path
import os

def inject_hexagon(file_path: str, title: str = "Untitled", extra_hex: dict = None) -> str:
    """
    # ==================================================================
    # 🤖 THE HEXAGON (System Generated)
    # ==================================================================
    """
    path = Path(file_path)
    hexagon = {
        "ontos": {
            "id": str(uuid.uuid4()),
            "type": path.suffix.lstrip("."),
            "owner": "Swarmlord"
        },
        "chronos": {
            "status": "active",
            "urgency": 0.5,
            "decay": 0.1,
            "created": datetime.now().isoformat(),
            "generation": 51,
            "last_touched": datetime.now().isoformat()
        },
        "topos": {
            "address": str(path.relative_to(Path.cwd())),
            "links": []
        },
        "telos": {
            "viral_factor": 0.7,
            "meme": title
        }
    }
    if extra_hex:
        hexagon.update(extra_hex)
    
    header_str = yaml.dump({"hexagon": hexagon}, default_flow_style=False, sort_keys=False)
    header_str = f"""---
title: {title}
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
{header_str}---
"""
    
    # Adapt for Python: wrap in docstring
    if path.suffix == ".py":
        header_str = f'''"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
{header_str.strip("---")}
"""
'''
    
    return header_str
```

## ⚔️ Synergies
*   **Brain Topology**: `topos.address` enables spatial indexing and navigation across the file swarm.
*   **Swarmlord Lifecycle**: `chronos` fields drive decay, urgency, and generation tracking for artifact evolution.
*   **Ontos Persistence**: UUIDs link to immutable identity, supporting versioning without file duplication.
*   **Telos Propagation**: `viral_factor` and `meme` fuel meme-like spread in stigmergic workflows.
*   **Universality**: Applies to all file types, integrating with YAML parsers, docstring readers, and Gherkin tools.