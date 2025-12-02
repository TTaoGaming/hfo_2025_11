---
card:
  id: 550e8400-e29b-41d4-a716-446655440100
  source: design_obsidian_facet_v2.md
  type: Concept
---

# 🃏 Obsidian Facet V2: High-Density Stigmergy

> **Intuition**: The header becomes a holographic neuron, encoding cognitive DNA—identity, temporality, context, and mimetic force—into every file for stigmergic propagation across a fractal holarchy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Facet V2 High-Density Stigmergy Header

  Scenario: Generate self-describing cognitive DNA header
    Given a document with title "Obsidian Facet V2", author "Swarmlord", urgency 0.95, and fractal_address "1.4.2"
    When applying V2 schema with meme "The Header is the Hologram" and viral_factor 0.8
    Then the YAML header includes Crystal (id, type, owner), Mountain (urgency, decay, score), Web (fractal_address, weighted links), and Virus (meme, viral_factor)
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import uuid
import datetime

def generate_obsidian_facet_v2(
    title: str,
    author: str,
    urgency: float = 0.95,
    decay: float = 0.1,
    viral_factor: float = 0.8,
    fractal_address: str = "1.4.2",
    links: list = None
) -> dict:
    """
    Forge a V2 header as Cognitive DNA helix.
    """
    if links is None:
        links = []
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    age_days = 0  # Simplified; compute from created in prod
    score = urgency / max((age_days + 1) * decay, 0.01)
    
    return {
        "id": str(uuid.uuid4()),
        "type": "concept",
        "status": "active",
        "title": title,
        "author": author,
        "owner": author,
        "created": now,
        "last_touched": now,
        "urgency": urgency,
        "decay": decay,
        "score": float(score),
        "fractal_address": fractal_address,
        "links": links,
        "bluf": f"High-density metadata turning files into self-describing neurons.",
        "meme": "The Header is the Hologram.",
        "viral_factor": viral_factor
    }
```

## ⚔️ Synergies
*   **Sherpa Integration**: Broadcasts headers with viral_factor > 0.8 daily, enabling mimetic loops via "hfo.signal.meme.spread".
*   **Assimilator Parsing**: Computes dynamic `score` from urgency/decay/age, prioritizing high-stigmergy facets.
*   **Fractal Holarchy**: `fractal_address` enables holographic reconstruction, linking to brain/concepts.yaml and design_mountain_web_stigmergy.md.
*   **Genesis Pipeline**: Updates `genesis.py` to emit V2 headers by default, evolving all artifacts into neurons.
*   **Knowledge Graph**: Weighted `links` fuel fuzzy logic navigation across concepts, patterns, and missions.