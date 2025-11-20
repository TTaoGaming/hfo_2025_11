Feature: PREY Loop - Rigorous Specification v2
    As the Swarmlord
    I want a single autonomous agent to execute a PREY loop with concrete, testable behavior
    So that implementation is unambiguous and verifiable

    # Lineage: OODA (Boyd) + MAPE-K (IBM) + JADC2 (DoD)
    # Status: RIGOROUS - Every step has measurable success criteria

    Background: Data Schemas and Constraints
        Given the following Pydantic models are enforced:
            """python
            class PerceptionResult(BaseModel):
                sources: List[str] = Field(min_length=1, max_length=50)
                context_tokens: int = Field(ge=100, le=10000)
                timestamp: datetime
                query: str
                retrieval_method: str  # "memory" | "web" | "hybrid"
            
            class ReactionPlan(BaseModel):
                steps: List[str] = Field(min_length=1, max_length=20)
                reasoning: str = Field(min_length=50)
                cynefin_domain: CynefinDomain  # SIMPLE | COMPLICATED | COMPLEX | CHAOTIC
                similar_cases: List[UUID4] = Field(default_factory=list)
                estimated_duration_seconds: int = Field(ge=1, le=600)
            
            class ExecutionResult(BaseModel):
                status: ExecutionStatus  # SUCCESS | FAILED | PARTIAL | TIMEOUT
                output: str
                tools_used: List[str]
                duration_seconds: float
                error_message: Optional[str] = None
            
            class YieldDecision(BaseModel):
                intent_satisfied: bool
                confidence_score: float = Field(ge=0.0, le=1.0)
                should_retry: bool
                retry_count: int
                audit_notes: str
            """
        And the following performance SLAs are enforced:
            | phase     | max_duration_seconds |
            | PERCEIVE  | 30                   |
            | REACT     | 15                   |
            | EXECUTE   | 120                  |
            | YIELD     | 10                   |
            | FULL_PREY | 180                  |

    Scenario: PREY Loop - Happy Path with Concrete Assertions
        Given an agent "Agent-001" with role "Observer"
        And the agent is initialized with mission_intent:
            """json
            {
                "description": "Analyze latest trends in AI agent frameworks",
                "rationale": "Research for architecture decisions",
                "constraints": [
                    {"description": "Use only 2024-2025 sources", "is_hard_constraint": true},
                    {"description": "Include at least 5 frameworks", "is_hard_constraint": true}
                ]
            }
            """
        
        # P - PERCEIVE
        When the agent enters the "PERCEIVE" phase
        Then it MUST call memory_service.retrieve_context(query="AI agent frameworks", limit=5)
        And it MUST call web_search.execute(query="AI agent frameworks 2025", max_results=10)
        And it MUST return PerceptionResult where:
            | field             | assertion                    |
            | len(sources)      | >= 5                         |
            | context_tokens    | 500 <= x <= 5000             |
            | timestamp         | within_last_minutes(5)       |
            | retrieval_method  | in ["memory", "web", "hybrid"] |
        And the phase duration MUST be < 30 seconds
        And if any API call fails, it MUST retry up to 3 times with exponential backoff (1s, 2s, 4s)
        And the PerceptionResult MUST be stored in agent.short_term_memory
        
        # R - REACT
        When the agent enters the "REACT" phase
        Then it MUST analyze the PerceptionResult using Cynefin Framework classification
        And it MUST query case_based_reasoning.find_similar(mission_intent, limit=3)
        And it MUST generate a ReactionPlan where:
            | field                       | assertion           |
            | len(steps)                  | >= 1 and <= 20      |
            | len(reasoning)              | >= 50               |
            | cynefin_domain              | is valid enum       |
            | estimated_duration_seconds  | <= 120              |
        And the plan MUST include specific tool calls with parameters
        And the phase duration MUST be < 15 seconds
        And the ReactionPlan MUST be validated against ReactionPlan schema
        
        # E - EXECUTE
        When the agent enters the "EXECUTE" phase
        Then it MUST execute each step in ReactionPlan.steps sequentially
        And for each tool call, it MUST:
            - Log the tool name and input to LangSmith trace
            - Set timeout = 30 seconds per tool call
            - Catch exceptions and log to ExecutionResult.error_message
        And it MUST return ExecutionResult where:
            | field             | assertion                          |
            | status            | in ["SUCCESS", "FAILED", "PARTIAL"] |
            | len(output)       | > 0 if status == SUCCESS           |
            | duration_seconds  | <= 120                             |
            | len(tools_used)   | >= 1                               |
        And if status == "FAILED", error_message MUST be populated
        And the phase duration MUST be < 120 seconds
        
        # Y - YIELD
        When the agent enters the "YIELD" phase
        Then it MUST perform self-audit by comparing ExecutionResult to mission_intent.constraints
        And it MUST check:
            - Were all hard constraints satisfied?
            - Is the output quality sufficient (len > 100 chars)?
            - Was execution within time budget?
        And it MUST return YieldDecision where:
            | field               | assertion                          |
            | intent_satisfied    | is bool                            |
            | confidence_score    | 0.0 <= x <= 1.0                    |
            | should_retry        | is bool                            |
            | len(audit_notes)    | >= 20                              |
        And if intent_satisfied == False and retry_count < 3:
            - Set should_retry = True
            - Update constraints with failure reason
            - Restart from PERCEIVE phase
        And if intent_satisfied == True:
            - Commit findings to long_term_memory
            - Publish SuccessSignal to NATS "hfo.result.success"
        And the phase duration MUST be < 10 seconds

    Scenario: PREY Loop - Agent Fails During EXECUTE Phase
        Given an agent is executing a ReactionPlan
        And one of the tool calls is web_scraper.fetch(url="https://invalid-url")
        When the tool raises an HTTPError exception
        Then the agent MUST catch the exception
        And log the error with trace_id to LangSmith
        And set ExecutionResult.status = "FAILED"
        And set ExecutionResult.error_message = str(exception)
        And transition to YIELD phase with the failed ExecutionResult
        And in YIELD phase, set YieldDecision.intent_satisfied = False
        And if retry_count < 3:
            - Set YieldDecision.should_retry = True
            - Add to audit_notes: "Tool failure: {tool_name}. Retrying with fallback."
            - Restart PREY loop with updated constraints
        And if retry_count >= 3:
            - Set YieldDecision.should_retry = False
            - Escalate to Navigator with HelpNeededSignal
            - Include all error_messages from 3 attempts

    Scenario: PREY Loop - PERCEIVE Phase Timeout
        Given an agent is in PERCEIVE phase
        And the web_search.execute() call is taking > 30 seconds
        When the phase timeout is exceeded
        Then the agent MUST terminate the web_search call
        And return a partial PerceptionResult with only memory_service results
        And log warning: "PERCEIVE timeout exceeded. Using partial context."
        And continue to REACT phase with reduced context
        And set a flag: perception_incomplete = True
        And in YIELD phase, reduce confidence_score by 0.2 due to incomplete perception

    Scenario: PREY Loop - Byzantine Retry After Consensus Failure
        Given an agent completed a PREY loop with YieldDecision.intent_satisfied = True
        And the agent is part of a Byzantine Quorum
        When the Byzantine vote indicates this agent is a potential hallucination
        Then the Swarmlord MUST send a RetrySignal to this agent
        And the agent MUST restart the PREY loop with additional constraint:
            "Previous attempt was flagged as outlier. Re-verify facts."
        And the retry_count MUST increment
        And the new attempt MUST use different sources (exclude previous URLs)
        And in the new YIELD phase, include audit note:
            "Byzantine retry #N. Changed approach to address consensus mismatch."

    Scenario: PREY Loop - Performance Budget Enforcement
        Given an agent has the following SLAs:
            | phase     | budget_seconds |
            | PERCEIVE  | 30             |
            | REACT     | 15             |
            | EXECUTE   | 120            |
            | YIELD     | 10             |
        When PERCEIVE takes 35 seconds (exceeds budget)
        Then the system MUST log a performance violation:
            "PERCEIVE exceeded budget: 35s > 30s (agent=Agent-001, mission_id=...)"
        And continue execution (non-blocking)
        And when EXECUTE takes 130 seconds (exceeds budget)
        Then the system MUST terminate EXECUTE phase
        And set ExecutionResult.status = "TIMEOUT"
        And transition to YIELD with the timeout status
        And the overall PREY loop MUST NOT exceed 180 seconds total
        And if total > 180 seconds, forcefully terminate and escalate

    Scenario: PREY Loop - Memory Commit with Vector Embedding
        Given an agent completed a PREY loop successfully
        And YieldDecision.intent_satisfied = True
        And YieldDecision.confidence_score >= 0.70
        When the agent commits to long_term_memory
        Then it MUST call memory_service.store(
            content=ExecutionResult.output,
            metadata={
                "mission_id": mission_intent.id,
                "agent_id": agent.agent_id,
                "confidence": confidence_score,
                "timestamp": datetime.utcnow()
            }
        )
        And the memory_service MUST generate a vector embedding via pgvector
        And create a MemoryNode in the Knowledge Graph
        And link the node to the MissionIntent with edge type "IMPLEMENTS"
        And the commit operation MUST complete in < 5 seconds
        And if commit fails, log error but DO NOT fail the PREY loop
