---
card:
  id: 550e8400-e29b-41d4-a716-446655440103
  source: examples_obsidian_facet_v2.md
  type: Tool
---

# 🃏 Obsidian Facet V2

> **Intuition**: Stigmergy blooms in knowledge vaults through domain-flavored YAML frontmatters—Ontos, Thermos, Semios, Quantos—that encode eternal intent, hot tasks, binding protocols, and probabilistic hypotheses as environmental traces.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Facet V2 for Stigmergic Knowledge Structuring

  Scenario: Apply domain-specific YAML facet to an Obsidian note
    Given a note domain like "Ontology", "Physics", "Semiotics", or "Quantum"
    And core metadata like id, title, owner, urgency, and links
    When generating the flavored YAML frontmatter with Ontos/Chronos/Topos/Telos mappings
    Then the note header enables emergent coordination via philosophical, thermodynamic, linguistic, or quantum primitives
    And Mermaid graph visualizes relational stigmergy
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import yaml
from typing import Dict, Any
from uuid import uuid4

FLAVORS = {
    "ontology": {"headers": ["Ontos", "Chronos", "Topos", "Telos"], "bluf": "The 'Why' must always precede the 'How'."},
    "physics": {"headers": ["Mass", "Entropy", "Field", "Work"], "bluf": "Ingest 10k tokens into pgvector."},
    "semiotics": {"headers": ["Symbol", "Tense", "Syntax", "Pragmatics"], "bluf": "Defines the shape of messages."},
    "quantum": {"headers": ["Eigenstate", "Coherence", "Entanglement", "Wavefunction"], "bluf": "Exploring Free Energy Principle."}
}

def generate_obsidian_facet(flavor: str, title: str, owner: str, urgency: float = 0.5, **kwargs) -> str:
    """Generate domain-flavored YAML frontmatter for Obsidian stigmergy."""
    facet = FLAVORS.get(flavor.lower(), FLAVORS["ontology"])
    data = {
        f"# {h} ({desc or ''})": kwargs.get(h.lower(), "")
        for h, desc in zip(facet["headers"], ["Being", "Time", "Space", "Purpose"])
    }
    data.update({
        "id": kwargs.get("id", str(uuid4())),
        "type": kwargs.get("type", flavor),
        "title": title,
        "owner": owner,
        "urgency": urgency,
        "bluf": facet["bluf"],
        "last_touched": kwargs.get("last_touched", "2025-11-23")
    })
    return f"---\n{yaml.dump(data, default_flow_style=False, sort_keys=False).strip()}\n---"
```

## ⚔️ Synergies
*   **Obsidian Vault**: YAML frontmatter parsed natively for queries, dataviews, and plugins like Excalidraw/Mermaid.
*   **Stigmergy Engine**: Links and fractal_address enable indirect coordination across notes (e.g., governs/consumes/binds).
*   **Mermaid Viz**: Auto-renders graphs from YAML links for topological insight.
*   **YAML Ecosystem**: Integrates with pyyaml, Obsidian plugins, or HFO signals for NATS pub/sub.
*   **Domain Extensions**: Hooks into ontology tools (Protégé), task runners (Celery), protocols (Pydantic), or ML research (Active Inference libs).