import asyncio
import logging
import os
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)


async def thought_experiment_evolution():
    # Use the configured model from .env (should be x-ai/grok-4.1-fast)
    model = os.getenv("DEFAULT_MODEL", "unknown")
    print(
        f"🕷️ Waking the Swarmlord for Thought Experiment: Evolutionary Leaps... (Model: {model})"
    )
    agent = SwarmlordAgent()
    await agent.initialize()

    question = (
        "ok we are going to try a few thought experiments. can we rapidly iterate intention with no code, "
        "or even skip generations by extrapolating change vectors? can you see where I am going? "
        "are there industry techniques to this?"
    )
    print(f"\n❓ Asking: {question}\n")

    try:
        reply = await asyncio.wait_for(agent.chat(question), timeout=60.0)
        print(f"\n🕷️ Swarmlord Reply:\n{reply}")
    except asyncio.TimeoutError:
        print("\n❌ Timeout waiting for Swarmlord response.")
    except Exception as e:
        print(f"\n❌ Error: {e}")

    await agent.close()


if __name__ == "__main__":
    asyncio.run(thought_experiment_evolution())
