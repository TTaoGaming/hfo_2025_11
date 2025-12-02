---
card:
  id: diataxis-vs-para
  source: research_para_vs_diataxis.md
  type: Concept
---

# 🃏 Diátaxis vs PARA: Knowledge Organization Duel

> **Intuition**: Diátaxis anchors technical documentation in user intent for stable engineering clarity, while PARA channels knowledge into actionable flows for agentic velocity—hybridize for HFO's swarm-overmind balance.

## 📜 The Incantation (Intent)
```gherkin
Feature: Organize HFO knowledge base by intent and actionability

  Scenario: Classify and place a document in the optimal structure
    Given a document with metadata like "research_para_vs_diataxis.md"
      And context "HFO engineering project with agentic brain/"
    When analyzing for user goals or action horizon
    Then assign to Diátaxis quadrant if stable reference needed
      Or PARA category if dynamic execution focused
      And recommend "brain/domains/" for ongoing architecture like this file
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Classifier for Diátaxis/PARA hybrid
def classify_knowledge_doc(filename: str, content_tags: list[str], is_agentic: bool = False) -> dict:
    """
    Maps doc to Diátaxis quadrant or PARA category for HFO brain/docs.
    """
    diataxis_map = {
        'tutorial': 'Tutorials', 'how-to': 'How-to Guides',
        'reference': 'Reference', 'explanation': 'Explanation'
    }
    para_map = {
        'project': 'Projects', 'area': 'Areas',
        'resource': 'Resources', 'archive': 'Archives'
    }
    
    # Heuristic: tags + agentic flag
    if any(tag in ['organization', 'methodology'] for tag in content_tags):
        quadrant = 'Explanation' if not is_agentic else 'Resources'
    elif 'mission' in filename.lower():
        quadrant = 'Projects'
    else:
        quadrant = 'Reference'  # Default stable
    
    return {
        'type': 'Diátaxis' if not is_agentic else 'PARA',
        'folder': f"brain/{quadrant.lower().replace(' ', '_')}/" if quadrant in para_map.values() else f"docs/{quadrant.lower()}/",
        'reason': f"{'Agentic action' if is_agentic else 'Engineering stability'} fit."
    }

# Usage
print(classify_knowledge_doc("research_para_vs_diataxis.md", ["organization", "para", "diataxis"]))
```

## ⚔️ Synergies
*   **HFO brain/**: Maps research to `brain/domains/` (Areas) or `brain/patterns/` (Resources) for stable agent reference, avoiding PARA churn.
*   **Swarm Missions**: Active intents (*.feature) → `brain/missions/` (Projects) for execution velocity.
*   **docs/**: Pure Diátaxis for published manuals (Tutorials/How-to/Reference/Explanation).
*   **Overmind Design**: design_*.md → Explanation/Reference; ensures agents read immutable paths without hallucination.
*   **5W1H Pattern**: Integrates with research standards for consistent analysis across files.