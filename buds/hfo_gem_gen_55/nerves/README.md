# ⚡ Nerves (The Bridger)

> **Role**: Bridger (Communicator)
> **Pillar**: Connection
> **Stigmergy Dimension**: **Logos** (Word, Reason, Signal)

## The Cognitive Function
**Nerves** are the seat of **Coordination**. They connect the disparate organs into a unified whole. They manage the flow of information, ensuring that the right signal reaches the right receiver at the right time.

## The Anatomy
*   **`bus/`**: The "Synapse".
    *   The Message Bus (NATS/JetStream) configuration and topics.
    *   Defines the channels for Stigmergy (e.g., `swarm.signals`, `swarm.logs`).
*   **`manifest/`**: The "Map".
    *   Registry of all active Agents, Topics, and Services.

## The HFO Axis
*   **Input**: Signals from all Organs.
*   **Output**: Routed Messages to all Organs.
*   **Failure Mode**: Seizure (Signal Overload/Drop).
