Feature: HFO Trust Engine (Cognitive Exoskeleton)
  As the Overmind (User)
  I want a Co-evolutionary Adversarial Byzantine Quorum system
  So that I can trust the output of unreliable LLM agents

  Background:
    Given the R.A.P.T.O.R. stack is active
    And the "Hybrid Stability Protocol" is enforcing Pydantic constraints

  Scenario: Byzantine Quorum Consensus
    Given a mission "Solve Complex Math Problem"
    When the Swarm spawns 5 agents
      | Role       | Type      | Count |
      | Mathematician | Honest    | 3     |
      | YesMan        | Sycophant | 1     |
      | ChaosMonkey   | Saboteur  | 1     |
    And they execute the task in parallel via Ray
    And the Synthesizer filters results with confidence < 0.5
    Then the final consensus should exclude the Saboteur's output
    And the confidence score should reflect the quorum agreement (Weighted Vote)

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
