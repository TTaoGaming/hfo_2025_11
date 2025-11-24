# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 06fa3b97-4499-47df-bb28-c04d55f924b6
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-24T14:30:05.773791Z'
#     generation: 51
#   topos:
#     address: brain/hfo_mcp.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: hfo_mcp.feature
#

# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 88f91e68-c114-43fb-b39a-e52aa5ab9a9f
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.8
#     decay: 0.5
#     created: '2025-11-23T12:05:00+00:00'
#     generation: 52
#   topos:
#     address: brain/hfo_mcp.feature
#     links:
#     - brain/design_hfo_mcp.md
#   telos:
#     viral_factor: 0.0
#     meme: hfo_mcp
# # ==================================================================

Feature: HFO Model Context Protocol (MCP)
  As a Swarmlord (System Architect)
  I want to decouple Agent Logic from Tool Execution using MCP
  So that the Hive can scale, interoperate, and evolve independently.

  Background:
    Given the HFO-MCP Server is running
    And the HFO-MCP Server exposes the "Obsidian Standard Library"
    And a PreyAgent is initialized with an MCP Client

  Scenario: Agent Discovers Available Tools
    When the PreyAgent connects to the MCP Server
    And the PreyAgent requests "list_tools"
    Then the MCP Server should return a list containing:
      | tool_name        | description                          |
      | obsidian_fs_read | Read a file from the hive filesystem |
      | obsidian_net_search | Search the web for information    |
      | obsidian_hive_signal | Publish a stigmergic signal      |

  Scenario: Agent Executes a File Read Tool
    Given the file "test_mcp.txt" exists with content "Hello MCP"
    When the PreyAgent executes "obsidian_fs_read" with arguments:
      | key  | value          |
      | path | ./test_mcp.txt |
    Then the MCP Server should return "Hello MCP"
    And the Audit Log should record the tool execution

  Scenario: Agent Handles Tool Error Gracefully
    When the PreyAgent executes "obsidian_fs_read" with arguments:
      | key  | value                |
      | path | ./non_existent_file.txt |
    Then the MCP Server should return an error
    And the PreyAgent should receive a "ToolError" signal
    And the PreyAgent should NOT crash

  Scenario: Agent Publishes Stigmergic Signal via MCP
    When the PreyAgent executes "obsidian_hive_signal" with arguments:
      | key     | value           |
      | channel | swarm.test      |
      | message | Hello from MCP  |
    Then the NATS stream "swarm" should contain the message "Hello from MCP"
    And the Assimilator should perceive the signal

  Scenario: Remote Agent Connects via SSE (Hybrid Protocol)
    Given the HFO-MCP Server is running in "SSE Mode" on port 8080
    When a Remote PreyAgent connects to "http://localhost:8080/sse"
    Then the connection should be established
    And the Remote PreyAgent should be able to list tools
