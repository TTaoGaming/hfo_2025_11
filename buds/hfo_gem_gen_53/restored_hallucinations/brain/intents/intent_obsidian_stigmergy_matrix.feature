# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 2c6aa2e0-b2d9-4d08-baad-cd2dda9c2c16
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-24T14:30:05.754042Z'
#     generation: 51
#   topos:
#     address: brain/intent_obsidian_stigmergy_matrix.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: intent_obsidian_stigmergy_matrix.feature
#

---
id: 550e8400-e29b-41d4-a716-446655440304
type: intent
status: active
title: 'Intent: The OBSIDIAN Stigmergy Matrix'
created: '2025-11-23T13:35:00Z'
last_touched: '2025-11-23T13:35:00Z'
urgency: 1.0
stigmergy_score: 100.0
author: Swarmlord
links:
- brain/design_obsidian_stigmergy_matrix.md: implements
tags:
- intent
- gherkin
- obsidian
- matrix
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440304
    type: intent
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-23T13:35:00Z'
    generation: 52
  topos:
    address: brain/intent_obsidian_stigmergy_matrix.feature
    links: []
  telos:
    viral_factor: 1.0
    meme: O.B.S.I.D.I.A.N. Roles.
---

Feature: The OBSIDIAN Stigmergy Matrix
  As the Swarmlord
  I want to enforce the OBSIDIAN Stigmergy Matrix
  So that Agent Roles align with Biological Stigmergy mechanisms

  Scenario Outline: Role to Stigmergy Mapping
    Given an agent with role "<Role>"
    When it interacts with the Substrate
    Then it performs the function of "<Stigmergy>"
    And it utilizes the concept of "<Concept>"

    Examples:
      | Role        | Stigmergy       | Concept                  |
      | Observer    | Olfaction       | Gradient Analysis        |
      | Bridger     | Boundary        | Boundary Conditions      |
      | Shaper      | Secretion       | Deposition               |
      | Injector    | Intensification | Logistics / Blood        |
      | Disruptor   | Dissipation     | Adversarial Byzantine    |
      | Immunizer   | Inhibition      | Anti-Fragility           |
      | Assimilator | Accretion       | Stigmergic Construction  |
      | Navigator   | Nucleation      | Cluster Formation        |

  Scenario: The Growth Loop (Intensification)
    Given a signal exists in the Substrate
    When an Injector reinforces it
    Then it spawns more AI agents (Blood)
    And the signal strength increases (Signal++)

  Scenario: The Decay Loop (Dissipation)
    Given a signal exists in the Substrate
    When the Disruptor attacks it (MITRE ATT&CK)
    Then the signal is challenged
    And it must prove its resilience or vanish (Signal--)

  Scenario: The Control Loop (Inhibition)
    Given a toxic or erroneous signal exists
    When an Immunizer detects the error
    Then it blocks the path (Inhibition)
    And it updates the system to be Anti-Fragile against future attacks
