Feature: SWARM Loop - Byzantine Quorum with Rigorous Math
    As the Swarmlord
    I want a 10-agent Byzantine swarm with concrete quorum calculations
    So that consensus is mathematically sound and adversarial-resistant

    # Lineage: D3A (Military) + Byzantine FT (Lamport) + MAP-Elites (Mouret)
    # Status: RIGOROUS - All math and thresholds defined

    Background: Byzantine Quorum Mathematics
        Given the Byzantine Fault Tolerance formula: N >= 3F + 1
        Where:
            - N = total number of agents
            - F = maximum number of faulty (disruptor) agents
        And for N=10 agents with F=3 disruptors:
            - Quorum threshold Q = ceil(N * 0.67) = ceil(10 * 0.67) = 7 votes
            - This ensures: Q > (N + F) / 2 = 6.5, satisfying BFT requirement
        And confidence calculation:
            - raw_confidence = majority_votes / total_votes
            - final_confidence = min(raw_confidence, 0.90)  # Cap at 90%
        And disruptor detection uses:
            - Statistical outlier: z-score > 2.5
            - Semantic divergence: cosine_similarity < 0.3 to median response
            - Timing anomaly: response_time > 2 * median_response_time

    Scenario: SWARM Loop - Complete Cycle with Concrete Assertions
        Given a mission_intent "Solve complex reasoning task: What is 25 * 17?"
        And swarm_size = 10
        And disruptor_min = 1, disruptor_max = 3
        And coordination_model = "x-ai/grok-4.1-fast"  # Cheap Navigator
        And execution_models = ["x-ai/grok-4.1-fast", "openai/gpt-oss-120b", "google/gemini-2.5-flash-lite-sep", "qwen/qwen3-next-80b-a3b-instruct", "deepseek/deepseek-v3.2-exp"]
        
        # S - SET
        When the NavigatorOrchestrator.set_mission(mission_intent) is called
        Then it MUST validate mission_intent against MissionIntent schema
        And create SwarmState with:
            | field        | value                    |
            | generation_id| current_gen + 1          |
            | phase        | SwarmPhase.SET           |
            | swarm_size   | 10                       |
        And initialize MAP-Elites archive with:
            - dims = [response_quality, response_diversity]
            - ranges = [(0.0, 1.0), (0.0, 1.0)]
            - bins = [10, 10]
        And define search_space = {
            "temperature": (0.3, 1.0),
            "top_p": (0.8, 1.0),
            "disruptor_ratio": (0.1, 0.3)
        }
        And the SET phase MUST complete in < 5 seconds
        
        # W - WATCH
        And the system initializes observability:
            - Create LangSmith trace with run_id = mission_intent.id
            - Connect to NATS JetStream at "nats://localhost:4222"
            - Subscribe to subjects: ["hfo.stigmergy.heartbeat", "hfo.consensus.voting"]
        And the WATCH phase MUST complete in < 3 seconds
        
        # A - ACT (Scatter-Gather)
        When the orchestrator.scatter_gather(mission_intent) is called
        Then it MUST randomly select n_disruptors from range [disruptor_min, disruptor_max]
        And spawn 10 Ray actors:
            - (10 - n_disruptors) agents with role = AgentRole.SHAPER
            - n_disruptors agents with role = AgentRole.DISRUPTOR
        And each actor MUST execute build_prey_loop().invoke(agent_state)
        And the scatter operation MUST be non-blocking (Ray futures)
        And the gather operation MUST use ray.get(futures, timeout=180)
        And the ACT phase MUST complete in < 200 seconds total
        And if any agent timeout, mark as FAILED and continue with available responses
        And collect responses where each response is:
            """python
            {
                "agent_id": str,
                "role": AgentRole,
                "response": str,
                "confidence": float,
                "duration_seconds": float
            }
            """
        And the minimum required responses is 7 (even if 3 agents fail)
        And if responses < 7, abort mission with InsufficientQuorumError
        
        # R - REVIEW (Byzantine Quorum)
        When the orchestrator.byzantine_vote(responses) is called
        Then it MUST extract all response texts
        And compute response embeddings using sentence_transformer
        And calculate pairwise cosine_similarities
        And identify the median response (highest avg similarity)
        And for each response, calculate:
            - z_score = (similarity_to_median - mean) / std_dev
            - is_outlier = z_score < -2.5
        And flag outliers as potential_disruptors
        And group responses by semantic similarity (threshold = 0.85)
        And find the largest consensus group (majority)
        And calculate:
            - majority_size = len(largest_group)
            - quorum_threshold = ceil(len(responses) * 0.67)
            - quorum_met = majority_size >= quorum_threshold
        And if NOT quorum_met:
            - Log: "Quorum failed: {majority_size}/{len(responses)} < {quorum_threshold}"
            - Expand swarm by 5 agents (total = 15)
            - Re-scatter with expanded swarm
            - Re-vote
            - If still no quorum after 2 expansions (max 20 agents), return STALEMATE
        And if quorum_met:
            - consensus = largest_group.median_response
            - raw_confidence = majority_size / len(responses)
            - final_confidence = min(raw_confidence, 0.90)
        And the Immunizer MUST check if disruptors were detected:
            - expected_disruptors = n_disruptors (known from spawn)
            - detected_disruptors = len(potential_disruptors)
            - if detected_disruptors < expected_disruptors:
                - Log WARNING: "Immunizer failed to detect all disruptors"
                - This is a TEST FAILURE (system is blind to attacks)
        And the REVIEW phase MUST complete in < 30 seconds
        
        # M - MUTATE (Evolution)
        When the orchestrator.mutate(consensus, swarm_state) is called
        Then it MUST add the solution to MAP-Elites archive:
            - solution = swarm_params (temperature, top_p, disruptor_ratio)
            - objective = final_confidence
            - measures = [response_quality, response_diversity]
        And the archive.add_single(solution, objective, measures)
        And if the archive is getting crowded in one cell:
            - Apply mutation operators:
                1. Gaussian noise to temperature (std=0.1)
                2. Crossover between two elite solutions
                3. Random reset of worst-performing parameter
        And trigger DSPy prompt optimization:
            - Collect top 5 solutions from archive
            - Use DSPy.ChainOfThought to optimize PREY prompts
            - Update agent_prompt_template for next generation
        And check for "Persistent Green" anti-pattern:
            - Query archive for last 5 generations
            - If ALL have confidence >= 0.88:
                - Flag as "Persistent Green - Insufficient Challenge"
                - Increase disruptor_ratio by 0.1
                - Add harder test cases to mission_intent constraints
                - Log: "System may be overfitting. Injecting adversarial stress."
        And the MUTATE phase MUST complete in < 20 seconds
        And return final artifact:
            """python
            {
                "mission": mission_intent.description,
                "answer": consensus,
                "confidence": final_confidence,
                "evidence": {
                    "total_agents": len(responses),
                    "majority_size": majority_size,
                    "disruptors_injected": n_disruptors,
                    "disruptors_detected": detected_disruptors,
                    "quorum_met": quorum_met
                },
                "metadata": {
                    "generation_id": swarm_state.generation_id,
                    "archive_size": len(archive),
                    "persistent_green_flag": bool
                }
            }
            """

    Scenario: Byzantine Quorum - Tie Vote with Expansion
        Given 10 agents have voted
        And votes are split: 5 vote "Answer A", 5 vote "Answer B"
        And quorum_threshold = 7
        When the byzantine_vote is calculated
        Then quorum_met = False (5 < 7 and 5 < 7)
        And the orchestrator MUST expand the swarm by 5 agents
        And spawn 5 additional PreyActors
        And re-scatter the mission to all 15 agents
        And re-gather responses
        And re-calculate quorum with new threshold = ceil(15 * 0.67) = 11
        And if STILL no consensus after expansion:
            - Try one more expansion (max 20 agents, threshold = 14)
        And if no consensus after 2 expansions:
            - Return consensus = None, confidence = 0.0, status = "STALEMATE"
            - reason = "Irreconcilable perspectives. Manual review required."

    Scenario: Byzantine Quorum - Disruptor Detection Failure
        Given 10 agents have submitted responses
        And 3 agents are designated disruptors (injected by system)
        And the disruptors submit intentionally wrong answers
        When the Immunizer analyzes responses
        And detects only 1 outlier (missed 2 disruptors)
        Then the test MUST FAIL with assertion error:
            "Immunizer only detected 1/3 disruptors. Detection algorithm is insufficient."
        And log the undetected disruptors for debugging
        And recommend: "Adjust outlier detection threshold or add additional signals"
        And this scenario is a RED FLAG that the system is vulnerable

    Scenario: SWARM Loop - Cost Enforcement (FinOps)
        Given a mission_intent with swarm_size = 10
        And execution_model_group = "Cheap QD Swarm"
        And the price table:
            | model                              | price_per_1M_tokens |
            | x-ai/grok-4.1-fast                 | $0.28               |
            | openai/gpt-oss-120b                | $0.26               |
            | google/gemini-2.5-flash-lite-sep   | $0.17               |
            | qwen/qwen3-next-80b-a3b-instruct   | $0.10               |
            | deepseek/deepseek-v3.2-exp         | $0.32               |
        When the orchestrator calculates estimated_cost:
            - avg_input_tokens = 100 tokens per agent
            - avg_output_tokens = 200 tokens per agent
            - total_tokens = (100 + 200) * 10 = 3000 tokens
            - avg_price = mean([0.28, 0.26, 0.17, 0.10, 0.32]) = $0.226 per 1M
            - estimated_cost = (3000 / 1_000_000) * 0.226 = $0.000678
        Then estimated_cost < max_cost_per_mission ($0.05)
        And the mission is APPROVED for execution
        And if estimated_cost > max_cost_per_mission:
            - Reject mission with CostExceededError
            - Suggest: "Reduce swarm_size or use cheaper models"

    Scenario: SWARM Loop - NATS Connection Failure
        Given the orchestrator is publishing a MissionSignal
        When the NATS server at "nats://localhost:4222" is unreachable
        Then the orchestrator MUST retry connection 3 times:
            - Attempt 1: wait 1 second
            - Attempt 2: wait 2 seconds
            - Attempt 3: wait 4 seconds (exponential backoff)
        And if all retries fail:
            - Switch to LOCAL_QUEUE mode
            - Buffer signals in memory (max 100)
            - Log warning: "NATS unavailable. Operating in degraded mode."
            - Continue SWARM execution without stigmergy
        And when NATS connection restores:
            - Flush all buffered signals to JetStream
            - Log metric: signals_lost_count, reconnection_time

    Scenario: SWARM Loop - Persistent Green Detection
        Given the MAP-Elites archive has 5 consecutive generations
        And all 5 generations have final_confidence >= 0.88
        When the MUTATE phase analyzes the archive
        Then it MUST detect "Persistent Green" pattern
        And log warning:
            "Persistent Green detected (5 gens @ 88%+ confidence). 
             System may be overfitting or tests are too easy.
             Injecting harder challenges."
        And automatically adjust:
            - disruptor_ratio: increase from 0.2 to 0.3
            - Add constraint: "Include edge cases and corner cases"
            - Reduce temperature: decrease from 0.7 to 0.5 (more deterministic = harder to game)
        And in next generation, expect confidence to DROP to 70-85% range
        And if confidence remains > 88% for 10 generations:
            - Escalate to human: "Test suite may be insufficient"
