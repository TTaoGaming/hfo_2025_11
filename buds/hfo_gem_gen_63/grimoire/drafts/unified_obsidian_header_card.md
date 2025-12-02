---
card:
  id: 550e8400-e29b-41d4-a716-446655440104
  source: unified_obsidian_header.md
  type: Concept
---

# 🃏 Unified Obsidian Header (HFO Standard)

> **Intuition**: A singular YAML holon header fractalizes identity, time, space, and purpose across every artifact, enabling a self-organizing, graph-native hive without central databases.

## 📜 The Incantation (Intent)
```gherkin
Feature: Unified Obsidian Header Enforcement

  Scenario: Generating any new holon file
    Given a new file is created for type "intent/code/doc/config/test"
    When the genesis process invokes header generation
    Then the file MUST prepend the exact YAML Quadrivium:
      | Section | Keys |
      |---------|------|
      | ONTOS  | id, type, title, owner |
      | CHRONOS| status, urgency, decay, last_touched |
      | TOPOS  | fractal_address, links |
      | TELOS  | bluf, meme, viral_factor, tags |
    And validation guards pass schema conformance
    And the header enables unified graphing via links and fractal_address
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import uuid
import yaml
from datetime import datetime
from typing import Dict, Any, List

def generate_holon_header(
    holon_type: str,
    title: str,
    owner: str,
    status: str = "active",
    urgency: float = 0.5,
    decay: float = 0.5,
    fractal_address: str = "1.0.0",
    bluf: str = "",
    meme: str = "",
    viral_factor: float = 0.0,
    tags: List[str] = None,
    links: List[Dict[str, Any]] = None
) -> str:
    """
    Generates the canonical YAML Holon Header (Quadrivium).
    """
    if tags is None:
        tags = []
    if links is None:
        links = []
    
    header = {
        # 🏛️ ONTOS (Identity & Type)
        "id": str(uuid.uuid4()),
        "type": holon_type,
        "title": title,
        "owner": owner,
        
        # ⏳ CHRONOS (Time & State)
        "status": status,
        "urgency": urgency,
        "decay": decay,
        "last_touched": datetime.now().isoformat(),
        
        # 📍 TOPOS (Space & Structure)
        "fractal_address": fractal_address,
        "links": links,
        
        # 🎯 TELOS (Purpose & Meaning)
        "bluf": bluf,
        "meme": meme,
        "viral_factor": viral_factor,
        "tags": tags,
    }
    return f"---\n{yaml.dump(header, default_flow_style=False, sort_keys=False)}---\n"
```

## ⚔️ Synergies
*   **Genesis.py**: Invokes `generate_holon_header()` to stamp all new files during creation.
*   **Guards/Validators**: Schema enforcement scans for exact Quadrivium keys in `make guards`.
*   **Assimilator Agent**: Parses `links` and `fractal_address` to build dynamic holonic graphs/Mermaid viz.
*   **Fractal Hierarchy**: `topos.fractal_address` (e.g., "1.2.3") enables database-free navigation (Brain=1, Body=2).
*   **Viral Mechanics**: `telos.viral_factor` drives replication/caching strategies in distributed nodes.
*   **Unified Graphing**: Cross-file `links` (e.g., {id: "uuid", rel: "implements"}) powers knowledge graphs for all types.