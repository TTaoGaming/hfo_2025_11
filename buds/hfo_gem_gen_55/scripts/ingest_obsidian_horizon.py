import asyncio
import logging
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("IngestObsidianHorizon")


async def ingest_obsidian_horizon():
    logger.info("🕷️ Waking the Swarmlord for Mass Ingestion...")
    agent = SwarmlordAgent()
    await agent.initialize()

    # Define the Stigmergy Temperature Model
    temperature_model = """
    # Stigmergy Temperature Model
    Defines the state of information in the Hive Fleet Obsidian.

    1. **Hot (Episodic)**: Volatile, high-frequency signals (NATS). Immediate context, short lifespan.
    2. **Cool (Semantic)**: Processed, stored in Vector DB. Accessible, searchable, but subject to refinement.
    3. **Cold (Karmic)**: Refined, crystallized, immutable. Archived in the Obsidian Vault (Markdown).
    4. **Glacial (DNA)**: Deep storage, foundational axioms, rarely changed.
    """

    # Define the Obsidian Horizon Hourglass & 3 Webs
    obsidian_horizon_content = """
    # Obsidian Horizon Hourglass & The Three Webs

    **The Obsidian Horizon Hourglass** is the Chronos Engine of HFO. It flips between Planning (Future) and Execution (Present) and Archiving (Past).

    **The Three Webs (State-Action Space):**
    1. **The Karmic Web (Past, Z < 0)**: The Ancestor. Roots, history, archives. Represents the "Cold" state of memory.
    2. **The Swarm Web (Present, Z = 0)**: The Commander. Live execution, NATS signals, Temporal workflows. Represents the "Hot" state.
    3. **The Simulation Web (Future, Z > 0)**: The Oracle. Speculative leaps, MCTS, Bayesian simulations. Represents the "Virtual" state.

    **GitOps for Reality:**
    - **Simulation Web** = Feature/Dev Branches (Infinite forks, MCTS leaps).
    - **Swarm Web** = Main Branch (Production, Single Source of Truth).
    - **Pull Requests** = Fitness Reviews (Elites from Sim Web merged to Swarm Web).

    **Intention Hyperdrive:**
    Using "Change Vectors" (Embeddings) to extrapolate future states without code generation.
    """

    # Ingest Temperature Model
    logger.info("📥 Ingesting Stigmergy Temperature Model...")
    await agent.memory.add_memory(
        content=temperature_model,
        metadata={
            "type": "definition",
            "topic": "stigmergy_temperature",
            "temperature": "cool",  # User specified "cool" for current memory
            "source": "user_instruction",
        },
    )

    # Ingest Obsidian Horizon
    logger.info("📥 Ingesting Obsidian Horizon & 3 Webs...")
    await agent.memory.add_memory(
        content=obsidian_horizon_content,
        metadata={
            "type": "architecture",
            "topic": "obsidian_horizon",
            "temperature": "cool",
            "source": "user_instruction",
        },
    )

    logger.info("✅ Ingestion Complete.")
    await agent.close()


if __name__ == "__main__":
    asyncio.run(ingest_obsidian_horizon())
