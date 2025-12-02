---
card:
  id: 550e8400-e29b-41d4-a716-446655440108
  source: design_hexagonal_holon_header.md
  type: Tool
---

# 🃏 The Hexagonal Holon Header

> **Intuition**: A bicameral architecture bifurcating human narrative intent (Face) from machine-computed ontology (Hexagon), fostering composable stigmergy through modular, hexagonal metadata.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hexagonal Holon Header Auto-Completion

  Scenario: Genesis agent completes a partial header Face into a full Hexagon
    Given a new file with only the human-written Face containing "title", "bluf", and optional "story"
    When the Genesis agent detects the file change
    Then the agent computes and appends the machine-filled Hexagon with:
      | ontos | UUID id, type, owner |
      | chronos | status, urgency, decay |
      | topos | address from filepath, links |
      | telos | viral_factor, meme |
    And the header is now stigmergy-ready for validation and assimilation
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import yaml
import uuid
import os
from datetime import datetime

def genesis_complete_header(file_path: str) -> None:
    """
    Parse Face from YAML header, compute Hexagon, and rewrite full header.
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split YAML header from body (assume --- delimited)
    parts = content.split('---\n', 2)
    if len(parts) < 2:
        return  # No header or invalid
    
    header_str = parts[0] + '---\n'
    body = parts[1] if len(parts) > 1 else ''
    
    # Parse Face
    face = yaml.safe_load(header_str)
    if not face or 'title' not in face:
        return
    
    # Compute Hexagon
    hexagon = {
        'ontos': {
            'id': str(uuid.uuid4()),
            'type': 'doc',  # Infer from context/tags
            'owner': 'Swarmlord'
        },
        'chronos': {
            'status': 'active',
            'urgency': 1.0,  # e.g., keyword-based from bluf
            'decay': 0.5
        },
        'topos': {
            'address': os.path.basename(file_path),
            'links': []
        },
        'telos': {
            'viral_factor': 1.0,  # e.g., based on title/bluf importance
            'meme': face.get('title', '').split(':')[0].strip()
        }
    }
    
    # Merge Face + Hexagon
    full_header = {**face, 'hexagon': hexagon}
    
    # Write back
    new_content = '---\n' + yaml.dump(full_header, default_flow_style=False, sort_keys=False) + '---\n\n' + body
    with open(file_path, 'w') as f:
        f.write(new_content)
```

## ⚔️ Synergies
*   **Genesis.py**: Core integration for detecting and triggering header auto-completion on file creation.
*   **guard_stigmergy_headers.py**: Validates presence and structure of `hexagon` key post-completion.
*   **assimilator.py**: Consumes `hexagon.topos.links` to construct knowledge graphs and propagate stigmergy.
*   **Composable Extensions**: Reserves "Up (Logos)" for logic constraints and "Down (Pathos)" for future modules like Kyros (security) or Oikos (economics).
*   **Unified HFO Headers**: Implements brain/analysis_unified_hfo_header.md for broader holon file ontology.