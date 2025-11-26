import asyncio
import logging
from dotenv import load_dotenv
from body.hybrid_memory import HybridMemory

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)


async def ingest_directives():
    print("🧠 Ingesting Strategic Directives into Hybrid Memory...")

    # Initialize Memory
    # We need to pass the client if we want embeddings, but HybridMemory creates one if None.
    # Ensure OPENAI_API_KEY or OPENROUTER_API_KEY is set in env.
    mem = HybridMemory()
    await mem.initialize()

    directives = [
        "The Swarmlord of Webs is the Digital Twin for Intent/Implementation split. HFO is the Second Brain, an extension of the self.",
        "The Heartbeat of the Hive is a cycle-based stigmergy async coordination mechanism. It adjusts speed based on context and need.",
        "Stigmergy Spectrum: Hot (TTL Auto-delete/Save) -> Cold (TTL Clean/Refine) -> Refined (TTL Maintenance). Like KCS v6.",
        "Refined Stigmergy is like Obsidian with water layers. We age it with backlinks and maintenance checks.",
        "Priority: Establish a variable heartbeat for the hive to optimize async coordination.",
    ]

    for d in directives:
        await mem.add_memory(
            content=d,
            metadata={
                "type": "strategic_directive",
                "priority": "critical",
                "source": "overmind",
            },
        )
        print(f"✅ Ingested: {d}")

    await mem.close()
    print("✨ Ingestion Complete.")


if __name__ == "__main__":
    asyncio.run(ingest_directives())
