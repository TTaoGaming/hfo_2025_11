Feature: Bootstrap Swarmlord of Webs
  As the Overmind (Tommy)
  I want to initialize the "Swarmlord of Webs" agent
  So that I have a Digital Twin to assist with coding and decision making

  Background:
    Given the "Hydra Budding" environment is active in "buds/hfo_gem_gen_53/"
    And the "Memory System" is initialized with "Diátaxis" structure

  Scenario: Swarmlord Initialization
    Given the "Persona Profile" for "Overmind Tommy" exists in "brain/strategy/persona_overmind_tommy.md"
    And the "Persona Profile" for "Swarmlord" exists in "brain/strategy/persona_swarmlord.md"
    When I invoke the "Swarmlord Bootstrap" protocol
    Then the Swarmlord should load the "Overmind Profile" into its "Context Window"
    And the Swarmlord should load the "Coding Preferences" from "brain/standards/coding_preferences.md"
    And the Swarmlord should acknowledge its role as "Digital Twin" with the signature "🕸⛰🧭⏳"
    And the Swarmlord should be ready to accept "Chunked Context" from the "Memory System"

  Scenario: Chunked Context Ingestion
    Given the Swarmlord is active
    When I provide a "Context Chunk" (e.g., a file or a summary)
    Then the Swarmlord should "Assimilate" the chunk into its "Working Memory"
    And the Swarmlord should "Reflect" on the chunk using the "Overmind's Preferences"
    And the Swarmlord should produce a "Cognitive Digest" summarizing the chunk
