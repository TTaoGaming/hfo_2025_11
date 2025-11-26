import asyncio
import logging
import os
import glob
from typing import Dict, Any
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("UnifiedIngest")


class UnifiedIngestor:
    def __init__(self):
        self.agent = SwarmlordAgent()

    async def initialize(self):
        await self.agent.initialize()

    async def ingest_file(self, file_path: str, metadata: Dict[str, Any]):
        """Ingests a single file into the Hybrid Memory."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Add file path to metadata
            metadata["source_file"] = file_path
            metadata["filename"] = os.path.basename(file_path)

            logger.info(f"📥 Ingesting {file_path}...")
            await self.agent.memory.add_memory(content=content, metadata=metadata)

        except Exception as e:
            logger.error(f"❌ Failed to ingest {file_path}: {e}")

    async def ingest_directory(
        self, dir_path: str, pattern: str, metadata: Dict[str, Any]
    ):
        """Ingests all files matching a pattern in a directory."""
        search_path = os.path.join(dir_path, pattern)
        files = glob.glob(search_path, recursive=True)

        logger.info(f"📂 Found {len(files)} files in {search_path}")

        for file_path in files:
            await self.ingest_file(file_path, metadata)

    async def ingest_frameworks(self):
        """Ingests KCS and Diataxis frameworks as foundational knowledge."""

        kcs_content = """
        # Knowledge-Centered Service (KCS)

        **Core Principle**: Integrate knowledge creation and maintenance into the problem-solving process.

        **The Double Loop**:
        1.  **Solve Loop (A Loop)**:
            *   **Capture**: Record knowledge in the workflow.
            *   **Structure**: Use a consistent template.
            *   **Reuse**: Search early, search often.
            *   **Improve**: Update existing knowledge.
        2.  **Evolve Loop (B Loop)**:
            *   **Content Health**: Analyze patterns, archive old data.
            *   **Process Integration**: Optimize the workflow.
            *   **Performance Assessment**: Value creation over activity.
            *   **Leadership**: Promote a knowledge-sharing culture.

        **HFO Application**:
        - **Capture**: NATS signals (Hot).
        - **Structure**: Obsidian Templates (Cool).
        - **Reuse**: Vector Search (HybridMemory).
        - **Improve**: Assimilator refinement (Cold).
        """

        diataxis_content = """
        # Diataxis Framework

        **Core Principle**: Documentation should be organized by *user needs*, not software architecture.

        **The Four Quadrants**:
        1.  **Tutorials** (Learning-oriented): "Take me by the hand." Lessons, workshops.
        2.  **How-To Guides** (Problem-oriented): "Show me how to do X." Recipes, steps.
        3.  **Reference** (Information-oriented): "Tell me what X is." API docs, specs.
        4.  **Explanation** (Understanding-oriented): "Explain why X matters." Concepts, background.

        **HFO Application**:
        - **Tutorials**: `scripts/` (Genesis, Setup).
        - **How-To**: `Makefile` commands.
        - **Reference**: `AGENTS.md`, Pydantic Models.
        - **Explanation**: `brain/` (Philosophy, Architecture).
        """

        logger.info("📥 Ingesting KCS Framework...")
        await self.agent.memory.add_memory(
            content=kcs_content,
            metadata={"type": "framework", "topic": "KCS", "temperature": "glacial"},
        )

        logger.info("📥 Ingesting Diataxis Framework...")
        await self.agent.memory.add_memory(
            content=diataxis_content,
            metadata={
                "type": "framework",
                "topic": "Diataxis",
                "temperature": "glacial",
            },
        )

    async def close(self):
        await self.agent.close()


async def main():
    ingestor = UnifiedIngestor()
    await ingestor.initialize()

    # 1. Ingest Frameworks (KCS, Diataxis)
    await ingestor.ingest_frameworks()

    # 2. Ingest Archives (Gen 1-53) - Placeholder for now, pointing to eyes/archive if it had content
    # In a real scenario, we would point this to the actual path of the archives.
    # For now, we will ingest the current 'brain' as the crystallized wisdom of Gen 51.
    await ingestor.ingest_directory(
        dir_path="brain",
        pattern="**/*.md",
        metadata={"type": "archive", "generation": "51", "temperature": "cold"},
    )

    await ingestor.close()


if __name__ == "__main__":
    asyncio.run(main())
