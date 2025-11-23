# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: e661800f-9788-46ed-87cc-6b176bbe1970
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T10:21:31.458242+00:00'
#   topos:
#     address: brain/biology_stigmergy.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: biology_stigmergy.feature
#

---
owner: Swarmlord
status: Placeholder
title: Biology Stigmergy
type: Intent
---

Feature: Evolutionary Pheromones
  As the Bridger
  I want to use a Pheromone Language
  So that signals convey evolutionary meaning.

  Scenario: Pheromone Schema
    Given a Stigmergy Signal
    Then it must contain "Pheromone Metadata":
      | Field | Description |
      | Species | Ant (Trail), Termite (Build), Mold (Explore) |
      | Strength | 0.0 to 1.0 (Importance) |
      | Decay | Rate of evaporation |

  Scenario: Emergent Behavior
    Given multiple agents emitting "Ant Pheromones" (Trails)
    When other agents encounter the trail
    Then they should follow the gradient of highest strength
    And the trail should reinforce itself (Positive Feedback).
