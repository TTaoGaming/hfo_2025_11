Feature: Hot Stigmergy Verification
  As the Swarmlord
  I want to verify the NATS JetStream connection
  So that I can ensure the "Hot" nervous system of Gen 63 is operational

  Scenario: Connect and Pulse
    Given the NATS server is running at "nats://localhost:4222"
    When I attempt to connect to the NATS server
    And I publish a "heartbeat" message to subject "hfo.gen63.heartbeat"
    Then I should receive the message on the same subject
    And the connection status should be "CONNECTED"
