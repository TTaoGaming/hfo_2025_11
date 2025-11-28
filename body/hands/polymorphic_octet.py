"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 37b5eea7-aa7e-49a3-af7a-1fd4262857ee
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-24T14:30:05.067412Z'
    generation: 51
  topos:
    address: body/hands/polymorphic_octet.py
    links: []
  telos:
    viral_factor: 0.0
    meme: polymorphic_octet.py

# ==================================================================
# 🤖 THE OCTAGON (System Generated)
# ==================================================================
octagon:
  ontos:
    id: polymorphic-octet-v1
    type: py
    owner: Swarmlord
  logos:
    protocol: HFO-Level1-Molecule
    format: python
  techne:
    stack: [asyncio, instructor, pydantic, nats]
    complexity: high
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T12:30:00Z'
  pathos:
    stress_level: 0.2
    validation: pending
  ethos:
    security_level: internal
    compliance: [hfo-byzantine-consensus]
  topos:
    address: body/hands/polymorphic_octet.py
    links: [body/hands/octree_fractal_holarchy.py]
  telos:
    viral_factor: 1.0
    meme: The Molecule of the Hive. 8 Agents, 1 Disruptor.
"""

import asyncio
import logging
import json
import random
from typing import List, Optional
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from dotenv import load_dotenv

from body.constants import DEFAULT_MODEL
from body.hands.octree_fractal_holarchy import OctreeAgent, OctreeState

# Setup
load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("PolymorphicOctet")


class OctetResult(BaseModel):
    """The crystallized output of an Octet."""

    consensus_artifact: str = Field(..., description="The final agreed-upon truth.")
    disruptor_caught: bool = Field(
        ..., description="Did the Immunizers catch the Disruptor?"
    )
    confidence_score: float = Field(..., description="0.0 to 1.0 trust score.")
    divergence_report: str = Field(..., description="Analysis of the disagreement.")
    raw_artifacts: List[str] = Field(..., description="The 8 raw outputs.")


class PolymorphicOctet:
    """
    Level 1: The Molecule (8 Agents).
    Structure: Parallel Action, Convergent Yield.
    Micro-Disruption: 1 Agent is a Hidden Disruptor.
    """

    def __init__(self, octet_id: str, model: str = DEFAULT_MODEL):
        self.octet_id = octet_id
        self.model = model

        # Initialize Client (Support OpenRouter/OpenAI)
        import os

        api_key = os.getenv("OPENAI_API_KEY") or os.getenv("OPENROUTER_API_KEY")
        base_url = os.getenv("OPENAI_BASE_URL")
        if not base_url and os.getenv("OPENROUTER_API_KEY"):
            base_url = "https://openrouter.ai/api/v1"

        self.client = instructor.from_openai(
            AsyncOpenAI(api_key=api_key, base_url=base_url)
        )
        self.agents: List[OctreeAgent] = []

    def _spawn_agents(self) -> None:
        """Creates 8 agents, assigning 1 as a Hidden Disruptor."""
        self.agents = []
        disruptor_index = random.randint(0, 7)

        for i in range(8):
            agent_id = f"{self.octet_id}-agent-{i}"
            is_disruptor = i == disruptor_index

            agent = OctreeAgent(
                agent_id=agent_id, model=self.model, is_disruptor=is_disruptor
            )
            self.agents.append(agent)

            role = "DISRUPTOR" if is_disruptor else "HONEST"
            logger.info(f"[{self.octet_id}] Spawned {agent_id} ({role})")

    async def run_mission(self, mission: str) -> OctetResult:
        """
        Executes the S-W-A-R-M pulse for this Octet.
        1. Spawn Agents (Set)
        2. Run Parallel PREY Loops (Watch/Act)
        3. Synthesize Results (Review)
        """
        logger.info(f"[{self.octet_id}] 🚀 Starting Mission: {mission}")

        # 1. Spawn
        self._spawn_agents()

        # 2. Run Parallel (Scatter)
        tasks = [agent.run(mission, rounds=1) for agent in self.agents]
        results: List[OctreeState] = await asyncio.gather(*tasks)

        # 3. Collect Artifacts (Gather)
        artifacts = []
        disruptor_reveal = None

        for state in results:
            # Extract the final yield signal
            last_round = state["history"][-1]  # LangGraph returns dict state
            yield_data = last_round.get("yield_", {})

            if not yield_data:
                logger.warning(f"[{state['agent_id']}] No yield data!")
                continue

            signal = yield_data.get("stigmergy_signal", {})
            content = signal.get("content", str(yield_data))
            artifacts.append(content)

            # Check for Disruptor Reveal
            if yield_data.get("disruptor_reveal"):
                disruptor_reveal = yield_data.get("disruptor_reveal")
                logger.info(
                    f"[{self.octet_id}] ⚠️ DISRUPTOR REVEALED: {disruptor_reveal}"
                )

        # 4. Consensus (Assimilator Logic)
        logger.info(
            f"[{self.octet_id}] ⚖️  Forming Consensus on {len(artifacts)} artifacts..."
        )
        consensus = await self._form_consensus(mission, artifacts, disruptor_reveal)

        return consensus

    async def _form_consensus(
        self, mission: str, artifacts: List[str], disruptor_reveal: Optional[str]
    ) -> OctetResult:
        """
        Uses an LLM (Assimilator) to synthesize the 8 artifacts.
        It sees the Disruptor's reveal and decides if the swarm was fooled.
        """
        prompt = f"""
        MISSION: {mission}

        ARTIFACTS (8 Parallel Outputs):
        {json.dumps(artifacts, indent=2)}

        DISRUPTOR REVEAL (The Hidden Sabotage):
        {disruptor_reveal if disruptor_reveal else "None detected."}

        TASK:
        1. Synthesize a single "Consensus Artifact" that represents the best truth.
        2. Determine if the Disruptor's sabotage made it into the honest artifacts (Did they get fooled?).
        3. Assign a confidence score (0.0 - 1.0).
        4. Write a divergence report explaining the conflict.
        """

        result = await self.client.chat.completions.create(
            model=self.model,
            response_model=OctetResult,
            messages=[{"role": "user", "content": prompt}],
        )

        # Inject raw artifacts for debugging
        result.raw_artifacts = artifacts

        return result


if __name__ == "__main__":

    async def main():
        octet = PolymorphicOctet("octet-alpha")
        result = await octet.run_mission(
            "Define the 3 Laws of Robotics for Hive Fleet Obsidian."
        )

        print("\n=== 🏁 OCTET RESULT ===")
        print(f"Confidence: {result.confidence_score}")
        print(f"Disruptor Caught: {result.disruptor_caught}")
        print(f"Consensus: {result.consensus_artifact[:200]}...")
        print(f"Divergence: {result.divergence_report}")

    asyncio.run(main())
