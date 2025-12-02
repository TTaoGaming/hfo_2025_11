---
card:
  id: 118b92c6-187b-4d70-9381-1a756f37012f
  source: architecture_three_webs.md
  type: Concept
---

# 🃏 The Three Webs Architecture

> **Intuition**: A tripartite cognitive scaffold partitioning swarm intelligence into past wisdom (Karmic Web), present execution (Present Web), and future foresight (Simulation Web) for balanced reactivity, deliberation, and adaptive evolution.

## 📜 The Incantation (Intent)
```gherkin
Feature: Three Webs Cognitive Coordination

  Scenario: Resolve Uncertainty Through Inter-Web Flow
    Given the swarm encounters an event in the Present Web
    And retrieves contextual wisdom from the Karmic Web
    When the Present Web detects high uncertainty in action selection
    And delegates optimization to the Simulation Web
    Then the Simulation Web returns a golden path plan
    And the Present Web executes the plan
    And commits experiential memory back to the Karmic Web
```

## 🧪 The Catalyst (Code)
```python
# The Essence
class ThreeWebsOrchestrator:
    def __init__(self):
        self.karmic = KarmicWeb()  # GraphRAG + VectorDB
        self.present = PresentWeb()  # NATS + Temporal + Ray
        self.simulation = SimulationWeb()  # DSPy + MAP-Elites

    def process_event(self, event):
        # Retrieve past context
        context = self.karmic.retrieve_relevant(event)
        
        # Execute in present
        action_result = self.present.execute(context)
        
        # Escalate uncertainty to future planning
        if action_result.uncertainty > 0.7:
            optimized_plan = self.simulation.evolve_golden_path(action_result)
            action_result = self.present.execute(optimized_plan)
        
        # Commit to memory
        self.karmic.commit_experience(action_result)
        
        return action_result
```

## ⚔️ Synergies
*   **Karmic Web**: Queries Postgres/pgvector/NetworkX via AssimilatorAgent for stigmergic graph retrieval, feeding context to Present Web.
*   **Present Web**: SwarmController on NATS JetStream/Temporal/Ray spawns DisruptorAgent simulations and loops experience back to Karmic Web.
*   **Simulation Web**: DSPy/PyRibs/OpenELM for evolutionary forge, providing optimized plans under uncertainty.
*   **Obsidian Hex-Hive**: Hexagonal Ports & Adapters pattern ensures loose coupling across webs.
*   **Panarchic Loop**: Enables adaptive cycles of change/persistence, aligning with Hyper-Heuristic Horizon (H3) for self-evolving algorithms.