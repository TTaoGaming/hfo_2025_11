import asyncio
import logging
import os
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)


async def verify_temperature_model():
    # Use the configured model from .env
    model = os.getenv("DEFAULT_MODEL", "unknown")
    print(f"🕷️ Waking the Swarmlord for Verification... (Model: {model})")
    agent = SwarmlordAgent()
    await agent.initialize()

    question = "What is the Stigmergy Temperature Model and what is the current state of the Swarmlord's memory?"
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
    asyncio.run(verify_temperature_model())
