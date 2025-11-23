# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: cb6ae65b-1318-433b-9832-48eafe214657
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:31.503211+00:00'
#   topos:
#     address: brain/design_mountain_web_stigmergy.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: design_mountain_web_stigmergy.feature
#

Feature: The Mountain and The Web (Deep Stigmergy)
  As the Swarmlord
  I want to implement a Fractal Stigmergy System (Mountain & Web)
  So that the Hive can coordinate across Time (Static) and Space (Hot) without central control.

  Scenario: The Obsidian Facet (Unified Schema)
    Given an artifact is created in the Hive
    Then it must have a YAML header (The Facet)
    And the header must contain "id", "type", "created", "last_touched", "urgency", and "stigmergy_score"
    And the "stigmergy_score" must decay over time unless "last_touched" is updated.

  Scenario: The Sherpa (Retrieval Holon)
    Given the "Assimilator.Sherpa" agent is active
    When it scans the "Mountain" (File System)
    Then it must identify files with High Urgency (>0.7) and Old Last_Touched (>24h)
    And it must broadcast a "hfo.signal.file.touched" message to the "Web" (NATS).

  Scenario: The Gardener (Pruning Holon)
    Given the "Assimilator.Gardener" agent is active
    When it scans the "Mountain"
    Then it must identify files with Low Stigmergy Score (<10.0)
    And it must move them to "memory/archive/" (The Cave).

  Scenario: The Weaver (Synthesis Holon)
    Given the "Assimilator.Weaver" agent is active
    When it receives a "hfo.signal.file.touched" message
    Then it must analyze the file's context
    And it must update the file's YAML header with new "links" to related artifacts.
