"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: refinery-swarm-impl
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.9
    decay: 0.1
    created: '2025-11-26T18:45:00Z'
    generation: 55
  topos:
    address: body/hands/refinery_swarm.py
    links: []
  telos:
    viral_factor: 0.9
    meme: refinery_swarm.py
    mission: "Distill the Essence of HFO"
"""

import asyncio
import logging
import os
import json
import random
from datetime import datetime
from typing import Optional
from collections import deque
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
import nats
from nats.js.api import StreamConfig, RetentionPolicy

# --- Configuration ---
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL_NAME = "gemma3:270m"
API_KEY = "ollama"
LIVING_DOC_PATH = "brain/living_essence_hfo.md"

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("RefinerySwarm")


# --- Tools ---
class ToolSet:
    @staticmethod
    def list_dir(path: str = ".") -> str:
        """List files in a directory."""
        try:
            return str(os.listdir(path))
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def read_file(path: str) -> str:
        """Read the first 2000 chars of a file."""
        try:
            if not os.path.exists(path):
                return "Error: File not found."
            with open(path, "r") as f:
                return f.read()[:2000]
        except Exception as e:
            return f"Error: {e}"


# --- Pydantic Models for LLM ---


class EssenceFragment(BaseModel):
    topic: str = Field(
        ...,
        description="The specific concept being analyzed (e.g., 'Stigmergy', 'Fractal Holarchy')",
    )
    insight: str = Field(
        ..., description="A concise insight about this concept found in the code."
    )
    source_file: str = Field(..., description="The file read to gain this insight.")
    confidence: float = Field(
        ..., description="Confidence in this insight (0.0 to 1.0)"
    )


class RefineryAction(BaseModel):
    thought: str = Field(..., description="Reasoning process.")
    tool_call: Optional[str] = Field(
        None, description="Tool to call (e.g., 'read_file:AGENTS.md')"
    )
    yield_fragment: Optional[EssenceFragment] = Field(
        None, description="The essence fragment to publish."
    )


# --- The Agent ---


class RefineryAgent:
    def __init__(self, agent_id: str, nc, js, is_assimilator: bool = False):
        self.agent_id = agent_id
        self.nc = nc
        self.js = js
        self.is_assimilator = is_assimilator
        self.loop_count = 0
        self.memory: deque = deque(maxlen=10)

        # LLM Client
        self.client = instructor.patch(
            AsyncOpenAI(base_url=OLLAMA_BASE_URL, api_key=API_KEY),
            mode=instructor.Mode.JSON,
        )

    async def perceive(self) -> str:
        """Gather context from NATS and local state."""
        # In a real implementation, we'd read NATS messages here.
        # For now, we just return the last few memories.
        context = f"I am {self.agent_id}. I have seen: {list(self.memory)}"
        return context

    async def react(self, context: str) -> RefineryAction:
        """Ask the LLM what to do."""
        try:
            # Randomly pick a file to explore if no specific plan
            target_files = [
                "AGENTS.md",
                "README.md",
                "body/hfo_sdk/stigmergy.py",
                "brain/persona_swarmlord_of_webs.md",
            ]
            suggested_file = random.choice(target_files)

            prompt = f"""
            You are {self.agent_id}, a Refinery Agent in the Hive Fleet Obsidian.
            Your mission is to distill the ESSENCE of HFO.

            Context: {context}

            Available Tools:
            - read_file(path)
            - list_dir(path)

            Task:
            1. If you haven't read a file recently, choose one (e.g., {suggested_file}) and call 'read_file:<path>'.
            2. If you have read a file and found an insight, create a 'yield_fragment'.
            3. Keep your thoughts concise.
            """

            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI agent refining knowledge.",
                    },
                    {"role": "user", "content": prompt},
                ],
                response_model=RefineryAction,
                max_retries=2,
            )
            return response
        except Exception as e:
            logger.error(f"[{self.agent_id}] LLM Error: {e}")
            return RefineryAction(thought="LLM failed, sleeping.", tool_call=None)

    async def execute(self, action: RefineryAction):
        """Execute the tool call."""
        if action.tool_call:
            if action.tool_call.startswith("read_file:"):
                path = action.tool_call.split(":")[1].strip()
                content = ToolSet.read_file(path)
                self.memory.append(f"Read {path}: {content[:100]}...")
                logger.info(f"[{self.agent_id}] 📖 Read {path}")
            elif action.tool_call.startswith("list_dir:"):
                path = action.tool_call.split(":")[1].strip()
                content = ToolSet.list_dir(path)
                self.memory.append(f"List {path}: {content[:100]}...")

        if action.yield_fragment:
            await self.yield_insight(action.yield_fragment)

    async def yield_insight(self, fragment: EssenceFragment):
        """Publish the insight to NATS."""
        subject = f"hfo.refinery.{self.agent_id}"
        payload = fragment.model_dump_json()
        await self.js.publish(subject, payload.encode())
        logger.info(f"[{self.agent_id}] 💡 Yielded Insight: {fragment.topic}")

    async def run_lifecycle(self):
        logger.info(f"[{self.agent_id}] Online.")
        while True:
            # PREY Loop
            context = await self.perceive()
            action = await self.react(context)
            await self.execute(action)

            # Jitter
            await asyncio.sleep(random.uniform(2, 5))


class AssimilatorAgent(RefineryAgent):
    async def run_lifecycle(self):
        logger.info(f"[{self.agent_id}] Assimilator Online. Listening for insights...")

        async def cb(msg):
            try:
                data = json.loads(msg.data.decode())
                fragment = EssenceFragment(**data)
                await self.assimilate(fragment)
            except Exception as e:
                logger.error(f"Assimilator Error: {e}")

        await self.nc.subscribe("hfo.refinery.>", cb=cb)

        # Keep alive
        while True:
            await asyncio.sleep(1)

    async def assimilate(self, fragment: EssenceFragment):
        """Append to the Living Document."""
        entry = f"\n## {fragment.topic} (Confidence: {fragment.confidence})\n"
        entry += f"**Source**: `{fragment.source_file}`\n"
        entry += f"> {fragment.insight}\n"
        entry += f"*Captured by {self.agent_id} at {datetime.now().isoformat()}*\n"

        try:
            with open(LIVING_DOC_PATH, "a") as f:
                f.write(entry)
            logger.info(f"[{self.agent_id}] ✍️  Assimilated: {fragment.topic}")
        except Exception as e:
            logger.error(f"Failed to write to doc: {e}")


# --- Main ---


async def main():
    logger.info("🦅 HFO Refinery Swarm: Initializing...")

    # Initialize Living Doc
    if not os.path.exists(LIVING_DOC_PATH):
        with open(LIVING_DOC_PATH, "w") as f:
            f.write(
                "# 🦅 HFO Living Essence Document\n\n*Evolving insights from the Refinery Swarm.*\n"
            )

    try:
        nc = await nats.connect(NATS_URL)
        js = nc.jetstream()

        # Ensure Stream (Update if exists)
        subjects = ["hfo.mission.>", "hfo.heartbeat.>", "hfo.refinery.>"]
        config = StreamConfig(
            retention=RetentionPolicy.LIMITS,
            max_age=3600 * 24,
            storage="file",
            subjects=subjects,
        )

        try:
            await js.add_stream(name="HIVE_MIND", config=config)
        except Exception:
            await js.update_stream(name="HIVE_MIND", config=config)

    except Exception as e:
        logger.error(f"NATS Error: {e}")
        return

    # Spawn Agents
    # 1 Assimilator (Agent 0)
    # 3 Refinery Agents (Agents 1-3) - Small swarm for now
    agents = []
    agents.append(AssimilatorAgent("agent_0_assimilator", nc, js, is_assimilator=True))
    for i in range(1, 4):
        agents.append(RefineryAgent(f"agent_{i}_refiner", nc, js))

    logger.info(f"🚀 Launching {len(agents)} Agents (Model: {MODEL_NAME})...")

    try:
        await asyncio.gather(*(agent.run_lifecycle() for agent in agents))
    except asyncio.CancelledError:
        logger.info("🛑 Swarm Stopping...")
    finally:
        await nc.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
