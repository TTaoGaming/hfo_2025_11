---
card:
  id: 550e8400-e29b-41d4-a716-446655440105
  source: unified_header_options.md
  type: Concept
---

# 🃏 Unified Header: The Quadrivium

> **Intuition**: File headers as a philosophical quadrivium—Ontos (identity), Chronos (time), Topos (space), Telos (purpose)—crystallize stigmergic intent, prioritizing "why" over "how" for emergent intelligence.

## 📜 The Incantation (Intent)
```gherkin
Feature: Unified Quadrivium Headers for Intent-Based Stigmergy

  Scenario: Generate a Quadrivium header for a knowledge artifact
    Given an artifact with identity "uuid-v4", type "intent", title "Mission Alpha"
      And temporal properties urgency "1.0", decay "0.0"
      And spatial properties fractal_address "1.1.0", links [{"id": "uuid-target", "rel": "requires"}]
      And purposeful properties bluf "Why this exists.", meme "Intent is King."
    When forging the YAML header
    Then the header conforms to:
      | Section | Fields |
      |---------|--------|
      | Ontos  | id, type, title |
      | Chronos| urgency, decay |
      | Topos  | fractal_address, links |
      | Telos  | bluf, meme |
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Parse Quadrivium YAML header from file content
import yaml
import re
from typing import Dict, Any

def parse_quadrivium_header(content: str) -> Dict[str, Any]:
    """
    Extracts Ontos, Chronos, Topos, Telos from unified YAML frontmatter.
    """
    yaml_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        raise ValueError("No Quadrivium header found.")
    
    header = yaml.safe_load(yaml_match.group(1))
    
    quadrivium = {
        "ontos": {k: v for k, v in header.items() if k in ["id", "type", "title"]},
        "chronos": {k: v for k, v in header.items() if k in ["urgency", "decay"]},
        "topos": {k: v for k, v in header.items() if k in ["fractal_address", "links"]},
        "telos": {k: v for k, v in header.items() if k in ["bluf", "meme"]}
    }
    return quadrivium
```

## ⚔️ Synergies
*   **Obsidian Integration**: Builds on `brain/unified_obsidian_header.md` for fractal note-linking via Topos.
*   **Intent-Based Engineering**: Fuels Gherkin scenarios by surfacing Telos (purpose) for LLM orchestration.
*   **GraphRAG/Neo4j**: Topos edges map directly to graph nodes, enabling NetworkX ingestion (vs. Option 3).
*   **Evolutionary Pruning**: Chronos decay enables "survival of the fittest" without full Option 4 metabolism.
*   **Stigmergy Core**: Aligns with 4-path tradeoffs, recommending Quadrivium for meaning over speed/structure/evolution.