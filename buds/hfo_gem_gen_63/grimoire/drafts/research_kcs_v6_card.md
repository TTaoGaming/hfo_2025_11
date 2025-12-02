---
card:
  id: kcs-v6
  source: research_kcs_v6.md
  type: Concept
---

# 🃏 KCS v6: Knowledge-Centered Service

> **Intuition**: Knowledge emerges as a byproduct of real-time problem-solving, creating self-healing loops where documentation is captured, structured, and evolved during the work itself.

## 📜 The Incantation (Intent)
```gherkin
Feature: KCS Double Loop for Self-Healing Knowledge Base

  Scenario: Agent solves an issue with capture, reuse, and evolution
    Given an agent encounters a problem with "Issue" and "Environment" context
    When searching the knowledge brain for existing articles
    And no matching verified article is found
    Then capture a WIP article in active_memory with structured fields (Issue, Environment, Resolution)
    And after verification move to long_term_memory as Approved/Published
    And if existing article is flawed flag or fix it in the moment
```

## 🧪 The Catalyst (Code)
```python
# The Essence: KCS Solve Loop Implementation
from typing import Dict, Optional
from hfo.brain import KnowledgeBase  # Hypothetical HFO brain interface

def kcs_solve_loop(issue: str, environment: Dict[str, str], resolution: str, kb: KnowledgeBase) -> Dict:
    """
    Execute KCS Solve Loop: Capture -> Structure -> Reuse/Improve.
    """
    # Step 1: Capture & Structure
    article = {
        "issue": issue,
        "environment": environment,
        "resolution": resolution,
        "cause": "",  # To be analyzed
        "state": "WIP",
        "confidence_votes": []
    }
    
    # Step 2: Reuse - Search brain
    existing = kb.search(issue, environment)
    if existing:
        if kb.validate(existing, resolution):  # Works? Vote up
            kb.vote(existing["id"], +1)
            return {"action": "reused", "article_id": existing["id"]}
        else:  # Fix it
            kb.update(existing["id"], article)
            kb.set_state(existing["id"], "Draft")
            return {"action": "fixed", "article_id": existing["id"]}
    
    # Step 3: Improve/Evolve - Create new
    article_id = kb.create(article)
    kb.set_state(article_id, "Draft")  # For Evolve Loop (SME review)
    return {"action": "captured", "article_id": article_id}
```

## ⚔️ Synergies
*   **Diátaxis Fusion**: Uses KCS article structure (Issue/Env/Resolution) within Diátaxis folders (guides/reference in brain/).
*   **HFO Brain States**: Maps WIP/Draft/Approved/Published/Archived to active_memory/long_term_memory lifecycles.
*   **Stigmergy Integration**: Confidence votes as environmental signals for content health and performance assessment.
*   **Swarmlord Workflow**: Embeds "Flag It or Fix It" rule into agent processes for proactive Evolve Loop triggering.