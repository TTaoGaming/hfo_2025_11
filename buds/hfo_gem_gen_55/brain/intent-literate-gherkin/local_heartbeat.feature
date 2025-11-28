Feature: Local Heartbeat Agent (Lvl 0)

  As the Overmind (User)
  I want a local, offline, 24/7 AI agent on my Chromebook Plus
  So that I have a continuous "Heartbeat" monitoring the HFO system without cloud dependency.

  Background:
    Given the "Chromebook Plus" hardware environment
    And the "Ollama" inference engine is active

  Scenario: Offline 24/7 Pulse
    Given the "Gemma 3 4B" model is loaded
    When the system is disconnected from the internet
    Then the Heartbeat Agent should continue to process "Lvl 0" signals
    And the latency should remain under "200ms" per token

  Scenario: Stigmergic Memory Access
    Given the Heartbeat Agent has limited local context
    When it encounters a "Signal" requiring history
    Then it should query the "HFO Stigmergy Memory" (LanceDB)
    And it should not attempt to store long-term state in VRAM

  Scenario: Infrastructure Integration
    Given the HFO Gen 55 "Octree" architecture
    When the Heartbeat Agent emits a "Pulse"
    Then it should be routed via "NATS JetStream" to "Lvl 1" Squads
    And it should be logged in "Chronos" (Time)
