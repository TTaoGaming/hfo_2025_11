---
card:
  id: hfo-living-essence
  source: living_essence_hfo.md
  type: Concept
---

# 🦅 HFO Living Essence

> **Intuition**: A dynamic, self-pruning chronicle of evolving insights from the Refinery Swarm, ensuring perpetual vitality within finite contextual bounds.

## 📜 The Incantation (Intent)
```gherkin
Feature: HFO Living Essence Management
  Scenario: Truncate document to avoid context limits
    Given the Living Essence document exceeds maximum context length
    When truncation is necessary to preserve potency
    Then the document is intelligently shortened while retaining core evolving insights
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Self-pruning living document
def prune_living_essence(content: str, max_length: int = 4000) -> str:
    """
    Truncates markdown content to fit context limits,
    preserving headers, italics, and key insights.
    """
    if len(content) <= max_length:
        return content
    
    lines = content.split('\n')
    pruned_lines = []
    current_length = 0
    
    for line in lines:
        if current_length + len(line) + 1 > max_length:
            # Add truncation notice
            pruned_lines.append("*[Truncated to avoid context limits; essence preserved]*")
            break
        pruned_lines.append(line)
        current_length += len(line) + 1
    
    return '\n'.join(pruned_lines)
```

## ⚔️ Synergies
*   **Refinery Swarm**: Serves as the central knowledge nexus, feeding evolving HFO insights back into swarm processes.
*   **Context Guardians**: Integrates with token-limit enforcers across the swarm for seamless runtime adaptation.
*   **Grimoire Evolution**: Enables recursive refraction of its own content into new cards, fostering meta-growth.