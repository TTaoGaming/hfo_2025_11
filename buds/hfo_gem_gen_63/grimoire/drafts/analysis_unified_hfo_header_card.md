---
card:
  id: 550e8400-e29b-41d4-a716-446655440107
  source: analysis_unified_hfo_header.md
  type: Concept
---

# 🃏 Unified HFO Header: The Holographic Cell

> **Intuition**: Every document is a living cell in a holographic hive, flattening the Quadrivium's ontological depth—Ontos (identity), Chronos (thermodynamics), Topos (fractality), Telos (virality)—into a human-readable YAML facade that machines parse as a fractal graph.

## 📜 The Incantation (Intent)
```gherkin
Feature: Unified HFO Header Synthesis

  Scenario: Generate a Holographic Cell Header for any document
    Given a document with identity data, thermodynamic state, spatial links, and viral purpose
    When synthesizing the Quadrivium into a flat YAML header
    Then the header exposes human aliases mapping 1:1 to Ontos, Chronos, Topos, Telos quadrants
    And it supports recursive scaling from L0 scripts to L3 fleets
    And it enforces readability without nesting while enabling graph/vector queries
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import yaml
from uuid import uuid4
from typing import Dict, Any, List

def generate_hfo_header(
    doc_type: str,
    title: str,
    address: str = "1.1.0",
    urgency: float = 1.0,
    decay: float = 0.0,
    bluf: str = "",
    links: List[Dict[str, str]] = None,
    status: str = "active"
) -> str:
    """
    Synthesizes a Holographic Cell header per the Unified HFO Standard.
    """
    if links is None:
        links = []
    
    header = {
        # 🏛️ ONTOS (Identity)
        "id": str(uuid4()),
        "type": doc_type,
        "title": title,
        
        # ⏳ CHRONOS (Thermodynamics)
        "status": status,
        "urgency": urgency,  # Energy
        "decay": decay,      # Entropy
        
        # 📍 TOPOS (Fractal Geometry)
        "address": address,  # Holonic Address
        "links": links,      # Synapses
        
        # 🎯 TELOS (Viral Purpose)
        "bluf": bluf,
        "viral": urgency,    # Infectivity mirrors energy
    }
    return yaml.dump(header, default_flow_style=False, sort_keys=False)
```

## ⚔️ Synergies
*   **Genesis Integration**: `genesis.py` auto-generates headers for new swarm artifacts.
*   **Guard Enforcement**: `guard_stigmergy_headers.py` validates all files conform to the 4 quadrants.
*   **Graph Assimilation**: Maps `address` to Fractal Tree (holarchy) and `links` to Neo4j/Postgres knowledge graph.
*   **Mountain Mechanics**: `urgency`/`decay` drive rot/float prioritization in the swarm's thermodynamics.
*   **Critiques & Evolutions**: Synthesizes `unified_dual_headers.md` (bicameral split) while critiquing `unified_obsidian_header.md` (flat facets).