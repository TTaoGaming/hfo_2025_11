Feature: Claim Check Pattern (Rich Stigmergy)

  Background:
    Given the Hive Fleet Obsidian architecture
    And the requirement for "Hexagonal Composability"
    And the requirement for "Complete Decoupling" via NATS JetStream

  Scenario: Decoupling Large Payloads via Claim Check
    Given a Producer Agent (e.g., Shaper) has generated a "Heavy Artifact" (e.g., >1MB Markdown/JSON)
    When the Producer publishes a signal to NATS
    Then the signal payload MUST NOT contain the full artifact content
    And the signal payload MUST contain a "Claim Check" (Pointer/URL/ID) to the artifact
    And the signal payload MUST contain "Rich Metadata" (ID, Role, Tags, Confidence, Summary)
    And the Artifact MUST be persisted to **Postgres (pgvector)** BEFORE the signal is published
    And High-Level Digests MAY be persisted to Filesystem for human readability

  Scenario: Consumer Processing via Claim Check
    Given a Consumer Agent (e.g., Reviewer) subscribes to a NATS subject
    When the Consumer receives a "Rich Signal"
    Then the Consumer CAN decide to process or ignore based on Metadata alone (without reading the artifact)
    And if the Consumer decides to process, it MUST use the "Claim Check" to retrieve the full artifact from Postgres
    And the Consumer MUST handle "Artifact Not Found" errors gracefully (Eventual Consistency)

  Scenario: Hexagonal Composability of Swarm Stages
    Given the SWARM Loop (Set -> Watch -> Act -> Review -> Mutate)
    Then each stage MUST be an independent "Island of Computation"
    And each stage MUST communicate with the next ONLY via NATS Signals (Claim Checks)
    And no stage shall share in-memory state with another stage
    And the "Act" phase MUST be completely decoupled from the "Review" phase

  Scenario: Rich Stigmergy Metadata Standard
    Given a Stigmergy Signal
    Then it MUST adhere to the following schema:
      | Field        | Type   | Description                                      |
      | id           | UUID   | Unique Task/Artifact ID                          |
      | role         | String | The role that produced it (e.g., Shaper)         |
      | mission_slug | String | The mission context                              |
      | round        | Int    | The iteration round                              |
      | location     | Dict   | The Claim Check (type, path, url)                |
      | tags         | List   | Semantic tags for filtering                      |
      | summary      | String | Short blurb (<200 chars) for quick decisioning   |
      | checksum     | String | SHA256 hash for integrity verification           |
