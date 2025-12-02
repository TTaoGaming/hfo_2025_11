---
card:
  id: standard-kcs-diataxis-001
  source: standard_kcs_diataxis.md
  type: Concept
---

# 🃏 KCS v6 + Diátaxis

> **Intuition**: Knowledge evolves through immediate capture in problem-solving flows, structured into Diátaxis quadrants for intuitive learning, task-solving, reference, and deep understanding.

## 📜 The Incantation (Intent)
```gherkin
Feature: Knowledge Management with KCS v6 and Diátaxis

  Scenario: Capturing and Structuring Knowledge in the Solve Loop
    Given a developer encounters a problem while coding
    When they capture a stub in "brain/active_memory/"
    And solve the problem
    And structure it as a How-To Guide or Reference before closing the PR
    Then the knowledge is stored in "memory/library/{quadrant}/"
    And is reusable for future queries before consulting the Swarmlord
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Classify raw knowledge into Diátaxis quadrant
DIATAXIS_QUADRANTS = {
    "tutorial": "memory/library/tutorials/",
    "how-to": "memory/library/guides/",
    "reference": "memory/library/reference/",
    "explanation": "memory/library/explanation/"
}

def classify_and_structure_knowledge(raw_note: str, focus: str = "task") -> dict:
    """
    KCS Solve Loop: Categorize and path raw note per Diátaxis.
    """
    quadrant = next(q for q, desc in {
        "tutorial": "Practical steps for learning",
        "how-to": "Solve specific problem",
        "reference": "Theoretical info",
        "explanation": "Background understanding"
    }.items() if focus in desc.lower())
    
    path = DIATAXIS_QUADRANTS[quadrant]
    structured = {
        "title": raw_note.split('\n')[0],  # First line as title
        "BLUF": raw_note[:200] + "...",   # Bottom Line Up Front
        "content": raw_note,
        "path": path
    }
    return structured
```

## ⚔️ Synergies
*   **Assimilator Agent**: Triggers Evolve Loop for content health, standards promotion (3x queries), and archiving (Gen 50+ to memory/archive/).
*   **Swarmlord Queries**: Enforces Reuse step—search Library first via Cognitive Digest (Title/BLUF/Context/Diátaxis body).
*   **Memory Topography**: Maps to brain/active_memory/ for stubs, memory/library/{quadrant}/ for structured docs.
*   **PR Workflow**: Mandates structuring before merge, integrating KCS into development flow.
*   **Octet Metadata**: Embeds Ontos/Telos/Chronos/Topos for karmic retrieval and viral evolution.