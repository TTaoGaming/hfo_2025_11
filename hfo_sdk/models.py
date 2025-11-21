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
        default="/tmp/hfo_swarm", description="Directory for artifacts"
    )
