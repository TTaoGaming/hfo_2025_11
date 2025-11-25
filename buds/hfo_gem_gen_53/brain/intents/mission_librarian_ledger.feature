Feature: The Librarian Swarm (Ledger-Based)
  As the Overmind (Tommy)
  I want to migrate the legacy repo using a "Ledger" to track state
  So that I can process the entire history without hitting Context Limits

  Background:
    Given the "Migration Ledger" exists at "buds/hfo_gem_gen_53/migration_ledger.json"
    And the "Literate Spec Standard" is defined

  Scenario: Initialize Ledger
    Given the legacy folders "brain/", "body/", "memory/"
    When I run the "Ledger Initializer"
    Then it should list all files with status "PENDING"
    And it should group files by "Cluster" (e.g., Infrastructure, Biology, Strategy)

  Scenario: The Librarian Loop (3-Round)
    Given a cluster of "PENDING" files (e.g., "Stigmergy")
    When the Librarian Swarm activates
    Then Round 1: "Scan" the files for Keywords, Conflicts, and Evolution
    And Round 2: "Critique" the findings for "High Abstraction" and "Obsidian Alignment"
    And Round 3: "Refine" into a "Swarmlord Digest" (BLUF, Matrix, Map, Intent Options)
    And the Digest should present "Conflicting Opinions" as "Strategic Choices" for the Overmind
    And the Ledger should be updated to "MIGRATED"
