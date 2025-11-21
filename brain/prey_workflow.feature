Feature: The PREY Loop (Agent Cognitive Cycle)
  As the Swarm Architect
  I want every agent to follow the PREY Loop (Perceive, React, Execute, Yield)
  So that agent behavior is observable, modular, and capable of self-correction (OODA + Reflexion)

  # Core Philosophy: "Think before you Act. Reflect before you Yield."

  Scenario: The Perceive Phase (Input & Context)
    Given an agent receives a "Task"
    When the "Perceiver" activates
    Then it must ingest the "Task Description"
    And query "Short-Term Memory" (Context)
    And output a structured "Perception Object" (What do I see?)

  Scenario: The React Phase (Planning & Decision)
    Given a "Perception Object"
    When the "Reactor" activates
    Then it must formulate a "Plan of Action" (Tools, Steps)
    And check against "Safety Guardrails" (Carapace)
    And output a structured "Reaction Object" (What will I do?)

  Scenario: The Execute Phase (Action & Tooling)
    Given a "Reaction Object"
    When the "Executor" activates
    Then it must call the necessary "Tools" (Web, Code, File)
    And capture the "Raw Output"
    And output a structured "Execution Object" (What did I do?)

  Scenario: The Yield Phase (Reflexion & Output)
    Given an "Execution Object"
    When the "Yielder" activates
    Then it must perform a "Self-Audit" (Did I succeed?)
    And generate a "Confidence Score"
    And save a "Stigmergy Artifact" (Log)
    And return the "Final Result" to the Swarm
