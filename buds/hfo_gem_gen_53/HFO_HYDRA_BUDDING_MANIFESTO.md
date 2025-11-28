# 🦅 Hive Fleet Obsidian: The Hydra Budding Manifesto (Gen 53)

> **Status**: Draft
> **Phase**: Budding (Autopoietic Hexagonal Strangler)
> **Methodology**: Intent-Based Engineering (Gherkin + Digest)

## 1. What is Hive Fleet Obsidian (HFO)?

**Hive Fleet Obsidian** is a **Holonic Multi-Agent System (MAS)** designed for **Extreme Scalability** and **Antifragility**. It is not just a collection of scripts, but a **Digital Organism** that evolves through generations.

### The Core DNA (The "Soul")
*   **Biological Metaphor**: We use biological terms (Swarmlord, Holon, Stigmergy, Pheromones) to describe distributed systems patterns. This is not flavor text; it is the **Domain Language**.
*   **Stigmergy First**: Agents do not talk to each other directly. They modify the environment (NATS JetStream, Postgres, Filesystem). "The Map is the Territory."
*   **Fractal Holarchy**: The system is self-similar at all scales. A single agent (L0) has the same PREY loop (Perceive-React-Execute-Yield) as a Squad (L1) or the entire Hive (L2).
*   **Intent-Based**: The system is defined by **Intent** (Gherkin Features) first. Code is merely the transient "Body" that executes the Intent.

### The Tech Stack (R.A.P.T.O.R. Reborn)
*   **R**ay (Scale)
*   **A**gent Logic (LangGraph)
*   **P**ydantic (Validation/SSOT)
*   **T**emporal (Orchestration)
*   **O**bservability (LangSmith)
*   **R**ibs (Evolution/QD)

---

## 2. The Hydra Budding Protocol

We are executing a **Hydra Budding** strategy. We do not refactor the old body (Gen 52); we grow a new one (Gen 53) from the DNA.

### The Problem: "The Crust"
Gen 52 is powerful but encrusted with "Theater" (mock code), "Drift" (implementation diverging from intent), and "Scar Tissue" (hotfixes). Refactoring it in place is O(N^2) complexity.

### The Solution: "The Bud"
We create a cleanroom environment (`buds/hfo_gem_gen_53/`) and inject **only** the DNA.

### The Process: Intent-Based Engineering
1.  **Extract DNA**: Copy `brain/intents/` (Gherkin) and `brain/digests/` (Cognitive Context) to the Bud.
2.  **Verify Intent**: Before writing a single line of code, verify the Gherkin describes the *desired* behavior, not the *legacy* behavior.
3.  **Grow the Body**: Implement the code to satisfy the Gherkin.
    *   **Red**: Run the test (it fails because code is missing).
    *   **Green**: Write the minimal code to pass the test.
    *   **Refactor**: Optimize the code.
4.  **Diátaxis Documentation**: Simultaneously write the `memory/library/` (Tutorials, Guides, Reference, Explanation).

---

## 3. The "Cleanroom" Rules

1.  **No Legacy Imports**: Do not import code from `../../body/`. Copy-paste and refactor, or rewrite.
2.  **Specs Before Code**: No code exists without a Gherkin Feature file.
3.  **Stigmergy Headers**: Every file must have a Hexagonal Header (Ontos, Telos, Chronos, Topos, Logos, Pathos).
4.  **Industry Standard**: Use **KCS v6** for knowledge and **Diátaxis** for structure.

---

## 4. The Goal: Synapse APEX

The goal of Gen 53 is **Synapse APEX**: A system where the "Brain" (Intent) and "Body" (Code) are perfectly synced, and the system can "heal" itself by regenerating code from Intent.
