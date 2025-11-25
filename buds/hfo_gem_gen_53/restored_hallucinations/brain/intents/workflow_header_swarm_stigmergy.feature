# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 4e59e8d9-8e8f-44e4-85c3-a32c4598419a
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.480837Z'
#     generation: 51
#   topos:
#     address: brain/workflow_header_swarm_stigmergy.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: workflow_header_swarm_stigmergy.feature
#
Feature: Header Swarm Stigmergy Workflow

  As the Swarmlord
  I want the Header Swarm to emit "Hot" Stigmergy Signals while creating "Cold" Artifacts
  So that the Hive Mind is aware of the crystallization process in real-time

  Background:
    Given the Stigmergy Taxonomy is defined as:
      | Category | Medium   | Persistence | Purpose             | Examples                     |
      | Hot      | NATS     | Ephemeral   | Coordination/Signal | Pheromones, Heartbeats       |
      | Cold     | Files/DB | Durable     | Memory/Knowledge    | Markdown Headers, Vectors    |

  Scenario: Crystallization Workflow (Hot & Cold)
    Given a file "brain/design_mountain_web_stigmergy.md" exists without a header
    When the "Header Swarm" is triggered via Temporal
    Then the Swarm initiates "Round 1: Divergence"
    And emits a Hot Signal "swarm.header.started" with metadata:
      | field   | value       |
      | target  | filename.md |
      | squad   | 10 agents   |

    When "Round 1" completes
    Then 10 "Draft Headers" are generated (Internal State)
    And a Hot Signal "swarm.header.divergence_complete" is emitted

    When "Round 2: Convergence" completes
    Then 5 "Refined Headers" are synthesized
    And a Hot Signal "swarm.header.convergence_complete" is emitted

    When "Round 3: Consensus" completes
    Then a single "Golden Header" is selected
    And the Cold Artifact "brain/design_mountain_web_stigmergy.md" is updated with the Hexagon
    And a Hot Signal "swarm.header.crystallized" is emitted with the final Hexagon metrics
