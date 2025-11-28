# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: d2dfc96b-3f24-4a66-ac61-ea0fd267a615
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:06:41.129680Z'
#     generation: 51
#   topos:
#     address: memory/episodic/gen_50_archive/memory_graphrag.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: memory_graphrag.feature
#
Feature: Memory GraphRAG System (The Karmic Web)
    As the Swarmlord
    I want a self-organizing Knowledge Graph (The Karmic Web)
    So that the swarm learns from every generation and avoids repeating mistakes

    # Core Concept: "The Bus Builds the Brain"
    # The Stigmergy Layer (NATS) provides the raw stream of consciousness.
    # The Memory Layer (GraphRAG) crystallizes this into long-term wisdom.

    Scenario: Capture - Assimilation of Stigmergy Signals
        Given a "ResultSignal" is published to "hfo.result.success"
        And the signal contains valid "Code" and "Reasoning"
        When the "Assimilator" agent consumes the signal
        Then it must create a "MemoryNode" in the Knowledge Graph
        And generate a "VectorEmbedding" for the content via "pgvector"
        And link the node to the original "MissionIntent" (Edge: IMPLEMENTS)

    Scenario: Structure - Semantic Linking and Indexing
        Given a new "MemoryNode" is created
        When the "Indexer" process analyzes the content
        Then it identifies key "Concepts" (e.g., "Recursion", "API_Call")
        And creates "ConceptNodes" if they don't exist
        And creates edges between the "MemoryNode" and "ConceptNodes" (Edge: USES)
        And calculates similarity with existing nodes to find "Duplicates"

    Scenario: Reuse - Retrieval Augmented Generation (RAG)
        Given a "Navigator" agent is planning a mission
        When it queries the Memory System with a "ProblemDescription"
        Then the system performs a "Hybrid Search" (Vector + Graph Traversal)
        And retrieves the top 5 most relevant "MemoryNodes"
        And excludes nodes marked as "DEPRECATED" or "HALLUCINATION"
        And formats the results into a "ContextBlock" for the agent

    Scenario: Improve - Evolution and Conflict Resolution
        Given an existing "MemoryNode" (Legacy Pattern)
        And a new "MemoryNode" (Gen 50 Pattern) that solves the same problem
        When the "Assimilator" detects a high "SemanticOverlap" (> 0.90)
        Then it compares the "PerformanceMetrics" (Speed, Cost, Quality)
        And if the new node is superior, it marks the old node as "OBSOLETE"
        And adds a "SUPERSEDES" edge from the New Node to the Old Node

    Scenario: Pruning - Forgetting Low-Value Knowledge
        Given a "MemoryNode" that has not been accessed in 50 generations
        And has a "UtilityScore" below the threshold
        When the "Gardener" process runs
        Then the node is moved to "ColdStorage" (Archive)
        And removed from the active "VectorIndex" to maintain query speed
