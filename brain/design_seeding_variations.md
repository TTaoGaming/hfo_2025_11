---
title: Design - Hexagonal Seeding Variations
status: Draft
domain: Architecture
owners:
- Swarmlord
type: Design Document
hexagon:
  ontos:
    id: 6a391fda-4419-4868-96e2-55f64fc04b95
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.577958Z'
    generation: 51
  topos:
    address: brain/design_seeding_variations.md
    links: []
  telos:
    viral_factor: 0.0
    meme: design_seeding_variations.md
---


# 💎 Design: Hexagonal Seeding Variations (The Silica Saturation)

> **Context**: We need to define the "Seeding" mechanism—how the Hexagonal Headers (Pheromones) are injected, maintained, and evolved. This is the "Sandstorm" that permeates the Hive.

## 🧠 The Metaphor: "The Silica Saturation"
*   **Concept**: A pervasive, fine-grained "dust" (headers) that coats every object in the Hive.
*   **Function**:
    *   **Identification**: Friend/Foe (Me/Not Me).
    *   **Dimensionality**: Defines the 6 dimensions (Ontos, Telos, etc.) of the object.
    *   **Stigmergy**: Provides the "scent" for other agents to follow.

## 🧬 Variation 1: The Static Crystal (Current Baseline)
*   **Description**: Hard-coded YAML headers injected at file creation.
*   **Pros**: Simple, deterministic, easy to index (Regex/YAML).
*   **Cons**: Brittle. If the file evolves, the header might become stale (Drift).
*   **Implementation**: `genesis.py` injects once. `guard_stigmergy_headers.py` checks existence.
*   **Confidence**: **High** (for existence), **Low** (for accuracy over time).

## 🧬 Variation 2: The Living Pheromone (Dynamic Decay)
*   **Description**: Headers include `last_visited_by`, `last_updated`, and `decay_rate`.
*   **Mechanism**: Every time an agent touches a file, it updates the `chronos` section. If a file isn't touched for $X$ days, its `urgency` decays.
*   **Pros**: Reflects the *actual* "heat" of the file. Allows "Garbage Collection" of cold memories.
*   **Cons**: High write churn. Git history pollution (every read/touch might trigger a commit).
*   **Mitigation**: Only update on significant changes or use a sidecar "Pheromone DB" (Redis/NATS KV) instead of file headers.

## 🧬 Variation 3: The Holographic Shard (Fractal Context)
*   **Description**: The header contains a compressed "Merkle Proof" or "Hash Link" to the parent Holon (Squad/Swarm).
*   **Mechanism**: `topos` includes `parent_hash`. This creates a verifiable chain of custody back to the original Intent.
*   **Pros**: **Defense in Depth**. A file cannot be "faked" without breaking the chain. Allows "Zoom Out" from any file to see the whole Hive.
*   **Cons**: Complex to maintain. Renaming/Moving files breaks the chain (requires re-hashing).

## 🧬 Variation 4: The Quantum Superposition (Byzantine Versions)
*   **Description**: The header allows for *multiple* conflicting truths (e.g., `telos_v1`, `telos_v2_disruptor`).
*   **Mechanism**: Used during "Active Debate". The file holds the state of the argument until a Consensus Council collapses it to a single Truth.
*   **Pros**: Native support for **Epistemic Humility**. The system acknowledges it doesn't know yet.
*   **Cons**: Extremely complex parsing. Tools need to handle "Schrodinger's Files".

## 🏆 Recommendation: "The Living Hologram" (Hybrid 2 + 3)
*   **Phase 1**: Stick with **Static Crystal** for stability.
*   **Phase 2**: Add **Holographic Links** (`parent_hash`) to enforce the "Chain of Intent".
*   **Phase 3**: Move **Living Pheromones** (Decay/Heat) to NATS KV (Sidecar) to avoid Git pollution.

---

## 🛡️ Defense in Depth & Epistemic Humility

### The Confidence Ladder (HFO Levels)
*   **Level 0 (Atomic Agent)**: **50-80% Confidence**. "I think this is true, but I am alone." (Skepticism: High).
*   **Level 1 (Squad - 10 Agents)**: **Max 90% Confidence**. "We have debated, but there is a Disruptor among us." (Skepticism: Medium).
*   **Level 2 (Swarm - 100 Agents)**: **Max 99% Confidence**. "The Council of 100 has spoken." (Skepticism: Low).
*   **Level 3+ (Hive - 1000+ Agents)**: **99.9...% Confidence**. Asymptotic approach to Truth. Never 100%.

### The Hidden Disruptor (Double Spy)
*   **Role**: A "Bad Honest Actor".
*   **Function**: Intentionally injects plausible falsehoods or challenges assumptions.
*   **Ratio**: $\approx 10\%$ of the population (1 in 10).
*   **Goal**: If the Swarm cannot detect the Disruptor, the Swarm is weak.
