# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 6284e88a-d8fe-44ce-bd2a-bd681c7eb2cb
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.404984Z'
#     generation: 51
#   topos:
#     address: brain/pattern_rich_metadata_stigmergy.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: pattern_rich_metadata_stigmergy.feature
#
Feature: Rich Metadata Stigmergy
  As the Swarmlord
  I want to define a "Rich Metadata" schema for Stigmergy
  So that the Swarm can coordinate with high-fidelity signals (Qualitative/Quantitative/Dispersion/Evaporation)

  Scenario: Claim Check Pattern with Rich Metadata
    Given an agent produces a heavy artifact (Payload)
    When the agent saves the artifact to Cold Storage (Postgres)
    Then the agent must emit a Signal to Hot Storage (NATS)
    And the Signal must contain the following Rich Metadata:
      | Field | Type | Description |
      | id | UUID | The Claim Check ID (Pointer to Payload) |
      | type | String | The type of artifact (e.g., "report", "code", "plan") |
      | quality_score | Float | 0.0-1.0 confidence/quality metric |
      | dispersion | Float | 0.0-1.0 how widely this should be broadcast |
      | evaporation_rate | Float | Rate at which this signal decays (ACO) |
      | context_tags | List[Str] | Semantic tags for routing |
      | sentiment | String | Qualitative feel (e.g., "urgent", "stable", "risky") |

  Scenario: Industry Hunt Mission
    Given the Swarm is active
    When I launch the mission "Hunt for Rich Metadata Stigmergy Best Practices"
    Then the Swarm should search for:
      | Topic | Context |
      | Ant Colony Optimization | Pheromone decay, trail reinforcement |
      | Termite Mounds | Stigmergic building, environmental cues |
      | Slime Mold | Network optimization, resource finding |
      | Digital Stigmergy | GitHub (Issues/PRs), Wikipedia (Edits), StackOverflow (Votes) |
      | Industry Patterns | Event Sourcing, CQRS, Claim Check, Saga Pattern |
    And the Swarm should synthesize a "Stigmergy Schema" for HFO.
