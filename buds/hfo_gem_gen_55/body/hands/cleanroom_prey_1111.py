"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: cleanroom-prey-1111-impl
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.8
    decay: 0.1
    created: '2025-11-26T12:00:00Z'
    generation: 55
  topos:
    address: buds/hfo_gem_gen_55/body/hands/cleanroom_prey_1111.py
    links: []
  telos:
    viral_factor: 0.0
    meme: cleanroom_prey_1111.py
"""

import asyncio
import logging
import uuid
import time
import os
from typing import List
from pydantic import BaseModel, Field
from body.hfo_sdk.stigmergy import StigmergyClient

# Setup Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("CleanroomPrey")

# --- Pydantic Models (The DNA) ---


class PerceptionReport(BaseModel):
    loop_id: int
    context_summary: str
    detected_artifacts: List[str]


class ReactionPlan(BaseModel):
    loop_id: int
    intent: str
    steps: List[str]


class ExecutionResult(BaseModel):
    loop_id: int
    status: str
    output: str


class YieldArtifact(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    loop_id: int
    content: str
    parent_artifacts: List[str]
    timestamp: float = Field(default_factory=time.time)


# --- The Agent ---


class PreyAgent:
    def __init__(self, agent_id: str, stigmergy: StigmergyClient):
        self.agent_id = agent_id
        self.stigmergy = stigmergy
        self.memory: List[YieldArtifact] = []

    async def perceive(self, loop_id: int) -> PerceptionReport:
        logger.info(f"[{self.agent_id}] Loop {loop_id}: Perceiving...")

        # Fetch history from Stigmergy (Hot State)
        # In a real scenario, we'd filter by relevant subjects
        # For this cleanroom test, we rely on the agent's internal memory
        # which simulates the "Accumulated Context" from the Gherkin spec.

        context = f"Loop {loop_id} Start."
        artifacts = []

        # "Iterative Context Accumulation"
        if self.memory:
            last_artifact = self.memory[-1]
            context += f" Previous Output: {last_artifact.content}"
            artifacts.append(last_artifact.id)
            logger.info(f"  -> Recalled previous artifact: {last_artifact.id}")
        else:
            logger.info("  -> No previous context (Genesis Loop)")

        return PerceptionReport(
            loop_id=loop_id, context_summary=context, detected_artifacts=artifacts
        )

    async def react(self, perception: PerceptionReport) -> ReactionPlan:
        logger.info(f"[{self.agent_id}] Loop {perception.loop_id}: Reacting...")
        # Simulate LLM thinking / Planning
        # In a full implementation, this would call Ollama/Gemma
        plan = ReactionPlan(
            loop_id=perception.loop_id,
            intent=f"Build upon {perception.context_summary}",
            steps=["Step 1: Analyze Context", "Step 2: Generate Increment"],
        )
        return plan

    async def execute(self, plan: ReactionPlan) -> ExecutionResult:
        logger.info(f"[{self.agent_id}] Loop {plan.loop_id}: Executing...")
        # Simulate work duration
        await asyncio.sleep(0.1)
        return ExecutionResult(
            loop_id=plan.loop_id, status="success", output=f"Result for {plan.intent}"
        )

    async def yield_phase(
        self, result: ExecutionResult, perception: PerceptionReport
    ) -> YieldArtifact:
        logger.info(f"[{self.agent_id}] Loop {result.loop_id}: Yielding...")

        artifact = YieldArtifact(
            loop_id=result.loop_id,
            content=result.output,
            parent_artifacts=perception.detected_artifacts,
        )

        # Publish to NATS (Hot Stigmergy)
        subject = f"hfo.mission.cleanroom.{self.agent_id}.loop{result.loop_id}"
        try:
            await self.stigmergy.publish(subject, artifact.model_dump())
            logger.info(f"  -> Published to NATS: {subject}")
        except Exception as e:
            logger.error(f"  -> Failed to publish to NATS: {e}")
            # In "Anytime Robustness", we might retry here, but for now we log.

        # Update local memory (Short-term episodic)
        self.memory.append(artifact)

        return artifact

    async def run_loop(self, loop_id: int):
        # Anytime Robustness: Retry logic could be wrapped here
        try:
            perception = await self.perceive(loop_id)
            reaction = await self.react(perception)
            execution = await self.execute(reaction)
            artifact = await self.yield_phase(execution, perception)
            logger.info(
                f"[{self.agent_id}] Loop {loop_id} Complete. Artifact: {artifact.id}"
            )
            return artifact
        except Exception as e:
            logger.error(f"[{self.agent_id}] Loop {loop_id} Failed: {e}")
            raise e


# --- Runner ---


async def main():
    # Ensure NATS URL is available
    if not os.getenv("NATS_URL"):
        os.environ["NATS_URL"] = "nats://localhost:4222"  # Default fallback

    stigmergy = StigmergyClient()
    try:
        await stigmergy.connect()
    except Exception as e:
        logger.warning(
            f"Could not connect to NATS: {e}. Proceeding in offline mode (local memory only)."
        )
        # Mocking publish for offline mode if needed, but StigmergyClient might raise error.
        # We'll let it fail or handle it in yield_phase.

    agent = PreyAgent(agent_id="cleanroom_tester", stigmergy=stigmergy)

    logger.info("Starting Cleanroom Genesis 1-1-1-1 Sequence")

    # The 3-Loop Test
    for i in range(1, 4):
        await agent.run_loop(i)

    logger.info("Sequence Complete.")


if __name__ == "__main__":
    asyncio.run(main())
