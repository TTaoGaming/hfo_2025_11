# stigmergy_header:
#   id: hfo-feature-heartbeat-1181
#   type: intent
#   status: draft
#   generation: 60
#   context: "The Cognitive Cycle of the Obsidian Spider"
#   tags: [heartbeat, prey, 1181, map-reduce-filter]

Feature: HFO Heartbeat PREY 1181 (Stigmergy Map-Reduce-Filter)
  As the Swarmlord
  I want a 1-1-8-1 Cognitive Cycle using identical Prey Agents via NATS JetStream
  So that the Swarm acts in unison with decoupled async stigmergy and self-auditing capabilities.

  Background:
    Given the NATS JetStream is enabled
    And the "hfo.heartbeat.pulse" stream is active
    And 8 Identical Prey Agents are subscribed to "hfo.phase.chant"

  Scenario: The Standard 1-1-8-1 Cycle
    # 1. Perceive (Map Input)
    Given a Prey Agent is listening as "Observer"
    When a Heartbeat Pulse occurs
    Then the Prey Agent reads the "Hot" NATS JetStream
    And produces a "ContextFrame" (Stigmergy Signal)

    # 2. Orchestrate (Map Logic)
    When a Prey Agent receives the "ContextFrame" as "Orchestrator"
    Then the Prey Agent determines the "Intent"
    And publishes "MissionOrders" to "hfo.phase.chant" for the Swarm

    # 3. Chant (Reduce/Process - Async Stigmergy)
    When the 8 Prey Agents receive the "MissionOrders"
    Then they execute their tasks concurrently (Async)
    And each Prey Agent publishes a "ChantVerse" (Level 0 Artifact)
    And the slowest hiker does not block the others (Decoupled)

    # 4. Reflexion (Filter/Audit)
    When a Prey Agent observes the "ChantVerses" as "Auditor"
    Then it aggregates the results (Reduce)
    And compares the "Intent" with the "Outcome"
    And if the Outcome matches the Intent
      Then the cycle is "Committed" to the Iron Ledger as a "Level 1 Artifact"
      And the Level 1 Artifact contains links to the 8 Level 0 Artifacts
    But if the Outcome violates the Intent or Safety Protocols
      Then the cycle is "Vetoed" and the action is rejected

  Scenario: Handling the Slowest Hiker
    Given the 8 Prey Agents are chanting
    When one Prey Agent is delayed beyond the "Pulse Window"
    Then the Auditor marks that Agent as "Silent"
    And proceeds with the Audit based on available Verses (Partial Consensus)

  Scenario: The Veto (Filter)
    Given the Orchestrator orders a "Dangerous Action"
    When the Prey Agents chant their Verses
    And the Auditor detects a violation in the consensus
    Then the Auditor triggers a "Veto"
    And the "Dangerous Action" is NOT executed
