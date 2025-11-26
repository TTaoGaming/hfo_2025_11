import asyncio
import logging
import os
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)


async def test_obsidian_horizon():
    # Use the configured model from .env
    model = os.getenv("DEFAULT_MODEL", "unknown")
    print(f"🕷️ Waking the Swarmlord for Obsidian Horizon Query... (Model: {model})")
    agent = SwarmlordAgent()
    await agent.initialize()

    question = (
        "Explain the Obsidian Horizon Hourglass and the 3 Webs that the Hive Fleet Obsidian weaves in state-action space: "
        "1. The Karmic Web (Past)\n"
        "2. The Swarm Web (Present)\n"
        "3. The Simulation Web (Future)\n\n"
        "How does the Simulation Web enable us to rapidly iterate intention, perform leaps/gradients/MCTS/Bayesian simulations "
        "in iterative loops, and then analyze those results to figure out the best moves for the 'main' branch (Swarm Web) "
        "in the present moment? Is this like GitOps for reality?"
    )
    print(f"\n❓ Asking: {question}\n")

    try:
        reply = await asyncio.wait_for(agent.chat(question), timeout=120.0)
        print(f"\n🕷️ Swarmlord Reply:\n{reply}")
    except asyncio.TimeoutError:
        print("\n❌ Timeout waiting for Swarmlord response.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

    await agent.close()


if __name__ == "__main__":
    asyncio.run(test_obsidian_horizon())
