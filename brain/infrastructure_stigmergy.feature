---
owner: Swarmlord
status: Placeholder
title: Infrastructure Stigmergy
type: Intent
---

Feature: Stigmergy Layer (NATS)
  As the Bridger (Communicator)
  I want to use NATS JetStream for Stigmergy
  So that agents can coordinate asynchronously without direct coupling.

  Scenario: Emission
    Given an agent completes a task
    When it produces an "Artifact"
    Then it should publish a "Signal" to the NATS Subject `hfo.mission.{id}.{phase}`
    And the payload should contain the Artifact ID and Metadata.

  Scenario: Reaction
    Given an agent is subscribed to `hfo.mission.>`
    When a relevant Signal is received
    Then the agent should "Wake Up" (React)
    And it should retrieve the Artifact from the Object Store (or Memory)
    And it should process the next step.
