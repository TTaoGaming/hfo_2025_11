---
title: Claim Check Pattern (Rich Stigmergy)
status: Active (Gen 51)
domain: Architecture
owners:
- Swarmlord
type: Design Pattern

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 60e75863-bbfb-4ead-b384-1634a35532a8
    type: doc
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T06:32:09.831196Z'
  topos:
    address: 1.0.0
    links: []
  telos:
    viral_factor: 0.0
    meme: Claim Check Pattern (Rich Stigmergy)
---


# 🎫 Claim Check Pattern (Rich Stigmergy)

## ⚡ BLUF (Bottom Line Up Front)
The **Claim Check Pattern** is the mechanism that enables **Total Decoupling** and **Hexagonal Composability** in Hive Fleet Obsidian. It ensures that NATS JetStream remains a high-speed nervous system (Signals) while heavy data (Artifacts) is offloaded to durable storage (Memory). This allows the Swarm to function as an **Emergent Complex Adaptive System**.

## 🧬 The Core Concept

### The Problem: Fat Messages
If an Agent generates a 50KB Markdown report and sends it over NATS:
1.  **Throughput Drops**: NATS is optimized for small, fast messages.
2.  **Coupling Increases**: The consumer *must* parse the whole blob to know if it cares.
3.  **Memory Bloat**: The NATS JetStream store fills up with ephemeral data.

### The Solution: Rich Stigmergy
We split the output into two parts:
1.  **The Artifact (Body)**: The full content, saved to **Postgres (pgvector)**.
    *   *Why Postgres?* It allows for immediate semantic indexing and querying.
    *   *Exception*: High-level "Digests" (Human Readable) are also saved to Disk.
2.  **The Signal (Pheromone)**: A lightweight JSON pointer sent over NATS.

The Signal contains **Rich Metadata** (Tags, Summary, Confidence) so consumers can filter *without* retrieving the body. This is **Rich Stigmergy**.

## 📊 Visualization

### 1. The Decoupled Flow

```mermaid
graph LR
    subgraph Producer [Act Phase]
        Shaper[Shaper Agent]
        DB[(Postgres/pgvector)]
    end

    subgraph Transport [Nervous System]
        NATS((NATS JetStream))
    end

    subgraph Consumer [Review Phase]
        Immunizer[Immunizer Agent]
    end

    Shaper -->|1. Write Artifact| DB
    Shaper -->|2. Publish Signal| NATS
    NATS -->|3. Push Signal| Immunizer
    Immunizer -->|4. Read Metadata| Immunizer
    Immunizer -->|5. Claim Check| DB
```

### 2. Hexagonal Composability (The SWARM Loop)

By using Claim Checks, each stage of the SWARM loop becomes an independent "Hexagon" that plugs into the NATS bus. They don't know about each other.

```mermaid
graph TD
    subgraph SetPhase [Set Phase]
        Navigator -->|Signal: Mission| NATS
    end

    subgraph WatchPhase [Watch Phase]
        Observer -->|Claim: Mission| NATS
        Observer -->|Signal: Plan| NATS
    end

    subgraph ActPhase [Act Phase]
        Shaper -->|Claim: Plan| NATS
        Shaper -->|Signal: Finding| NATS
    end

    subgraph ReviewPhase [Review Phase]
        Immunizer -->|Claim: Finding| NATS
        Immunizer -->|Signal: Digest| NATS
    end

    NATS((NATS JetStream))
```

## 🛠️ Implementation Standard

### The Payload Schema
Every Stigmergy Signal MUST adhere to this schema to be a valid Claim Check.

```json
{
  "id": "task-uuid-1234",
  "role": "Shaper",
  "mission_slug": "operation-phoenix",
  "round": 1,
  "confidence": 0.95,
  "tags": ["research", "security", "critical"],
  "location": {
    "type": "postgres",
    "table": "artifacts",
    "id": "task-uuid-1234",
    "url": "postgres://hfo:hfo@localhost:5435/hfo_memory"
  },
  "summary": "Vulnerability detected in sector 7G...",
  "checksum": "sha256:a1b2c3d4..."
}
```

### The "Rich" Metadata Rules
1.  **Filterable**: A consumer must be able to say "I only want `critical` tags" without downloading the file.
2.  **Descriptive**: The `summary` (first 200 chars) allows for "Fast Thinking" (Heuristic filtering).
3.  **Verifiable**: The `checksum` ensures the artifact hasn't been tampered with (Security).

## 🦅 Strategic Value
*   **Emergence**: Because components are decoupled, you can add new "Listeners" (e.g., a Dashboard, an Auditor, a Learning Module) without changing the Producer.
*   **Resilience**: If the Reviewer crashes, the Artifact is safe on disk, and the Signal is safe in the NATS Stream. The Reviewer can restart and "Claim" it later.
*   **Scalability**: You can have 1 Shaper and 100 Reviewers, or 100 Shapers and 1 Reviewer. The architecture doesn't care.
