# Intent: Local Heartbeat Agent

> **Status**: Active
> **Role**: Lvl 0 (Atomic)
> **Hardware**: Chromebook Plus (Local)

## Context
The "Heartbeat" is the lowest level of the HFO Holarchy. It provides the rhythm for the swarm. It must be:
1.  **Local**: No cloud latency or cost.
2.  **Offline**: Resilient to network failure.
3.  **Always On**: 24/7 monitoring.

## Implementation
*   **Engine**: Ollama
*   **Model**: Gemma 3 4B (Google Native)
*   **Memory**: Stateless (Model) + Stigmergy (LanceDB/NATS)
