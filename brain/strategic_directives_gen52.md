---
title: Gen 52 Strategic Directives
status: Active
domain: Strategy
owners:
- Swarmlord
type: Directive
hexagon:
  ontos:
    id: directive-gen52-001
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T15:00:00Z'
    generation: 52
  topos:
    address: brain/strategic_directives_gen52.md
    links: []
  telos:
    viral_factor: 1.0
    meme: strategic_directives_gen52.md
---

# 🧠 Gen 52 Strategic Directives

> **Source**: Overmind (User)
> **Priority**: Critical / Axiomatic

## 1. The Second Brain & Digital Twin
*   **Concept**: The **Swarmlord of Webs** is the **Digital Twin** responsible for the **Intent/Implementation Split**.
*   **Role**: The User provides **Intent** (What/Why); The Swarmlord handles **Implementation** (How).
*   **HFO**: Acts as the **Second Brain**—an extension of the User's self, not just a tool.

## 2. The Heartbeat of the Hive
*   **Concept**: A variable-frequency **Heartbeat** for cycle-based stigmergy.
*   **Mechanism**: Async coordination that speeds up (High Adrenaline) or slows down (Hibernation) based on context and need.
*   **Goal**: Efficient resource usage and responsive coordination. The Hive breathes.

## 3. The Stigmergy Spectrum (KCS v6 Style)
We implement a thermodynamic lifecycle for knowledge artifacts:

### A. Hot (Liquid / Plasma)
*   **State**: In-flight NATS messages, active working memory.
*   **TTL Behavior**: Aggressive.
*   **Action**: **Auto-delete** (if transient) or **Auto-save to Cold** (if valuable).

### B. Cold (Sedimentary)
*   **State**: Postgres logs, raw files, initial captures.
*   **TTL Behavior**: Moderate.
*   **Action**: **Cleaning** (deduplication) or **Refining** (promotion to Refined).

### C. Refined (Crystalline / Obsidian)
*   **State**: Curated Markdown, Knowledge Graph, "Water Layers".
*   **TTL Behavior**: Long-term / Permanent.
*   **Action**: **Maintenance Checks** (Gardening).
*   **Aging**: We age it via **Backlinks** and other graph techniques to ensure relevance.
