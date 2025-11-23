Feature: Holonic Knowledge Leveling

  As the Swarmlord
  I want to assign Levels (0-3) and Attributes (STR, WIS, CHA) to all Knowledge Artifacts
  So that I can filter Truth from Noise based on Consensus and Durability

  Background:
    Given the Leveling Table is defined as:
      | Level | Name    | Agents | Trust | Storage   |
      | 0     | Spark   | 1      | 0.1   | NATS      |
      | 1     | Ember   | 10     | 0.5   | File      |
      | 2     | Flame   | 100    | 0.8   | VectorDB  |
      | 3     | Inferno | 1000   | 0.99  | GraphDB   |

  Scenario: Level Up from Spark to Ember
    Given a "Spark" artifact exists in NATS with:
      | attribute | value |
      | WIS       | 1     |
      | content   | "Sky is Green" |
    When a Squad of 10 Agents reviews the artifact
    And 9 Agents vote "Reject"
    Then the artifact fails to Level Up
    And the artifact is extinguished (Deleted)

  Scenario: Level Up from Ember to Flame
    Given an "Ember" artifact exists in Filesystem with:
      | attribute | value |
      | WIS       | 10    |
      | content   | "Sky is Blue" |
    When a Platoon of 100 Agents reviews the artifact
    And 85 Agents vote "Accept"
    Then the artifact Levels Up to "Flame"
    And the artifact is written to "VectorDB"
    And the Trust Score increases to 0.8

  Scenario: Attribute Check for Query Routing
    Given a User asks "What is the established truth?"
    When the Query Router filters artifacts
    Then only artifacts with "Level >= 2" are returned
    And artifacts with "STR < 0.5" (Decayed) are excluded
