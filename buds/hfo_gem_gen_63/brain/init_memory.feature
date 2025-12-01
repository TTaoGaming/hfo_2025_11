Feature: Cold Stigmergy Initialization
  As the Swarmlord
  I want to initialize the persistent memory systems (SQLite and LanceDB)
  So that the Obsidian Spider has a place to store long-term knowledge

  Scenario: Initialize Iron Ledger (SQLite)
    Given the SQLite database path is configured
    When I run the initialization script
    Then the database file should be created
    And the "holons" table should exist

  Scenario: Initialize Vector Mirror (LanceDB)
    Given the LanceDB path is configured
    When I run the initialization script
    Then the LanceDB directory should be created
    And the "memories" table should be accessible
