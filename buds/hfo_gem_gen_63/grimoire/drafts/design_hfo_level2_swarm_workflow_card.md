---
card:
  id: HFO-L2-SWARM
  source: design_hfo_level2_swarm_workflow.md
  type: Spell
---

# 🃏 HFO Level 2: The SWARM Workflow

> **Intuition**: The hive breathes evolution through the diamond pulse of 1-8-64-8-1, expanding singular intent into fractal frenzy before contracting into mutational wisdom.

## 📜 The Incantation (Intent)
```gherkin
Feature: HFO Level 2 Swarm Workflow Execution

  Scenario: Process Mission Intent through S-W-A-R-M Pulse
    Given a MissionManifest defined by Navigator with constraints and success criteria
    When WATCH phase spawns 8 async dimensional watchers generating ContextStreams
    And ACT phase deploys 64 Octarchy agents in PREY loops producing raw artifacts with hidden disruptors
    And REVIEW phase runs Byzantine consensus via 8 assimilators to yield 8 Validated Facets
    And MUTATE phase synthesizes 1 Holon artifact while applying DSPy/QD optimization to evolve prompts
    Then produce Final Artifact and updated dspy_state.json for next evolutionary cycle
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import asyncio
import dspy  # For prompt mutation
from typing import Dict, Any, List

async def swarm_pulse(mission_manifest: Dict[str, Any]) -> tuple[Dict[str, Any], Dict[str, Any]]:
    """
    Orchestrates the 1-8-64-8-1 S-W-A-R-M workflow.
    """
    # Phase 1: SET (already provided as input)
    
    # Phase 2: WATCH (8 agents)
    context_streams = await asyncio.gather(*[
        watcher.scan(mission_manifest) for watcher in [
            ontos_watcher, logos_watcher, techne_watcher, chronos_watcher,
            pathos_watcher, ethos_watcher, topos_watcher, telos_watcher
        ]
    ])
    
    # Phase 3: ACT (64 agents: 8 squads x 8)
    artifacts = []
    for squad_context in context_streams:
        squad_artifacts = await map_reduce_act(squad_context)  # PREY loops w/ disruptor
        artifacts.extend(squad_artifacts)
    
    # Phase 4: REVIEW (8 assimilators)
    validated_facets = await asyncio.gather(*[
        assimilator.consensus_review(squad_artifacts) for assimilator, squad_artifacts
        in zip(assimilators, chunk_artifacts(artifacts, 8))
    ])
    
    # Phase 5: MUTATE (1 agent)
    holon = injector.synthesize(validated_facets)
    disruption_data = gather_disruption_metrics()
    new_prompts = dspy_teleprompter.optimize(disruption_data)  # QD + DSPy
    
    return holon, {"prompts": new_prompts, "dspy_state": update_dspy_state()}
```

## ⚔️ Synergies
*   **HFO L2 Architecture**: Builds atop the core brain structure, linking to `design_hfo_level2_architecture.md`.
*   **Fractal Disruption**: Integrates Hidden Disruptors from `design_hfo_level2_fractal_disruption.md` in ACT phase for evolutionary friction.
*   **DSPy Teleprompter**: Leverages DSPy for prompt mutation in MUTATE, using success/fail signals from REVIEW.
*   **QD Optimizer**: Applies MAP-Elites for Quality-Diversity selection of champion personas.
*   **Agent Ecosystem**: Pulls contexts from AGENTS.md, requirements.txt, git logs via WATCHers; feeds into Octarchy squads.