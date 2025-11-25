# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 855d79ca-5dde-47cd-8227-4ae24d9de6d0
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-24T14:30:05.743279Z'
#     generation: 51
#   topos:
#     address: brain/intent_stigmergy_thermodynamics.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: intent_stigmergy_thermodynamics.feature
#

---
id: 550e8400-e29b-41d4-a716-446655440301
type: intent
status: active
title: 'Intent: Stigmergy Thermodynamics (Hot/Cold/Refined)'
created: '2025-11-23T13:00:00Z'
last_touched: '2025-11-23T13:00:00Z'
urgency: 1.0
stigmergy_score: 100.0
author: Swarmlord
links:
- brain/design_hfo_stigmergy_variants.md: defines
tags:
- intent
- gherkin
- stigmergy
- thermodynamics
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440301
    type: intent
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-23T13:00:00Z'
    generation: 52
  topos:
    address: brain/intent_stigmergy_thermodynamics.feature
    links: []
  telos:
    viral_factor: 1.0
    meme: Hot Lava -> Cold Glass -> Refined Gem.
---

Feature: Stigmergy Thermodynamics (Gen 52)
  As the Swarmlord
  I want to categorize Stigmergy into Hot, Cold, and Refined states
  So that the system mimics the formation of Obsidian and Gems

  Scenario: Hot State (Lava)
    Given a signal is emitted by an Agent
    When it enters the NATS JetStream
    Then it is classified as "Hot" (Lava)
    And it has high urgency and fluidity
    And it is transient (Fire & Forget)

  Scenario: Cold State (Volcanic Glass)
    Given a "Hot" signal is captured by the Genesis Protocol
    When it is written to the Filesystem
    Then it is classified as "Cold" (Volcanic Glass / Obsidian)
    And it is sharp, immutable, and structured (YAML/Markdown)
    And it serves as the "Source of Truth"

  Scenario: Refined State (Gem)
    Given a "Cold" file exists in the Filesystem
    When it is processed by the Assimilator
    Then it is classified as "Refined" (Gem / Knowledge)
    And it is stored in the Knowledge Graph (Postgres/Vector)
    And it is linked, indexed, and ready for retrieval
