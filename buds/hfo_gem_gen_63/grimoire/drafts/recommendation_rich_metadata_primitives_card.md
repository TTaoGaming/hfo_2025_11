---
card:
  id: rich-metadata-stigmergy-primitives
  source: recommendation_rich_metadata_primitives.md
  type: Concept
---

# 🃏 Rich Metadata Stigmergy Primitives

> **Intuition**: Emulate nature's stigmergy—ant pheromones and slime molds—through composable primitives of signal, decay, spread, and payload for self-cleaning, efficient swarm coordination.

## 📜 The Incantation (Intent)
```gherkin
Feature: Composable Stigmergy Primitives

  Scenario: Agent emits decaying signal with payload pointer
    Given an agent has rich metadata payload stored in cold storage with UUID pointer
    When the agent emits a lightweight StigmergySignal via NATS JetStream on hierarchical subject "hfo.signal.<region>.<type>.<id>"
      with tunable quality, evaporation rate, dispersion, and urgency
    Then subscribers in relevant regions receive the signal
      and compute its current strength via exponential decay S(t) = S₀ · e^{-λt}
      and fetch payload only if strength exceeds threshold
      and the signal self-evaporates to prevent data accumulation
```

## 🧪 The Catalyst (Code)
```python
# The Essence
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
import math
import uuid

class StigmergySignal(BaseModel):
    pointer: str = Field(..., description="UUID/URL to payload in Postgres/S3")
    quality: float = Field(0.5, ge=0.0, le=1.0)
    evaporation: float = Field(0.05, description="Decay constant λ proxy")
    urgency: str = Field("normal", description="Priority: low|normal|high|alarm")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    subject: Optional[str] = Field(None, description="e.g., hfo.signal.brain.idea.123")

def current_strength(signal: StigmergySignal, now: Optional[datetime] = None) -> float:
    """Compute decayed signal strength."""
    if now is None:
        now = datetime.utcnow()
    delta_t = (now - signal.timestamp).total_seconds()
    lambda_decay = signal.evaporation  # Tunable per tick or normalized
    return signal.quality * math.exp(-lambda_decay * delta_t)
```

## ⚔️ Synergies
*   **NATS JetStream**: Enables <1ms signal broadcast with subject hierarchies for targeted spread and noise reduction.
*   **Postgres/pgvector + S3**: Claim-check pattern for durable, heavy payloads referenced by lightweight pointers.
*   **Agent Swarms**: Subscribers compute decay on-the-fly, prioritizing fresh/high-quality signals for anti-fragile focus.
*   **Biomimetic Tuning**: Parameters like evaporation/decay integrate with "Janitor" processes and parameter sweeps for task-specific optimization.
*   **Event Sourcing Alignment**: Supports migration from filesystem (assimilator.py) to structured cold storage for scalable stigmergy.