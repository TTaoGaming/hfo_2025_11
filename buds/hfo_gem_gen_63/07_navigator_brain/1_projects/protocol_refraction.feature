Feature: Protocol Refraction (The Codex)
  As the Swarmlord
  I want to refract Tacit Memory (Vectors) into Explicit Knowledge (Diataxis Files)
  So that the Hive Mind has a structured, visible library of wisdom.

  Background:
    Given the "Unified Memory" in LanceDB is active
    And the "Protocol Refraction" phase is initiated

  Scenario: Refracting a Source File
    Given a source file exists in memory (e.g., "buds/hfo_gem_gen_63/src/heartbeat_1181.py")
    When the Refractor Swarm processes this source
    Then the "Diataxis Architect" classifies it (e.g., "Reference")
    And the "Codex Scribe" generates a Markdown file in "memory/codex/reference/"
    And the file contains valid YAML Stigmergy Headers
    And the file traces back to the original Source ID

  Scenario: Swarm Roles
    The Refraction process must utilize the following roles:
    | Role | Responsibility |
    | Architect | Classify content into Diataxis Quadrants (Tutorial, How-To, Reference, Explanation) |
    | Scribe | Write the content in KCS format with YAML headers |
    | Auditor | Verify the output against the Schema |
