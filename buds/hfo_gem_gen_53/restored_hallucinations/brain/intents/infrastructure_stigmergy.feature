# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 37205d1d-fbdf-4476-b978-82b55fefc7b7
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.293201Z'
#     generation: 51
#   topos:
#     address: brain/infrastructure_stigmergy.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: infrastructure_stigmergy.feature
#
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
