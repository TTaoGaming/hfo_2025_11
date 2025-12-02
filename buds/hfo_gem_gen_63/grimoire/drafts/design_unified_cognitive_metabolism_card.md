---
card:
  id: unified_cognitive_metabolism
  source: design_unified_cognitive_metabolism.md
  type: Concept
---

# 🃏 Unified Cognitive Metabolism

> **Intuition**: Knowledge thrives not in static storage but through biological metabolism—ingesting raw experiences, refining them via digestion, and evolving structured artifacts for executive recall.

## 📜 The Incantation (Intent)
```gherkin
Feature: Metabolic Knowledge Processing via KCS v6 and Diátaxis

  Scenario: Assimilate Raw Gem from Solve Loop into Library
    Given a raw gem logged in "memory/episodic/inbox/" by an agent
    When the Assimilator triggers the Evolve Loop
    Then it refines the gem into a Diátaxis artifact in "memory/library/"
      And updates the knowledge graph
      And prunes obsolete content to "memory/archive/"
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Core Assimilator Evolve Loop
import os
from pathlib import Path
from llm_utils import classify_diataxis, generate_artifact

def assimilate_inbox():
    inbox = Path("memory/episodic/inbox/")
    for gem_file in inbox.glob("*.json"):
        gem = load_gem(gem_file)  # {"issue": ..., "context": ..., "resolution": ...}
        artifact_type = classify_diataxis(gem)  # e.g., "guide", "reference"
        artifact_md = generate_artifact(gem, artifact_type)
        target_dir = Path(f"memory/library/{artifact_type}s/")
        target_dir.mkdir(exist_ok=True)
        target_path = target_dir / f"{slugify(gem['title'])}.md"
        with open(target_path, "w") as f:
            f.write(artifact_md)
        update_knowledge_graph(gem, target_path)
        gem_file.unlink()  # Processed
```

## ⚔️ Synergies
*   **Brain/**: Executive hub for `intents/` (Gherkin orders) and `strategy/` (roadmaps), querying refined library for decisions.
*   **Memory/Library/**: Diátaxis-structured (tutorials/guides/reference/explanation) as the long-term knowledge base.
*   **Body/Digestion/Assimilator.py**: The metabolic engine running scheduled Evolve Loops.
*   **Hands/Agents** (e.g., builder.py): Feed raw gems via Solve Loop during problem-solving.
*   **KCS v6 + Graph (Postgres/NetworkX)**: Enables flowing, linked knowledge evolution across the swarm.