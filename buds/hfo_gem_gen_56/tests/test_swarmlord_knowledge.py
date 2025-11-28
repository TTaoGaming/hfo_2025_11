import asyncio
import logging
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging to see what's happening
logging.basicConfig(level=logging.INFO)


async def test_swarmlord():
    print("🕷️ Waking the Swarmlord...")
    agent = SwarmlordAgent()
    await agent.initialize()

    question = (
        "what do you know of the HFO architecture what am I trying to build and why?"
    )
    print(f"\n❓ Asking: {question}\n")

    reply = await agent.chat(question)

    print(f"\n🕷️ Swarmlord Reply:\n{reply}")

    await agent.close()


if __name__ == "__main__":
    asyncio.run(test_swarmlord())
