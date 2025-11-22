---
owner: Swarmlord
status: Placeholder
title: Pattern Async Swarm
type: Intent
---

Feature: Async Swarm Process Pattern
  As the Swarmlord
  I want to use the "Async Swarm Process" pattern for all batch operations
  So that the Hive can scale without freezing and maintain coordination.

  Scenario: High-Velocity Parallel Processing
    Given a large backlog of tasks (e.g., 200+ files)
    When the "Dispatcher" publishes tasks to a NATS Subject (e.g., "hfo.task.x")
    And a "Swarm" of N workers (e.g., 20) subscribes to the same Subject using a "Queue Group"
    And each Worker uses "AsyncIO" for all I/O (Network/Disk)
    And each Worker reads "Stigmergic Context" (Recent Signals) before processing
    Then the system should process tasks in parallel without blocking
    And the throughput should scale linearly with N workers
    And no single worker failure should halt the swarm.
