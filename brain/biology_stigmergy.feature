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
