Feature: Level 1 SWARM Loop (Tactical)
    As the Swarmlord
    I want to coordinate a 10-agent Byzantine swarm
    So that I can achieve high-confidence results through adversarial validation

    # Lineage Note: SWARM is a composition of:
    # - D3A (Decide, Detect, Deliver, Assess) - Military Targeting Cycle
    # - Byzantine Fault Tolerance (Lamport) - Distributed Consensus
    # - MAP-Elites (Mouret/Clune) - Quality-Diversity Evolution

    Scenario: Execute a SWARM cycle with adversarial review
        Given a mission intent "Solve a complex reasoning task"
        And a swarm size of 10 agents
        And selects "Cheap Navigators" for coordination
        And selects "Cheap QD Swarm" for execution
        And excludes "Gemini 3 Pro" from swarm operations

        # S - Set (Decide)
        When the Swarmlord "Sets" the mission parameters
        And defines the "Search Space" for evolution
        And establishes "Constraints" (Time, Budget, Safety)

        # W - Watch (Detect)
        And the system "Watches" for stigmergy signals via "NATS JetStream"
        And initializes "LangSmith" traces for observability

        # A - Act (Deliver)
        And the swarm "Acts" using a "Scatter-Gather" pattern
        And spawns 10 agents (including 1-3 "Disruptors") to execute the "PREY Loop"
        And agents communicate via "Virtual Stigmergy"

        # R - Review (Assess)
        And the system "Reviews" the results via "Byzantine Quorum"
        And "Immunizer" agents (Blue Team) attempt to detect the disruptors
        And the consensus confidence is capped at 90% (Persistent Green is a Code Smell)

        # M - Mutate (Evolve)
        And the system "Mutates" the "DSPy" prompts and swarm parameters using "MAP-Elites"
        And updates the "Quality-Diversity" archive
        And evolves the entire swarm strategy for the next cycle
