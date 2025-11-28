@gen55 @workflow @canonical
Feature: The HFO Swarm Workflow (Fractal Funnel)
  As the Swarmlord
  I want a recursive 1-8-64-8-1 workflow
  So that I can ingest massive data with high fidelity and reduce hallucination via adversarial consensus

  Background:
    Given the context is "Gen 55 (The Gem)"
    And the pattern is "1-8-64-8-1" (Powers of 8)

  Scenario: The 5-Phase Fractal Funnel
    The workflow must follow the Set-Watch-Act-Review-Mutate cycle.

    Given a high-level "Intent" (e.g., "Ingest Gen 50")

    # Phase 1: Set (Orchestrate)
    When the "Swarmlord" (1 Agent) executes "Set"
    Then it shall scan the target domain
    And it shall partition the work into 8 "Sectors"
    And it shall produce 8 "Mission Manifests"

    # Phase 2: Watch (Observe)
    When the 8 "Observers" (8 Agents) execute "Watch"
    Then each Observer shall monitor its assigned Sector
    And each Observer shall subdivide the Sector into 8 "Squad Tasks"
    And they shall produce 64 "Task Tickets"

    # Phase 3: Act (Swarm)
    When the 64 "Shapers" (64 Agents) execute "Act"
    Then 56 "Honest Shapers" shall execute the work faithfully
    And 8 "Hidden Disruptors" shall inject subtle errors (Venom)
    And they shall produce 64 "Raw Artifacts" (Mixed Honest/Poisoned)

    # Phase 4: Review (Consensus)
    When the 8 "Review Squads" (8 Agents) execute "Review"
    Then each Squad shall consist of 3 Immunizers, 1 Disruptor Leader, and 4 Assimilators
    And the "Immunizers" shall flag potential venom
    And the "Disruptor Leader" shall reveal the hidden poison
    And the "Assimilators" shall form a Byzantine Quorum (>75% agreement)
    And they shall produce 8 "Sector Reports" (Refined) and 1 "Adversarial Audit Log"

    # Phase 5: Mutate (Evolve)
    When the "Swarmlord" (1 Agent) executes "Mutate"
    Then it shall compare the Sector Reports against the Original Intent
    And it shall evaluate the "Health Score" from the Audit Log
    And it shall update the "Immunizer Blocklists" and "Disruptor Playbooks"
    And it shall produce 1 "Final Result" or trigger a "Mutation" (Next Round)

  Scenario: The Iterative Reduction Loop
    The workflow must run in 3 rounds to distill truth.

    Given the workflow is active
    Then "Round 1" shall be "Ingest" (Focus on Quantity)
    And "Round 2" shall be "Refine" (Focus on Quality/Filtering)
    And "Round 3" shall be "Synthesize" (Focus on Insight/Connecting Dots)
