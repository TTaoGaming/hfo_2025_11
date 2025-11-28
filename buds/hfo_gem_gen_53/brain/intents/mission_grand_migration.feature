Feature: The Grand Migration Triad
  As the Overmind (Tommy)
  I want to migrate the wisdom, documentation, and data from Gen 52 to Gen 53
  So that we build the new "Bud" on a foundation of "Total Recall" without "Technical Debt"

  Background:
    Given the "Gen 52" system is brittle but functional
    And the "NATS JetStream" is active for Stigmergy
    And the "PGVector" database is ready for embeddings

  Scenario: Phase 1 - The Digest Swarm (Wisdom)
    Given a swarm of 50 agents
    When they scan the "body/infrastructure_*.py" files
    Then they should extract "Design Patterns" and "Lessons Learned"
    And they should synthesize a "Swarmlord Digest" in "buds/hfo_gem_gen_53/memory/library/reference/"

  Scenario: Phase 2 - The Librarian Swarm (Docs)
    Given the Digest is complete
    When the swarm scans the "brain/intents/" folder
    Then they should convert Gherkin Features into "Diátaxis Explanations"
    And save them to "buds/hfo_gem_gen_53/memory/library/explanation/"

  Scenario: Phase 3 - The Archaeologist Swarm (Data)
    Given the Docs are complete
    When the swarm scans the "memory/episodic/" folder
    Then they should "Vectorize" the content
    And insert it into the "Gen 53 Knowledge Graph" (Postgres)
