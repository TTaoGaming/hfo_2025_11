---
type: design
status: proposal
author: Swarmlord (Gen 51)
date: 2025-11-24
tags: [organization, architecture, documentation, sota]
---

# 🧠 Design: Brain Organization Patterns & SOTA Options

> **Context**: The `brain/` directory has become a flat, high-entropy zone containing mixed intents (Gherkin), designs (Markdown), and configurations.
> **Goal**: Propose 4 distinct organizational patterns based on State-of-the-Art (SOTA) industry standards to restore cognitive clarity.

## 🧐 SOTA Context: How Industry Leaders Organize Knowledge

In 2024-2025, "Docs as Code" is the standard. However, the *structure* varies by philosophy:

1.  **Diátaxis Framework** (Canonical): Used by Google, Microsoft, Ubuntu. Splits content by *user need* (Learning vs. Doing vs. Understanding).
2.  **ARC42 / C4 Model** (Architectural): Used in Enterprise Systems. Splits by *abstraction level* (Context -> Container -> Component).
3.  **PARA Method** (Personal Knowledge Management - PKM): Used in Second Brain systems. Splits by *actionability* (Projects vs. Areas).
4.  **Zettelkasten / Digital Garden**: Networked, atomic notes. Less hierarchy, more linking. (Hard to navigate in a file tree).

---

## 🧩 Option 1: The Diátaxis Adaptation (Functional)
*Best for: Onboarding new agents/humans and clear separation of "Theory" vs. "Practice".*

This pattern separates files based on what the reader is trying to *do*.

### Structure
```text
brain/
├── tutorials/          # "Learning-oriented" (Onboarding, Hello World)
│   ├── getting_started.md
│   └── genesis_protocol.md
├── guides/             # "Problem-oriented" (How-to, Workflows)
│   ├── workflow_obsidian_hourglass.md
│   └── how_to_add_new_organ.md
├── explanation/        # "Understanding-oriented" (Design, Architecture, Philosophy)
│   ├── design_octree_fractal_holarchy.md
│   ├── research_stigmergy_abstractions.md
│   └── vision_synapse_apex.md
├── reference/          # "Information-oriented" (Specs, Gherkin, Configs)
│   ├── intents/        # Gherkin (.feature)
│   ├── schemas/        # YAML/JSON
│   └── glossary.md
└── standards/          # Governance & Rules
```

### Tradeoffs
*   **Pros**: Industry standard, extremely clear for consumers. Separates "Why" (Explanation) from "How" (Guides).
*   **Cons**: Can fragment a single feature (e.g., "Stigmergy" is split across Explanation, Reference, and Guides).
*   **Verdict**: **High Clarity, Medium Cohesion.**

---

## 🏗️ Option 2: The Domain-Driven Design (DDD) / Vertical Slice
*Best for: Large, complex systems where features are independent.*

This pattern groups everything related to a specific "Domain" or "Pillar" together.

### Structure
```text
brain/
├── core/               # The Kernel
│   ├── identity/       # Persona, Vision
│   └── governance/     # Standards, GitOps
├── architecture/       # High-level System Design
│   ├── octree/
│   └── hexagonal/
├── domains/            # Vertical Slices (The "Pillars")
│   ├── stigmergy/      # All Stigmergy docs, designs, features
│   ├── memory/         # All Memory docs
│   ├── antifragility/  # All Immune System docs
│   └── temporal/       # All Time/Loop docs
├── missions/           # Active & Past Missions
└── archive/            # Deprecated
```

### Tradeoffs
*   **Pros**: High cohesion. Everything about "Stigmergy" is in one folder. Easier to refactor domains.
*   **Cons**: Can lead to deep nesting. "Cross-cutting concerns" (like Logging) are hard to place.
*   **Verdict**: **High Cohesion, Medium Discoverability.**

---

## 📂 Option 3: The PARA Method (Action-Oriented)
*Best for: High-velocity teams focused on "What is active NOW?"*

Adapted from Tiago Forte's Second Brain.

### Structure
```text
brain/
├── projects/           # Active Initiatives (Short-term)
│   ├── project_octree_migration/
│   └── project_rich_metadata/
├── areas/              # Ongoing Responsibilities (Long-term)
│   ├── architecture/
│   ├── devops/
│   ├── security/
│   └── research/
├── resources/          # Static Knowledge (Reference)
│   ├── patterns/       # Design Patterns
│   ├── standards/      # Coding Standards
│   └── external_docs/
└── archives/           # Completed/Inactive
    ├── gen_50/
    └── project_genesis/
```

### Tradeoffs
*   **Pros**: Very clear what is "Active" vs. "Static". Keeps the workspace focused.
*   **Cons**: "Architecture" is often permanent, so it lives in "Areas", but specific changes are "Projects". Can get confusing.
*   **Verdict**: **High Focus, Low Stability.**

---

## 🦅 Option 4: The "Biological Holarchy" (HFO Native)
*Best for: Maintaining the "Hive Fleet" metaphor and aligning with the Codebase (`body/`, `eyes/`).*

This treats the `brain/` as an organ with specific sub-regions.

### Structure
```text
brain/
├── cortex/             # High-level Strategy & Executive Function
│   ├── vision/         # Vision, Persona, North Stars
│   └── strategy/       # Roadmaps, Hourglass, Master Plans
├── lobes/              # Functional Knowledge Centers
│   ├── parietal/       # Spatial/Structural (Octree, Hexagons)
│   ├── temporal/       # Time/Process (Workflows, Loops)
│   └── frontal/        # Decision/Logic (Governance, Standards)
├── hippocampus/        # Memory & Research
│   ├── research/       # Deep Dives, SOTA analysis
│   └── digests/        # Summaries, Logs
├── brainstem/          # Core Functions & Specs
│   ├── intents/        # Gherkin Features (The "Nerves")
│   └── config/         # YAML Registry (The "DNA")
└── synaptic_gap/       # Interfaces & Protocols (Stigmergy)
```

### Tradeoffs
*   **Pros**: Perfectly aligned with the project's "Biological" theme. Fun.
*   **Cons**: Requires knowing the metaphor to find things (e.g., "Where is the config? Oh, Brainstem"). High cognitive load for outsiders.
*   **Verdict**: **High Theme, Low Accessibility.**

---

## 🏆 Recommendation: The "Hybrid Pragmatist" (Modified DDD)

We recommend a **Modified DDD** approach (Option 2) with a touch of Diátaxis for the top level. This balances "Finding by Feature" with "Finding by Type".

### Proposed Structure for HFO Gen 52

```text
brain/
├── 1_strategy/         # (Why) Vision, Persona, Roadmaps, High-level Design
│   ├── vision_synapse_apex.md
│   └── strategy_obsidian_hourglass.md
├── 2_architecture/     # (What) Core Structures & Patterns
│   ├── octree/
│   ├── hexagonal/
│   └── patterns/       # Async Swarm, Claim Check
├── 3_domains/          # (How) Vertical Slices (Design + Gherkin + Research)
│   ├── stigmergy/
│   ├── memory/
│   ├── antifragility/
│   └── operations/     # GitOps, Governance
├── 4_standards/        # (Rules) Governance, Schemas, Formats
│   ├── standards/
│   └── registry.yaml
└── 5_archive/          # (History)
```

### Migration Plan
1.  Create directories.
2.  Move `vision_`, `persona_`, `strategy_` -> `1_strategy/`.
3.  Move `design_`, `architecture_` -> `2_architecture/` or `3_domains/` (depending on scope).
4.  Move `feature` files alongside their designs in `3_domains/` (Co-location).
5.  Update `README.md` in `brain/` to map the new territory.
