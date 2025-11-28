# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 867197c9-206a-46c3-b44a-63b9bea3c5ee
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.256520Z'
#     generation: 51
#   topos:
#     address: brain/architecture_organs_roles_champions.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: architecture_organs_roles_champions.feature
#
---
owner: Swarmlord
status: Placeholder
title: Architecture Organs Roles Champions
type: Intent
---

Feature: Organs, Roles, and Champions
  As the Architect
  I want to define the physiological structure of the Hive
  So that every component has a clear biological purpose.

  Scenario: Organ Definition
    Given a directory in the repo
    Then it must map to a "Biological Organ" (e.g., brain, body, eyes)
    And it must have a "Primary Seat" (Role).

  Scenario: Role Definition
    Given a "Role" (e.g., Navigator, Observer)
    Then it must map to a "JADC2 Function" (e.g., C2, Sensor)
    And it must have a set of "Responsibilities".

  Scenario: Champion Evolution
    Given a Role
    When a specific "Champion" (Agent Instance) is instantiated
    Then it should be selected via "MAP-Elites" based on performance
    And its "Gene Seed" (Prompt/Config) should be recorded.
