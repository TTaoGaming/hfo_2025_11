---
card:
  id: standard-obsidian-octet-001
  source: standard_obsidian_octet.md
  type: Concept
---

# 🃏 💎 The OBSIDIAN Octet

> **Intuition**: The OBSIDIAN Octet distills reality into eight fractal dimensions—Ontos, Chronos, Topos, Telos, Logos, Pathos, Ethos, Techne—ensuring every Hive entity, from file to swarm, is holistically defined, queryable, and alive.

## 📜 The Incantation (Intent)
```gherkin
Feature: Entity Definition via OBSIDIAN Octet

  Scenario: Defining a Hive Entity with Full Octet
    Given a new entity such as a file, agent, or database record
    When initializing its metadata or state
    Then it MUST include the Hexagon (Ontos, Chronos, Topos, Telos)
    And it MAY extend to the full Octet (Logos, Pathos, Ethos, Techne)
    And all dimensions are populated with valid values for identity, time, location, purpose, logic, emotion, trust, and tools
    And the entity is queryable across dimensions in pgvector database
```

## 🧪 The Catalyst (Code)
```python
# The Essence: ObsidianOctet dataclass for structured entity definition
from dataclasses import dataclass, field
from typing import Dict, Any, List
from uuid import uuid4
from datetime import datetime

@dataclass
class ObsidianOctet:
    ontos: Dict[str, Any] = field(default_factory=lambda: {"id": str(uuid4()), "type": "unknown", "owner": "Swarmlord"})
    chronos: Dict[str, Any] = field(default_factory=lambda: {
        "status": "active", "urgency": 1.0, "decay": 0.0, "created": datetime.utcnow().isoformat()
    })
    topos: Dict[str, Any] = field(default_factory=lambda: {"address": "", "links": []})
    telos: Dict[str, Any] = field(default_factory=lambda: {"viral_factor": 1.0, "meme": ""})
    logos: Dict[str, Any] = field(default_factory=lambda: {"protocol": "", "format": "json"})
    pathos: Dict[str, Any] = field(default_factory=lambda: {"stress": 0.0, "health": 1.0})
    ethos: Dict[str, Any] = field(default_factory=lambda: {"security": "internal", "compliance": []})
    techne: Dict[str, Any] = field(default_factory=lambda: {"stack": [], "complexity": "low"})

    def to_yaml(self) -> str:
        """Serialize to YAML frontmatter string."""
        import yaml
        return yaml.dump(self.__dict__)

    @classmethod
    def from_yaml(cls, yaml_str: str) -> 'ObsidianOctet':
        """Deserialize from YAML string."""
        import yaml
        data = yaml.safe_load(yaml_str)
        return cls(**data)

# Usage: entity = ObsidianOctet(ontos={"id": "agent-001"}, telos={"meme": "scrape web"})
```

## ⚔️ Synergies
*   **File Headers**: YAML frontmatter in every MD/PY file starts with Hexagon for fractal consistency.
*   **Agent State**: `self.state: ObsidianOctet` tracks Pathos (e.g., high stress triggers Yield).
*   **Hive Database**: pgvector schema with 8 columns enables queries like "high-urgency Python agents in Body".
*   **Query Engine**: Cross-dimension searches (e.g., Chronos urgency + Techne stack) power swarm orchestration.
*   **Fractal Scaling**: Applies from Level 0 (File) to Level 2 (Hive), mirroring biology/military/software patterns.