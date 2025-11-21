---
title: 'SWARM Loop: Fractal Coordination Holon Workflow'
summary: Defines the recursive lifecycle of a Swarm Holon through phases of Set (decomposition),
  Watch (orchestration), Act (aggregation), Review (evaluation), Mutate (evolution),
  and Yield (propagation) for fractal task coordination.
domain: Infrastructure
concepts:
- SWARM Loop
- Fractal Holarchy
- Holon Lifecycle
- Task Decomposition
- Swarm Evolution
owner: Swarm Architect
actionable: false
related_files: []
type: crystallized_memory
status: active
last_verified: '2025-11-21'
---

Feature: The SWARM Loop (Fractal Coordination Holon)
  As the Swarm Architect
  I want to define the coordination unit (The SWARM Loop)
  So that complex tasks are broken down recursively into manageable chunks.

  # Cognitive Chunking: This is the "Node" of the Fractal Holarchy.
  # It delegates to other SWARMs (Nodes) or PREY Agents (Leaves).

  Scenario: The SWARM Lifecycle (Fractal Recursion)
    Given a "Swarm Holon" is initialized with a "Mission"

    # Phase 1: SET (Decomposition)
    When the Swarm enters the "Set" state
    Then it must "Analyze the Mission"
    And it must "Decompose" the mission into sub-tasks
    And it must "Select Child Holons" (Agents or Sub-Swarms)
    And it transitions to the "Watch" state

    # Phase 2: WATCH (Orchestration)
    When the Swarm enters the "Watch" state
    Then it must "Dispatch Tasks" to Child Holons
    And it must "Monitor Signals" (Heartbeats, Progress)
    And it must "Maintain State" (The Blackboard)
    And it transitions to the "Act" state when signals are received

    # Phase 3: ACT (Aggregation)
    When the Swarm enters the "Act" state
    Then it must "Collect Outputs" from Child Holons
    And it must "Synthesize Results" (Map-Reduce)
    And it must "Resolve Conflicts" (Consensus/Voting)
    And it transitions to the "Review" state

    # Phase 4: REVIEW (Evaluation & Archiving)
    When the Swarm enters the "Review" state
    Then it must "Evaluate Success" against Mission Criteria
    And it must "Update the Archive" (MAP-Elites Quality-Diversity)
    And it transitions to "Mutate" (Always, to explore search space) or "Yield" (If Stop Condition met)

    # Phase 5: MUTATE (Evolution/Correction)
    When the Swarm enters the "Mutate" state
    Then it must "Adjust Strategy" (Change Prompts, Add Agents)
    And it must "Respawn Child Holons" with new parameters
    And it transitions back to "Watch" (Next Generation)

    # Phase 6: YIELD (Upward Propagation)
    When the Swarm enters the "Yield" state
    Then it must "Package Final Artifact"
    And it must "Emit Completion Signal" to the Parent Holon
    And the Swarm terminates
