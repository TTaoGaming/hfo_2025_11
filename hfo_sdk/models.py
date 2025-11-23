"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 3ec25aaa-86aa-4df5-aa80-12faf39fd612
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.604863+00:00'
    generation: 51
  topos:
    address: hfo_sdk/models.py
    links: []
  telos:
    viral_factor: 0.0
    meme: models.py
"""

from pydantic import BaseModel, Field


from body.constants import DEFAULT_MODEL


class MissionIntent(BaseModel):
    description: str = Field(..., description="The high-level goal of the mission")
    domain: str = Field(
        default="general", description="The domain context (e.g., coding, research)"
    )


class SwarmConfig(BaseModel):
    cohort_size: int = Field(default=10, description="Total number of agents")
    disruptor_count: int = Field(default=1, description="Number of adversarial agents")
    model: str = Field(default=DEFAULT_MODEL, description="LLM to use")
    base_output_dir: str = Field(
        default="memory/episodic", description="Directory for artifacts"
    )
    nats_url: str = Field(
        default="nats://localhost:4222", description="NATS JetStream URL"
    )


class MissionSignal(BaseModel):
    """A signal published to NATS to initiate a mission round."""

    mission_id: str
    round_id: int
    intent: MissionIntent
    context: str = Field(default="", description="Context from previous rounds")
    tags: list[str] = Field(
        default_factory=list, description="Semantic tags for the mission"
    )
    priority: int = Field(default=1, description="Priority level (1-5)")


class ResultSignal(BaseModel):
    """A signal published by an agent (or controller) containing the result."""

    mission_id: str
    round_id: int
    agent_role: str
    content: str
    artifacts: list[str] = []
    confidence: float = Field(default=0.0, description="Self-reported confidence score")
    references: list[str] = Field(
        default_factory=list, description="Links to other artifacts or signals"
    )
