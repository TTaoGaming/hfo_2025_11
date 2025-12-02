---
card:
  id: hfo-brain-org-hybrid
  source: design_brain_organization_options.md
  type: Concept
---

# 🃏 Hybrid Brain Holarchy

> **Intuition**: Fuse Domain-Driven Design's vertical cohesion with Diátaxis clarity to sculpt a brain directory that pulses like a living hive—domains as neurons, strategy as cortex.

## 📜 The Incantation (Intent)
```gherkin
Feature: Organize Brain Directory for Hive Mind Clarity

  Scenario: Restructure flat brain/ into Hybrid DDD layers
    Given a high-entropy brain/ with mixed designs, intents, and configs
    When we impose prefixed layers:
      | 1_strategy/    | Vision, roadmaps, personas          |
      | 2_architecture/| Patterns, octree, hexagonal         |
      | 3_domains/     | Stigmergy, memory, antifragility    |
      | 4_standards/   | Governance, schemas, registry       |
      | 5_archive/     | Deprecated content                  |
    And co-locate related Gherkin, designs, and research per domain
    Then cognitive load drops with high cohesion and discoverability
      And new agents onboard 3x faster via clear vertical slices
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import os
import shutil
from pathlib import Path

def organize_brain_hybrid(brain_root: Path = Path("brain")):
    """Sculpt Hybrid DDD structure, migrate core files."""
    layers = {
        "1_strategy": ["vision_synapse_apex.md", "strategy_obsidian_hourglass.md"],
        "2_architecture": ["design_octree_fractal_holarchy.md"],
        "3_domains": {"stigmergy": [], "memory": [], "antifragility": []},
        "4_standards": ["registry.yaml"],
        "5_archive": [],
    }
    
    for layer, files in layers.items():
        layer_dir = brain_root / layer
        layer_dir.mkdir(exist_ok=True)
        if isinstance(files, dict):
            for domain, domain_files in files.items():
                domain_dir = layer_dir / domain
                domain_dir.mkdir(exist_ok=True)
        else:
            for file in files:
                src = brain_root / file
                if src.exists():
                    shutil.move(src, layer_dir / file)
    
    # Update README with structure map
    readme = brain_root / "README.md"
    readme.write_text("# Hive Brain Map\n\n" + "\n".join([f"## {k}\n- {v}" for k, v in layers.items()]))
```

## ⚔️ Synergies
*   **Stigmergy Domains**: Co-locates Gherkin intents with designs in `3_domains/stigmergy/`, enabling emergent protocol evolution.
*   **Octree Migration**: `2_architecture/octree/` nests perfectly for fractal holarchy scaling.
*   **Agent Onboarding**: `1_strategy/` funnels new swarm agents into vision before tactical dives.
*   **GitOps Alignment**: `4_standards/` centralizes registry.yaml for schema-driven ops.
*   **Body/Eyes Integration**: Mirrors organ metaphors (`body/`, `eyes/`), priming holographic filesystem unity.