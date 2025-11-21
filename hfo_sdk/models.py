from pydantic import BaseModel, Field


class MissionIntent(BaseModel):
    description: str = Field(..., description="The high-level goal of the mission")
    domain: str = Field(
        default="general", description="The domain context (e.g., coding, research)"
    )


class SwarmConfig(BaseModel):
    cohort_size: int = Field(default=10, description="Total number of agents")
    disruptor_count: int = Field(default=1, description="Number of adversarial agents")
    model: str = Field(default="x-ai/grok-4.1-fast", description="LLM to use")
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


class ResultSignal(BaseModel):
    """A signal published by an agent (or controller) containing the result."""

    mission_id: str
    round_id: int
    agent_role: str
    content: str
    artifacts: list[str] = []
