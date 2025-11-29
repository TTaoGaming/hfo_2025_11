Feature: Memory Confidence Protocol (HFO Leveling)
  As the Swarmlord
  I want to enforce strict confidence caps on HFO artifacts
  So that I can prevent hallucinations and ensure epistemic humility

  Background:
    Given the HFO Gem Gen 59 environment is active
    And the "Memory Confidence Protocol" is enforced

  Scenario: Level 0 Confidence Capping
    Given an agent has generated an internal confidence score of <internal_score>
    When the agent produces an HFO Level 0 artifact
    Then the artifact's final confidence score should be <final_score>
    And the confidence should never exceed 50%

    Examples:
      | internal_score | final_score |
      | 100%           | 50%         |
      | 80%            | 40%         |
      | 50%            | 25%         |
      | 0%             | 0%          |

  Scenario: Level 1 Confidence Capping
    Given the Synthesizer has generated an internal confidence score of <internal_score>
    When the Synthesizer produces an HFO Level 1 artifact
    Then the artifact's final confidence score should be <final_score>
    And the confidence should never exceed 75%

    Examples:
      | internal_score | final_score |
      | 100%           | 75%         |
      | 80%            | 60%         |
      | 50%            | 37.5%       |

  Scenario: Hallucination Detection
    Given an artifact is presented to the memory system
    When the artifact has a confidence score greater than 75%
    Then the system should flag the artifact as "Hallucination"
    And the system should reject the artifact
    And the system should log a "Confidence Violation Error"
