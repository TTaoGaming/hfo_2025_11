---
card:
  id: 550e8400-e29b-41d4-a716-446655440215
  source: design_stigmergy_substrate.md
  type: Concept
---

# 🃏 Stigmergy Substrate

> **Intuition**: The environment is the message—agents shape a multi-modal substrate (signal/file/db) to enable emergent, loosely-coupled coordination mimicking nature's pheromone trails.

## 📜 The Incantation (Intent)
```gherkin
Feature: Stigmergy Substrate for Async AI Coordination

  Scenario: Route and Elevate High-Urgency Signal via Substrate Phases
    Given a new "Error Log" signal erupts into the Liquid Substrate (NATS JetStream)
    When a Reflex Agent (Low-cost model) monitors the Liquid Substrate
    And detects "urgency: high" potential
    Then it tags the signal and quenches it into the Crystalline Substrate (Filesystem)
    And devitrifies a summary into the Sedimentary Substrate (Postgres/Vector DB)
    So that a Reason Agent (High model) can mine it later for root-cause analysis
    And deposit a fix back into the Crystalline Substrate
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Substrate deposit/read cycle (Hexagonal Port)
import asyncio
from typing import Dict, Any, Literal
from nats.aio.client import Client as NATS

async def substrate_cycle(
    nats: NATS,
    fs_path: str,
    vector_db,
    action: Literal["deposit", "mine"],
    medium: Literal["liquid", "crystalline", "sedimentary"],
    payload: Dict[str, Any],
    tags: Dict[str, str] = None
) -> Dict[str, Any]:
    """
    Stigmergic interaction: Deposit pheromone or mine traces without direct agent coupling.
    """
    if action == "deposit":
        if medium == "liquid":
            await nats.publish("hive.signals", payload)  # Erupt magma
        elif medium == "crystalline":
            with open(fs_path, "w") as f:
                f.write(str(payload))  # Quench obsidian
        elif medium == "sedimentary":
            vector_db.insert(payload, metadata=tags or {})  # Layer sediment
    elif action == "mine":
        # Poll/query substrate (async backpressure handled by medium)
        if medium == "liquid":
            msgs = await nats.fetch("hive.signals", 10)
            return [msg.data for msg in msgs]
        # ... similar for others
    return {}
```

## ⚔️ Synergies
*   **Hexagonal Holon Architecture**: Utilizes ports/adapters for substrate mediums, ensuring agent independence (links to architecture_hexagonal_holon.md).
*   **QD Optimization**: Tiered AI spectrum (Reflex/Logic/Reason/Apex) routes via substrate phases for cost-efficiency.
*   **Obsidian Phase Transitions**: Liquid (NATS) → Crystalline (FS) → Sedimentary (Vector DB) enables resilient backpressure and evolution.
*   **Defined Workflow**: Matches brain/design_stigmergy_substrate.feature for Gherkin validation.
*   **Scalability Hooks**: Supports 1000+ Reflex swarms with single Apex oversight, no direct inter-agent calls.