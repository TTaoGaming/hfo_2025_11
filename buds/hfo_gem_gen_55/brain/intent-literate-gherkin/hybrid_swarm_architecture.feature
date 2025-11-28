Feature: Hybrid Swarm Architecture (Gen 55)

  As the Overmind
  I want a Hybrid Architecture with a swappable Local Heartbeat and Infinite Cloud Swarm
  So that I maintain 24/7 autonomy while leveraging SOTA intelligence.

  Background:
    Given the "Chromebook Plus" hardware constraints (8GB RAM)
    And the "OpenRouter" API key is available

  Scenario: The Weekly Local Champion (Heartbeat)
    Given the "Local Model Registry" defines the current SOTA model
    And the model is optimized for "Edge/Laptop" (2B-4B parameters)
    When the "Heartbeat" service starts
    Then it should load the model defined in "local_model_registry.yaml"
    And it should run 24/7 in an offline-capable loop

  Scenario: Cloud Swarm Delegation
    Given the Heartbeat detects a task requiring "Deep Reasoning" or "Massive Scale"
    When the Heartbeat emits a "Delegation Signal"
    Then the system should spawn agents via "OpenRouter"
    And these agents should write back to "HFO Stigmergy" (NATS/LanceDB)

  Scenario: Stigmergic Memory Persistence (Lvl 0)
    Given the Heartbeat generates "Pulse" and "Status" data
    When the data is finalized
    Then it should be stored in "LanceDB" with "privilege_level=0"
    And it should be accessible to all HFO agents
