from enum import Enum
from typing import Dict, Any, Optional
from pydantic import BaseModel, Field, UUID4
from datetime import datetime
import uuid
from .intent import MissionIntent
from .state import AgentRole, IntentStatus

class SignalType(str, Enum):
    HEARTBEAT = "heartbeat"
    MISSION = "mission"
    VOTE = "vote"
    CONSENSUS = "consensus"
    DISRUPTION = "disruption"

class BaseSignal(BaseModel):
    """Base class for all Stigmergy signals (The 'Webs')."""
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    type: SignalType
    producer_id: str = Field(..., description="ID of the agent producing the signal")

    class Config:
        use_enum_values = True

class HeartbeatSignal(BaseSignal):
    """Proof of Life from an agent."""
    type: SignalType = SignalType.HEARTBEAT
    role: AgentRole
    status: str = "active"
    current_step: str = "idle"
    metrics: Dict[str, float] = Field(default_factory=dict, description="Health/Performance metrics")

class MissionSignal(BaseSignal):
    """Command from the Swarmlord to the Hive."""
    type: SignalType = SignalType.MISSION
    mission: MissionIntent
    priority: int = Field(default=1, ge=1, le=5)
    target_roles: list[AgentRole] = Field(default_factory=list, description="Roles required for this mission")

class VoteSignal(BaseSignal):
    """Byzantine vote from a Reviewer/Immunizer."""
    type: SignalType = SignalType.VOTE
    mission_id: UUID4
    verdict: bool = Field(..., description="True = Approve, False = Reject")
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasoning: str

class ConsensusSignal(BaseSignal):
    """Final decision reached by the Quorum."""
    type: SignalType = SignalType.CONSENSUS
    mission_id: UUID4
    approved: bool
    final_confidence: float
    participating_agents: int
    quorum_met: bool

class DisruptionSignal(BaseSignal):
    """Noise injected by a Disruptor or detected anomaly."""
    type: SignalType = SignalType.DISRUPTION
    target_mission_id: Optional[UUID4] = None
    noise_level: float = Field(default=0.5, ge=0.0, le=1.0)
    payload: Dict[str, Any] = Field(default_factory=dict)
