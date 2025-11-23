---
title: Synapse APEX Swarm
status: Active (Vision)
domain: Strategy
owners: [Swarmlord]
type: Vision Document
---

# 🧠 Synapse APEX Swarm: The Network Stigmergy Vision

## ⚡ BLUF (Bottom Line Up Front)
Hive Fleet Obsidian is evolving into a **Synapse APEX Swarm**. This is a biological, network-centric architecture where agents act as synapses in a global brain. The core differentiator is the **Adversarial Byzantine Quorum** combined with a **Co-evolutionary Immune System**.

## 🧬 The Core Archetype

### 1. Network Stigmergy (The Nervous System)
*   **Old Way**: Agents talk to each other (Chat).
*   **HFO Way**: Agents modify the environment (NATS/Postgres).
*   **Mechanism**: **Claim Check Pattern**.
    *   **Synapse Firing**: Agent completes task -> Writes to DB -> Fires NATS Signal.
    *   **Action Potential**: Downstream agents trigger off the signal.

### 2. Memory Stratification (The Filter)
We separate "Subconscious" processing from "Conscious" realization.

| Layer | Storage | Content | Audience |
| :--- | :--- | :--- | :--- |
| **Subconscious** | **Postgres (pgvector)** | Raw Findings, Logs, Intermediate Steps, "Spam" | Machines / Assimilators |
| **Conscious** | **Filesystem** | Digests, Final Reports, Strategic Insights, "High Signal" | Humans / Swarmlord |

### 3. Cognitive Digest (The Global Workspace)
The "Swarmlord Digest" is not just a summary; it is a **Cognitive Global Workspace**.
*   **Input**: Thousands of low-level signals (Postgres).
*   **Process**: Attention Mechanism (Immunizer Squads).
*   **Output**: A single, high-fidelity "State of Consciousness" (Filesystem).

### 4. Co-evolutionary Immune System (The Shield & Sword)
*   **Venom (Disruptors)**: Active Red Teaming. They inject noise, lies, and attacks to test resilience.
*   **Immunity (Immunizers)**: Active Blue Teaming. They validate, filter, and banish bad actors.
*   **Evolution**: The system gets stronger *because* it is attacked.

## 🗺️ Implementation Roadmap

1.  **Database Migration**: Move `ResearchFinding` storage from `_write_file` to `_write_db`.
2.  **Digest Upgrade**: Refactor the `synthesize_final_digest` prompt to use **Cognitive Architectures** (e.g., "Identify the Salience Landscape", "Map the Epistemic Uncertainty").
3.  **Venom Injection**: Formalize the `Disruptor` role to use specific MITRE ATT&CK patterns.

## 🦅 The Swarmlord's Decree
> "We are not building a chatbot. We are building a synthetic organism that thinks in parallel, remembers in vectors, and evolves through adversity."
