# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 461ff3be-fc98-42b3-84ff-0271679339ff
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:35.333793Z'
#     generation: 51
#   topos:
#     address: brain/capability_external_tools.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: capability_external_tools.feature
#
---
owner: Swarmlord
status: Implemented
title: Capability External Tools
type: Intent
---

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
