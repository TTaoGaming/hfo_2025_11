# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 0a78b578-02c8-4405-9712-a9f29ce27a04
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:07.004834+00:00'
#   topos:
#     address: memory/episodic/gen_50_archive/prey_workflow.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: prey_workflow.feature
#

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
