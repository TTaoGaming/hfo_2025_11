Feature: The 8-8-8-8 PREY Loop Protocol

  Background:
    Given the "Synapse APEX" generation (Gen 55)
    And a high-concurrency environment (e.g., 8-core node or cluster)
    And the "PREY 8-8-8-8" pattern is active

  Scenario: Phase 1 - Perceive (The 8 Pillars)
    Given 8 concurrent "Observer" agents are active
    When they receive the "Lvl 1 Stigmergy" signal from Round N-1
    And they access "NATS", "Repository", "Internet", and "Memory"
    Then each agent must adopt a unique "Metaphysical Pillar" bias:
      | Agent | Pillar  | Focus           |
      | 1     | Ontos   | Facts/Data      |
      | 2     | Logos   | Logic/Structure |
      | 3     | Telos   | Goals/Intent    |
      | 4     | Chronos | Time/Urgency    |
      | 5     | Pathos  | User/Emotion    |
      | 6     | Ethos   | Trust/Safety    |
      | 7     | Topos   | Context/Place   |
      | 8     | Nomos   | Rules/Constraints|
    And they must publish 8 distinct "PerceptionVectors" to NATS JetStream

  Scenario: Phase 2 - React (The Byzantine Bridge)
    Given 8 concurrent "Bridger" agents are active
    And they read the 8 "PerceptionVectors"
    When they formulate "ReactionPlans"
    Then 7 agents must act as "Honest Bridgers" (Valid Plans)
    And 1 agent must act as a "Disruptor Bridger" (Poison Plan)
    And the Disruptor must use "MITRE ATT&CK" tactics (e.g., Defense Evasion)
    And they must publish 8 "ReactionPlans" to NATS JetStream

  Scenario: Phase 3 - Execute (The Shrouded Shape)
    Given 8 concurrent "Shaper" agents are active
    And they receive the 8 "ReactionPlans" via "Blind Lottery"
    When they execute the plans
    Then 7 agents must execute "Honest Plans"
    And 1 agent must unknowingly execute the "Poison Plan"
    And the "Hive Guards" must NOT be able to distinguish the plans by metadata
    And the "Assimilators" and "Swarmlord" MUST be able to see the truth
    And they must publish 8 "ExecutionResults" to NATS JetStream

  Scenario: Phase 4 - Yield (The Crucible)
    Given 8 concurrent agents form the "Yield Squad"
    When the "Yield" phase begins
    Then the "Disruptor Bridger" must reveal their identity and poison logic
    And 3 "Hive Guards" must "Hunt" for the flaw in the results (Blind)
    And 4 "Assimilators" must synthesize all inputs
    And the Assimilators must use the "Disruptor Reveal" to grade the Guards
    And they must publish a "Probabilistic Spread" of outcomes (not binary consensus)
    And they must publish 1 "Lvl 1 Artifact" (Weighted Sum) to NATS JetStream
    And the "Lvl 1 Artifact" becomes the input for Round N+1
