# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 258a0517-45f2-4589-b036-a99999d42063
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.342449Z'
#     generation: 51
#   topos:
#     address: brain/workflow_karmic_web.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: workflow_karmic_web.feature
#
---
owner: Swarmlord
status: Missing
title: Workflow Karmic Web
type: Intent
---

Feature: The Karmic Web (Precedent Hunting)
  As the Swarmlord
  I want to hunt for "Exemplars" from the past (History, GitHub, Nature)
  So that I can solve problems using "Case-Based Reasoning" instead of guessing.

  Background:
    Given the "Karmic Swarm" is active
    And the "Tool Registry" has "Web Search" and "Brain Search" enabled

  Scenario: Hunting for a Precedent
    Given a user intent "Build a distributed task queue"
    When the Karmic Swarm receives the intent
    Then it should categorize the domain using "Cynefin" (Simple, Complicated, Complex, Chaotic)
    And it should generate search queries for:
      | Category       | Source          |
      | Biomimicry     | Nature          |
      | Open Source    | GitHub/GitLab   |
      | Industry       | Engineering Blogs|
    And it should execute the searches
    And it should synthesize the findings into a "Karmic Report"
    And the report should contain at least 3 "Exemplars"
