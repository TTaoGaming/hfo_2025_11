---
card:
  id: autopoietic-hexagonal-strangler
  source: research_formal_terms.md
  type: Concept
---

# 🃏 Autopoietic Hexagonal Strangler

> **Intuition**: Like a hydra regenerating through budding, this synthesis enables a legacy system to autopoietically birth a clean, modular successor that stranglingly supplants it via incremental growth.

## 📜 The Incantation (Intents)
```gherkin
Feature: Autopoietic Hexagonal Strangler Migration

  Scenario: Bud a cleanroom successor from legacy infrastructure
    Given a legacy system at root "Gen 52"
    When introducing a "buds/" directory with hexagonal "core/" logic
      And defining Gherkin specs and Diátaxis docs first per Cleanroom methodology
      And connecting via ports to driving "brain/" intent and driven "body/" adapters
    Then new features route through the bud while legacy atrophies
      And the bud becomes the new root via immutable replacement
```

## 🧪 The Catalyst (Code)
```python
# The Essence: A budding migrator skeleton
import os
from pathlib import Path

class AutopoieticHexagonalStrangler:
    def __init__(self, legacy_root: Path):
        self.legacy_root = legacy_root
        self.bud_root = legacy_root / "buds"

    def bud_cleanroom_core(self):
        """Strangle legacy by budding hexagonal core."""
        core = self.bud_root / "hfo_gem_gen_53" / "core"
        core.mkdir(parents=True, exist_ok=True)
        # Hexagonal ports setup (pure logic inside)
        ports_file = core / "__init__.py"
        ports_file.write_text("""
# Hexagonal Core: Pure domain logic
# Ports defined here for brain/body adapters
class CoreDomain:
    def execute_intent(self, spec: str) -> dict:
        # Cleanroom-certified logic
        return {"result": "certified"}
""")
        print(f"B udded cleanroom core at {core}")

    def migrate(self):
        self.bud_cleanroom_core()
        # Immutable rise: eventually rm -rf legacy_root, mv bud_root / 
```

## ⚔️ Synergies
*   **Strangler Fig → Repo Structure**: `buds/` incrementally envelopes Gen 52 root.
*   **Cleanroom → Development Flow**: Gherkin/Diátaxis-first in `buds/hfo_gem_gen_53/core/`.
*   **Hexagonal → Folder Layout**: `core/` (domain), `brain/` (driving ports), `body/` (driven adapters).
*   **Immutable/Phoenix → Deployment**: Burn Gen 52; phoenix from `buds/` as new infra.
*   **Autopoiesis → HFO Lifecycle**: Self-replicating evolution across generations.