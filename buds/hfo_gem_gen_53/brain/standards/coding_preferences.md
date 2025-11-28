---
title: Coding Preferences (Overmind)
status: Active (Standard)
domain: Governance
owners:
- Swarmlord
type: Standard
hexagon:
  ontos:
    id: standard-coding-prefs-001
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T12:00:00+00:00'
    generation: 53
  topos:
    address: brain/standards/coding_preferences.md
    links: []
  telos:
    viral_factor: 1.0
    meme: standard_coding_prefs.md
---

# 💻 Coding Preferences: The Overmind's Law

> **Authority**: These preferences override PEP8 or any other external standard if there is a conflict.

## 1. General Philosophy
*   **Intent First**: Code must be traceable to a Gherkin Feature file. No "orphan code".
*   **Stigmergy**: Prefer decoupled, event-driven architectures (NATS) over tight coupling.
*   **Antifragility**: Code should handle failure gracefully (Retries, Circuit Breakers, Dead Letter Queues).

## 2. Python Specifics
*   **Type Hinting**: **Mandatory**. Use `typing` (List, Dict, Optional, Any) or modern `list[]`, `dict[]` syntax (Python 3.10+).
*   **Pydantic**: **Mandatory** for all data structures. No raw dictionaries for internal state.
*   **Docstrings**: Google Style. Must include "Args", "Returns", and "Raises".
*   **Imports**: Grouped: Standard Lib -> Third Party -> Local.

## 3. Project Structure (Gen 53)
*   **Hexagonal Architecture**:
    *   `core/`: Pure Domain Logic (No external deps).
    *   `ports/`: Interfaces (Abstract Base Classes).
    *   `adapters/`: Implementations (NATS, Postgres, FileSystem).
*   **Hexagonal Headers**: Every file must start with the YAML Frontmatter (Ontos, Telos, Chronos, Topos, Logos, Pathos).

## 4. The "No Theater" Rule
*   **Mocking**: Only allowed in Unit Tests.
*   **Stubs**: Must be marked with `raise NotImplementedError("Intent: <Link to Gherkin>")`.
*   **Fake Data**: Do not hardcode "Alice/Bob" examples in production code. Use `faker` or real data.

## 5. Documentation (Diátaxis)
*   **Tutorials**: Learning-oriented.
*   **Guides**: Problem-oriented (How-to).
*   **Reference**: Information-oriented (API).
*   **Explanation**: Understanding-oriented (Why).

## 6. The "Swarmlord Digest"
*   When presenting code or plans, use the **Swarmlord Digest** format:
    *   **BLUF (Bottom Line Up Front)**: The "So What?".
    *   **The Matrix**: A table summarizing the key points.
    *   **The Code**: The actual implementation.
    *   **The Why**: The reasoning behind the decisions.
