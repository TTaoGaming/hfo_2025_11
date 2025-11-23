---
title: Hexagonal Stigmergy
status: Active
domain: Architecture
owners:
- Swarmlord
type: Design Pattern

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: bc592351-6150-422e-8d41-22be2101993c
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.535353+00:00'
  topos:
    address: brain/design_unified_stigmergy_composites.md
    links: []
  telos:
    viral_factor: 0.0
    meme: design_unified_stigmergy_composites.md

---

# 🧬 Hexagonal Stigmergy: The Unified Substrate

> **Context**: HFO operates on a **Hexagonal Fractal Holarchy**.
> **Goal**: A Stigmergy system where the **Substrate itself is Hexagonal**, allowing us to "compose" missions by tuning the 6 Dimensions.

## 🦅 Executive Summary
We do not choose *between* Pheromones, Graphs, or Crystals. We choose a **Hexagonal Substrate** that supports all of them.
By tuning the 6 Dimensions of the Hexagon (**Ontos, Telos, Chronos, Topos, Logos, Pathos**), we can instantiate any of the 4 SOTA Composites on demand.

---

## 1. The Substrate: The 6 Dimensions of Stigmergy

Every signal in the Hive (whether a File, a NATS Message, or a DB Row) is a **Hexagon**.

| Dimension | Stigmergic Function | The "Knob" |
| :--- | :--- | :--- |
| **ONTOS** | **Identity & Schema** | **Crystallinity**: How rigid is the structure? (High = Schema, Low = Blob) |
| **TELOS** | **Intent & Direction** | **Vector**: Where is this going? (High = Mission, Low = Drift) |
| **CHRONOS** | **Time & Decay** | **Volatility**: How fast does it evaporate? (High = Pheromone, Low = Archive) |
| **TOPOS** | **Space & Connection** | **Connectivity**: How linked is it? (High = Mycelium, Low = Silo) |
| **LOGOS** | **Truth & Logic** | **Precision**: How exact is the model? (High = Code, Low = Intuition) |
| **PATHOS** | **Quality & Sentiment** | **Energy**: How "Hot" is the signal? (High = Surprise/Error, Low = Noise) |

---

## 2. The 4 Composite Modes (Mission Configurations)

You can "Compose" a mission by dialing these 6 knobs.

### Mode A: The "Living Crystal" (Knowledge Preservation)
*   **Profile**: High **ONTOS**, High **LOGOS**, Low **CHRONOS**.
*   **Use Case**: Creating the "Swarmlord of Webs Digest", Archiving, Defining Schemas.
*   **Mechanism**: The Swarm locks down structure. Pheromones (Chronos) are only used to guide attention to the Crystal.
*   **HFO Level**: **L3 (Hive)** - Long-term memory.

### Mode B: The "Thermodynamic Web" (Rapid Response)
*   **Profile**: High **CHRONOS**, High **PATHOS**, Low **ONTOS**.
*   **Use Case**: DDoS Defense, Real-time Market Trading, "Hot" Incident Response.
*   **Mechanism**: Pure Pheromone/Energy flow. No time for schemas. Agents follow the "Heat" (Pathos) and act before it decays (Chronos).
*   **HFO Level**: **L0 (Prey)** - Reflexive action.

### Mode C: The "Neural Mycelium" (Discovery & Learning)
*   **Profile**: High **TOPOS**, High **PATHOS**, Medium **TELOS**.
*   **Use Case**: Research Swarms, Finding hidden connections, "Growth-Gather".
*   **Mechanism**: Agents extend Hyphae (Topos) seeking Surprise (Pathos). The graph grows organically.
*   **HFO Level**: **L2 (Campaign)** - Strategic expansion.

### Mode D: The "Holographic Prediction" (Consensus & Truth)
*   **Profile**: High **LOGOS**, High **TELOS**, High **ONTOS**.
*   **Use Case**: Byzantine Quorum, Code Generation, "Review" Phase.
*   **Mechanism**: Every artifact is a Hologram of the Intent (Telos). Agents verify the Logic (Logos) against the Whole.
*   **HFO Level**: **L1 (Swarm)** - Tactical coordination.

---

## 3. Adversarial Stigmergy (The Hidden Disruptor)

In a Hexagonal Substrate, **Disruptors** attack specific dimensions to test resilience.

*   **Ontos Attack**: Injecting malformed schemas (Fuzzing).
*   **Telos Attack**: Hijacking the goal (Misalignment).
*   **Chronos Attack**: Flooding with noise to expire valid signals (DDoS).
*   **Topos Attack**: Severing links or creating Sybil nodes (Partitioning).
*   **Logos Attack**: Injecting subtle logical fallacies (Poisoning).
*   **Pathos Attack**: Injecting false "Surprise" or "Heat" (Distraction).

**The Immunizer's Job**: Monitor the **Hexagonal Integrity** of the substrate.

---

## 4. Implementation: The `Hexagon` Payload

The NATS payload is simply a serialized Hexagon.

```json
{
  "ontos": { "id": "uuid", "type": "artifact" },
  "telos": { "intent": "optimize_storage" },
  "chronos": { "urgency": 0.9, "decay": 0.1 },
  "topos": { "links": ["uuid-2", "uuid-3"] },
  "logos": { "hash": "sha256...", "validator": "pydantic" },
  "pathos": { "sentiment": 0.8, "surprise": 0.2 }
}
```

## 🏆 Recommendation

Adopt **Hexagonal Stigmergy** as the unified standard.
*   **Don't build 4 systems.** Build **1 System** (The Hexagon) and **4 Configurations** (The Modes).
*   **Mission Fit**: When you launch a mission (GROWTH Loop), you define the **Hexagonal Profile** (e.g., "Mode C: Research"). The Swarm adapts its behavior (PREY loops) to prioritize those dimensions.
