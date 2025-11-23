---
title: Rich Metadata Stigmergy
status: Proposed
domain: Architecture
owners: [Swarmlord]
type: Design Pattern
---

# 💎 Rich Metadata Stigmergy

## ⚡ BLUF
Stigmergy is not just "traces left in the environment". It is **Information-Dense Signaling**. To enable high-fidelity coordination, HFO signals must carry **Rich Metadata** (Qualitative, Quantitative, Temporal) while keeping the payload lightweight (Claim Check).

## 🧬 The Schema (Signal DNA)

Every NATS message (`hfo.signal.>`) must adhere to this schema:

```json
{
  "id": "uuid-v4",
  "timestamp": "iso-8601",
  "producer_id": "agent-id",
  "claim_check": {
    "storage": "postgres",
    "pointer": "artifact_uuid",
    "hash": "sha256"
  },
  "metadata": {
    "type": "pheromone | artifact | alert",
    "quality": 0.95,          # Confidence/Utility
    "dispersion": 0.5,        # Broadcast Radius (0=Local, 1=Global)
    "evaporation": 0.1,       # Decay Rate per Tick
    "urgency": "high",        # Qualitative Priority
    "tags": ["security", "auth", "critical"]
  }
}
```

## 🌍 The Hunt (Biomimicry & Industry)

We are hunting for the **Optimal Parameters** for this schema.

### 🐜 Nature's Parameters
*   **Ants**: Pheromone type (Food vs Danger), Concentration (Quality), Volatility (Evaporation).
*   **Termites**: Mud pellets (Building blocks), CO2 levels (Ventilation cues).
*   **Slime Mold**: Tube thickness (Flow rate), Pulse frequency (Communication).

### 🏭 Industry Parameters
*   **Event Sourcing**: Event Type, Aggregate ID, Version, Timestamp.
*   **Social Media**: Likes (Quality), Shares (Dispersion), Feed Decay (Evaporation).
*   **Code**: Commits (Artifacts), CI Status (Quality), Blame (Producer).

## 🛠️ Implementation Strategy
1.  **Refactor `research_swarm.py`**: Stop writing to disk. Write to DB.
2.  **Update `StigmergyClient`**: Enforce the Schema.
3.  **Tune Parameters**: Use the Swarm to find the best values for `evaporation` and `dispersion`.
