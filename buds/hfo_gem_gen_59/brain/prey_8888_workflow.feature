Feature: PREY 8888 Recursive Reduction Workflow
  As the Swarmlord
  I want to execute the PREY 8888 workflow
  So that I can ingest a single file using a Byzantine Quorum of 8 agents and synthesize a high-confidence Level 1 artifact

  Background:
    Given the HFO Gem Gen 59 environment is active
    And the "PREY 8888" protocol is loaded
    And the "Memory Confidence Protocol" is active

  Scenario: Execute PREY 8888 on a single file
    Given I have a target file "input_document.md"
    When I initiate the PREY 8888 workflow
    Then the system should spawn 8 independent "PREY" agents
    And each PREY agent should execute the "Perceive" phase on "input_document.md"
    And each PREY agent should execute the "React" phase to plan 8 OBSIDIAN stigmergy artifacts
    And each PREY agent should execute the "Execute" phase to create an HFO Level 0 artifact
    And each PREY agent should execute the "Yield" phase with self-reflection
    And the system should collect 8 HFO Level 0 artifacts
    And the "Synthesizer" agent should ingest the 8 Level 0 artifacts
    And the Synthesizer should perform a Byzantine Quorum check
    And the Synthesizer should produce exactly 1 HFO Level 1 artifact
    And the Level 1 artifact should contain the synthesized wisdom of the 8 agents

  Scenario: Recursive Reduction Logic
    Given 8 HFO Level 0 artifacts are available
    When the Synthesizer performs recursive reduction
    Then it should analyze ALL 8 artifacts without discarding outliers
    And it should identify areas of Consensus where agents agree
    And it should identify Outliers where agents diverge
    And it should calculate the Consensus Percentage
    And if Consensus is greater than 75% (6/8 agents), it should mark the artifact as "High Confidence"
    And if Consensus is less than 75%, it should flag the artifact as "Contested" but preserve the data
    And the final Level 1 artifact must explicitly state the Consensus Percentage

  Scenario: Stigmergy Artifact Generation
    Given an agent is in the "Execute" phase
    When it creates an HFO Level 0 artifact
    Then the artifact should be tagged with "HFO_Lvl0"
    And the artifact should contain a "Stigmergy_Header"
    And the artifact should be persisted to the "Hot Stigmergy" stream
