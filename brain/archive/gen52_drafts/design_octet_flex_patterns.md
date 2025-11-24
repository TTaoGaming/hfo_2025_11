---
title: Octet Flex Patterns (Base-8 Configurations)
status: Active
domain: Architecture
owners:
- Swarmlord
type: Design Document
hexagon:
  ontos:
    id: octet-flex-patterns-v1
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-23T15:30:00Z'
    generation: 51
  topos:
    address: brain/archive/gen52_drafts/design_octet_flex_patterns.md
    links:
    - brain/gen52_octree_fractal.feature
  telos:
    viral_factor: 1.0
    meme: 8 Agents, Infinite Configurations.
---


# 🐙 Octet Flex Patterns: Configuring the Byte

> **Context**: While the "Rainbow Octet" (1 of each O.B.S.I.D.I.A.N. role) is the "Perfect Crystal", real-world workflows (PREY/SWARM) often require specialization or batching.
> **Constraint**: The Squad Size is strictly **8 Agents** (Base-8).
> **Variable**: The **Role Distribution** within the Octet.

## 1. The Morphic Octet (Time-Division Multiplexing)
*Best for: Synchronous SWARM Loops (Batching).*

Instead of having 8 different roles *simultaneously*, the entire Octet shifts roles *sequentially* to match the SWARM phase.

*   **Phase 1 (Watch)**: 8 **Observers** (Parallel Scan).
*   **Phase 2 (Act)**: 8 **Shapers** (Parallel Generation).
*   **Phase 3 (Review)**: 8 **Immunizers** (Peer Review).
*   **Phase 4 (Mutate)**: 8 **Assimilators** (Merge/Learn).

**Pros**: Maximum throughput for that specific phase.
**Cons**: High latency if a phase gets stuck (no pipeline).

## 2. The Rainbow Octet (Space-Division Multiplexing)
*Best for: Autonomous, Complex Missions (The "Mini-Hive").*

The standard "Perfect Crystal". Contains all necessary organs to survive alone.

*   **Composition**: 1x **O**, 1x **B**, 1x **S**, 1x **I**, 1x **D**, 1x **I**, 1x **A**, 1x **N**.

**Pros**: Fully autonomous. Can handle unexpected events.
**Cons**: Bottlenecks on single roles (e.g., only 1 Shaper means slow coding).

## 3. The Parallel Octet (The "Byte Array")
*Best for: Map-Reduce / Scatter-Gather.*

A specialized squad focused on one specific task type. Requires an external L2 Navigator to direct it.

*   **Composition**: 8x **Shapers** (The "Dev Squad") OR 8x **Observers** (The "Scout Squad").

**Pros**: Extreme speed on specific tasks.
**Cons**: Fragile. Blind (no Observers) or Toothless (no Shapers) if isolated.

## 4. The Pipeline Octet (The "Stream")
*Best for: Continuous Data Processing.*

Agents are arranged in a fixed flow. Data enters Agent 1 and leaves Agent 8.

*   **Flow**: 2 **O** (Input) -> 2 **B** (Route) -> 2 **S** (Process) -> 2 **A** (Store).

**Pros**: Continuous throughput. No context switching.
**Cons**: Weakest link determines speed.

## 🧬 The "Stem Cell" Protocol (L0 Flex)
To enable these patterns, the L0 Agent must be a **Stem Cell**.
It is not *hardcoded* as a "Shaper". It is instantiated with a **Persona** at runtime.

*   `agent = PreyAgent(role=Role.SHAPER)`
*   *Task Complete*
*   `agent.morph(role=Role.IMMUNIZER)`

This allows the **Morphic Octet** to exist.
