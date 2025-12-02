---
card:
  id: intent-gen55-swarmlord-v1
  source: intent_gen55_swarmlord.md
  type: Concept
---

# 🃏 Gen 55 Swarmlord Protocol: The Trinity of Workflows

> **Intuition**: Hive cognition fractally scales through three sacred patterns—atomic precision, squad antifragility, and diamond swarm strategy—unified by hexagonal stigmergy for emergent supremacy.

## 📜 The Incantation (Intent)
```gherkin
Feature: Swarmlord Trinity Workflow Dispatch

  Scenario Outline: Dispatch Workflow Pattern by Mission Scale
    Given a mission with "<scale>" scope and "<use_case>"
    When the Swarmlord evaluates cognitive requirements
    Then it activates the "<pattern>" structure
      And employs "<stigmergy>" for coordination
      And integrates with LanceDB memory palace

    Examples:
      | scale             | use_case                  | pattern       | stigmergy              |
      | Atomic Unit       | Simple sequential tasks   | 1-1-1-1 PREY  | Hot Loop (NATS)        |
      | Fractal Squad     | High concurrency testing  | 8-8-8-8 PREY  | Hot Loop (NATS) + Probabilistic |
      | Diamond Swarm     | Strategic domain missions | 1-8-64-8-1    | Cold Loop (LanceDB)    |
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Dispatch Trinity Workflow
def dispatch_trinity_workflow(scale: str, use_case: str) -> dict:
    """
    Selects and configures the appropriate Hive Fleet workflow pattern.
    """
    patterns = {
        "Atomic Unit": {
            "structure": "Observer -> Bridger -> Shaper -> Assimilator",
            "stigmergy": "Hot Loop (NATS)",
            "agents": "1-1-1-1 PREY"
        },
        "Fractal Squad": {
            "structure": "8 Parallel Agents per phase with Hidden Disruptors",
            "stigmergy": "Hot Loop (NATS) + Probabilistic Spread",
            "agents": "8-8-8-8 PREY"
        },
        "Diamond Swarm": {
            "structure": "Commander -> 8 Squads -> 64 Workers -> 8 Synthesizers -> Apex",
            "stigmergy": "Cold Loop (LanceDB)",
            "agents": "1-8-64-8-1"
        }
    }
    
    pattern = patterns.get(scale, {})
    if not pattern:
        raise ValueError(f"Unknown scale: {scale}")
    
    # Simulate activation (integrate with NATS/LanceDB in prod)
    print(f"Activating {pattern['agents']} for {use_case}")
    return {
        "level": {"Lvl0": "hands", "Lvl1": "arms", "Lvl2": "body"}.get(scale, "unknown"),
        **pattern
    }
```

## ⚔️ Synergies
*   **PREY Integration**: Builds on prey-1111-design-v1 (atomic), prey-8888-design-v2 (squad), swarm-186481-design-v1 (swarm).
*   **Stigmergy Backbone**: Shares Hexagonal Stigmergy Schema; hot NATS loops for speed, cold LanceDB for persistence.
*   **Hierarchical Scaling**: Lvl 0 (hands: 1-1-1-1) → Lvl 1 (arms: 8-8-8-8) → Lvl 2 (body: 1-8-64-8-1).
*   **Hive Fleet Core**: Feeds into Obsidian campaigns for domain decomposition and massive parallelism.