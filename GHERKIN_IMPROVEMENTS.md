# 🔧 Improved Gherkin Specifications
## Concrete Examples with Complete Then Steps and Failure Cases

**Purpose**: Show what your Gherkin SHOULD look like  
**Status**: Reference implementation for fixing intent/*.feature files

---

## Example 1: Byzantine Quorum (Complete Specification)

```gherkin
Feature: Byzantine Quorum Voting
    As the Swarmlord
    I want a fault-tolerant voting mechanism
    So that the system can reach consensus despite malicious or faulty agents

    Background:
        Given the quorum threshold is 0.67 (2/3 majority)
        And the confidence cap is 0.90 (persistent green prevention)

    Scenario: Unanimous Agreement - Confidence Capped
        Given a swarm of 10 agents
        When all 10 agents produce identical response "Solution A"
        Then the quorum should APPROVE
        And the consensus response should be "Solution A"
        And the confidence should be 0.90 (capped, not 1.0)
        And a "POTENTIAL_GROUPTHINK" warning should be logged
        And the participating agents count should be 10

    Scenario: Strong Majority - Above Threshold
        Given a swarm of 10 agents
        When 8 agents produce response "Solution A"
        And 2 agents produce response "Solution B"
        Then the quorum should APPROVE
        And the consensus response should be "Solution A"
        And the confidence should be 0.80 (8/10)
        And the participating agents count should be 10
        And the vote distribution should show:
            | Response    | Count |
            | Solution A  | 8     |
            | Solution B  | 2     |

    Scenario: Exact Threshold - Passes
        Given a swarm of 9 agents
        When 6 agents produce response "Solution A"
        And 3 agents produce response "Solution B"
        Then the quorum should APPROVE
        And the consensus response should be "Solution A"
        And the confidence should be 0.67 (exactly at threshold)

    Scenario: Below Threshold - Quorum Fails
        Given a swarm of 10 agents
        When 6 agents produce response "Solution A"
        And 4 agents produce response "Solution B"
        Then the quorum should REJECT
        And the consensus response should be empty
        And the confidence should be 0.60 (below 0.67)
        And a "QUORUM_FAILED" signal should be published to "hfo.consensus.failed"
        And a retry should be triggered with adjusted parameters

    Scenario: Perfect Split - No Consensus
        Given a swarm of 10 agents
        When 5 agents produce response "Solution A"
        And 5 agents produce response "Solution B"
        Then the quorum should REJECT
        And the confidence should be 0.50
        And the system should log "SPLIT_VOTE"
        And the Navigator should request tie-breaking via:
            - Adding 1 more agent from a different model family
            - Re-running with different temperature settings
            - Escalating to human review if cost threshold exceeded

    Scenario: Disruptor Detection - Outlier Rejection
        Given a swarm of 10 agents
        When 8 agents produce response "Solution A"
        And 1 agent produces response "Solution B"
        And 1 agent (Disruptor) produces response "Gibberish XYZ"
        Then the quorum should APPROVE
        And the consensus response should be "Solution A"
        And the confidence should be 0.80
        And the "Gibberish XYZ" response should be flagged as "OUTLIER"
        And the Disruptor agent should be marked for investigation
        And the Immunizer should receive the outlier for training

    Scenario: Timeout - Incomplete Quorum
        Given a swarm of 10 agents
        And the voting timeout is 30 seconds
        When 7 agents respond within 30 seconds
        And 3 agents do not respond (crashed or slow)
        Then the quorum should evaluate with only 7 votes
        And if 5+ agree, APPROVE with confidence 5/7 = 0.71
        And if <5 agree, REJECT and mark as "INCOMPLETE_QUORUM"
        And the 3 non-responding agents should be health-checked
        And their status should be updated to "TIMEOUT" or "CRASHED"
```

---

## Example 2: Scatter-Gather Pattern (With Failure Cases)

```gherkin
Feature: Ray-Based Scatter-Gather Pattern
    As the Navigator
    I want to distribute work across multiple Ray actors
    So that I can parallelize agent execution and increase throughput

    Background:
        Given Ray is initialized with 4 CPUs
        And the mission intent is "Analyze code quality"
        And the swarm size is set to 10 agents

    Scenario: Successful Spawn and Gather - Happy Path
        When the Navigator spawns 10 Ray actors
        Then all 10 actors should be in "ACTIVE" state within 5 seconds
        And each actor should have a unique actor_id
        And ray.get(actor.health_check.remote()) should return "OK" for all actors
        And the actors should be distributed across available CPUs
        
        When the Navigator scatters the mission to all actors
        Then all 10 actors should receive the mission within 1 second
        And each actor should start executing the PREY loop
        
        When the Navigator gathers results after 30 seconds
        Then all 10 results should be collected
        And each result should include:
            | Field         | Type   |
            | agent_id      | string |
            | response      | string |
            | model_used    | string |
            | confidence    | float  |
            | execution_time_ms | int |

    Scenario: Actor Failure During Execution
        Given 10 Ray actors are spawned
        When agent "agent-5" crashes mid-execution (simulate via ray.kill)
        Then the system should detect the failure within 10 seconds
        And the Navigator should mark "agent-5" as "CRASHED"
        And the gather operation should return only 9 results
        And the quorum should evaluate with 9 agents (not 10)
        And the crashed actor should NOT block the system

    Scenario: Resource Exhaustion - Out of Memory
        Given Ray cluster has only 512MB available memory
        When the Navigator attempts to spawn 100 actors
        Then Ray should raise a ResourceExhausted error
        And the Navigator should catch the error
        And fall back to spawning 10 actors (within memory limits)
        And log a "RESOURCE_CONSTRAINED" warning
        And continue with reduced swarm size

    Scenario: Partial Failure - Some Actors Don't Respond
        Given 10 Ray actors are spawned successfully
        When 8 actors complete and return results
        And 2 actors hang indefinitely (simulate via infinite loop)
        And the gather timeout is 60 seconds
        Then after 60 seconds, the Navigator should:
            - Collect the 8 completed results
            - Mark the 2 hanging actors as "TIMEOUT"
            - Force-kill the hanging actors via ray.kill()
            - Proceed to quorum with 8 results
            - Log the incident for debugging

    Scenario: Network Partition - Ray Cluster Split
        Given a multi-node Ray cluster with 3 nodes
        When node 2 loses network connectivity
        And 3 actors were running on node 2
        Then Ray should detect the partition within 30 seconds
        And the 3 actors on node 2 should be marked "UNREACHABLE"
        And the Navigator should re-spawn 3 replacement actors on nodes 1 and 3
        And continue execution with the replacement actors
        And log the partition event to observability system

    Scenario: Graceful Shutdown - Clean Resource Cleanup
        Given 10 Ray actors are spawned
        When the mission completes successfully
        Then the Navigator should call ray.kill() on all actors
        And all actors should terminate within 5 seconds
        And memory should be released back to the Ray cluster
        And no zombie actors should remain
        And the system should log "ACTORS_CLEANED_UP"
```

---

## Example 3: NATS JetStream Contract (Precise Schema)

```gherkin
Feature: NATS JetStream Stigmergy Layer
    As an agent
    I want to publish and consume messages via NATS JetStream
    So that I can coordinate with other agents without tight coupling

    Background:
        Given a NATS JetStream server is running on localhost:4222
        And the following streams are configured:
            | Stream Name | Subjects              | Storage | Retention | MaxAge | Replicas |
            | MISSIONS    | hfo.mission.*         | File    | WorkQueue | 1h     | 3        |
            | HEARTBEATS  | hfo.agent.*.heartbeat | Memory  | Limits    | 2m     | 1        |
            | VOTES       | hfo.consensus.*       | File    | Interest  | 10m    | 3        |
            | RESULTS     | hfo.result.*          | File    | Limits    | 24h    | 3        |

    Scenario: Publish Heartbeat - Schema Validation
        Given an agent "Agent-007" with role "Shaper"
        When the agent publishes a heartbeat
        Then the message should be sent to subject "hfo.agent.Agent-007.heartbeat"
        And the message should conform to this JSON schema:
            ```json
            {
              "type": "heartbeat",
              "producer_id": "Agent-007",
              "timestamp": "2025-11-20T19:00:00Z",
              "role": "Shaper",
              "status": "ACTIVE",
              "current_step": "Execute",
              "metrics": {
                "cpu_percent": 45.2,
                "memory_mb": 128,
                "tasks_completed": 5
              }
            }
            ```
        And the message should be stored in the "HEARTBEATS" stream
        And the message should expire after 2 minutes (TTL)

    Scenario: Consume Mission - Async Pull
        Given a mission signal is published to "hfo.mission.new"
        When agent "Agent-007" subscribes to "hfo.mission.*"
        Then the agent should receive the mission within 1 second
        And the agent should acknowledge the message
        And the message should be removed from the stream (WorkQueue retention)
        And no other agent should receive the same mission (exclusive delivery)

    Scenario: Publish Vote - Durability Guarantee
        Given agent "Agent-007" completes a task
        When the agent publishes a vote to "hfo.consensus.voting"
        Then the message should be persisted to disk (File storage)
        And the message should be replicated to 3 NATS nodes
        And even if 1 node fails, the message should still be retrievable
        And the message should remain available for 10 minutes (MaxAge)

    Scenario: Stream Full - Backpressure Handling
        Given the "MISSIONS" stream has MaxMsgs=10000
        When 10001 missions are published
        Then the oldest mission should be evicted (FIFO)
        And the publisher should receive a "STREAM_FULL" warning
        And the Navigator should implement backpressure:
            - Pause publishing for 1 second
            - Wait for consumers to drain the queue
            - Retry publishing

    Scenario: NATS Server Down - Graceful Degradation
        Given agents are running
        When the NATS server crashes
        Then agents should detect connection loss within 5 seconds
        And agents should buffer messages locally (max 100 messages)
        And agents should attempt reconnection every 10 seconds
        And if NATS is down for >60 seconds:
            - Switch to fallback mode (in-memory Python queue)
            - Log "STIGMERGY_DEGRADED" warning
            - Continue execution with reduced resilience
        And when NATS recovers:
            - Flush buffered messages to NATS
            - Resume normal stigmergy operation
```

---

## Example 4: PREY Loop (With Retry Logic)

```gherkin
Feature: PREY Loop Execution
    As an agent
    I want to execute the Perceive-React-Execute-Yield loop
    So that I can autonomously complete tasks with self-correction

    Background:
        Given an agent "Agent-001" with role "Observer"
        And a research intent "Analyze React 19 features"

    Scenario: Complete PREY Cycle - Success
        # P - Perceive
        When the agent enters "Perceive" phase
        Then it should query memory for similar missions (RAG)
        And it should search the internet for "React 19 features"
        And it should construct a Context Object with:
            | Field              | Source           |
            | memory_precedents  | Vector DB        |
            | web_search_results | Search API       |
            | raw_data_size_kb   | Calculated       |
        And the agent should transition to "React" phase

        # R - React
        When the agent enters "React" phase
        Then it should analyze the Context Object
        And it should generate a Plan with specific steps:
            1. Extract feature list from docs
            2. Compare with React 18
            3. Identify breaking changes
            4. Summarize benefits
        And the Plan should be stored in agent state
        And the agent should transition to "Execute" phase

        # E - Execute
        When the agent enters "Execute" phase
        Then it should execute each step in the Plan sequentially
        And it should produce an Execution Result containing:
            | Field            | Type   |
            | feature_list     | array  |
            | comparison_table | string |
            | summary          | string |
        And the agent should transition to "Yield" phase

        # Y - Yield
        When the agent enters "Yield" phase
        Then it should perform a Self-Audit asking "Did I satisfy the intent?"
        And if the answer is "Yes":
            - Commit the result to memory
            - Publish a "SUCCESS" signal to NATS
            - Set agent status to "IDLE"
        And the PREY loop should complete

    Scenario: Execute Fails - Retry with Constraints
        Given the agent is in "Execute" phase
        When step 2 fails with error "API rate limit exceeded"
        Then the agent should NOT crash
        And the agent should return to "React" phase
        And the agent should update constraints:
            - Add "rate_limit_delay=60s"
            - Reduce "max_api_calls=5"
        And the agent should generate a new Plan
        And retry the Execute phase with updated constraints
        And the retry count should be incremented
        And if retry count > 3:
            - Mark mission as "FAILED"
            - Publish "FAILURE" signal with error details
            - Yield with partial results

    Scenario: Self-Audit Fails - Quality Check
        Given the agent completes Execute phase
        When the agent enters "Yield" phase
        And the Self-Audit checks "Does the summary mention new features?"
        And the summary is generic (quality score < 0.6)
        Then the Self-Audit should return "No"
        And the agent should transition back to "React" phase
        And the agent should add constraint:
            - "require_specific_examples=True"
        And the agent should retry Execute with improved prompt
        And the improved result should satisfy the Self-Audit

    Scenario: Infinite Loop Prevention - Max Iterations
        Given the agent is in a PREY loop
        When the agent retries 5 times
        And each Self-Audit still fails
        Then the system should detect the infinite loop
        And force the agent to Yield with status "MAX_RETRIES_EXCEEDED"
        And publish a "LOOP_DETECTED" warning
        And escalate to Navigator for human review
```

---

## Key Improvements Demonstrated

### 1. Complete Then Steps
Every scenario now has:
- ✅ Clear assertions ("should be", "should contain")
- ✅ Expected values (timeouts, counts, schemas)
- ✅ State transitions ("should transition to X phase")

### 2. Failure Scenarios
Every feature now includes:
- ✅ Resource exhaustion
- ✅ Network failures
- ✅ Timeouts
- ✅ Partial failures
- ✅ Graceful degradation

### 3. Precise Specifications
- ✅ Byzantine quorum algorithm (2/3 majority, 90% cap)
- ✅ NATS schema (JSON structure, subjects, retention)
- ✅ Retry logic (max attempts, backoff strategy)
- ✅ Timeout values (5s, 30s, 60s)

### 4. Observable Outcomes
- ✅ Metrics logged ("GROUPTHINK_WARNING")
- ✅ Signals published ("QUORUM_FAILED")
- ✅ State changes ("CRASHED", "TIMEOUT")

---

## Action Items for Your Features

1. **swarm_workflow.feature**:
   - Add Then steps for each When
   - Add failure scenario for quorum failure
   - Specify Byzantine algorithm precisely

2. **prey_workflow.feature**:
   - Add Then steps for phase transitions
   - Add retry scenario with max iterations
   - Specify Self-Audit criteria

3. **stigmergy_layer.feature**:
   - Add NATS stream configuration table
   - Add message schema examples
   - Add NATS server failure scenario

4. **memory_graphrag.feature**:
   - Add Then steps for graph operations
   - Add failure scenario for vector DB timeout
   - Specify RAG retrieval algorithm

---

**Status**: Reference for fixing Gherkin specs  
**Effort**: 2-3 days to apply to all features  
**Impact**: Prevents implementation ambiguity
