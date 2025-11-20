"""
Missing Pydantic Models - Fill Intent-Implementation Gap

These models are referenced in Gherkin specs but don't exist in src/models/.
Add these to bridge the gap between intent and implementation.
"""

from typing import List, Dict, Any, Literal, Optional
from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum


# ============================================================================
# PREY Loop Artifacts (Referenced in prey_workflow.feature)
# ============================================================================

class ContextObject(BaseModel):
    """
    Output of the Perceive phase.
    Gherkin: 'And it should output a "Context Object" containing raw data'
    """
    raw_data: Dict[str, Any] = Field(
        ..., 
        description="Unprocessed data gathered from tools (search results, docs, etc.)"
    )
    sources: List[str] = Field(
        default_factory=list,
        description="List of sources (URLs, file paths, API endpoints)"
    )
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    
    # Metadata for memory limits scenario
    original_size_mb: Optional[float] = Field(None, description="Original size before compression")
    compressed: bool = Field(False, description="Was context compressed due to size limits?")
    truncated: bool = Field(False, description="Was context truncated (sampled)?")
    sampled_sources: Optional[int] = Field(None, description="Number of sources after sampling")


class Plan(BaseModel):
    """
    Output of the React phase.
    Gherkin: 'Then it should generate a "Plan" with specific steps'
    """
    steps: List[str] = Field(
        ..., 
        description="Ordered list of actions to execute"
    )
    reasoning: str = Field(
        ..., 
        description="Explanation of why this plan was chosen"
    )
    case_based_examples: List[str] = Field(
        default_factory=list,
        description="Similar past missions used for Case-Based Reasoning"
    )
    cynefin_domain: Optional[Literal["clear", "complicated", "complex", "chaotic"]] = Field(
        None,
        description="Cynefin Framework classification of the problem"
    )


class ExecutionStatus(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    PARTIAL = "partial"


class ExecutionResult(BaseModel):
    """
    Output of the Execute phase.
    Gherkin: 'And it should produce an "Execution Result"'
    """
    status: ExecutionStatus = Field(
        ..., 
        description="Outcome of execution"
    )
    outputs: Dict[str, Any] = Field(
        default_factory=dict,
        description="Results produced (code, text, data, etc.)"
    )
    errors: List[str] = Field(
        default_factory=list,
        description="List of errors encountered (if any)"
    )
    
    # For retry detection scenario
    retry_count: int = Field(
        default=0, 
        description="Number of retries so far"
    )
    previous_results: List[str] = Field(
        default_factory=list,
        description="Hashes of previous results (for detecting infinite loops)"
    )


# ============================================================================
# Byzantine Quorum Configuration (Referenced in swarm_workflow.feature)
# ============================================================================

class VoteAggregationMethod(str, Enum):
    MAJORITY = "majority"  # Simple majority (50%+1)
    WEIGHTED_CONFIDENCE = "weighted_confidence"  # sum(conf * verdict) / sum(conf)
    SUPERMAJORITY = "supermajority"  # 66%+ required


class QuorumConfig(BaseModel):
    """
    Explicit Byzantine Quorum parameters.
    Gherkin: 'And the quorum configuration is...'
    
    This was MISSING from MissionIntent and caused ambiguity.
    """
    threshold: float = Field(
        0.7, 
        ge=0.5, 
        le=1.0,
        description="Minimum agreement required (e.g., 0.7 = 7/10 agents)"
    )
    vote_aggregation: VoteAggregationMethod = Field(
        VoteAggregationMethod.WEIGHTED_CONFIDENCE,
        description="Method for combining votes"
    )
    confidence_cap: float = Field(
        0.9,
        ge=0.0,
        le=1.0,
        description="If consensus exceeds this, trigger adversarial re-review"
    )
    timeout_seconds: int = Field(
        60,
        ge=1,
        description="Max time to wait for votes"
    )
    min_participating: int = Field(
        7,
        ge=1,
        description="Minimum agents required for valid quorum"
    )
    
    # For task-aware confidence cap
    task_subjectivity: Optional[float] = Field(
        None,
        ge=0.0,
        le=1.0,
        description="0=deterministic (math), 1=fully subjective (art). Affects cap."
    )


# ============================================================================
# MAP-Elites Archive Configuration (Referenced in swarm_workflow.feature)
# ============================================================================

class BehaviorDimension(BaseModel):
    """A single dimension in the MAP-Elites behavior space."""
    name: str = Field(..., description="Dimension name (e.g., 'cost', 'accuracy')")
    bins: int = Field(10, ge=2, le=100, description="Number of bins for discretization")
    min_value: float = Field(..., description="Minimum value of the dimension")
    max_value: float = Field(..., description="Maximum value of the dimension")


class QDArchiveConfig(BaseModel):
    """
    Quality-Diversity (MAP-Elites) evolution parameters.
    Gherkin: 'Given a MAP-Elites archive with dimensions...'
    
    This was MISSING and caused "Mutate" phase to be underspecified.
    """
    behavior_dimensions: List[BehaviorDimension] = Field(
        ...,
        description="Behavior space dimensions (e.g., [cost, accuracy])"
    )
    mutation_operator: str = Field(
        "gpt4_paraphrase",
        description="How to mutate prompts/configurations"
    )
    mutation_temperature: float = Field(
        0.7,
        ge=0.0,
        le=2.0,
        description="Randomness in mutation (0=deterministic, 2=very random)"
    )
    validation_set_size: int = Field(
        50,
        ge=10,
        description="Number of test cases for evaluating variants"
    )
    fitness_objectives: List[str] = Field(
        default_factory=lambda: ["accuracy", "cost"],
        description="Objectives to optimize (can be multi-objective)"
    )


# ============================================================================
# Search Space (Referenced in swarm_workflow.feature)
# ============================================================================

class SearchSpace(BaseModel):
    """
    Defines the space of possible solutions for evolution.
    Gherkin: 'And defines the "Search Space" for evolution'
    """
    parameter_ranges: Dict[str, tuple[float, float]] = Field(
        default_factory=dict,
        description="Ranges for each tunable parameter (e.g., {'temperature': (0.0, 2.0)})"
    )
    categorical_options: Dict[str, List[str]] = Field(
        default_factory=dict,
        description="Categorical choices (e.g., {'model': ['gpt-4', 'claude-3']})"
    )
    constraints: List[str] = Field(
        default_factory=list,
        description="Hard constraints (e.g., 'cost < $0.30')"
    )


# ============================================================================
# Additional Signals (Not in signals.py but referenced in Gherkin)
# ============================================================================

class ResultSignal(BaseModel):
    """
    Published by PREY agent when execution completes.
    Gherkin: 'Then it should publish a "ResultSignal" to "hfo.result.completed"'
    """
    agent_id: str
    mission_id: str
    execution_result: ExecutionResult
    self_audit_passed: bool = Field(
        ..., 
        description="Did the agent's self-audit pass?"
    )
    confidence: float = Field(..., ge=0.0, le=1.0)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class BlockedSignal(BaseModel):
    """
    Published when agent gets stuck in infinite retry.
    Gherkin: 'And publish a "BlockedSignal" to "hfo.agent.blocked"'
    """
    agent_id: str
    mission_id: str
    retry_count: int
    last_error: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class MissionAbortSignal(BaseModel):
    """
    Published when mission is aborted due to insufficient agents.
    Gherkin: 'And publish "MissionAbortSignal" to "hfo.mission.aborted"'
    """
    mission_id: str
    reason: str
    remaining_agents: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)


# ============================================================================
# Validation Set (Referenced in MAP-Elites scenario)
# ============================================================================

class ValidationCase(BaseModel):
    """A single test case for evaluating prompt/config quality."""
    input: str = Field(..., description="Test input")
    expected_output: str = Field(..., description="Ground truth output")
    category: Optional[str] = Field(None, description="Test category (e.g., 'math', 'reasoning')")


class ValidationSet(BaseModel):
    """
    Collection of test cases for MAP-Elites evaluation.
    Gherkin: 'And a validation set of 50 test cases'
    """
    cases: List[ValidationCase] = Field(
        ..., 
        min_length=1,
        description="Test cases"
    )
    metadata: Dict[str, Any] = Field(
        default_factory=dict,
        description="Metadata about the validation set (creation date, source, etc.)"
    )


# ============================================================================
# Usage Example (for documentation)
# ============================================================================

if __name__ == "__main__":
    # Example: Create a QuorumConfig for a Byzantine vote
    quorum = QuorumConfig(
        threshold=0.7,
        vote_aggregation=VoteAggregationMethod.WEIGHTED_CONFIDENCE,
        confidence_cap=0.9,
        timeout_seconds=60,
        min_participating=7
    )
    print("Quorum Config:", quorum.model_dump_json(indent=2))
    
    # Example: Create a QD Archive for MAP-Elites
    archive = QDArchiveConfig(
        behavior_dimensions=[
            BehaviorDimension(name="cost", bins=10, min_value=0.0, max_value=1.0),
            BehaviorDimension(name="accuracy", bins=10, min_value=0.0, max_value=1.0),
        ],
        mutation_operator="gpt4_paraphrase",
        mutation_temperature=0.7,
        validation_set_size=50
    )
    print("QD Archive Config:", archive.model_dump_json(indent=2))
