---
card:
  id: 22869021-6fc4-48b6-94a9-c17ee546cc8b
  source: guide_holographic_intuition.md
  type: Concept
---

# 🃏 Holographic Intuition

> **Intuition**: Every swarm artifact is an Obsidian Facet—a holographic cell membrane phase-shifting between crystalline files, liquid signals, and sedimentary memories—to enable fractal stigmergy as above, so below.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Facet Phase Transitions

  Scenario: Pheromone Alarm Propagation
    Given a crystalline Markdown artifact with ObsidianFacet YAML frontmatter
    When an agent emits a liquid NATS JetStream signal with high urgency and file location pointer
    Then subscribed agents query the sedimentary Postgres vector store or swarm the location to react
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import List

class ObsidianFacet(BaseModel):
    # --- Identity (The Anchor) ---
    id: UUID              # Unique Soul
    author: str           # Who made this?
    timestamp: datetime   # When?
    location: str         # Where is the body? (file://...)

    # --- The Pulse (Hot / Liquid) ---
    urgency: float        # 0.0 to 1.0 (How loud?)
    decay: float          # 0.0 to 1.0 (How fast does it die?)
    signal_type: str      # "Discovery", "Danger", "Request"

    # --- The Vector (Cold / Sediment) ---
    tags: List[str]       # Folksonomy
    embedding: List[float]# Semantic Meaning (The "Vibe")
    links: List[UUID]     # Mycelial Connections
```

## ⚔️ Synergies
*   **NATS JetStream**: Powers liquid state signals using Claim Check pattern for instant, body-less propagation.
*   **Postgres Vector Store**: Enables sedimentary recall via semantic embeddings for ancestral memory queries.
*   **Fractal Holarchy**: Scales uniformly from agent-level ToDo lists (internal stigmergy) to squad channels and hive-wide missions.
*   **HFO Agents/Squads**: Disruptors emit alarms, Immunizers subscribe to urgency thresholds, Navigators query for synthesis.