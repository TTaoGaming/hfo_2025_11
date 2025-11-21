---
title: 'HIVE Loop: Strategic Double Diamond Workflow'
summary: Defines the Level 3 HIVE strategic loop as a recursive Double Diamond process
  (Discover-Define-Develop-Deliver) for solving complex problems via scout and builder
  swarms.
domain: Strategy
concepts:
- HIVE Loop
- Double Diamond
- Swarm Architecture
- Fractal Workflows
- Evolutionary Algorithms
owner: Swarm Architect
actionable: false
related_files: []
type: crystallized_memory
status: active
last_verified: '2025-11-21'
---

Feature: The HIVE Loop (Strategic Double Diamond)
  As the Swarm Architect
  I want to define the Level 3 Strategic Loop (HIVE)
  So that the system can solve complex, ambiguous problems by exploring the problem space before the solution space.

  # Pattern: Double Diamond (Discover -> Define -> Develop -> Deliver)
  # HFO Twist: Recursive & Fractal. Each phase can spawn a GROWTH or SWARM loop.

  Scenario: The HIVE Lifecycle
    Given a "Strategic Objective" (e.g., "Map the AI Agent Ecosystem")

    # Diamond 1: Problem Space (Diverge -> Converge)

    # Phase 1: DISCOVER (Diverge)
    When the Hive enters the "Discover" state
    Then it must "Explore the Domain" broadly
    And it spawns "Scout Swarms" (Level 1) to gather raw intelligence
    And it accumulates "Unstructured Data" in the Stigmergy Layer

    # Phase 2: DEFINE (Converge)
    When the Hive enters the "Define" state
    Then it must "Synthesize Findings" from the Scouts
    And it identifies "Key Insights" and "Problem Clusters"
    And it produces a "Mission Specification" (The 'Brief')

    # Diamond 2: Solution Space (Diverge -> Converge)

    # Phase 3: DEVELOP (Diverge)
    When the Hive enters the "Develop" state
    Then it must "Ideate Solutions" based on the Brief
    And it spawns "Builder Swarms" (Level 2 GROWTH) to prototype and test
    And it uses "Evolutionary Algorithms" (MAP-Elites) to explore solution variations

    # Phase 4: DELIVER (Converge)
    When the Hive enters the "Deliver" state
    Then it must "Select Best Solutions" from the population
    And it "Refines and Polishes" the final artifacts
    And it "Publishes" the result to the Long-Term Memory (GraphRAG)
    And the Hive terminates or loops back to Discover (Continuous Improvement)
