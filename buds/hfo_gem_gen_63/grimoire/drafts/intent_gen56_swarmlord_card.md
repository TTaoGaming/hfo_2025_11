---
card:
  id: trinity-of-workflows
  source: intent_gen56_swarmlord.md
  type: Concept
---

# 🃏 The Trinity of Workflows

> **Intuition**: Scalable hive intelligence emerges from a fractal trinity of workflows—atomic hands, squad arms, and swarm body—unifying stigmergy across scales for emergent supremacy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hive Fleet Workflow Trinity

  Scenario: Selecting and Executing Workflow by Cognitive Scale
    Given a task with "scope" of "individual", "concurrency", or "campaign"
    And "use_case" requiring sequential logic, adversarial testing, or domain decomposition
    When the Swarmlord dispatches the Trinity pattern
    Then it executes:
      | Scope      | Pattern       | Structure       | Stigmergy      |
      | Individual | Atomic Unit   | 1-1-1-1 PREY    | Hot Loop (NATS)|
      | Concurrency| Fractal Squad | 8-8-8-8 PREY    | Hot + Prob.    |
      | Campaign   | Diamond Swarm | 1-8-64-8-1      | Cold Loop (LanceDB) |
    And all patterns integrate via Hexagonal Stigmergy Schema writing to shared LanceDB Memory
```

## 🧪 The Catalyst (Code)
```python
# The Essence
def select_trinity_workflow(scope: str, use_case: str, task: dict) -> dict:
    """
    Dispatches Hive Fleet workflow pattern based on scale.
    """
    patterns = {
        "individual": {
            "name": "Atomic Unit (1-1-1-1 PREY)",
            "structure": ["Observer", "Bridger", "Shaper", "Assimilator"],
            "stigmergy": "Hot Loop (NATS)"
        },
        "concurrency": {
            "name": "Fractal Squad (8-8-8-8 PREY)",
            "structure": "8 Parallel Agents per phase + Hidden Disruptors",
            "stigmergy": "Hot Loop (NATS) + Probabilistic Spread"
        },
        "campaign": {
            "name": "Diamond Swarm (1-8-64-8-1)",
            "structure": ["Commander", "8 Squads", "64 Workers", "8 Synthesizers", "Apex"],
            "stigmergy": "Cold Loop (LanceDB)"
        }
    }
    pattern = patterns.get(scope, patterns["individual"])
    # Execute via shared LanceDB integration
    return {"level": scope, "pattern": pattern, "task": task}
```

## ⚔️ Synergies
*   **Hexagonal Stigmergy Schema**: All patterns share this core for communication, unifying NATS hot loops and LanceDB cold storage.
*   **PREY Designs**: Builds on prey-1111-design-v1 (atomic), prey-8888-design-v2 (squad), enabling low-resource to high-concurrency scaling.
*   **Swarm Architecture**: Integrates with swarm-186481-design-v1 for Lvl 2 body-scale campaigns and domain decomposition.
*   **Hive Levels**: Lvl 0 (hands: 1-1-1-1), Lvl 1 (arms: 8-8-8-8), Lvl 2 (body: 1-8-64-8-1) for fractal hierarchy.