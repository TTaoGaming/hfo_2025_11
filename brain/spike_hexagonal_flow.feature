# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 6298ff03-a91a-48dc-bfa7-28294a9f0fbf
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:31.531657+00:00'
#   topos:
#     address: brain/spike_hexagonal_flow.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: spike_hexagonal_flow.feature
#

Feature: Spike Hexagonal Flow
  """
  This spike verifies the end-to-end lifecycle of a Hexagonal Holon.
  It tests the transition from Crystalline (Code) to Liquid (Signal) to Sedimentary (DB).
  """

  As a Swarmlord
  I want to execute a "Tracer Bullet" through the Hexagonal Architecture
  So that I can verify the Stigmergy Substrate is ready for the Swarm

  Scenario: The Shapeshifter Test
    Given I forge a new "Hexagonal Holon" with Urgency 0.9
    When I adapt it to the "Liquid State" (NATS Signal)
    And I adapt it to the "Sedimentary State" (Vector Metadata)
    Then the "Identity" (Ontos) must match across all states
    And the "Urgency" (Chronos) must be preserved
    And the "Viral Factor" (Telos) must be present in the Signal
