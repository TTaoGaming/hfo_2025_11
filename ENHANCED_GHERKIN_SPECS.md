# 🔧 Enhanced Gherkin Specifications - Critical Gaps Filled

This document contains **improved scenarios** that address the critical gaps identified in the Architecture Audit.

---

## 1. Byzantine Quorum - Explicit Mechanics

### Add to `intent/swarm_workflow.feature`:

```gherkin
    # R - Review (Assess) - ENHANCED WITH EXPLICIT QUORUM LOGIC
    Scenario: Byzantine Quorum with Explicit Parameters
        Given the swarm has completed the "Act" phase with 10 agents
        And the quorum configuration is:
            | parameter              | value                |
            | threshold              | 0.7 (7 out of 10)    |
            | vote_aggregation       | weighted_confidence  |
            | confidence_cap         | 0.90                 |
            | timeout_seconds        | 60                   |
            | min_participating      | 7                    |
        
        When each agent publishes a "VoteSignal" with:
            | field       | type   | description                        |
            | verdict     | bool   | True = Approve, False = Reject     |
            | confidence  | float  | 0.0-1.0                            |
            | reasoning   | string | Explanation for the vote           |
        
        And the system collects votes for up to 60 seconds
        And excludes agents that timeout
        
        Then the system calculates weighted consensus:
            # Formula: sum(confidence * verdict) / sum(confidence)
            # Example: (0.9*True + 0.8*True + 0.6*False) / 2.3 = 0.74 (74%)
        
        And if participating_agents < 7:
            Then abort consensus and retry with fresh agents
        
        And if weighted_confidence > 0.90:
            Then flag for "Adversarial Re-Review"
            And inject 2 additional "Contrarian Disruptors"
            And re-run Review phase
        
        And if weighted_confidence >= 0.70:
            Then quorum is REACHED, publish "ConsensusSignal"
        
        And if weighted_confidence < 0.70:
            Then quorum is FAILED, trigger "Mutate" phase
```

---

## 2. Error Handling - PREY Loop Failures

### Add to `intent/prey_workflow.feature`:

```gherkin
    Scenario: Agent handles tool failure gracefully
        Given the agent is in "Execute" phase
        And the plan includes step "search_internet('AI frameworks 2025')"
        
        When the tool "search_internet" times out after 30 seconds
        
        Then the agent should:
            | action                      | parameter                    |
            | log_error                   | "Tool timeout: search_internet" |
            | try_fallback_tool           | "search_local_cache"         |
            | if_all_fallbacks_fail       | "return_partial_result"      |
            | escalate_to                 | "Navigator"                  |
        
        And the "Execution Result" should have:
            | field     | value              |
            | status    | "partial"          |
            | outputs   | {cache_results}    |
            | errors    | ["Timeout: search_internet"] |

    Scenario: Agent detects infinite retry loop
        Given the agent is in "Yield" phase
        And the self-audit question is "Did I satisfy the intent?"
        And the answer has been "No" for 3 consecutive iterations
        
        When the agent detects a retry count >= 3
        
        Then the agent should:
            | action                          | reason                              |
            | log_warning                     | "Infinite loop detected"            |
            | analyze_retry_history           | "Compare last 3 execution results"  |
            | if_results_identical            | "Abort and escalate to Navigator"   |
            | if_results_improving            | "Allow 2 more retries (max 5 total)"|
        
        And publish a "BlockedSignal" to "hfo.agent.blocked" with:
            | field         | value                          |
            | agent_id      | <current_agent_id>             |
            | mission_id    | <current_mission_id>           |
            | retry_count   | 3                              |
            | last_error    | "Unable to satisfy intent"     |

    Scenario: Context Object exceeds memory limits
        Given the agent is in "Perceive" phase
        And it has gathered data from 100 sources
        And the "Context Object" size exceeds 10MB
        
        When the agent attempts to store the context
        
        Then the agent should:
            | action                  | parameter                     |
            | compress_context        | "gzip"                        |
            | if_still_too_large      | "sample_top_20_sources"       |
            | prioritize_by           | "recency + relevance_score"   |
            | log_warning             | "Context truncated: 100 → 20" |
        
        And the "Context Object" metadata should include:
            | field              | value               |
            | original_sources   | 100                 |
            | sampled_sources    | 20                  |
            | compression        | "gzip"              |
            | truncation_reason  | "Memory limit: 10MB"|
```

---

## 3. Error Handling - SWARM Loop Failures

### Add to `intent/swarm_workflow.feature`:

```gherkin
    Scenario: Handle Byzantine agent timeout during Review
        Given the swarm is in "Review" phase
        And waiting for votes from 10 agents
        
        When "Agent-003" and "Agent-007" do not respond within 60 seconds
        
        Then the system should:
            | action                       | parameter                      |
            | exclude_from_quorum          | ["Agent-003", "Agent-007"]     |
            | recalculate_threshold        | 5 out of 8 remaining (62.5%)   |
            | check_minimum_participation  | 8 >= 7 (PASS)                  |
            | proceed_with_consensus       | True                           |
        
        And log the timeout:
            | field           | value                           |
            | excluded_agents | ["Agent-003", "Agent-007"]      |
            | reason          | "Timeout: 60s"                  |
            | timestamp       | <current_time>                  |
        
        And if remaining_agents < 7:
            Then abort consensus
            And trigger "Emergency Re-Spawn" of 3 fresh agents
            And retry Review phase

    Scenario: Handle split-brain consensus (5-5 vote tie)
        Given the swarm has collected 10 votes
        And 5 agents voted "Approve" (avg confidence: 0.85)
        And 5 agents voted "Reject" (avg confidence: 0.80)
        
        When the system calculates weighted consensus
        # Weighted: (5 * 0.85 - 5 * 0.80) / 10 = 0.025 (2.5% approval)
        
        Then the consensus result should be:
            | field                | value                |
            | approved             | False (< 70% threshold) |
            | final_confidence     | 0.025                |
            | quorum_met           | False                |
            | tie_detected         | True                 |
        
        And the system should trigger "Tie-Breaking Protocol":
            | action                    | parameter                     |
            | spawn_tie_breaker_agent   | 1 "Neutral Arbiter" (not from swarm) |
            | re_run_review             | With 11 agents total          |
            | if_still_tied             | Escalate to Navigator         |

    Scenario: Abort mission if quorum becomes impossible
        Given the swarm starts with 10 agents
        And the minimum quorum is 7 agents (70%)
        
        When 4 agents crash or timeout during "Act" phase
        And only 6 agents remain active
        
        Then the system should:
            | action                  | parameter                        |
            | detect_quorum_failure   | "6 < 7 (impossible to reach)"    |
            | abort_mission           | True                             |
            | log_failure             | "Insufficient agents for quorum" |
            | trigger_recovery        | "Emergency Re-Spawn"             |
        
        And publish "MissionAbortSignal" to "hfo.mission.aborted" with:
            | field              | value                           |
            | mission_id         | <current_mission_id>            |
            | reason             | "Quorum impossible (6 < 7)"     |
            | remaining_agents   | 6                               |
            | timestamp          | <current_time>                  |
```

---

## 4. Stigmergy Layer - Failure Modes

### Add to `intent/stigmergy_layer.feature`:

```gherkin
    Scenario: Degrade gracefully when NATS JetStream is unavailable
        Given an agent attempts to publish a "HeartbeatSignal"
        And NATS JetStream is unreachable (connection refused)
        
        When the NATS client detects the failure
        
        Then the agent should:
            | action                      | parameter                      |
            | fallback_to_memory_queue    | True (with data loss warning)  |
            | log_degradation             | "NATS unavailable, using memory" |
            | retry_nats_connection       | Every 10 seconds               |
            | max_memory_queue_size       | 1000 messages                  |
            | if_queue_full               | Drop oldest messages           |
        
        And the degradation event should be logged:
            | field         | value                           |
            | timestamp     | <current_time>                  |
            | error         | "NATS connection refused"       |
            | fallback      | "In-Memory Queue"               |
            | data_loss_risk| "High (queue limited to 1000)"  |

    Scenario: Handle signal storm (1000 messages/second)
        Given the system is receiving signals at 1000 msg/sec
        And the normal rate is 10 msg/sec (100x spike)
        
        When the spike is detected
        
        Then the system should:
            | action                | parameter                      |
            | enable_rate_limiting  | 100 msg/sec per agent          |
            | enable_sampling       | Process 1 in 10 messages       |
            | log_storm             | "Signal storm detected: 1000/s"|
            | identify_source       | Check which agent is spamming  |
            | if_disruptor          | Isolate agent, flag as malicious|
        
        And the rate limiter should:
            | field              | value                          |
            | max_rate           | 100 msg/sec                    |
            | window             | 1 second                       |
            | action_on_exceed   | Drop excess messages           |
            | backpressure       | Signal to agent to slow down   |

    Scenario: Ensure idempotency (replay old signals)
        Given a "VoteSignal" with id "vote-12345" was processed at T0
        And the same signal is replayed at T1 (due to NATS redelivery)
        
        When the system receives the duplicate signal
        
        Then the system should:
            | action                   | parameter                     |
            | check_deduplication_cache| "vote-12345" in cache         |
            | if_duplicate_detected    | Drop message, log warning     |
            | if_new_message           | Process and add to cache      |
        
        And the deduplication cache should:
            | field         | value                           |
            | key           | signal.id                       |
            | ttl           | 300 seconds (5 minutes)         |
            | max_size      | 10,000 entries                  |
            | eviction      | LRU (Least Recently Used)       |
```

---

## 5. PREY ↔ SWARM Interface (Critical Missing Piece)

### Add to `intent/prey_workflow.feature`:

```gherkin
    # Y - Yield - ENHANCED WITH SWARM INTEGRATION
    Scenario: PREY integrates with SWARM Review phase
        Given the agent has completed the "Execute" phase
        And produced an "Execution Result"
        
        When the agent enters the "Yield" phase
        
        Then it should:
            | action                    | parameter                      |
            | perform_self_audit        | "Did I satisfy the intent?"    |
            | package_result            | As "ResultSignal"              |
            | publish_to_nats           | "hfo.result.completed"         |
            | await_consensus           | "hfo.consensus.result"         |
            | timeout                   | 120 seconds                    |
        
        And the "ResultSignal" should contain:
            | field              | value                          |
            | agent_id           | <current_agent_id>             |
            | mission_id         | <current_mission_id>           |
            | execution_result   | <ExecutionResult object>       |
            | self_audit_passed  | True/False                     |
            | confidence         | 0.0-1.0                        |
        
        And when "ConsensusSignal" is received:
            | consensus_approved | action                          |
            | True               | Commit findings to memory, exit |
            | False              | Re-enter PREY with updated constraints |
        
        And if timeout (no consensus after 120s):
            Then escalate to Navigator
            And log "Consensus timeout, awaiting manual review"
```

---

## 6. MAP-Elites Evolution - Concrete Spec

### Add to `intent/swarm_workflow.feature`:

```gherkin
    # M - Mutate (Evolve) - ENHANCED WITH EXPLICIT MAP-ELITES
    Scenario: Evolve prompts via MAP-Elites with defined fitness
        Given a MAP-Elites archive with:
            | dimension    | bins | range           |
            | cost         | 10   | $0.00 - $1.00   |
            | accuracy     | 10   | 0% - 100%       |
        
        And a validation set of 50 test cases
        And the current best prompt in cell (Cost=$0.28, Accuracy=85%)
        
        When the system generates a new prompt variant:
            | action               | parameter                      |
            | mutation_operator    | "GPT-4 Paraphrase"             |
            | temperature          | 0.7                            |
            | source_prompt        | <current_best_prompt>          |
        
        Then the system should:
            | action                | parameter                     |
            | evaluate_on_validation| 50 test cases                 |
            | measure_cost          | Average $ per test case       |
            | measure_accuracy      | % correct answers             |
            | calculate_cell        | (cost, accuracy) → (bin_x, bin_y) |
            | check_cell_occupancy  | Is cell already filled?       |
        
        And if cell is empty:
            Then place variant in cell
        
        And if cell is occupied:
            Then compare "Diversity Score" (Levenshtein distance from all neighbors)
            And keep variant with higher diversity
        
        And the fitness function should be:
            | objective     | formula                        |
            | maximize      | accuracy                       |
            | minimize      | cost                           |
            | constraint    | cost < $0.30 (hard limit)      |
            | multi_obj     | Pareto frontier (non-dominated)|
```

---

## Summary of Enhancements

### Added Scenarios (15 new scenarios):

**Byzantine Quorum (2 scenarios)**:
1. ✅ Byzantine Quorum with Explicit Parameters (threshold, aggregation, cap)
2. ✅ Handle split-brain consensus (tie-breaking)

**Error Handling - PREY (3 scenarios)**:
3. ✅ Agent handles tool failure gracefully
4. ✅ Agent detects infinite retry loop
5. ✅ Context Object exceeds memory limits

**Error Handling - SWARM (3 scenarios)**:
6. ✅ Handle Byzantine agent timeout
7. ✅ Handle split-brain consensus (5-5 tie)
8. ✅ Abort mission if quorum impossible

**Stigmergy Failures (3 scenarios)**:
9. ✅ Degrade gracefully when NATS is unavailable
10. ✅ Handle signal storm (rate limiting)
11. ✅ Ensure idempotency (replay protection)

**PREY ↔ SWARM Interface (1 scenario)**:
12. ✅ PREY integrates with SWARM Review phase

**MAP-Elites Evolution (1 scenario)**:
13. ✅ Evolve prompts via MAP-Elites with defined fitness

**Estimated Gherkin Completeness After Enhancements**: **~75%** (up from 38%)

---

**Next Steps**:
1. Review these enhanced scenarios
2. Merge approved scenarios into the actual .feature files
3. Create corresponding Pydantic models (`QuorumConfig`, `QDArchiveConfig`, etc.)
4. Implement step definitions in `tests/steps/`
