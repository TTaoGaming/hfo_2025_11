# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 5d2544b2-8f55-473f-9e5d-04dd753db35b
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.519509Z'
#     generation: 51
#   topos:
#     address: brain/design_stigmergy_substrate.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: design_stigmergy_substrate.feature
#
Feature: Stigmergy Substrate (The Natural Async System)
  """
  The Stigmergy Substrate is the environment where the Swarm lives.
  It is a natural, asynchronous system with loose coupling, powered by a diverse population of AIs.
  It supports Quality-Diversity (QD) by allowing different AI grades (High/Low Reasoning) to interact via the same Hexagonal Protocol.
  """

  As a Swarmlord
  I want a multi-modal Stigmergy Substrate
  So that I can orchestrate a diverse swarm of AIs (Fast/Cheap vs. Slow/Smart) in a loosely coupled, async manner

  Scenario: The Three States of Matter (Polymorphic Substrate)
    """
    The Substrate exists in three forms to support different tempos.
    """
    Given the "Hexagonal Holon" is the universal carrier
    When it enters the "Crystalline State" (Filesystem)
      Then it supports "Human-AI Collaboration" and "GitOps"
    When it enters the "Liquid State" (NATS JetStream)
      Then it supports "High-Speed Coordination" and "Reflexive Action"
    When it enters the "Sedimentary State" (Vector DB/Graph)
      Then it supports "Deep Recall" and "Long-Term Memory"

  Scenario: QD AI Composition (The Cognitive Spectrum)
    """
    Different agents use different AI models based on the task value.
    """
    Given a "Task" with a specific "Value" and "Urgency"
    When the "Swarm Orchestrator" assigns an Agent
    Then it selects the "Cognitive Grade" based on the "QD Matrix":
      | Grade          | Model              | Role                | Cost | Speed | Reasoning |
      | Reflex (Low)   | x-ai/grok-4.1-fast | Signal Processing   | $    | +++++ | +         |
      | Logic (Mid)    | gpt-4o-mini        | Routine Operations  | $$   | +++   | +++       |
      | Reason (High)  | gemini-2.0-flash   | Strategic Planning  | $$$  | ++    | +++++     |
      | Apex (Ultra)   | o1-preview         | Novelty Generation  | $$$$ | +     | ++++++    |

  Scenario: Loose Coupling via Pheromones (Async Coordination)
    """
    Agents do not talk to each other; they talk to the Substrate.
    """
    Given an "Agent A" (Producer) and "Agent B" (Consumer)
    When "Agent A" completes a task
    Then it deposits a "Hexagonal Pheromone" (Signal) into the "Liquid Substrate"
    And "Agent A" immediately moves to the next task (Async)
    And "Agent B" senses the Pheromone when it is ready (Decoupled)
    And "Agent B" reacts based on the Pheromone's "Telos" (Intent) and "Chronos" (Urgency)
