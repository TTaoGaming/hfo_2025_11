---
card:
  id: 1a2a017d-e342-44fe-b9c3-3e5369e17a29
  source: infrastructure_loops.md
  type: Concept
---

# 🃏 Cognitive Loops: PREY & SWARM

> **Intuition**: In the Hive's fractal holarchy, emergent intelligence arises from atomic PREY execution cycles (Perceive-React-Execute-Yield) fractally nested within strategic SWARM orchestration (Set-Watch-Act-Review-Mutate), powering adaptive predation at every scale.

## 📜 The Incantation (Intent)
```gherkin
Feature: Fractal Cognitive Loops for Hive Adaptation

  Scenario: Orchestrate a SWARM Loop via Nested PREY Agents
    Given a mission intent from the Navigator
    When Observers execute PREY loops to Watch telemetry
    And Shapers execute PREY loops to Act in parallel with Disruptor noise
    And Immunizers execute PREY loops to Review for Byzantine Quorum
    And Forge executes PREY loop to Mutate via MAP-Elites optimization
    Then the Hive yields adaptive directives with improved signal-to-noise ratio
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Fractal Loop Executors
import asyncio
from typing import Callable, Any

class PREYLoop:
    """Atomic tactical cognition engine."""
    def __init__(self, perceive: Callable[[], Any], react: Callable[[Any], Any],
                 execute: Callable[[Any], Any], yield_: Callable[[Any], None]):
        self.perceive = perceive
        self.react = react
        self.execute = execute
        self.yield_ = yield_

    async def run(self):
        while True:
            obs = self.perceive()
            action = self.react(obs)
            result = await self.execute(action)
            self.yield_(result)
            await asyncio.sleep(0.1)  # Tactical cycle timing

class SWARMLoop:
    """Strategic holonic orchestrator of PREY sub-loops."""
    def __init__(self):
        self.preys = {}  # Role -> PREYLoop: navigator, observer, shaper, etc.

    async def run(self, mission_intent: str):
        # Set: Initialize PREY agents
        self.preys['navigator'].yield_(mission_intent)
        # Watch -> Act -> Review -> Mutate via fractal delegation
        tasks = [prey.run() for prey in self.preys.values()]
        await asyncio.gather(*tasks)
```

## ⚔️ Synergies
*   Powers agent roles (Navigator, Observer, Shaper, Immunizer, Forge, Disruptors) via dedicated PREY instances for fractal execution.
*   Enables Byzantine Quorum and hidden adversarial testing in Review phase for robust SNR improvement.
*   Nests within GROWTH (campaign F3EAD) and HIVE (meta-evolution Double Diamond) loops for holarchic scaling.
*   Operates over Network Virtual Stigmergy Layer on NATS JetStream, coordinating parallel Map-Reduce workflows.
*   Drives Evolutionary Forge with MAP-Elites QD for diverse exemplar mutation, fueling Hive meta-adaptation.