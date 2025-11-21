from enum import Enum
from typing import List, Dict, Any
from pydantic import BaseModel, Field, UUID4
from datetime import datetime
import uuid


class IntentStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"


class Constraint(BaseModel):
    """A specific constraint or rule that must be followed."""

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    description: str
    is_hard_constraint: bool = True


class MissionIntent(BaseModel):
    """
    The Single Source of Truth (SSOT) for a User's Intent.
    Maps to the 'Set' phase of the SWARM loop.
    """

    id: UUID4 = Field(default_factory=uuid.uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    # The 'What' and 'Why'
    description: str = Field(..., description="High-level description of the mission")
    rationale: str = Field(
        ..., description="Why this mission is important (Commander's Intent)"
    )

    # The 'How' (Constraints)
    constraints: List[Constraint] = Field(default_factory=list)

    # Swarm Configuration (SSOT for Act/Mutate)
    swarm_size: int = Field(default=10, ge=1, description="Total number of agents")
    disruptor_min: int = Field(
        default=1, ge=0, description="Minimum number of disruptors"
    )
    disruptor_max: int = Field(
        default=3, ge=0, description="Maximum number of disruptors"
    )
    evolution_strategy: str = Field(
        default="MAP-Elites+DSPy", description="Strategy for the Mutate phase"
    )

    # Model Strategy (FinOps)
    coordination_model_group: str = Field(
        default="Cheap Navigators", description="Model group for coordination/planning"
    )
    execution_model_group: str = Field(
        default="Cheap QD Swarm", description="Model group for execution/workers"
    )
    excluded_models: List[str] = Field(
        default_factory=list, description="List of explicitly excluded models"
    )

    # Success Criteria (Gherkin mapping)
    acceptance_criteria: List[str] = Field(
        default_factory=list,
        description="List of Gherkin scenarios or success conditions",
    )

    status: IntentStatus = IntentStatus.PENDING
    metadata: Dict[str, Any] = Field(default_factory=dict)
