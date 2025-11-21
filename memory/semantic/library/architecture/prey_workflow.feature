---
title: 'PREY Loop: Atomic Holon State Machine'
summary: Defines the PREY Loop (Perceive, React, Execute, Yield) as the fundamental,
  non-delegating lifecycle for holons in the swarm architecture.
domain: Architecture
concepts:
- PREY Loop
- Holon Lifecycle
- State Machine
- Cognitive Feedback
- Stigmergy
owner: Swarm Architect
actionable: false
related_files: []
type: crystallized_memory
status: active
last_verified: '2025-11-21'
---

Feature: The PREY Loop (Atomic Holon)
  As the Swarm Architect
  I want to define the atomic unit of cognition (The PREY Loop)
  So that every agent, regardless of scale, follows the same observable state machine.

  # Cognitive Chunking: This is the "Leaf Node" of the Fractal Holarchy.
  # It does not delegate. It executes.

  Scenario: The PREY Lifecycle
    Given a "Holon" is initialized with a "Task"

    # Phase 1: PERCEIVE (Input Processing)
    When the Holon enters the "Perceive" state
    Then it must "Gather Context" from the Environment
    And it must "Read Memory" (Short-term & Long-term)
    And it transitions to the "React" state

    # Phase 2: REACT (Cognitive Processing)
    When the Holon enters the "React" state
    Then it must "Synthesize" the Perception
    And it must "Formulate a Plan" (Sequence of Actions)
    And it must "Validate" the plan against Safety Guardrails
    And it transitions to the "Execute" state

    # Phase 3: EXECUTE (Output Generation)
    When the Holon enters the "Execute" state
    Then it must "Invoke Tools" or "Generate Content"
    And it must "Capture Results" (Success/Failure)
    And it transitions to the "Yield" state

    # Phase 4: YIELD (Learning & Persistence)
    When the Holon enters the "Yield" state
    Then it must "Reflect" on the outcome (Self-Correction)
    And it must "Calculate Reward" (Reinforcement Learning)
    And it must "Update Memory" (Stigmergy & Internal State)
    And it must "Emit a Signal" (Completion/Failure)
    And the Holon transitions to "Perceive" (Feedback Loop) or terminates
