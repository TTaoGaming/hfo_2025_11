# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: d3e1ceea-c5ac-428a-8477-5f2292274db7
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:06:41.134353Z'
#     generation: 51
#   topos:
#     address: memory/episodic/gen_50_archive/obsidian_hourglass.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: obsidian_hourglass.feature
#
Feature: The Obsidian Hourglass (Anytime Algorithm)
    As the Swarmlord (Navigator)
    I want to use the Obsidian Hourglass logic
    So that I can flip between Past Precedents and Future Simulations to solve the Present

    # Core Concept: The "Flip"
    # The Swarmlord stands at the "Neck" of the Hourglass (The Present).
    # It looks UP to the Past (Karmic Web) for patterns.
    # It looks DOWN to the Future (Simulation Web) for risks.
    # It decides based on the "Anytime" constraint (Time/Budget).

    Scenario: Phase 1 - The Past Bulb (Retrieval)
        Given a "Mission Intent" is received
        When the Swarmlord queries the "Karmic Web" (GraphRAG)
        Then it retrieves "Precedents" using "Case-Based Reasoning"
        And sorts them via "Cynefin Framework" (Simple, Complicated, Complex, Chaotic)
        And if a "High Confidence" match is found (> 0.9), it skips to Execution

    Scenario: Phase 2 - The Future Bulb (Simulation)
        Given no "High Confidence" precedent exists (Novelty)
        When the Swarmlord triggers the "Simulation Web"
        Then it spawns "Monte Carlo Tree Search" (MCTS) branches
        And uses "Thompson Sampling" to explore potential outcomes
        And calculates "Tail Risk" and "Success Probability" for each path

    Scenario: Phase 3 - The Neck (The Flip)
        Given inputs from the "Past" (Precedents) and "Future" (Simulations)
        When the "Anytime Constraint" is reached (Time limit or Budget limit)
        Then the Swarmlord selects the "Best Path Distribution"
        And issues "Stigmergic Orders" to the Swarm (L1)
        And logs the decision to the "Blackboard" for future learning
