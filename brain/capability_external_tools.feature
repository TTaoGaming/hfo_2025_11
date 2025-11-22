Feature: External Tool Capabilities
  As the Swarmlord
  I want the Swarm to have access to external tools like Web Search and Calculation
  So that agents can verify information and perform complex logic beyond their internal training

  Scenario: Agent performs a web search
    Given an agent is in the "Execute" phase
    And the agent requires external information about "current AI trends"
    When the agent invokes the "search_web" tool
    Then the system should query an external search engine
    And return relevant search results to the agent

  Scenario: Agent performs a calculation
    Given an agent is in the "React" phase
    And the agent needs to calculate a value
    When the agent invokes the "calculator" tool with expression "123 * 456"
    Then the system should return the correct mathematical result "56088"

  Scenario: Agent uses Sequential Thinking with External Data
    Given an agent has retrieved search results
    When the agent invokes "sequential_thinking"
    Then the agent should be able to synthesize the external data into a coherent thought
