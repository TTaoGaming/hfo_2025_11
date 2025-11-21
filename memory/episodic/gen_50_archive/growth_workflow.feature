Feature: The GROWTH Loop (Operational F3EAD)
  As the Swarm Architect
  I want to define the Level 2 Operational Loop (GROWTH)
  So that the system can execute targeted operations with military precision and adaptability.

  # Pattern: F3EAD (Find -> Fix -> Finish -> Exploit -> Analyze -> Disseminate)
  # HFO Twist: Stigmergic & Evolutionary.

  Scenario: The GROWTH Lifecycle
    Given a "Tactical Mission" (e.g., "Extract data from 100 URLs")

    # Phase 1: FIND (Targeting)
    When the Swarm enters the "Find" state
    Then it must "Identify Targets" (URLs, Files, API Endpoints)
    And it prioritizes them based on "Value" and "Risk"

    # Phase 2: FIX (Localization)
    When the Swarm enters the "Fix" state
    Then it must "Verify Targets" are accessible
    And it "Allocates Resources" (Agents, Tokens) to each target

    # Phase 3: FINISH (Action)
    When the Swarm enters the "Finish" state
    Then it spawns "Tactical Swarms" (Level 1) to execute the action (Scrape, Code, Attack)
    And it monitors for "Success/Failure" signals

    # Phase 4: EXPLOIT (Opportunity)
    When the Swarm enters the "Exploit" state
    Then it must "Analyze Immediate Results" for new leads
    And it recursively adds "New Targets" to the Find queue (Recursive Crawling)

    # Phase 5: ANALYZE (Intelligence)
    When the Swarm enters the "Analyze" state
    Then it must "Synthesize Data" into structured formats
    And it updates the "Knowledge Graph"

    # Phase 6: DISSEMINATE (Sharing)
    When the Swarm enters the "Disseminate" state
    Then it must "Publish Reports" to the Blackboard
    And it "Notifies" the Parent Holon (HIVE)
    And the Swarm terminates
