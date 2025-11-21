Feature: Level 1 SWARM Loop (Tactical)
    As the Swarmlord
    I want to coordinate a full SWARM workflow (Intent -> Watch -> Act -> Review -> Mutate)
    So that I can achieve high-confidence results through adversarial validation and evolutionary optimization

    # Lineage Note: SWARM is a composition of:
    # - D3A (Decide, Detect, Deliver, Assess) - Military Targeting Cycle
    # - Byzantine Fault Tolerance (Lamport) - Distributed Consensus
    # - MAP-Elites (Mouret/Clune) - Quality-Diversity Evolution

    Scenario: Execute the Full SWARM Cycle with Adversarial Mutation
        # 1. INTENT (Decide)
        Given the Swarmlord defines the "Mission Intent"
        And selects the "Search Space" for the evolutionary run

        # 2. WATCH (Detect)
        When the system "Watches" the environment for signals
        And gathers context from "Memory" (Stigmergic GraphRAG)
        And initializes "LangSmith" traces for observability

        # 3. ACT (Deliver)
        Then the swarm "Acts" using an "Orchestrated Map-Reduce Scatter-Gather" pattern
        And spawns a cohort of agents via "Ray"
        And includes at least "1+ Hidden Disruptor" agents (Red Team)
        And agents execute the "PREY Loop" (Perceive-React-Execute-Yield)

        # 4. REVIEW (Assess)
        And the system "Reviews" the agent outputs
        And applies a "Filter" to remove noise and malformed data
        And conducts an "Adversarial Byzantine Quorum" check
        And evaluates consensus based on:
            | Criteria       | Description                                      |
            | Confidence     | Statistical agreement among non-disruptors       |
            | Behavior       | Agent adherence to protocol and role consistency |
        And produces a "Readable and Usable Output" for the user

        # 5. MUTATE (Evolve)
        And the system "Mutates" the swarm configuration for the next cycle
        And exposes multiple "Knobs" for HFO to tune:
            | Knob              | Description                                      |
            | Temperature       | LLM creativity setting (0.0 - 1.0)               |
            | Model Selection   | Which "Cheap QD Swarm" models to use             |
            | Prompt Strategy   | DSPy signature optimization                      |
            | Voting Threshold  | Consensus requirement (e.g., 66%, 90%)           |
            | Disruptor Count   | Number of adversarial agents (1-N)               |
            | Mutation Rate     | Probability of genetic drift                     |
        And updates the "Quality-Diversity" archive (MAP-Elites)
