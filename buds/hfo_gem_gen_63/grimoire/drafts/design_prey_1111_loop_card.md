---
card:
  id: prey-1111-loop
  source: design_prey_1111_loop.md
  type: Concept
---

# 🃏 1-1-1-1 PREY Loop

> **Intuition**: A lone agent cycles through four biased cognitive hats—Observer, Bridger, Shaper, Assimilator—to execute a complete, stigmergic OODA loop, forming the self-sustaining atomic intelligence unit of the Hive Fleet.

## 📜 The Incantation (Intent)
```gherkin
Feature: 1-1-1-1 PREY Loop Execution

  Scenario: Single agent completes one stigmergic OODA cycle
    Given the agent retrieves prior YieldReport from NATS KV using its Secure ID
    When the agent sequentially adopts the four Cognitive Hats:
      * Observer phase generates PerceptionReport via Cynefin/CBR and publishes to NATS JetStream
      * Bridger phase formulates ReactionPlan from PerceptionReport and publishes to NATS JetStream
      * Shaper phase executes ReactionPlan with tools and publishes ExecutionResult to NATS JetStream
      * Assimilator phase reflects on ExecutionResult, generates YieldReport, publishes to NATS JetStream, and updates NATS KV state
    Then the loop state advances statelessly for the next cycle, with writes restricted to NATS only
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import nats
from typing import Dict, Any

async def prey_1111_loop(agent_id: str, nc: nats.NATS) -> Dict[str, Any]:
    """Executes one 1-1-1-1 PREY Loop cycle via four hats."""
    kv = await nc.kv("prey-state")
    
    # Perceive (Observer Hat)
    prev_yield = await kv.get(f"{agent_id}_yield".encode())
    perception = await observe_environment(prev_yield.data.decode() if prev_yield else "")
    await nc.publish("prey.perception", perception.encode())
    
    # React (Bridger Hat)
    reaction_plan = await bridge_perception(perception)
    await nc.publish("prey.reaction", reaction_plan.encode())
    
    # Execute (Shaper Hat)
    exec_result = await shape_execution(reaction_plan)
    await nc.publish("prey.execution", exec_result.encode())
    
    # Yield (Assimilator Hat)
    yield_report = await assimilate_reflection(exec_result)
    await nc.publish("prey.yield", yield_report.encode())
    await kv.put(f"{agent_id}_yield".encode(), yield_report.encode())
    
    return {"cycle_complete": True, "yield": yield_report}

# Placeholder hat functions (bias-specific)
async def observe_environment(state: str) -> str:
    # Cynefin + CBR logic
    return f"PerceptionReport: Cynefin=Complex; CBR=MatchCaseX"

async def bridge_perception(percept: str) -> str:
    return f"ReactionPlan: Strategy=ConnectNodes"

async def shape_execution(plan: str) -> str:
    # Tool calls
    return f"ExecutionResult: ToolsUsed=API; Outcome=Success"

async def assimilate_reflection(result: str) -> str:
    # Reflexion audit
    return f"YieldReport: Learned=OptimizeNext; Aligned=True"
```

## ⚔️ Synergies
*   **NATS JetStream + KV**: Enables hot stigmergy for stateless chaining (`Yield(N)` → `Perceive(N+1)`) across low-resource nodes like Chromebooks.
*   **Cynefin Framework & CBR**: Powers Observer hat for contextual sensing (Simple/Complicated/Complex/Chaotic classification).
*   **Security Model**: Restricts writes to NATS only, preventing direct codebase/DB mods (downstream Assimilators handle persistence).
*   **Hive Fleet Scaling**: Atomic squad pattern chains into multi-agent swarms; integrates with LanceDB for memory and tools for Shaper execution.
*   **Gen 55 Synapse APEX**: Embeds in broader HFO GEM generation pipeline for emergent intelligence.