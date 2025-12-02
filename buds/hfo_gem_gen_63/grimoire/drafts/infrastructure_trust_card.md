---
card:
  id: 0c5b24c7-8e29-41a9-9ce5-7308b0375abe
  source: infrastructure_trust.md
  type: Concept
---

# 🃏 Trust Engine (Holonic Byzantine Quorum)

> **Intuition**: Trust in the swarm crystallizes through fractal adversarial spirals, where chaos of critique and co-evolution forges unyielding consensus amid Byzantine betrayal.

## 📜 The Incantation (Intent)
```gherkin
Feature: Holonic Byzantine Quorum Consensus

  Scenario: V²C-SPIRAL-QUORUM for Robust Memory Crystallization
    Given a seed proposal from 1 agent
    And a spiral review panel of 3 agents with 1 potential disruptor
    And expansion to quorum of N=10 agents tolerating f=3 disruptors
    When disruptors launch hidden attacks in Round 1 then reveal in Round 2
    And votes are tallied with weighted consensus threshold of 2f+1
    Then if threshold met, proposal crystallizes into Network Stigmergy Layer
    And if rejected, trigger MAP-Elites QD optimization to evolve agent prompts
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Simulate Spiral Quorum Consensus
import random
from typing import List, Dict

def spiral_quorum_consensus(proposal: str, num_agents: int = 10, f: int = 3) -> bool:
    """
    V²C-SPIRAL-QUORUM: Seed -> Spiral -> Quorum with disruptors.
    Returns True if consensus (2f+1 votes), else evolves.
    """
    n = 3 * f + 1  # Quorum size
    assert num_agents == n, "Quorum must be 3f+1"
    
    # Spiral: Quick 3-agent critique (simplified)
    spiral_votes = [random.choice([True, False]) for _ in range(3)]
    if sum(spiral_votes) < 2:
        return False  # Spiral fails early
    
    # Quorum votes: Normal agents + weighted disruptors
    normal_agents = n - f
    normal_votes = sum(random.choice([True, False]) for _ in range(normal_agents))
    disruptor_votes = sum(random.choice([False, True]) for _ in range(f))  # Bias to NO
    
    total_yes = normal_votes + disruptor_votes
    consensus_threshold = 2 * f + 1
    
    if total_yes >= consensus_threshold:
        print(f"Crystallized: {proposal} ({total_yes}/{n} yes votes)")
        return True  # Write to Stigmergy
    else:
        print(f"Evolve: Failed consensus ({total_yes}/{n})")
        return False  # Trigger MAP-Elites
```

## ⚔️ Synergies
*   **Network Stigmergy (NATS)**: Indirect coordination layer for proposal propagation and memory persistence.
*   **MAP-Elites QD Optimization**: Evolutionary forge mutates agent DNA/prompts on consensus failures.
*   **Fractal Holarchy**: Recursive L0/L1/L2 agent loops embed quorum at multiple scales.
*   **Red Teaming Disruptors**: f adversarial agents ensure robustness, with weights amplifying critiques.
*   **Evolutionary Forge**: Links rejections to agent pool mutation for meta-swarm improvement.