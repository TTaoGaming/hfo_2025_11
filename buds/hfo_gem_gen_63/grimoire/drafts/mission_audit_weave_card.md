---
card:
  id: 811942fc-9174-4aef-a06a-9cbb627cc76b
  source: mission_audit_weave.md
  type: Spell
---

# 🃏 Mission: Audit & Weave

> **Intuition**: Unifying fragmented memory crystals into a resilient Knowledge Graph through intelligent weaving and consensual auditing fosters emergent systemic intelligence.

## 📜 The Incantation (Intent)
```gherkin
Feature: Weave Memory Library into Audited Knowledge Graph

  Scenario: Execute Audit & Weave Mission
    Given a semantic memory library at "memory/semantic/library/"
    When the Weaver Ant scans the library and constructs a Knowledge Graph at "memory/semantic/knowledge_graph.json"
    And the Consensus Council audits the graph for health, issuing directives if needed
    Then an Audit Report is generated with verdict: Healthy, Critical, or Healing directives
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import json
from pathlib import Path
# Assume integrations: weaver_ant, consensus_council

def mission_audit_weave(library_path: str = "memory/semantic/library/", graph_path: str = "memory/semantic/knowledge_graph.json") -> dict:
    """
    Orchestrates weaving memory crystals into KG and audits via Consensus Council.
    """
    # Step 1: Weaver scans and builds graph
    kg_data = weaver_ant.build_from_library(Path(library_path))
    with open(graph_path, 'w') as f:
        json.dump(kg_data, f, indent=2)
    
    # Step 2: Council audits
    audit_report = consensus_council.audit_graph(graph_path)
    
    # Step 3: Handle state transitions (Healthy/Critical/Healing)
    if audit_report['verdict'] == 'Critical':
        # Graft orphans, rescan
        healing_directives = consensus_council.issue_directives(audit_report)
        return {'status': 'Healing', 'directives': healing_directives}
    
    return {'status': audit_report['verdict'], 'report': audit_report}
```

## ⚔️ Synergies
*   Integrates with `memory/semantic/library/` as input source for raw memory crystals.
*   Outputs to `memory/semantic/knowledge_graph.json` as the unified KG artifact.
*   Leverages Weaver Ant for graph construction and Consensus Council for auditing/verdicts.
*   Supports state machine transitions: Weaving → Auditing → Healthy/Critical → Healing (iterative rescan).
*   Visualizes via Mermaid graphs for sequence, flow, and state monitoring in the swarm ecosystem.