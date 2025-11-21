Feature: Virtual Stigmergy Layer (NATS JetStream)
    As the Swarmlord
    I want a persistent, asynchronous "Blackboard" (Stigmergy)
    So that agents can coordinate without direct point-to-point coupling

    # Core Concept: "The Bus Builds the Brain"
    # Agents write to the environment (NATS), and the environment triggers other agents.

    Scenario: Agent publishes a "Heartbeat" (Proof of Life)
        Given an active agent "Agent-007"
        When the agent enters the "PREY Loop"
        Then it must publish a "Heartbeat" signal to "hfo.stigmergy.heartbeat" every 30 seconds
        And the signal must contain:
            | field     | value          |
            | agent_id  | Agent-007      |
            | status    | ACTIVE         |
            | timestamp | <current_time> |

    Scenario: Swarmlord scatters a "Mission" via the Blackboard
        Given a new MissionIntent "Optimize Code"
        When the Swarmlord publishes a "MissionSignal" to "hfo.mission.new"
        Then the "MissionSignal" is persisted in the JetStream "MISSIONS" stream
        And available "Navigator" agents receive the signal asynchronously

    Scenario: Agents reach Consensus via Voting (Byzantine Fault Tolerance)
        Given a proposed solution "Solution-X" by "Agent-A"
        When "Agent-A" publishes a "VoteRequest" to "hfo.consensus.voting"
        And 3 other agents (Reviewers) consume the request
        And each Reviewer publishes a "VoteSignal" (APPROVE/REJECT)
        Then the system aggregates votes until a "Quorum" (e.g., 3/4) is reached
        And the final result is written to "hfo.consensus.result"

    Scenario: Disruptor Injection (Red Team)
        Given a "Disruptor" agent is active
        When it publishes a "NoiseSignal" or "FalseVote"
        Then the "Immunizer" agents must detect the anomaly via "Signal Entropy"
        And the "Disruptor" is isolated (but not deleted, for training data)

    Scenario: Architectural Visualization (Documentation)
        Given the Stigmergy Layer architecture is complex
        When the architecture is documented
        Then it must be visualized using "Mermaid" diagrams
        And the diagrams must be embedded in "Markdown" files for easy preview
        And the visual must clearly show the "Decoupled Flow" between Agents and NATS
