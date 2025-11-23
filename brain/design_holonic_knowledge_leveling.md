---
title: 'Holonic Knowledge Leveling: The RPG of Truth'
bluf: 'We gamify GraphRAG by assigning "Levels" (0-3) and "Attributes" (STR, DEX, INT, WIS, CHA) to knowledge artifacts. Information must "Level Up" through increasingly rigorous Swarm Consensus (Hot) to become Canonical Truth (Cold).'
story: '> **The Concept**: Information is not binary (True/False). It is a living organism that grows stronger with scrutiny.

  > **The Mechanic**:
  > 1. **Hot Phase (The Gym)**: Artifacts gain XP by surviving NATS debates (Swarm Consensus).
  > 2. **Cold Phase (The Save)**: Artifacts "Level Up" when written to Postgres/Graph with a higher Trust Score.

  > **The Goal**: A self-pruning Knowledge Graph where only "High Level" nodes are queried for critical decisions, while "Low Level" nodes provide creative noise.'
tags:
  - architecture
  - gamification
  - knowledge_graph
  - stigmergy

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440100
    type: design
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.8
    decay: 0.1
    created: '2025-11-23T12:00:00Z'
  topos:
    address: 1.0.0
    links:
      - brain/spec_holonic_leveling.feature
      - brain/design_mountain_web_stigmergy.md
  telos:
    viral_factor: 0.9
    meme: "🎮 Knowledge RPG: Level Up your Truth"

---

# 🎮 Holonic Knowledge Leveling (HKL)

## 1. The Leveling System (Log 10 Scale)

| Level | Rank | Agent Count | Trust Score | Requirement | Storage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Lvl 0** | **Spark** | 1 (Individual) | 10% | Raw Output, No Consensus | Ephemeral (NATS) |
| **Lvl 1** | **Ember** | 10 (Squad) | 50% | 80% Squad Consensus | Episodic (File/JSON) |
| **Lvl 2** | **Flame** | 100 (Platoon) | 80% | Multi-Squad Verification | Semantic (Vector DB) |
| **Lvl 3** | **Inferno** | 1000 (Hive) | 99% | Temporal Persistence (>1 week) | Canonical (Graph DB) |

## 2. The Attribute System (D&D for Data)

Every Artifact (Holon) has a character sheet:

*   **STR (Strength)**: **Durability**. How long has this truth survived without being refuted?
    *   *Metric*: Time since creation / Decay rate.
*   **DEX (Dexterity)**: **Velocity**. How fast does this signal travel through the NATS network?
    *   *Metric*: Re-broadcast count / Latency.
*   **INT (Intelligence)**: **Density**. How much meaning is packed into the tokens?
    *   *Metric*: Vector Embedding Density (Information/Token ratio).
*   **WIS (Wisdom)**: **Consensus**. How many unique agents agree with this?
    *   *Metric*: Unique Signatures in the Ledger.
*   **CHA (Charisma)**: **Virality**. How many other nodes link to this?
    *   *Metric*: In-degree centrality in the Graph.

## 3. The Gameplay Loop (Hot -> Cold -> Hot)

1.  **Spawn (Lvl 0)**: An agent has an idea. It emits a **Spark** (Hot Signal).
2.  **Party Up (Lvl 0 -> 1)**: The Spark attracts a Squad. They debate. If they agree, they mint an **Ember** (Cold File).
3.  **Raid (Lvl 1 -> 2)**: The Ember is picked up by a Platoon (Research Swarm). They stress-test it against other Embers. If it survives, it becomes a **Flame** (Vector).
4.  **Ascension (Lvl 2 -> 3)**: The Flame burns in the Knowledge Graph. If it links to many other Flames and survives the test of time (Temporal), it becomes an **Inferno** (Canonical Truth).

## 4. GraphRAG Implications

*   **Query Routing**:
    *   "What is the absolute truth?" -> Query **Lvl 3 Only**.
    *   "What are the latest rumors?" -> Query **Lvl 0-1 Stream**.
    *   "Give me a creative solution." -> Mix **Lvl 1** (Novelty) with **Lvl 2** (Stability).

*   **Pruning**:
    *   Lvl 0 Sparks that don't level up within 24h are extinguished (Garbage Collection).
    *   Lvl 1 Embers that lose STR (refuted) are archived.
