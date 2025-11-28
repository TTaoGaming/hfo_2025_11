"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 10a74feb-5a27-4def-88d9-aada2048087a
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.272531+00:00'
    generation: 51
  topos:
    address: venom/test_prey_real.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_prey_real.py
"""

import asyncio
import os
import logging
from dotenv import load_dotenv
from body.hands.prey_agent import PreyAgent
from body.models.state import AgentRole

# Load environment variables
load_dotenv()

logging.basicConfig(level=logging.INFO)


async def test_prey_real():
    print("🧪 Testing PREY Agent (Real Integration)...")

    # Check for API Key
    if not os.getenv("OPENROUTER_API_KEY"):
        print("❌ OPENROUTER_API_KEY not found. Skipping real test.")
        return

    # Initialize Agent
    # Using a cheap model for testing
    agent = PreyAgent(
        agent_id="test-unit-01",
        role=AgentRole.OBSERVER,
        model_name="x-ai/grok-4.1-fast",
    )

    # Define a simple task
    task = "List the files in the 'brain' directory and summarize the 'README.md' if it exists."

    print(f"   Task: {task}")

    try:
        # Run the agent
        final_state = await agent.run(task)

        print("\n✅ Agent Execution Complete!")
        print(f"   Final Step: {final_state['current_step']}")
        print(f"   Confidence: {final_state['confidence_score']}")

        # Check if NATS published (logs should show it)

    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(test_prey_real())
