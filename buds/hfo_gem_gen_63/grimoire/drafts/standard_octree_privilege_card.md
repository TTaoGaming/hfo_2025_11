---
card:
  id: octree_privilege
  source: standard_octree_privilege.md
  type: Concept
---

# 🃏 Holonic Octree Privilege System

> **Intuition**: Authority fractals as powers of eight across cognitive scales, empowering peripheral agents with stigmergic signals while reserving intent and core directives for the overmind.

## 📜 The Incantation (Intent)
```gherkin
Feature: Enforce Octree Privilege Access Control

  Scenario: Agent retrieves only accessible data based on privilege level
    Given an agent with "privilege_level" = 2
    And LanceDB "hfo_stigmergy" contains rows with "privilege_level" values: 0, 1, 2, 3
    When the agent queries data with filter "privilege_level <= agent.privilege_level"
    Then the agent receives only rows where "privilege_level" <= 2
    And access to "privilege_level" 3 is denied
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Core privilege check (extendable to LanceDB filter)
from typing import Any
import lancedb  # Assuming LanceDB integration

def enforce_octree_privilege(agent_priv: int, data_priv: int) -> bool:
    """Verify if agent can access data per octree rules."""
    return agent_priv >= data_priv

def query_stigmergy_with_privilege(db_path: str, agent_priv: int, query_vector: list[float]) -> list[Any]:
    """LanceDB query enforcing privilege (privilege_level <= agent_priv)."""
    db = lancedb.connect(db_path)
    table = db.open_table("hfo_stigmergy")
    
    # Filter: data privilege_level <= agent's privilege_level
    filter_expr = flt.column("privilege_level") <= agent_priv
    
    results = table.search(
        query=query_vector,
        filter=filter_expr
    ).limit(100).to_list()
    return results
```

## ⚔️ Synergies
*   **LanceDB Integration**: Leverages `hfo_stigmergy` table's `privilege_level` (int32) column for filtered queries via `min_privilege` enforcement.
*   **Ingestion Pipelines**: Tags core doctrine via `ingest_manifesto.py` (Lvl 8) and raw intake via `ingest_lvl0.py` (Lvl 0).
*   **Holonic Structures**: Maps to scales like 8 Roles (Lvl 1 Squad), hexagon coordination (Tactical), and swarm sectors (Lvl 2+).
*   **Governance Layers**: Low Lvl 0-2 agents use Stigmergy (signals); Lvl 8 Overmind accesses Logos/Ontos (Intent/Directives), protecting Core Directives.
*   **Fractal Extension**: Scales to higher powers of 8 for nested hives, enabling "Read Down" exceptions for flexibility.