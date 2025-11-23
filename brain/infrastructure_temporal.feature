# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 86d83192-a8f9-4b6d-ad68-53b7a3faca3a
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:31.489823+00:00'
#   topos:
#     address: brain/infrastructure_temporal.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: infrastructure_temporal.feature
#

Feature: Temporal Orchestration (Stabilization Layer)
  As the Swarmlord
  I want to wrap the Research Swarm in a Temporal Workflow
  So that I can ensure durable execution, retries, and timeouts (Stabilization).

  Scenario: Execute Research Swarm via Temporal
    Given the Research Swarm logic is defined in "body/hands/research_swarm.py"
    And the Temporal Infrastructure is running on port 7235
    When I submit a "ResearchSwarmWorkflow" with a mission
    Then the workflow should execute the "run_research_swarm_activity"
    And the activity should connect to NATS
    And the activity should run the LangGraph application
    And the workflow should return the final digest
    And the workflow should retry on failure up to 3 times
    And the activity should timeout after 300 seconds

  Scenario: Async Operation Verification
    Given the Swarm is running in a Temporal Activity
    When the activity performs long-running tasks (Network/LLM)
    Then it should use async/await patterns
    And it should not block the Temporal Worker heartbeat
