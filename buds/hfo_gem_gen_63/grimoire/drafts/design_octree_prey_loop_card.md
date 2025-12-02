---
card:
  id: hfo-octree-prey-loop-v1
  source: design_octree_prey_loop.md
  type: Concept
---

# 🃏 Octree PREY Loop & Trust Engine

> **Intuition**: Trust emerges not from solitary agents but from adversarial quorums where hidden disruptors test the hive's immunity, scaling hallucinations into Byzantine consensus.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hive Trust via Atomic PREY Loop

  Scenario: Solipsistic Agent Yields Signal for Morphic Octet Validation
    Given a Level-0 OctreeAgent with read-only access and stigmergy emissions
    When the agent cycles through Perceive-React-Execute-Yield
    And emits a NATS signal "hfo.octree.{id}.yield" with self-reflection
    Then Level-1 Morphic Octet ingests signals
    And debates via O.B.S.I.D.I.A.N. roles with hidden Disruptor injection
    And commits changes if >66% quorum after Immunity Check and Reveal
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Atomic PREY Loop (L0 Agent)
import nats  # Stigmergy via NATS JetStream

async def prey_loop(agent_id: str, context: dict) -> dict:
    # P: Perceive - Gather full context (read-only)
    perception = await agent.perceive(context)  # Files, memory, web
    
    # R: React - Plan action
    plan = agent.react(perception)
    
    # E: Execute - Simulate/Draft (no real writes)
    draft = agent.execute(plan)  # Sandbox /tmp only
    
    # Y: Yield - Self-reflect & emit stigmergy signal
    reflection = agent.reflect(draft)
    signal = {
        "agent_id": agent_id,
        "proposal": draft,
        "reflection": reflection,
        "reveal_payload": None  # Hidden Disruptor appends here if applicable
    }
    
    # Emit to NATS for L1 quorum
    nc = await nats.connect()
    await nc.publish(f"hfo.octree.{agent_id}.yield", payload=str(signal).encode())
    await nc.close()
    
    return signal
```

## ⚔️ Synergies
*   **Fractal Holarchy**: Builds on `octree_fractal_holarchy.py` for L0 `OctreeAgent` instances (10-100 swarms).
*   **Stigmergy Backbone**: Relies on `hfo_sdk/stigmergy.py` for NATS JetStream signal buffering and ingestion.
*   **Quorum Chamber**: Integrates with pending `research_swarm.py` for L1 O.B.S.I.D.I.A.N. roles (Observer, Bridger, Shaper, etc.).
*   **Adversarial Trust**: Enforces "Negative Trust Protocol" linking to MITRE ATT&CK via Disruptor/Immunizer/Assimilator dynamics.
*   **Glass Box Enforcement**: Complements repo permissions where L0 writes sandbox only, L1 holds git commit keys.