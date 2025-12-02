---
card:
  id: fractal-hexadex-architecture-v3
  source: design_hexadex_architecture_v3.md
  type: Concept
---

# 🃏 Fractal Hexadex Architecture

> **Intuition**: The system's DNA fractally compresses into a 16-verse rhyming chant as an $8^N$ octree, with immutable N.O.B.S.I.D.I.A. bones and chameleon-like mutable flesh.

## 📜 The Incantation (Intent)
```gherkin
Feature: Fractal Hexadex Structure
  Scenario: Expanding the Octree from Root to Swarm
    Given N is the Navigator exponent at the 0-point Seed
    And the Static Octet bones are N O B S I D I A creed
    When the Dynamic Flex 8 verses shift with observer's gaze
    Then $8^N$ fractals bloom in recursive hexagonal blaze
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Recursive fractal generator for Hexadex octree
NOBSIDIA = ['N', 'O', 'B', 'S', 'I', 'D', 'I', 'A']

def hexadex_fractal(n: int, root='Swarmlord') -> list[str]:
    """
    Generates fractal structure as $8^N$ nodes.
    N=0: Root | N=1: Static Octet | N=2: Swarm with sub-pillars.
    """
    if n == 0:
        return [root]
    prev_layer = hexadex_fractal(n - 1, root)
    current_layer = []
    for pillar in NOBSIDIA:
        for node in prev_layer:
            current_layer.append(f"{pillar}:{node}")
    return current_layer

# Usage: hexadex_fractal(2) -> 64-node swarm
```

## ⚔️ Synergies
*   **N.O.B.S.I.D.I.A. Pillars**: Maps directly to holon archetypes (Navigator as root holon, Observer for input feeds).
*   **Fractal Holons**: Extends to recursive node spawning in simulation webs (e.g., Squad at N=1, Swarm at N=2).
*   **Dynamic Chameleon**: Integrates with polyglot renderers (Mermaid for graphs, Rust structs for types).
*   **Swarmlord Core**: Serves as the 0-Point Oath, anchoring all agent behaviors and RAG reflections.