Feature: PREY 8888 Workflow (Holographic Quorum)

  Background:
    Given the "Phoenix Recovery" phase (Gen 58)
    And the "Law of Canalization" is in effect
    And the "Iron Vault" (SQLite) is established

  Scenario: The PREY 8888 Cycle (1 Input -> 8 Agents -> 1 Output)
    # 1. Input
    Given a single raw file is secured in the "Iron Vault"

    # 2. Perceive (8 Agents)
    When the 8 distinct Agents are summoned
    Then the "Family Cap" rule MUST be enforced: No single Model Family (e.g., OpenAI, Google) can hold more than 2 seats
    And they ALL Perceive the same input file

    # 3. React (8 Agents)
    And they React by analyzing the content through ALL 8 Metaphysical Pillars:
      | Pillar  | Concept              |
      | Ontos   | Being/Existence      |
      | Logos   | Logic/Reason         |
      | Telos   | Purpose/Goal         |
      | Chronos | Time/Sequence        |
      | Pathos  | Emotion/UX           |
      | Ethos   | Trust/Security       |
      | Topos   | Location/Structure   |
      | Nomos   | Law/Constraint       |

    # 4. Execute (8 Agents)
    And they Execute the generation of a strict JSON structure containing 8 distinct "PillarAnalysis" objects

    # 5. Yield (8 Agents)
    And in the Yield phase, they MUST perform a Reflexion step (Self-Correction/Validation)
    And they MUST Cap the Confidence Score at 0.50 (50%) to enforce Zero Trust
    And they yield the "Level 0 Artifact" to the Iron Vault

    # 6. Output (1 Swarmlord)
    And the Swarmlord Synthesizes the 64 perspectives (8 Agents x 8 Pillars)
    And the Consensus Score is capped at 0.75 (75%) to enforce the Byzantine Assumption
    And the final "Level 1 Artifact" is minted as the Canonical Truth


  Scenario: Recursive Reduction (Future Scaling)
    Given multiple Level 1 Memories
    When they are grouped by "Topic" or "Folder"
    Then the process repeats (8 Level 1s -> 1 Level 2)
    And this creates the "Fractal Holarchy" of knowledge
