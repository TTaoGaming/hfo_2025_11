---
card:
  id: hfo-mechanic-movement
  source: mechanic_spider_movement.md
  type: Concept
---

# 🃏 Obsidian Spider Movement

> **Intuition**: The Spider senses vibrations in Indra's Net manifold, converging via Social Spider Optimization and temporal triangulation without exhaustive search.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Spider Navigation in Semantic Manifold

  Scenario: Triangulate Golden Path to Prey via SSO Swarm
    Given a vibration disturbance in the HNSW-indexed SVDAG manifold
    And three temporal anchors: Past CBR from LanceDB, Present Stigmergy from NATS JetStream, Future MCTS from Simulation Web
    When female spiders exploit strongest relevance signals
    And male spiders explore diversity towards females
    And MAP-Elites selects optimal species for vibration type
    Then the swarm converges on the prey node yielding the golden path optimal action
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Triangulate position and converge via simplified SSO
import numpy as np
from typing import List, Tuple

def triangulate_golden_path(
    past_cbr: List[Tuple[float, str]],  # (relevance, memory)
    present_stig: List[Tuple[float, str]],  # (signal, telemetry)
    future_mcts: List[Tuple[float, str]]   # (value, outcome)
) -> str:
    """Compute optimal next action via weighted temporal triangulation."""
    # Normalize relevances
    def normalize(scores): return np.array(scores) / np.sum(scores)
    
    past_weights = normalize([s for s, _ in past_cbr])
    present_weights = normalize([s for s, _ in present_stig])
    future_weights = normalize([s for s, _ in future_mcts])
    
    # Triangulate: weighted average in semantic space (simplified 1D projection)
    position = (0.3 * np.average(past_weights) +
                0.4 * np.average(present_weights) +
                0.3 * np.average(future_weights))
    
    # SSO convergence: select highest vibration prey
    all_candidates = past_cbr + present_stig + future_mcts
    prey = max(all_candidates, key=lambda x: x[0])[1]
    
    return f"Golden Path: {prey} at position {position:.2f}"
```

## ⚔️ Synergies
*   **HNSW Index**: Provides the sparse voxel DAG manifold for vibration propagation and semantic distance attenuation.
*   **NATS JetStream**: Serves as the web's nervous system for real-time stigmergy and disturbance signals.
*   **LanceDB**: Iron Ledger for CBR past anchors, enabling historical triangulation.
*   **MCTS Engine**: Powers future ($Z>0$) simulations in the Many Worlds web.
*   **MAP-Elites Grid**: Maintains speciated swarms for context-adaptive selection (e.g., aggressive for hot paths, deep for cold).