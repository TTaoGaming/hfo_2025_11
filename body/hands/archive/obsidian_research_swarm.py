import asyncio
import json
import logging
import uuid
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel
from body.config import Config

# HFO SDK & Models
from body.models.state import AgentRole
from body.hands.prey_agent import PreyAgent
from body.hfo_sdk.stigmergy import StigmergyClient

"""
🦅 Hive Fleet Obsidian: Obsidian Research Swarm
Intent: Implements the concurrent NATS-based research swarm (Karmic Hunt).
Linked to: brain/pattern_async_swarm.feature
"""

# Setup
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("SwarmController")

# Configuration
NATS_URL = Config.NATS_URL
SWARM_SIZE = 10  # Reduced from 50 to avoid local saturation
BATCH_SIZE = 5  # Run 5 agents at a time


class SwarmDigest(BaseModel):
    """The final synthesis of the swarm's work."""

    executive_summary: str
    consensus_points: List[str]
    dissenting_opinions: List[str]
    final_verdict: str
    confidence: float


class SwarmController:
    def __init__(self):
        self.stigmergy = StigmergyClient(NATS_URL)
        self.results = []

    async def run_mission(self, mission_text: str):
        logger.info(f"🦅 Swarm Controller Initiated. Mission: {mission_text}")

        # 1. Connect to Stigmergy (The Bus)
        await self.stigmergy.connect()

        # 2. Subscribe to Yield Signals (Gather Phase)
        # We listen for any agent yielding a result
        await self.stigmergy.nc.subscribe("hfo.mission.*.yield", cb=self._on_result)

        # 3. Scatter Phase (Launch Agents in Batches)
        agents = []
        for i in range(SWARM_SIZE):
            role = AgentRole.OBSERVER if i < SWARM_SIZE * 0.8 else AgentRole.DISRUPTOR
            agent_id = f"agent-{uuid.uuid4().hex[:4]}"
            agent = PreyAgent(agent_id, role, nats_url=NATS_URL)
            agents.append(agent)

        logger.info(f"🚀 Launching {SWARM_SIZE} Agents in batches of {BATCH_SIZE}...")

        # Semaphore to control concurrency
        sem = asyncio.Semaphore(BATCH_SIZE)

        async def run_agent_safe(agent):
            async with sem:
                try:
                    logger.info(f"▶️ Starting {agent.agent_id} ({agent.role})")
                    await agent.run(mission_text)
                    logger.info(f"✅ Finished {agent.agent_id}")
                except Exception as e:
                    logger.error(f"❌ Agent {agent.agent_id} failed: {e}")

        # Run all agents
        await asyncio.gather(*[run_agent_safe(a) for a in agents])

        # 4. Wait a moment for all messages to arrive via NATS
        logger.info("⏳ Waiting for Stigmergy signals to propagate...")
        await asyncio.sleep(2)

        # 5. Synthesize (Consensus Phase)
        digest = await self._synthesize_results(mission_text)

        # Output
        self._print_digest(digest)

        await self.stigmergy.close()

    async def _on_result(self, msg):
        """Callback for NATS messages."""
        try:
            data = json.loads(msg.data.decode())
            self.results.append(data)
            logger.info(f"📥 Received Yield from {msg.subject}")
        except Exception as e:
            logger.error(f"Failed to parse signal: {e}")

    async def _synthesize_results(self, mission_text: str) -> SwarmDigest:
        logger.info(f"🧠 Synthesizing {len(self.results)} results...")

        if not self.results:
            return SwarmDigest(
                executive_summary="No results collected.",
                consensus_points=[],
                dissenting_opinions=[],
                final_verdict="Failed.",
                confidence=0.0,
            )

        # Use a Navigator Agent (or just a direct LLM call via a temp agent) to synthesize
        # We'll reuse a PreyAgent class but just use its client for simplicity
        synthesizer = PreyAgent("synthesizer", AgentRole.NAVIGATOR, nats_url=NATS_URL)

        context = json.dumps(self.results, indent=2)
        prompt = f"""
        You are the Swarmlord.
        Mission: {mission_text}

        Swarm Results (Stigmergy):
        {context}

        Synthesize these findings into a final Swarm Digest.
        Identify consensus and dissent.
        """

        response = await synthesizer.client.chat.completions.create(
            model=synthesizer.model_name,
            response_model=SwarmDigest,
            messages=[{"role": "user", "content": prompt}],
        )
        return response

    def _print_digest(self, digest: SwarmDigest):
        print("\n" + "=" * 60)
        print("🦅 HIVE FLEET OBSIDIAN: SWARM DIGEST")
        print("=" * 60)
        print(f"Confidence: {digest.confidence}")
        print(f"Verdict: {digest.final_verdict}")
        print("\n## Executive Summary")
        print(digest.executive_summary)
        print("\n## Consensus Points")
        for p in digest.consensus_points:
            print(f"- {p}")
        print("\n## Dissenting Opinions")
        for d in digest.dissenting_opinions:
            print(f"- {d}")
        print("=" * 60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the Obsidian Research Swarm")
    parser.add_argument("--mission", type=str, help="The mission intent", default=None)
    args = parser.parse_args()

    default_mission = (
        "Analyze the 'Obsidian Horizon Hourglass' workflow defined in 'brain/workflow_obsidian_hourglass.feature'. "
        "Discuss the 'True Worth' of this algorithm. Is it the 'Strongest Thing'? "
        "How does the 'Evolutionary Built-in' cause it to get better with use? "
        "Provide a critical assessment of its potential vs. implementation complexity."
    )

    mission_text = args.mission if args.mission else default_mission

    controller = SwarmController()
    asyncio.run(controller.run_mission(mission_text))
