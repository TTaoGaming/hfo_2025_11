Feature: The 1-1-1-1 PREY Loop Protocol

  Background:
    Given the "Synapse APEX" generation (Gen 55)
    And a low-resource environment (e.g., Chromebook Plus)
    And the "Gemma 3 270M" model is active

  Scenario: Sequential Agent State Transition (The 4 Hats)
    Given an agent with Secure ID "Agent-007"
    And the current state is "Idle" or "Yield(N-1)"

    When the agent enters the "Perceive" phase
    Then it must adopt the "Observer" bias
    And apply "Cynefin" framework to categorize the situation
    And publish a "PerceptionReport" to NATS JetStream

    When the agent enters the "React" phase
    Then it must adopt the "Bridger" bias
    And formulate a plan based on the "PerceptionReport"
    And publish a "ReactionPlan" to NATS JetStream

    When the agent enters the "Execute" phase
    Then it must adopt the "Shaper" bias
    And execute the tools defined in the "ReactionPlan"
    And publish an "ExecutionResult" to NATS JetStream

    When the agent enters the "Yield" phase
    Then it must adopt the "Assimilator" bias
    And perform a "Self-Audit" (Reflexion) on the "ExecutionResult"
    And synthesize the findings into a "YieldReport"
    And publish it to "NATS JetStream"
    And update the NATS KV store with the new state for "Perceive(N+1)"

  Scenario: Stigmergic State Persistence
    Given the agent completes "Yield(N)"
    When the agent starts "Perceive(N+1)"
    Then it must retrieve the context from NATS KV using its Secure ID
    And NOT rely on local process memory

  Scenario: Permission Boundaries
    Given the agent is in any phase
    Then it has READ access to "File System", "Web", and "Memory"
    But it has WRITE access ONLY to "NATS JetStream"
