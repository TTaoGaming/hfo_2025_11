"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440022
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-26T12:00:00.000000Z'
    generation: 51
  topos:
    address: body/hands/test_model_coliseum.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_model_coliseum.py
# ==================================================================
# MODEL COLISEUM: The Stigmergy Gauntlet
# ==================================================================
# Goal: Benchmark Local Models for Swarm Intelligence vs. Efficiency
# Constraint: 8GB RAM Total (Target < 6GB Usage)
# ==================================================================
"""

import asyncio
import time
import logging
import psutil
from typing import List, Dict, Any
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI

# --- Configuration ---
MODELS = ["gemma3:270m", "qwen2.5:1.5b", "gemma3:1b", "smollm2:1.7b"]

CONCURRENCY_LEVELS = [1, 4, 8]
OLLAMA_BASE_URL = "http://localhost:11434/v1"
API_KEY = "ollama"

# Setup Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("Coliseum")


# --- Pydantic Schema (The Gauntlet) ---
class StigmergySignal(BaseModel):
    # The standard unit of communication in the Hive.
    id: str = Field(..., description="Unique UUID")
    type: str = Field(
        ..., description="Type of signal: 'discovery', 'alert', 'heartbeat'"
    )
    content: str = Field(..., description="The core message")
    complexity_score: float = Field(..., description="0.0 to 1.0")
    tags: List[str] = Field(..., description="Relevant tags")


# --- The Test Agent ---
class GladiatorAgent:
    def __init__(self, model: str, agent_id: int):
        self.model = model
        self.agent_id = agent_id
        self.client = instructor.patch(
            AsyncOpenAI(base_url=OLLAMA_BASE_URL, api_key=API_KEY),
            mode=instructor.Mode.JSON,
        )

    async def run_gauntlet(self) -> Dict[str, Any]:
        start_time = time.time()
        prompt = (
            f"You are Agent {self.agent_id}. "
            "Analyze this log entry: 'System pressure critical. Memory usage at 92%. Recommendation: Purge cache.' "
            "1. Classify the type (alert/discovery). "
            "2. Extract the content. "
            "3. Rate complexity (0.0-1.0). "
            "4. Tag it (e.g., 'memory', 'ops')."
        )

        result = {
            "agent_id": self.agent_id,
            "model": self.model,
            "success": False,
            "latency": 0.0,
            "error": None,
        }

        try:
            _ = await self.client.chat.completions.create(
                model=self.model,
                response_model=StigmergySignal,
                messages=[{"role": "user", "content": prompt}],
                max_retries=1,  # Fail fast for benchmarking
            )
            result["success"] = True
        except Exception as e:
            result["error"] = str(e)

        result["latency"] = time.time() - start_time
        return result


# --- The Arena ---
async def run_round(model: str, concurrency: int):
    logger.info(f"⚔️  ROUND START: {model} x {concurrency} Agents")

    agents = [GladiatorAgent(model, i) for i in range(concurrency)]
    tasks = [agent.run_gauntlet() for agent in agents]

    # Measure System RAM before
    mem_before = psutil.virtual_memory().percent

    start_time = time.time()
    results = await asyncio.gather(*tasks)
    total_time = time.time() - start_time

    # Measure System RAM after
    mem_after = psutil.virtual_memory().percent

    # Analysis
    success_count = sum(1 for r in results if r["success"])
    avg_latency = sum(r["latency"] for r in results) / concurrency

    logger.info(f"🏁 ROUND END: {model} x {concurrency}")
    logger.info(
        f"   Success Rate: {success_count}/{concurrency} ({success_count/concurrency*100:.1f}%)"
    )
    logger.info(f"   Total Time: {total_time:.2f}s")
    logger.info(f"   Avg Latency: {avg_latency:.2f}s")
    logger.info(
        f"   RAM Impact: {mem_before}% -> {mem_after}% (Delta: {mem_after - mem_before}%)"
    )

    return {
        "model": model,
        "concurrency": concurrency,
        "success_rate": success_count / concurrency,
        "avg_latency": avg_latency,
        "ram_delta": mem_after - mem_before,
        "ram_peak": mem_after,
    }


async def main():
    logger.info("🏟️  OPENING THE MODEL COLISEUM")
    logger.info("=================================")

    scoreboard = []

    for model in MODELS:
        logger.info(f"\n--- Testing Model: {model} ---")

        # Warmup (1 Agent)
        await run_round(model, 1)

        # Squad (4 Agents)
        await run_round(model, 4)

        # Octarchy (8 Agents) - The Ultimate Test
        res = await run_round(model, 8)
        scoreboard.append(res)

        # Cooldown to let RAM settle
        time.sleep(2)

    logger.info("\n🏆 FINAL SCOREBOARD (8 AGENTS) 🏆")
    logger.info(f"{'Model':<20} | {'Success':<10} | {'Latency':<10} | {'RAM Peak':<10}")
    logger.info("-" * 60)
    for score in scoreboard:
        logger.info(
            f"{score['model']:<20} | {score['success_rate']*100:.0f}%       | {score['avg_latency']:.2f}s      | {score['ram_peak']}%"
        )


if __name__ == "__main__":
    asyncio.run(main())
