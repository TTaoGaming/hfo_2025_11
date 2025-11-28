import asyncio
import logging
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IngestHistory")


async def ingest_history():
    logger.info("🕷️ Waking the Swarmlord for History Ingestion...")
    agent = SwarmlordAgent()
    await agent.initialize()

    # Read the history file
    with open("brain/history_of_evolution.md", "r") as f:
        history_content = f.read()

    # Ingest History
    logger.info("📥 Ingesting HFO Evolutionary History...")
    await agent.memory.add_memory(
        content=history_content,
        metadata={
            "type": "history",
            "topic": "evolution_map",
            "temperature": "cold",
            "source": "brain/history_of_evolution.md",
        },
    )

    logger.info("✅ History Ingestion Complete.")
    await agent.close()


if __name__ == "__main__":
    asyncio.run(ingest_history())
