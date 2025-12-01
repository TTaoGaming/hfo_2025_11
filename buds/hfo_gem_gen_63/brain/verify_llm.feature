Feature: Intelligence Verification
  As the Swarmlord
  I want to verify the OpenRouter LLM connection
  So that the Obsidian Spider can think and reason

  Scenario: Ask a Question
    Given the OpenRouter API key is configured
    When I send a "Hello, who are you?" prompt to the model
    Then I should receive a coherent text response
    And the response should not be empty
