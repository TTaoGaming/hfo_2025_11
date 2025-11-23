# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: baf2c225-dd69-46b4-93de-74403b4034fd
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.566691Z'
#     generation: 51
#   topos:
#     address: brain/intent_hexagonal_seeding.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: intent_hexagonal_seeding.feature
#
Feature: Hexagonal Stigmergy Seeding
  As the Swarmlord
  I want to seed every file in the repository with a "Hexagonal Stigmergy Header"
  So that I can track "Time as Version" and enable "Smart Cleanup" via composable fields

  Scenario: The Great Seeding
    Given the repository contains code and documentation
    And the architecture is evolving to "Gen 51 Synapse APEX"
    Then every file (except archives) must receive a "Hexagonal Header"
    And the header must contain 6 dimensions: "Ontos", "Telos", "Chronos", "Topos", "Logos", "Pathos"
    And "Chronos" must store the "Last Touched" timestamp as the "Version"
    And "Telos" must indicate the file's status (Active/Stale)

  Scenario: Time is Version
    Given a file is modified
    Then its "Chronos.version" must be updated to the current timestamp
    And this timestamp serves as the definitive "Truth" for conflict resolution

  Scenario: Smart Cleanup Preparation
    Given all files have headers
    Then a "Scavenger Agent" can scan the headers
    And identify "Stale" files (Old Chronos) or "Disconnected" files (Empty Topos)
    And propose them for "Archival" or "Refactoring"
