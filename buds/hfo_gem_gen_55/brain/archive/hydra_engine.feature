Feature: The Hydra Engine (Durable & Regenerative)
  As the Swarmlord
  I want a durable execution engine that can regenerate from specs
  So that the Swarm survives infrastructure failures and systemic poisoning

  Rule: Execution must be Durable (Temporal)
    Given a Swarm Workflow is running
    And the Workflow is managed by Temporal
    When the host process crashes or is killed
    Then the Workflow must resume from the last Checkpoint
    And no state should be lost

  Rule: Implementation must be Regenerative (Phoenix)
    Given a component implementation in "body/"
    And the corresponding Gherkin Spec in "brain/"
    When the implementation is flagged as "Poisoned" or "Drifted"
    Then the Phoenix Protocol must delete the implementation file
    And the Genesis Agent must regenerate it strictly from the Gherkin Spec
    And the new implementation must pass all Venom tests

  Rule: Poison must be Isolated (Bulkheads)
    Given a Squad of 8 Agents running in Ray
    When one Agent is compromised or crashes
    Then the failure must be contained to that Agent's Actor
    And the other 7 Agents must continue execution
    And the Supervisor must restart the failed Agent
