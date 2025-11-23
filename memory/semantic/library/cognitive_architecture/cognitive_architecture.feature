# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 71008acc-1038-49bc-8628-34fe0032868a
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:06:52.589623Z'
#     generation: 51
#   topos:
#     address: memory/semantic/library/cognitive_architecture/cognitive_architecture.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: cognitive_architecture.feature
#
---
title: 'Cognitive Architecture: Reasoning & Learning'
summary: Defines Gherkin scenarios for enforcing high reasoning mode, reinforcement
  learning loops, and knowledge inheritance in swarm agents to enhance hive intelligence.
domain: Cognitive Architecture
concepts:
- High Reasoning Mode
- Reinforcement Learning Loop
- Stigmergic Feedback
- Knowledge Inheritance
- Chain of Thought
owner: Swarm Architect
actionable: true
related_files: []
type: crystallized_memory
status: active
last_verified: '2025-11-21'
---

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
