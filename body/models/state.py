from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime
from .intent import MissionIntent

class AgentRole(str, Enum):
    NAVIGATOR = "Navigator"   # Commander
    OBSERVER = "Observer"     # Sensor
    BRIDGER = "Bridger"       # Communicator
    SHAPER = "Shaper"         # Effector
    INJECTOR = "Injector"     # Logistics
    DISRUPTOR = "Disruptor"   # Red Team
    IMMUNIZER = "Immunizer"   # Blue Team
    ASSIMILATOR = "Assimilator" # Learner

class PreyStep(str, Enum):
    PERCEIVE = "Perceive"
    REACT = "React"
    EXECUTE = "Execute"
    YIELD = "Yield"
    IDLE = "Idle"

class AgentState(BaseModel):
    """
    Represents the state of a single agent in the PREY loop.
    Used by LangGraph to manage state transitions.
    """
    agent_id: str
    role: AgentRole

    # Current Operational Context
    current_mission: Optional[MissionIntent] = None
    current_step: PreyStep = PreyStep.IDLE

    # Memory & Context
    short_term_memory: List[str] = Field(default_factory=list)
    tools_available: List[str] = Field(default_factory=list)

    # Telemetry
    last_heartbeat: datetime = Field(default_factory=datetime.utcnow)
    confidence_score: float = Field(default=0.0, ge=0.0, le=1.0)

    def update_heartbeat(self):
        self.last_heartbeat = datetime.utcnow()

class SwarmTelemetry(BaseModel):
    """
    High-level metrics for the Swarmlord Facade (Scalable View).
    Used when managing thousands/millions of agents where individual state tracking is too expensive.
    """
    total_agents: int = 0
    active_agents_count: int = 0
    agents_by_role: Dict[AgentRole, int] = Field(default_factory=dict)
    average_confidence: float = 0.0
    global_throughput_tps: float = 0.0
    system_health: float = 1.0

class SwarmPhase(str, Enum):
    SET = "Set"
    WATCH = "Watch"
    ACT = "Act"
    REVIEW = "Review"
    MUTATE = "Mutate"

class SwarmState(BaseModel):
    """
    Represents the collective state of the Hive Fleet (Level 1 Loop).
    """
    generation_id: int
    phase: SwarmPhase = SwarmPhase.SET

    # The Collective (Detailed View - for small swarms)
    active_agents: Dict[str, AgentState] = Field(default_factory=dict)

    # The Collective (Aggregate View - for massive swarms)
    telemetry: Optional[SwarmTelemetry] = None

    # Evolution State (DSPy & MAP-Elites)
    current_dspy_prompt: Optional[str] = Field(default=None, description="The current optimized prompt signature")
    mutation_history: List[str] = Field(default_factory=list, description="Log of mutations applied")

    # The Blackboard (Stigmergy)
    blackboard: Dict[str, Any] = Field(default_factory=dict)

    # Consensus
    quorum_reached: bool = False
    consensus_confidence: float = 0.0
