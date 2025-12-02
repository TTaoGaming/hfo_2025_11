---
card:
  id: 1d4b7684-69ea-4cbb-8586-36b8804f216f
  source: strategy_obsidian_hourglass.md
  type: Concept
---

# 🃏 Obsidian Horizon Hourglass

> **Intuition**: A 3D geometric transduction of the Hive's temporal state-action space, where past precedents gravitationally constrain the present singularity to project and collapse simulated futures, enabling causal inversion for autonomous liberation from human time-expenditure.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Horizon Hourglass State-Action Model

  Scenario: Compute Optimal Policy with Causal Flip on High Uncertainty
    Given priors retrieved from Karmic Web (Z < 0) via GraphRAG exemplars
      And current state at Singularity Neck (Z = 0)
      And Overmind intent encoded as Pydantic reward function
    When uncertainty in anytime policy exceeds threshold
    Then simulate diverse futures in Simulation Web (Z > 0) via QD optimization (MAP-Elites)
      And collapse wavefunction to golden path
      And invert causality to dictate present policy π*(s_t)
    Then execute durable swarm action
      And retro-feed outcomes to Evolutionary Memory
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import numpy as np
from typing import Callable, Dict, Any
# Hypothetical integrations: graphrag, pyribs, dspy

def obsidian_horizon_hourglass(
    current_state: Dict[str, Any],
    horizon: int = 10,
    reward_fn: Callable[[Dict], float],
    uncertainty_threshold: float = 0.7
) -> Dict[str, Any]:
    # Karmic Web: Retrieve priors (Z < 0)
    priors = retrieve_karmic_web(current_state)  # GraphRAG CBR
    
    # Present: Anytime policy (Z = 0)
    policy = anytime_policy(current_state, priors)  # LangGraph Swarm
    
    # Flip Check: High uncertainty triggers Simulation Web (Z > 0)
    uncertainty = compute_uncertainty(policy)
    if uncertainty > uncertainty_threshold:
        # QD Simulation: Generate diverse futures
        futures = quality_diversity_sim(horizon, reward_fn)  # PyRibs MAP-Elites
        
        # Collapse & Invert Causality
        golden_path = collapse_wavefunction(futures, reward_fn)
        policy = invert_causality(golden_path, current_state)
    
    # Execute & Retro
    action = execute_policy(policy)  # NATS Durable
    retro_analyze(action, reward_fn)  # Feedback to Karmic Web
    
    return {"optimal_policy": policy, "action": action}
```

## ⚔️ Synergies
*   **Karmic Web**: Integrates GraphRAG/Postgres for precedent retrieval (Cynefin-framed priors).
*   **Swarm Web**: Leverages LangGraph/NATS for anytime, durable execution at the Neck Singularity.
*   **Simulation Web**: Powers QD futures with PyRibs (MAP-Elites) and DSPy/Ray for Monte Carlo paths.
*   **Retro-Analysis**: Loops lessons back via Evolutionary Memory, reinforcing the Complex Adaptive System.
*   **Overmind Intent**: Binds via Pydantic reward functions, enabling E-MPC across temporal dimensions.