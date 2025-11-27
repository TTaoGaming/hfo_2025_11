"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: test-squad-local-v1
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-26T12:00:00Z'
    generation: 55
  topos:
    address: body/hands/test_squad_local.py
    links: []
  telos:
    viral_factor: 0.0
    meme: Test 8-8-8-8 Squad with Local Models
"""

import os

# CRITICAL: Runtime Fix for OMP Error #13
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
os.environ["OMP_NUM_THREADS"] = "1"

# Configure Local LLM (Ollama)
os.environ["LLM_BASE_URL"] = "http://localhost:11434/v1"
os.environ["LLM_API_KEY"] = "ollama"
os.environ["DEFAULT_MODEL"] = "gemma3:270m"

import asyncio
import logging
import uuid
from typing import List
from body.hands.prey_agent import PreyAgent
from body.models.state import AgentRole

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SquadTest")

async def run_agent(agent_id: str, task: str):
    """Runs a single agent with the given task."""
    logger.info(f"🚀 Agent {agent_id} starting...")

    # Initialize Agent
    agent = PreyAgent(
        agent_id=agent_id,
        role=AgentRole.SHAPER, # Corrected role
        model_name="gemma3:270m",
        nats_url="nats://localhost:4225" # Corrected Port
    )

    # Run the Agent
    try:
        result = await agent.run(task)
        # Access final_output from AgentState
        final_output = result.get('final_output', 'No output')
        logger.info(f"✅ Agent {agent_id} finished. Result: {final_output[:50]}...")
        return final_output
    except Exception as e:
        logger.error(f"❌ Agent {agent_id} failed: {e}")
        return None

async def main():
    """Runs the 8-Agent Squad Test."""
    logger.info("🦅 Starting 8-Agent Squad Test (Local Model: gemma3:270m)")

    task = "What is the primary function of a 'Fractal Entropy Funnel' in a cognitive architecture? Explain in 1 sentence."

    # Create 8 Agents
    agents = [f"Agent-{i+1}" for i in range(8)]

    # Run Concurrently
    tasks = [run_agent(agent_id, task) for agent_id in agents]
    results = await asyncio.gather(*tasks)

    # Analyze Results
    successful = [r for r in results if r is not None]
    logger.info(f"🏁 Squad Test Complete. {len(successful)}/8 Agents succeeded.")

    # Simple Consensus (Concatenation for now)
    logger.info("--- SQUAD CONSENSUS ---")
    for i, res in enumerate(successful):
        print(f"[{i+1}] {res}")

if __name__ == "__main__":
    asyncio.run(main())
