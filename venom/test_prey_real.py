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
