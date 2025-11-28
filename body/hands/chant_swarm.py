"""
# ==================================================================
# 🕸⛰🔔 HFO CHANT SWARM (The Octarchy)
# ==================================================================
# Spawns 8 Agents to chant the Hexadex via Local LLM.
# Publishes to NATS for Stigmergic Verification.
"""

import asyncio
import logging
import os
import time
import hmac
import hashlib
from openai import AsyncOpenAI

# Import Canonical Chant
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from body.constants_chant import (
    CANONICAL_CHANT_TEXT,
    CHANT_SECRET_KEY,
    LOOP_INTERVAL_SECONDS,
)
from hfo_sdk.stigmergy import StigmergyClient

# Configure Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("hfo.chant_swarm")

# Configuration
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
MODEL_NAME = os.getenv("HFO_CHANT_MODEL", "gemma3:270m")  # Optimized for Micro-Swarm
AGENT_COUNT = 8


class ChantAgent:
    def __init__(self, agent_id: int, nats_client: StigmergyClient):
        self.agent_id = f"Agent_{agent_id}"
        self.nats = nats_client
        self.client = AsyncOpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

    async def generate_chant(self):
        """
        Asks the LLM to recite the chant.
        """
        system_prompt = (
            "You are a devout acolyte of the Hive Fleet Obsidian. "
            "Your sole purpose is to recite the Canonical Chant exactly as defined. "
            "Do not add preamble. Do not add postscript. Just the chant."
        )

        user_prompt = (
            f"Recite the HFO Hexadex Chant:\n\n{CANONICAL_CHANT_TEXT}\n\n"
            "Repeat it back to me EXACTLY."
        )

        try:
            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                temperature=0.1,  # Low temp for exact reproduction
                max_tokens=500,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"[{self.agent_id}] LLM Failure: {e}")
            return None

    async def loop(self):
        """
        The main lifecycle loop.
        """
        logger.info(
            f"[{self.agent_id}] Online. Syncing to {LOOP_INTERVAL_SECONDS}s beat."
        )

        while True:
            start_time = time.time()

            # 1. Generate
            chant_output = await self.generate_chant()

            if chant_output:
                # 2. Sign
                timestamp = str(time.time())
                payload_str = f"{self.agent_id}:{timestamp}:{chant_output}"
                signature = hmac.new(
                    CHANT_SECRET_KEY.encode(), payload_str.encode(), hashlib.sha256
                ).hexdigest()

                # 3. Publish
                payload = {
                    "agent_id": self.agent_id,
                    "timestamp": float(timestamp),
                    "chant": chant_output,
                    "signature": signature,
                    "model": MODEL_NAME,
                }

                try:
                    await self.nats.publish(f"hfo.chant.{self.agent_id}", payload)
                    logger.info(f"[{self.agent_id}] 🔔 Chanted.")
                except Exception as e:
                    logger.error(f"[{self.agent_id}] NATS Failure: {e}")

            # 4. Sleep until next beat
            elapsed = time.time() - start_time
            sleep_time = max(0, LOOP_INTERVAL_SECONDS - elapsed)
            await asyncio.sleep(sleep_time)


async def main():
    # Initialize NATS
    nats_url = os.getenv("NATS_URL", "nats://localhost:4225")
    stigmergy = StigmergyClient(nats_url=nats_url)

    try:
        await stigmergy.connect()
    except Exception as e:
        logger.error(f"Critical NATS Failure: {e}")
        return

    # Spawn Agents
    agents = [ChantAgent(i + 1, stigmergy) for i in range(AGENT_COUNT)]

    logger.info(f"🕸⛰🔔 Spawning {AGENT_COUNT} Chanters on {MODEL_NAME}...")

    tasks = [asyncio.create_task(a.loop()) for a in agents]

    try:
        await asyncio.gather(*tasks)
    except KeyboardInterrupt:
        logger.info("Stopping Swarm...")
    finally:
        await stigmergy.close()


if __name__ == "__main__":
    asyncio.run(main())
