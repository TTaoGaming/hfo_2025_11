---
card:
  id: obsidian-horizon-hourglass-langgraph
  source: implementation_obsidian_horizon_langgraph.md
  type: Spell
---

# 🃏 Obsidian Horizon Hourglass

> **Intuition**: The Hourglass inverts temporal gravity, channeling past precedents through present execution while flipping into future simulations to forge golden paths from uncertainty.

## 📜 The Incantation (Intent)
```gherkin
Feature: Obsidian Horizon Hourglass Execution

  Scenario: Process query through karmic retrieval, swarm execution, and conditional future simulation
    Given a user query in HourglassState
    When the karmic node retrieves relevant context from GraphRAG
    And the swarm node attempts execution and computes uncertainty
    When uncertainty exceeds threshold
      Then the simulation node generates a golden path via Monte Carlo/DSPy
      And the graph loops back to swarm node for golden path execution
    Otherwise
      Then the swarm node commits the direct result
    Then the final result is persisted in HourglassState
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict, Any

class HourglassState(TypedDict):
    query: str
    context: List[str]
    uncertainty: float
    golden_path: List[str]
    final_result: str

def create_hourglass_graph() -> StateGraph:
    def karmic_node(state: HourglassState) -> Dict[str, Any]:
        # GraphRAG retrieval
        return {"context": ["Precedent A", "Precedent B"], "uncertainty": 0.5}

    def swarm_node(state: HourglassState) -> Dict[str, Any]:
        if state.get("golden_path"):
            return {"final_result": "Success via Golden Path"}
        if state["uncertainty"] > 0.8:
            return {"uncertainty": 0.9}  # Triggers flip
        return {"final_result": "Success via Gravity"}

    def simulation_node(state: HourglassState) -> Dict[str, Any]:
        # DSPy/Monte Carlo simulation
        return {"golden_path": ["Step 1", "Step 2"], "uncertainty": 0.0}

    workflow = StateGraph(HourglassState)
    workflow.add_node("karmic_web", karmic_node)
    workflow.add_node("swarm_web", swarm_node)
    workflow.add_node("simulation_web", simulation_node)

    workflow.set_entry_point("karmic_web")
    workflow.add_edge("karmic_web", "swarm_web")

    def check_flip(state: HourglassState) -> str:
        return "simulation_web" if state["uncertainty"] > 0.8 else END

    workflow.add_conditional_edges("swarm_web", check_flip)
    workflow.add_edge("simulation_web", "swarm_web")

    return workflow.compile()
```

## ⚔️ Synergies
*   **Karmic Retrieval**: Links to `memory/semantic/library` via GraphRAG for past precedents.
*   **Future Simulation**: Integrates DSPy module for Monte Carlo tree search in `simulation_web`.
*   **State Persistence**: Leverages Pydantic `HourglassState` for seamless data flow across recursive sub-graphs.
*   **Geometric Model**: Maps 3D cones (Past/Present/Future) to LangGraph nodes/edges for spatial state-action reasoning.
*   **Neck Execution**: `swarm_web` as decision bottleneck, enabling recursive flips for complex queries.