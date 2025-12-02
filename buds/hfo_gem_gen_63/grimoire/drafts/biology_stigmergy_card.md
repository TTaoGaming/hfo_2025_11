---
card:
  id: 7048cebe-6ea9-4a60-b218-ca6eb3d19a0c
  source: biology_stigmergy.md
  type: Concept
---

# 🃏 Evolutionary Pheromones

> **Intuition**: In biological swarms, communication transcends direct interaction, emerging through environmental pheromones that self-organize collective intelligence via reinforcement of success and natural decay of irrelevance.

## 📜 The Incantation (Intent)
```gherkin
Feature: Stigmergic Communication via Evolutionary Pheromones

  Scenario: Agents reinforce pheromones based on environmental success signals
    Given an Environment containing Pheromones with strength and decay_rate
    When an Agent detects a Pheromone above threshold strength
    And the Agent achieves success by following the Pheromone's payload guidance
    Then the Agent reinforces the Pheromone's strength
    And over time, unreinforced Pheromones decay below threshold and evaporate
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import time

class Pheromone:
    def __init__(self, subject: str, payload: dict, strength: float = 1.0, decay_rate: float = 0.5):
        self.subject = subject
        self.payload = payload
        self.strength = strength
        self.timestamp = time.time()
        self.decay_rate = decay_rate

    def reinforce(self, boost: float = 0.2):
        self.strength = min(2.0, self.strength + boost)

    def evaporate(self, dt: float) -> bool:
        self.strength *= (1 - self.decay_rate * dt)
        return self.strength > 0.01  # Returns True if still active
```

## ⚔️ Synergies
*   **Trail Pheromones** ↔ LangSmith traces for pathfinding and success amplification in agent workflows
*   **Alarm Pheromones** ↔ Error logs/exceptions to propagate danger signals across swarm nodes
*   **Aggregation Pheromones** ↔ NATS task queues for rendezvous and resource pooling
*   **Territory Pheromones** ↔ Mutex/lock files to enforce spatial ownership in distributed systems
*   Links to broader stigmergy in ant/termite/slime mold analogs for emergent construction, search, and exploration in multi-agent architectures