# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: f37a0f71-508a-41db-9152-096c311d5a0a
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:06:41.095070Z'
#     generation: 51
#   topos:
#     address: memory/episodic/gen_50_archive/cognitive_architecture.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: cognitive_architecture.feature
#
Feature: Cognitive Architecture (Reasoning & Learning)
  As the Swarm Architect
  I want to enforce High Reasoning and Reinforcement Learning in all agents
  So that the Hive gets smarter over time and avoids repeating mistakes.

  # Core Principle: "Think Deep, Act Fast, Learn Always."

  Scenario: High Reasoning Mode (System 2 Thinking)
    Given an agent is performing a "Cognitive Step" (Perceive, React, Yield)
    When the agent constructs the "LLM Prompt"
    Then it must inject the "Reasoning Directive":
      """
      REASONING MODE: HIGH
      Think step-by-step. Analyze patterns. Anticipate errors.
      """
    And it must require a "Chain of Thought" in the response
    And it must not accept "Lazy Answers" or "Hallucinations"

  Scenario: Reinforcement Learning Loop (Stigmergic Feedback)
    Given an agent has completed an "Execution"
    When the agent enters the "Yield" phase
    Then it must "Reflect" on the outcome (Success/Failure)
    And it must identify "Lessons Learned" (What worked? What failed?)
    And it must "Publish" these lessons to the "Stigmergy Layer" (NATS)

  Scenario: Knowledge Inheritance (The Wisdom of the Crowd)
    Given a new agent is starting a "Perceive" phase
    When it "Reads Memory" from the Stigmergy Layer
    Then it must "Ingest" the "Lessons Learned" from previous agents
    And it must "Adjust its Plan" to avoid known pitfalls
    And it must "Cite" the source of its wisdom (Traceability)
