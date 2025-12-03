---
octagon:
  ontos:
    id: intent-navigator-temporal
    type: intent
    owner: Swarmlord
  logos:
    protocol: OBSIDIAN-STACK
    format: literate-gherkin
  techne:
    stack:
    - temporalio
    - python-sdk
  chronos:
    status: active
    urgency: 1.0
    generation: 63
  pathos:
    stress_level: 0.0
    validation: pending
  ethos:
    security_level: internal
    compliance:
    - hfo-standard-gen63
  topos:
    address: buds/hfo_gem_gen_63/brain/intent_navigator_temporal.md
  telos:
    viral_factor: 1.0
    meme: The Durable Will of the Hive.
---

# 🕷️ Intent: The Navigator (Temporal Orchestrator)

> **Context**: Gen 63 (The Hydra Platform)
> **Goal**: To implement the **Navigator (Telos)** as a **Temporal Workflow**, ensuring that long-running research tasks are durable, retriable, and observable.

## 📜 Declarative Intent (Gherkin)

```gherkin
Feature: The Navigator (Orchestrator)
  As the Swarmlord
  I want my Research Agents to survive crashes and restarts
  So that "Deep Research" can span hours or days without data loss.

  Rule: The Navigator MUST use Temporal
    Given the file `buds/hfo_gem_gen_63/07_navigator_brain/workflows.py`
    Then it must define a `ResearchWorkflow` class
    And it must be decorated with `@workflow.defn`
    And it must orchestrate the "Sense -> Make Sense -> Act" loop.

  Rule: Activities MUST be Atomic
    Given the file `buds/hfo_gem_gen_63/07_navigator_brain/activities.py`
    Then it must define atomic tasks:
      | Activity | Description |
      | search_memory(query) | Query the Bridger (LanceDB) |
      | search_web(query) | Query the Scout (MCP) |
      | synthesize_report(context) | Call the LLM to write the report |

  Rule: The Agent is the Client
    Given the file `buds/hfo_gem_gen_63/07_navigator_brain/research_agent.py`
    Then it must NOT run the logic directly
    It must connect to the Temporal Client
    And submit the `ResearchWorkflow` for execution.
```
