# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 377cbf85-a1ff-47ef-9b59-85c9903434b1
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.251403Z'
#     generation: 51
#   topos:
#     address: brain/architecture_hybrid_memory.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: architecture_hybrid_memory.feature
#
---
owner: Swarmlord
status: Placeholder
title: Architecture Hybrid Memory
type: Intent
---

Feature: Hybrid Stigmergic GraphRAG Memory
  As the Assimilator (Memory)
  I want to combine NATS and Postgres
  So that I have both fast "Hot State" and deep "Cold Wisdom".

  Scenario: Hot State (Episodic)
    Given an agent emits a signal
    When it enters the NATS Stream
    Then it is available immediately for "Reflexive" reactions
    And it expires after a short TTL (e.g., 1 hour).

  Scenario: Cold Wisdom (Semantic)
    Given the NATS Stream is active
    When the "Crystal Spinner" (Assimilator) processes the stream
    Then it should extract "Concepts" and "Relations"
    And it should store them in the Postgres "Knowledge Graph"
    And it should generate Vector Embeddings for semantic search.
