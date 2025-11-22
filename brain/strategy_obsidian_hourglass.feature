Feature: Obsidian Horizon Hourglass (Geometric Spatial State-Action Model)
  # Domain: Strategy
  # Owner: Swarmlord
  # Type: Geometric Model

  As the Swarmlord (Navigator)
  I want to manipulate the Z-Axis (Time) of the State-Action Space
  So that I can wield power over the Past, Present, and Future to enact intent.

  Rule: The Swarm exists in the "Neck" (Z=0) and is subject to Temporal Gravity.

    Scenario: Gravity Flow (Past -> Present)
      Given the Swarm is operating in the "Neck" (Z=0)
      And the "Karmic Web" (Z<0) contains "All Human History" and "Biological Patterns"
      When the "Gravity" of historical precedents exerts force
      Then the Swarm MUST retrieve the "Nearest Neighbor" patterns from GraphRAG
      And the Swarm MUST execute the "Swarm Web" action aligned with those patterns.

    Scenario: The Flip (Future -> Present)
      Given the Swarm detects "High Uncertainty" or "Tail Risk" in the Neck
      When the Swarmlord triggers the "Horizon Event" (The Flip)
      Then the Swarm MUST freeze the "Neck" (Pause Execution)
      And the Swarm MUST project 1000+ paths into the "Simulation Web" (Z>0)
      And the Swarm MUST perform "Retro-Analysis" on these simulated futures
      And the Swarm MUST collapse the "Wavefunction" to a "MAP-Elites Probabilistic Distribution"
      And the Swarm MUST invert causality to execute the "Golden Path" in the Present.

    Scenario: Endless Compute (Anytime Algorithm)
      Given the "Simulation Web" is active
      When the Swarm has available compute resources
      Then the system MUST "Endlessly Eat Compute" to refine the probability distribution
      And the system MUST be able to yield the "Best Current Map" at any millisecond.
