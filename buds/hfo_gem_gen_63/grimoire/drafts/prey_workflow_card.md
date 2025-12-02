---
card:
  id: prey-workflow-v1
  source: prey_workflow.md
  type: Spell
---

# 🃏 PREY Loop

> **Intuition**: The atomic cognitive cycle powering every Hive agent, fractally ensuring perception informs reaction, execution produces artifacts, and yields stigmergically fuel the collective.

## 📜 The Incantation (Intent)
```gherkin
Feature: The PREY Workflow (Atomic Agent Loop)
  As the Swarmlord
  I want a standardized internal loop for all agents
  So that I can ensure consistent behavior and stigmergic communication

  Background:
    Given the context is "Gen 55 (The Gem)"
    And the pattern is "Perceive-React-Execute-Yield"

  Scenario: The Standard PREY Loop
    Given an agent is active

    When it enters the "Perceive" phase
    Then it shall query "Hot NATS" for recent signals
    And it shall query "Cold LanceDB" for relevant wisdom
    And it shall construct a "Context Object"

    When it enters the "React" phase
    Then it shall analyze the Context
    And it shall formulate a "Plan" or "Strategy"
    And it shall select the appropriate "Tools"

    When it enters the "Execute" phase
    Then it shall execute the Plan using the selected Tools
    And it shall generate an "Artifact" or "Result"

    When it enters the "Yield" phase
    Then it shall publish the Result to "Hot NATS" (KV)
    And it shall emit a "Stigmergy Signal"
    And it shall decide whether to "Loop" or "Terminate"
```

## 🧪 The Catalyst (Code)
```python
# The Essence: LangGraph-powered PREY Loop
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
from dataclasses import dataclass

@dataclass
class Context:
    task: str
    signals: dict  # From NATS
    wisdom: list   # From LanceDB

class AgentState(TypedDict):
    context: Annotated[Context, operator.add]
    plan: str
    result: str
    role: str

def perceive(state: AgentState) -> AgentState:
    # Query Hot NATS & Cold LanceDB
    signals = nats_get_recent(state["task"])  # Placeholder
    wisdom = lancedb_query(state["task"])     # Placeholder
    state["context"] = Context(state["task"], signals, wisdom)
    return state

def react(state: AgentState) -> AgentState:
    # LLM reasoning for plan
    prompt = f"Role: {state['role']}\nContext: {state['context']}\nPlan next steps."
    state["plan"] = llm.invoke(prompt).content  # Placeholder LLM
    return state

def execute(state: AgentState) -> AgentState:
    # Tool execution
    state["result"] = tools.run(state["plan"])  # Placeholder tools
    return state

def yield_phase(state: AgentState) -> str:
    # Publish to NATS
    nats_publish(state["result"])
    return END if is_complete(state) else "perceive"  # Loop or terminate

def prey_loop(role: str, task: str):
    workflow = StateGraph(AgentState)
    workflow.add_node("perceive", perceive)
    workflow.add_node("react", react)
    workflow.add_node("execute", execute)
    workflow.add_node("yield", yield_phase)
    workflow.set_entry_point("perceive")
    workflow.add_edge("perceive", "react")
    workflow.add_edge("react", "execute")
    workflow.add_edge("execute", "yield")
    app = workflow.compile()
    initial = {"task": task, "role": role}
    return app.invoke(initial)
```

## ⚔️ Synergies
* **Hybrid Memory**: Reads recent signals from Hot NATS (KV) in Perceive; queries vectors from Cold LanceDB for wisdom.
* **Swarm Workflow**: Atomic unit scales into Fractal Funnel (1-8-64-8-1) for multi-agent orchestration.
* **Role Adaptations**: Reflexive (Bridger: fast React), Deep (Shaper: reasoning), Critic (Reviewer: validation), Learning (Assimilator: LanceDB writes).
* **LangGraph Integration**: State machine enables iterative loops with conditional Yield decisions.
* **Stigmergy**: Yields publish to NATS, enabling emergent coordination across agents.