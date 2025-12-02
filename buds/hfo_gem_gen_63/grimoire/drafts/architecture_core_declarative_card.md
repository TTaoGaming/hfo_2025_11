---
card:
  id: declarative-intent-loading-gen51
  source: architecture_core_declarative.md
  type: Concept
---

# 🃏 Declarative Intent Loading

> **Intuition**: The documentation is the code—Gherkin features declare intent, which the Genesis Protocol compiles into autonomous agents that fulfill it in the world.

## 📜 The Incantation (Intent)
```gherkin
Feature: Declarative Intent Loading

  Scenario: Boot system behavior from Gherkin intents
    Given Gherkin feature files in "brain/*.feature" defining the "what" and "why"
    When the Genesis Protocol in "genesis.py" parses the features
    Then it spawns configured Agents in "body/" to execute the "how"
    And LangSmith traces runtime execution back to the originating scenarios
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Genesis Protocol Core
from behave.parser import FeatureParser  # Gherkin parser
from agent_factory import spawn_champion_agent

def genesis(feature_paths):
    """
    Parse declarative intents and spawn fulfilling agents.
    """
    parser = FeatureParser()
    for path in feature_paths:
        feature = parser.parse_file(path)
        for scenario in feature.scenarios:
            config = {
                'intent': scenario.name,
                'steps': [step.text for step in scenario.steps],
                'trace_id': feature.filename
            }
            agent = spawn_champion_agent(config)
            agent.activate()  # Loop: Observe -> Act -> Feedback
```

## ⚔️ Synergies
*   **Brain → Body Pipeline**: Loads intents from `brain/*.feature` to spawn agents in `body/hands/`
*   **Traceability Loop**: Integrates with LangSmith for linking runtime traces to Gherkin requirements
*   **Genesis Hub**: Central compiler (`genesis.py`) that bridges declarative "Word" to agent "Flesh"
*   **Gen 51 Philosophy**: Enables Intent-Based Engineering, making docs executable and feedback reflexive