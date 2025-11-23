# # ==================================================================
# # 🤖 THE HEXAGON (System Generated)
# # ==================================================================
# hexagon:
#   ontos:
#     id: 1da90f27-8e7a-4083-80a7-83882fa202d8
#     type: feature
#     owner: Swarmlord
#   chronos:
#     status: active
#     urgency: 0.5
#     decay: 0.5
#     created: '2025-11-23T11:07:36.206451Z'
#     generation: 51
#   topos:
#     address: eyes/tools/INGESTION_SPEC.feature
#     links: []
#   telos:
#     viral_factor: 0.0
#     meme: INGESTION_SPEC.feature
#
Feature: Universal Knowledge Ingestion
  As a Hive Fleet Obsidian Orchestrator
  I want to ingest the entire workspace history into a centralized vector database
  So that I can retrieve past knowledge with strict confidence and hierarchy controls

  Rule: All ingested knowledge is treated as Epistemic Uncertainty (Max Confidence 90%)

  Scenario: Ingesting a standard historical code file
    Given a file exists at "hfo_gem/gen_10/agent.py"
    And the file size is less than 1MB
    And the file extension is valid (e.g., .py, .md, .txt)
    When the ingestion process runs
    Then the file content is chunked into 2000-character segments with 200 overlap
    And each chunk is embedded using "text-embedding-3-small"
    And the metadata "confidence" is strictly set to 0.9
    And the metadata "level" is set to "hfo_lvl0" (Single Agent / Unverified)
    And the metadata "generation" is extracted as 10
    And the metadata "original_timestamp" is preserved from the file system
    And the record is stored in the "knowledge_bank" table

  Scenario: Ingesting a Swarm or Consensus result
    Given a file exists at "hfo_crew_ai_swarm_results/2025-10-31/consensus.md"
    Or the file path contains "consensus" or "hfo_crew_ai"
    When the ingestion process runs
    Then the metadata "level" is upgraded to "hfo_lvl1" (Multi-Agent Consensus)
    And the metadata "confidence" remains capped at 0.9
    And the record is stored in the "knowledge_bank" table

  Scenario: Filtering Noise and Slop
    Given a file exists at "bin/executable.exe" (Binary)
    Or a file exists at "logs/massive_debug.log" (Log file)
    Or a file exists with size greater than 1MB
    When the ingestion process runs
    Then the file is completely ignored
    And no vectors are consumed

  Scenario: Idempotency and Deduplication
    Given a file at "hfo_gem/gen_1/readme.md" has already been ingested
    When the ingestion process runs again
    Then the file is skipped
    And no duplicate entries are created in the database
