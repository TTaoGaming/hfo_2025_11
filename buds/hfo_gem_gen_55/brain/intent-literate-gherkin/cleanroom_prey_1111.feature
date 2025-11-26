Feature: Cleanroom Genesis of 1-1-1-1 PREY Loop (Atomic Unit)

  Background:
    Given the "Synapse APEX" generation (Gen 55)
    And the "Hot Stigmergy" layer (NATS JetStream) is active
    And the "Gemma 3 270M" model is loaded locally

  Scenario: Sequential State Machine (The 4 Hats)
    Given a single "Atomic Agent" (1-1-1-1)
    When the agent enters the "Perceive" phase
    Then it must produce a "PerceptionReport"
    And transition to the "React" phase

    When the agent enters the "React" phase
    Then it must read the "PerceptionReport"
    And produce a "ReactionPlan"
    And transition to the "Execute" phase

    When the agent enters the "Execute" phase
    Then it must execute the "ReactionPlan"
    And produce an "ExecutionResult"
    And transition to the "Yield" phase

    When the agent enters the "Yield" phase
    Then it must synthesize the "ExecutionResult"
    And produce a "YieldArtifact"
    And publish it to "NATS JetStream"

  Scenario: Iterative Context Accumulation (The 3-Loop Test)
    Given the agent completes "Loop 1" with Artifact A1
    And the agent completes "Loop 2" with Artifact A2
    When the agent begins "Loop 3"
    Then it must "Perceive" both A1 and A2 from the Stigmergy Layer
    And explicitly acknowledge the history in its "PerceptionReport"
    And produce Artifact A3 that builds upon A2

  Scenario: Anytime Robustness (Timeout & Retry)
    Given the agent is executing a phase
    If the operation exceeds the "Timeout Threshold" (e.g., 30s)
    Then the system must "Retry" the operation up to 3 times
    And if all retries fail, it must "Yield" a "FailureArtifact"
    And continue to the next loop iteration (Non-Blocking)
