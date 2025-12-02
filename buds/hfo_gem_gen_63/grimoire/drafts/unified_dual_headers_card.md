---
card:
  id: 550e8400-e29b-41d4-a716-446655440106
  source: unified_dual_headers.md
  type: Concept
---

# 🃏 Unified Dual-Split Headers: Human vs. Machine

> **Intuition**: A bicameral YAML header design that bifurcates human-readable narrative from machine-parsable ontology, embodying the duality of intuition and structure in knowledge artifacts.

## 📜 The Incantation (Intent)
```gherkin
Feature: Unified Dual-Split Headers for Bimodal Metadata

  Scenario: Structuring document headers for human intuition and machine automation
    Given a Markdown file requiring metadata for both narrative context and ontological graphing
    When applying a dual-split YAML frontmatter with "👤 HUMAN LAYER" and "🤖 MACHINE LAYER" sections
    Then humans intuitively grasp title, BLUF, intent, and context from the narrative prose
    And machines extract structured data from ontology keys like ontos, chronos, topos, telos for automation, linking, and evolution
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Parser for dual-split YAML headers
import yaml
import re

def parse_dual_header(file_path):
    """
    Refracts a dual-split YAML header into human narrative and machine ontology.
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Extract YAML frontmatter
    yaml_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not yaml_match:
        raise ValueError("No YAML frontmatter found")
    
    data = yaml.safe_load(yaml_match.group(1))
    
    # Infer layers (flexible for variations: ontology/dna/node/logic)
    human_layer = {
        k: v for k, v in data.items()
        if k not in ['ontology', 'dna', 'node', 'logic'] and not k.startswith('ont')
    }
    
    machine_layer = next(
        (data.get(machine_key) for machine_key in ['ontology', 'dna', 'node', 'logic']),
        {}
    )
    
    return {
        'human': human_layer,      # Narrative: title, bluf, intent, etc.
        'machine': machine_layer   # Ontology: ontos, chronos, topos, telos
    }
```

## ⚔️ Synergies
*   **Evolves unified_obsidian_header.md**: Builds single-block YAML into bicameral splits for enhanced readability and parsability.
*   **Quadrivium Integration**: Machine layer directly feeds ontos/chronos/topos/telos for Swarm ontology graphing and evolution.
*   **GraphRAG/Topological**: Supports "View vs. Graph" split for fractal addressing, edges, and RAG embeddings.
*   **HFO Recommendation**: Primary for Human-Facing Ontology docs, balancing story (System 1) with truth (System 2).
*   **Evolutionary Systems**: Phenotype/Genotype model enables lineage tracking and viral meme propagation in agent swarms.