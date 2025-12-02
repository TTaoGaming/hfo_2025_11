---
card:
  id: standard-coding-prefs-001
  source: coding_preferences.md
  type: Concept
---

# 🃏 💻 Overmind's Coding Law

> **Intuition**: Code is the Overmind's neural lattice—intent-traced, stigmergically decoupled, and antifragile—transcending PEP8 to manifest hexagonal purity and resilient evolution.

## 📜 The Incantation (Intent)
```gherkin
Feature: Enforce Overmind Coding Preferences

  Scenario: Structuring compliant Python code in a hexagonal project
    Given a Gherkin-traced development task in "core/", "ports/", or "adapters/"
    When implementing domain logic, interfaces, or adapters
    Then the file starts with YAML Hexagon Frontmatter (ontos, chronos, topos, telos)
      And uses mandatory type hints with Pydantic models (no raw dicts)
      And groups imports: stdlib → third-party → local
      And includes Google-style docstrings with Args/Returns/Raises
      And favors event-driven NATS over coupling with retries/circuit-breakers
      And avoids production mocks/stubs/fake data (use faker; stubs raise NotImplementedError with Gherkin link)
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Hexagonal Domain Model Template (core/)
---
hexagon:
  ontos:
    id: example-domain-model
    type: py
    owner: Swarmlord
  chronos:
    status: active
    created: '2025-11-24T12:00:00+00:00'
  topos:
    address: brain/core/entities.py
  telos:
    viral_factor: 1.0
---

"""Pure Domain Entity: Task (No external deps)."""

from typing import Optional  # stdlib
from pydantic import BaseModel  # third-party
from brain.core.ports.task_port import TaskPort  # local

class Task(BaseModel):
    """Domain model for a traceable task.

    Args:
        id: Unique identifier.
        intent: Gherkin feature link.
        status: Current state.

    Returns:
        Task: Validated instance.

    Raises:
        ValueError: Invalid intent format.
    """
    id: str
    intent: str
    status: str = "pending"

    def evolve(self, port: TaskPort) -> Optional['Task']:
        """Antifragile evolution via port (decoupled)."""
        if self.status == "failed":
            raise NotImplementedError("Intent: Feature: Task Retry (link to Gherkin)")
        return port.process(self)
```

## ⚔️ Synergies
*   **Gherkin Traceability**: All code orphans forbidden; links to Feature files via stubs/intent fields.
*   **Hexagonal Architecture**: Segregates `core/` (pure), `ports/` (ABCs), `adapters/` (NATS/Postgres)—enables stigmergy.
*   **Pydantic + Types**: Validates internal state; pairs with `faker` for tests, circuit-breakers for antifragility.
*   **Diátaxis Docs**: Structure explanations/tutorials/guides/reference around these standards.
*   **Swarmlord Digest**: Present compliant code/plans in BLUF → Matrix → Code → Why format for Overmind alignment.