---
card:
  id: 550e8400-e29b-41d4-a716-446655440099
  source: design_mountain_web_stigmergy.md
  type: Concept
---

# 🃏 Mountain & Web: Fractal Stigmergy

> **Intuition**: The filesystem manifests as a living mountain where artifacts organically sink into decay or float via uplift, interconnected by a vibrating agent web to forge emergent holonic swarm intelligence.

## 📜 The Incantation (Intent)
```gherkin
Feature: Fractal Stigmergy via Obsidian Facet

  Scenario: Uplifting a file on the Mountain triggers Web vibration
    Given a file on the Mountain with an Obsidian Facet containing "urgency", "decay_rate", and "last_touched"
    When an agent touches the file updating "last_touched" to now
    And the "stigmergy_score" is recalculated as urgency / (time_delta * decay_rate)
    Then the file floats higher in attention strata
    And a NATS signal "hfo.signal.file.touched" is published to the Web with the new score
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from datetime import datetime
import yaml
import nats  # Assuming NATS client

def calculate_stigmergy_score(facet: dict) -> float:
    """Compute stigmergy_score: Urgency / (TimeDelta * Decay), avoiding div-by-zero."""
    now = datetime.now()
    last_touched = datetime.fromisoformat(facet['last_touched'])
    delta = max((now - last_touched).total_seconds(), 1e-6)
    return facet['urgency'] / (delta * facet['decay_rate'])

def uplift_file(filepath: str, nc: nats.NATS) -> None:
    """Uplift file: update last_touched, recalc score, vibrate Web."""
    with open(filepath, 'r') as f:
        data = yaml.safe_load(f)
    data['last_touched'] = datetime.now().isoformat()
    data['stigmergy_score'] = calculate_stigmergy_score(data)
    with open(filepath, 'w') as f:
        yaml.dump(data, f)
    payload = {'file': filepath, 'new_score': data['stigmergy_score']}
    nc.publish('hfo.signal.file.touched', payload=payload)
```

## ⚔️ Synergies
*   **Obsidian Facet**: Standardized YAML schema (`id`, `urgency`, `last_touched`) enabling machine-readable neurons across all artifacts.
*   **Holonic Agents**: Sherpa (retrieval/uplift), Gardener (pruning low-score files), Weaver (link synthesis) as sub-holons of Assimilator.
*   **NATS JetStream**: Hot Web for vibrations (`hfo.signal.file.touched`), directing agent attention to static Mountain points.
*   **Strata Naming**: `YYYYMMDD_HHMMSS_{Title}.md` for age-visible filesystem sorting and natural decay.
*   **Dashboard Heatmap**: Visualizes urgency vs. freshness zones, revealing peaks, orphans, and clusters via `stigmergy_score` and `links`.
*   **brain/concepts.yaml & .feature**: Linked foundational docs for schema and Gherkin validation.