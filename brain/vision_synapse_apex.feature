Feature: Synapse APEX Swarm (Network Stigmergy)

  Background:
    Given the Hive Fleet Obsidian (HFO) is an "Emergent Complex Adaptive System"
    And the goal is to implement "Network Stigmergy" with "Adversarial Byzantine Quorum"
    And the system must support "Co-evolutionary Immune System" with "Venom"

  Scenario: Artifact Storage Separation (The Memory Filter)
    Given a Swarm Agent generates a "Low-Level Artifact" (Raw Finding, Log, Intermediate Step)
    Then the artifact MUST be stored in **Postgres (pgvector)**
    And the artifact MUST NOT be stored on the Filesystem (to prevent noise)
    And a "Claim Check" signal MUST be sent via NATS

    Given a Swarm Agent generates a "High-Level Artifact" (Digest, Final Report, Strategic Insight)
    Then the artifact MUST be stored on the **Filesystem** (for Human Readability)
    And the artifact MUST ALSO be indexed in Postgres (for Machine Recall)

  Scenario: Cognitive Digest Evolution (SOTA Synthesis)
    Given the Swarmlord needs to synthesize a "Digest" from multiple inputs
    Then the synthesis format MUST adopt "Current Cognitive Research" (e.g., Global Workspace Theory, Attention Schema)
    And the digest MUST highlight "High Signals" and suppress "Noise"
    And the digest MUST provide an "Overview of the Entire Swarm" state

  Scenario: Synapse APEX Architecture
    Given the Swarm operates as a "Synapse APEX"
    Then "Synapses" (Agents) communicate via "Neurotransmitters" (NATS Signals)
    And "Neurons" (Compute Nodes) process information asynchronously
    And the "Immune System" (Immunizers) actively hunts for "Pathogens" (Hallucinations/Bad Data)
    And "Venom" (Disruptors) actively tests the system for fragility
