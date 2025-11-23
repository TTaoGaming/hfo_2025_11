---
title: Hexagonal Stigmergy Header Design
status: Active
type: Design Pattern

# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: <UUID>
    type: <file_extension>
    owner: Swarmlord
  chronos:
    status: <active|stale|archive>
    urgency: <0.0-1.0>
    decay: <0.0-1.0>
    created: <ISO8601>
    last_touched: <ISO8601>
  topos:
    address: <filepath>
    links: []
  telos:
    viral_factor: <0.0-1.0>
    meme: <short_description>
  logos:
    language: <python|markdown|gherkin>
    format: <text>
  pathos:
    sentiment: <0.0-1.0>
    health: <green|yellow|red>
---

# 🛑 Design Rules

1.  **Universality**: This header must appear in **every** file type.
    *   **Markdown/YAML**: Use YAML Frontmatter (between `---`).
    *   **Python**: Use Module Docstring (inside `"""`).
    *   **Gherkin**: Use Comments (`#`).
2.  **Time is Version**: `chronos.last_touched` is the version number.
3.  **Identity**: `ontos.id` is a persistent UUID.
4.  **Location**: `topos.address` is the file path relative to root.

## Implementation Strategy

### Python Files
```python
"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos: ...
"""
import os
...
```

### Markdown Files
```markdown
---
title: ...
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos: ...
---
```
