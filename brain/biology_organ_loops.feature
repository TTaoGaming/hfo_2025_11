Feature: Physiology Loops
  As the Swarmlord
  I want to define the physiological rhythms of the Hive
  So that different organs operate at appropriate speeds.

  Scenario: Reflex Loop (Fast)
    Given a "Ganglia" (Nerves) component
    When a "Danger Signal" is received
    Then it should react within milliseconds (Reflex)
    And it should bypass the "Cortex" (Brain).

  Scenario: Cognitive Loop (Slow)
    Given the "Cortex" (Brain)
    When a "Strategic Decision" is needed
    Then it should deliberate (Reasoning)
    And it should take seconds or minutes.

  Scenario: Immune Loop (Background)
    Given the "Carapace" (Immune System)
    When the system is idle
    Then it should scan for "Pathogens" (Errors/Slop)
    And it should "Neutralize" them.
