# 🧠 HYDRA Memory Architecture: The IronLedger & The Lance
# ==============================================================================
# Authority: Swarmlord
# Generation: 59
# Status: Active
# Philosophy: "The Log is Truth, The Vector is a View."
# ==============================================================================

@memory @hydra @critical
Feature: HYDRA Memory System (SQLite + LanceDB)
  As the Swarmlord
  I want a memory system where the relational log (SQLite) is the eternal truth and the vector store (LanceDB) is a disposable, regenerative view
  So that the system is Anti-Fragile, Self-Healing, and capable of total regeneration from a single file.

  Background:
    Given the "IronLedger" is a local SQLite database at "memory/hfo_gen_59_memory.db"
    And the "VectorMirror" is a serverless LanceDB dataset at "memory/lancedb"
    And the "EmbeddingMotor" is configured to use SOTA model "openai/text-embedding-3-large"
    And the "SyncProtocol" is set to "Eventual Consistency" (The Assimilator Loop)

  # ============================================================================
  # 🟢 Rule 1: The Write Path (Canalization)
  # Agents NEVER write to VectorDB directly. They only scribe to the IronLedger.
  # ============================================================================
  Rule: Agents must write only to the IronLedger

    Scenario: Agent Ingests New Knowledge
      Given a PREY Agent has synthesized a "Level 1 Artifact" (Quorum Truth)
      When the Agent commits the artifact
      Then the artifact is inserted into the "level1_artifacts" table in SQLite
      And the "vectorized" flag is set to FALSE
      And the Agent receives a success confirmation immediately
      And NO interaction occurs with LanceDB at this stage

  # ============================================================================
  # 🟡 Rule 2: The Sync Path (Assimilation)
  # The Assimilator (Hydra Head) is responsible for the heavy lifting of embedding.
  # ============================================================================
  Rule: The Assimilator syncs the Log to the View

    Scenario: Assimilator Processes Pending Artifacts
      Given the Assimilator wakes up (Cron or Event)
      When it queries SQLite for rows where "vectorized" is FALSE
      Then it retrieves the text content of the Artifact
      And it sends the text to the "EmbeddingMotor" (OpenAI API)
      And it receives a 3072-dimensional vector
      And it upserts the {id, vector, metadata} into LanceDB
      And it updates the SQLite row setting "vectorized" to TRUE
      And it logs the sync operation

  # ============================================================================
  # 🔴 Rule 3: The Healing Path (Regeneration)
  # If the VectorDB is corrupted or deleted, it can be rebuilt 100% from SQLite.
  # ============================================================================
  Rule: The VectorDB is disposable and regenerative

    Scenario: Total Vector Amnesia (Disaster Recovery)
      Given the "memory/lancedb" folder has been deleted (Accident or Attack)
      When the "Phoenix Protocol" (Regeneration Script) is initiated
      Then the system connects to the IronLedger (SQLite)
      And it resets all "vectorized" flags to FALSE in "level1_artifacts"
      And it triggers the Assimilator to process ALL rows
      And the LanceDB is rebuilt exactly as it was
      And the system returns to "Green" status without data loss

  # ============================================================================
  # 🔵 Rule 4: The Query Path (Retrieval)
  # Search hits the VectorDB for IDs, then hydrates from SQLite for Context.
  # ============================================================================
  Rule: Retrieval is a Hybrid Operation

    Scenario: Agent Queries for Context
      Given an Agent asks "What is the Swarmlord Protocol?"
      When the query is embedded via the "EmbeddingMotor"
      And the vector is sent to LanceDB for "Nearest Neighbor Search" (ANN)
      Then LanceDB returns a list of {id, distance}
      And the system queries SQLite "level1_artifacts" using these IDs
      And the full text content is returned to the Agent
