---
title: The OBSIDIAN Octet (Standard)
status: Active
domain: Ontology
owners:
- Swarmlord
type: Standard
hexagon:
  ontos:
    id: standard-obsidian-octet-001
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T12:45:00+00:00'
    generation: 53
  topos:
    address: brain/standards/standard_obsidian_octet.md
    links: []
  telos:
    viral_factor: 1.0
    meme: standard_obsidian_octet.md
---

# 💎 The OBSIDIAN Octet: The 8 Dimensions of Reality

> **Context**: Every entity in Hive Fleet Obsidian (from a single file to a swarm of agents) must define its existence across these 8 dimensions. This is the "Header" for everything.

## 1. The Octet (The Greek Pillars)

| Dimension | Question | Description | Example |
| :--- | :--- | :--- | :--- |
| **1. Ontos** | *Who are you?* | Identity, Type, Owner, UUID. | `id: agent-001`, `type: python-script` |
| **2. Chronos** | *When are you?* | Time, Urgency, Decay, Generation. | `created: 2025-11-24`, `urgency: 0.9` |
| **3. Topos** | *Where are you?* | Address, Links, Context. | `address: body/hands/agent.py` |
| **4. Telos** | *Why are you?* | Purpose, Goal, Viral Factor. | `meme: "To scrape the web"` |
| **5. Logos** | *How do you think?* | Protocol, Format, Language. | `protocol: PREY-Loop`, `format: json` |
| **6. Pathos** | *How do you feel?* | State, Stress, Health, Validation. | `stress: 0.2`, `status: active` |
| **7. Ethos** | *Who do you trust?* | Security, Compliance, Permissions. | `security: internal`, `compliance: [gdpr]` |
| **8. Techne** | *What do you use?* | Stack, Tools, Complexity. | `stack: [python, nats]`, `complexity: low` |

## 2. The Fractal Application

### Level 0: The File (Header)
Every file must have a YAML frontmatter containing at least the **Hexagon** (Ontos, Chronos, Topos, Telos) and optionally the full **Octet**.

### Level 1: The Agent (State)
Every Agent's internal state (`self.state`) must track these 8 variables.
*   *Example*: An agent with high `Pathos.stress` might trigger a "Yield" action early.

### Level 2: The Hive (Database)
The `pgvector` database schema is organized by these 8 columns. This allows us to query:
*   "Show me all high-urgency (Chronos) agents in the Body (Topos)."
*   "Find all Python scripts (Logos) that use NATS (Techne)."

## 3. The Multi-Layered Meaning

*   **Biological**: Matches the Cell (Ontos), Metabolism (Chronos), Environment (Topos), Function (Telos).
*   **Military (JADC2)**: Matches Unit (Ontos), Timeline (Chronos), Grid (Topos), Mission (Telos).
*   **Software**: Matches UUID (Ontos), Timestamp (Chronos), Path (Topos), Docstring (Telos).
