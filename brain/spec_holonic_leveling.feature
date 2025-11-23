# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: eb0a877e-bf9e-4b4e-8420-f2b3b6f09164
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:31.522471+00:00'
#   topos:
#     address: brain/spec_holonic_leveling.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: spec_holonic_leveling.feature
#

Feature: Holonic Knowledge Leveling (Cooling System)

  As the Swarmlord
  I want to implement a "Cooling System" for Truth (Plasma -> Gas -> Liquid -> Crystal)
  So that I can filter Truth from Noise based on Log-10 Swarm Consensus

  Background:
    Given the Phase Transition Table is defined as:
      | Level | Phase   | Agents | Exemplar           | Storage   |
      | 0     | Plasma  | 1      | Stigmergy          | NATS      |
      | 1     | Gas     | 10     | Agile Squad        | File      |
      | 2     | Liquid  | 100    | Dunbar's Tribe     | VectorDB  |
      | 3     | Crystal | 1000   | Byzantine Quorum   | GraphDB   |

  Scenario: Condensation (Plasma to Gas)
    Given a "Plasma" signal exists in NATS with:
      | attribute | value |
      | content   | "Sky is Green" |
    When a Squad of 10 Agents reviews the signal
    And 9 Agents vote "Reject"
    Then the signal fails to Condense
    And the signal evaporates (Deleted)

  Scenario: Liquefaction (Gas to Liquid)
    Given a "Gas" artifact exists in Filesystem with:
      | attribute | value |
      | content   | "Sky is Blue" |
    When a Platoon of 100 Agents reviews the artifact
    And 85 Agents vote "Accept"
    Then the artifact Liquefies into "VectorDB"
    And the Trust Score increases to 0.8

  Scenario: Crystallization (Liquid to Crystal)
    Given a "Liquid" vector exists in VectorDB
    When the Assimilator (1000 nodes) tests it against the Graph
    And it survives a Byzantine Attack (1/3rd malicious)
    Then the artifact Crystallizes into "GraphDB"
    And it becomes a permanent Node

  Scenario: Query Routing by Phase
    Given a User asks "What is the absolute truth?"
    When the Query Router filters artifacts
    Then only artifacts in "Crystal" phase are returned
    And artifacts with "Decay > 0.5" are excluded
