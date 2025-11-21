Feature: HFO Trust Engine (Cognitive Exoskeleton)
  As the Overmind (User)
  I want a Co-evolutionary Adversarial Byzantine Quorum system
  So that I can trust the output of unreliable LLM agents

  Background:
    Given the R.A.P.T.O.R. stack is active
    And the "Hybrid Stability Protocol" is enforcing Pydantic constraints

  Scenario: Holonic Byzantine Quorum (3f+1)
    Given a mission "Critical Intelligence Analysis"
    And the Swarm size is N=10
    And the system tolerates f=3 traitors (N >= 3f + 1)
    When the Orchestrator spawns a Squad of 10 agents
    And the number of Disruptors is randomized between 1 and 3 (Hidden from Squad)
    And the Disruptors use "MITRE ATT&CK" playbooks to deceive
    And the Squad executes the task
    And a parallel Squad of 10 Reviewers critiques the outputs
    Then the Synthesizer should identify the "Consensus Cluster" of size >= 7
    And the Synthesizer should flag the outliers as "Suspected Disruptors"
    And the Immunizer should generate a patch for the "Attack Vector" used

  Scenario: Adversarial Hardening (Red Teaming)
    Given a proposed plan "Deploy to Production"
    When the Disruptor agent attacks the plan with "Security Flaws"
    And the Immunizer agent defends the plan with "Patches"
    Then the final plan should be robust against the identified flaws
    And the system should log the "Attack Vector" to Memory

  Scenario: Co-evolutionary Optimization (The Forge)
    Given a population of agent prompts in the MAP-Elites archive
    When the Swarm executes a cycle
    And the system evaluates "Performance" (Success Rate) vs "Novelty" (Strategy)
    Then the system should mutate the underperforming prompts
    And the next generation of agents should have higher trust scores

  Scenario: Confidence Weighting (Uncertainty Quantification)
    Given an agent produces a result
    When the result is validated against the Pydantic Schema
    And the agent assigns a confidence score "C" (0.0 to 1.0)
    Then the Synthesizer should weight the vote by "C"
    And results with "C < Threshold" should be discarded as noise
