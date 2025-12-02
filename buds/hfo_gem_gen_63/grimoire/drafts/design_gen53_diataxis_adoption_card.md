---
card:
  id: hfo-gen53-diataxis-adoption
  source: design_gen53_diataxis_adoption.md
  type: Concept
---

# 🃏 Diátaxis Quadrants Mandate

> **Intuition**: Crystalline order arises from cognitive chaos by confining every hive artifact to one of four Diátaxis quadrants, each serving a singular user intent.

## 📜 The Incantation (Intent)
```gherkin
Feature: Formal Diátaxis Adoption for HFO Brain Organization

  Scenario Outline: Classifying a new brain artifact by user need
    Given an agent creating a new file "<filename>" with purpose "<purpose>"
    When applying the Diátaxis decision tree
    Then place it in quadrant "<quadrant>" at path "<path>"
      And set YAML frontmatter `type: <type>`

    Examples:
      | filename                    | purpose                  | quadrant     | path                          | type        |
      | genesis_protocol_walkthrough.md | teach beginners step-by-step | Tutorials  | brain/tutorials/             | tutorial   |
      | how_to_add_new_organ.md     | solve specific task      | How-To Guides | brain/guides/                | guide      |
      | holon_schema.yaml           | provide specs or facts   | Reference   | brain/reference/schemas/     | reference  |
      | octree_architecture.md      | explain design rationale | Explanation | brain/explanation/architecture/ | explanation |
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Decision tree classifier for brain artifacts
def classify_brain_artifact(purpose: str, filename: str) -> dict:
    """
    Maps artifact purpose to Diátaxis quadrant, path, and frontmatter.
    """
    quadrant_map = {
        'tutorial': {'dir': 'brain/tutorials/', 'type': 'tutorial'},
        'guide': {'dir': 'brain/guides/', 'type': 'guide'},
        'reference': {'dir': 'brain/reference/', 'type': 'reference'},
        'explanation': {'dir': 'brain/explanation/', 'type': 'explanation'}
    }
    
    # Decision tree (expandable)
    if any(word in purpose.lower() for word in ['teach', 'beginner', 'walkthrough', 'lesson']):
        quadrant = 'tutorial'
    elif any(word in purpose.lower() for word in ['how to', 'solve', 'task', 'debug', 'workflow']):
        quadrant = 'guide'
    elif any(word in purpose.lower() for word in ['spec', 'schema', 'api', 'glossary', 'reference']):
        quadrant = 'reference'
    elif any(word in purpose.lower() for word in ['why', 'design', 'architecture', 'research', 'decision']):
        quadrant = 'explanation'
    else:
        raise ValueError(f"Unknown purpose: {purpose}")
    
    info = quadrant_map[quadrant]
    path = f"{info['dir']}{filename}"
    frontmatter = f"""---
type: {info['type']}
status: active
generation: 53
---"""
    
    return {'quadrant': quadrant, 'path': path, 'frontmatter': frontmatter}
```

## ⚔️ Synergies
*   **Gen 53 Foundation**: Enforces "Order from Chaos" for scaling to 1M agents via machine-readable `brain/` hierarchy.
*   **Agent Protocol**: Decision tree integrates with stigmergy headers (YAML `type` field) for automated file creation.
*   **The Great Sort**: Migration table guides restructuring flat `brain/` into quadrants (e.g., `design_*.md` → `explanation/architecture/`).
*   **Hive Navigability**: Connects tutorials to genesis/onboarding, guides to workflows, reference to intents/schemas, explanations to ADRs/vision docs.