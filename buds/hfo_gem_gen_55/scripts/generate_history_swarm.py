import asyncio
import logging
import os
from typing import Dict
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("HistorySwarm")

# Constants
ARCHIVE_ROOT = "eyes/archive/hfo_gem"
OUTPUT_FILE = "brain/history_of_evolution_swarm.md"
WORKER_COUNT = 8  # One for each Stigmergy Dimension

# The 8 Stigmergy Dimensions (Octet)
STIGMERGY_DIMENSIONS = {
    "Logos": "Logic, Protocol, Code, Language, Algorithms.",
    "Nomos": "Law, Order, Governance, Constraints, Rules.",
    "Ontos": "Being, Essence, Identity, Roles, Types.",
    "Chronos": "Time, Evolution, History, Speed, Decay.",
    "Pathos": "Emotion, Stress, Pain Points, Failure, Urgency.",
    "Ethos": "Ethics, Trust, Security, Compliance, Safety.",
    "Topos": "Place, Architecture, Location, Links, Structure.",
    "Telos": "Purpose, Goal, Vision, Viral Factor, Meme.",
}


async def get_archived_content(gen: int) -> str:
    """Retrieves content from the archive for a specific generation."""
    content = ""

    if gen == 51:
        # Gen 51: Current Repo Root (Stabilization)
        logger.info("📂 Reading Gen 51 from Repository Root...")
        files = [
            "GAP_ANALYSIS_GEN51.md",
            "AGENTS.md",
            "Swarmlord_of_Webs_Digest_2025-11-22_Stabilization.md",
        ]
        for filename in files:
            if os.path.exists(filename):
                try:
                    with open(filename, "r", encoding="utf-8") as f:
                        content += f"\n\n--- FILE: {filename} ---\n"
                        content += f.read(8000)
                except Exception as e:
                    logger.warning(f"⚠️ Failed to read {filename}: {e}")
        return content

    elif gen == 52:
        # Gen 52: Current Repo Root (Evolution Digests)
        logger.info("📂 Reading Gen 52 from Repository Root Digests...")
        import glob

        files = glob.glob("Swarmlord_Digest_Gen52_*.md")
        files.append("Swarmlord_Digest_2025-11-23_Gen52_Evolution.md")
        for filename in files:
            if os.path.exists(filename):
                try:
                    with open(filename, "r", encoding="utf-8") as f:
                        content += f"\n\n--- FILE: {filename} ---\n"
                        content += f.read(8000)
                except Exception as e:
                    logger.warning(f"⚠️ Failed to read {filename}: {e}")
        return content

    elif gen == 53:
        # Gen 53: Buds Folder
        logger.info("📂 Reading Gen 53 from buds/hfo_gem_gen_53...")
        root = "buds/hfo_gem_gen_53"
        files = [
            "AGENTS.md",
            "README.md",
            "HFO_HYDRA_BUDDING_MANIFESTO.md",
            "research_formal_architecture.md",
        ]
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content += f"\n\n--- FILE: {filename} ---\n"
                        content += f.read(8000)
                except Exception as e:
                    logger.warning(f"⚠️ Failed to read {file_path}: {e}")
        return content

    # Standard Archive Logic (Gen 1-50)
    gen_dir = os.path.join(ARCHIVE_ROOT, f"gen_{gen}")
    if not os.path.exists(gen_dir):
        return ""

    # Priority files
    priority_files = [
        "original_gem.md",
        "HFO_GENE_SEED.md",
        "summary.md",
        "deep_dive.md",
        "README.md",
    ]

    for filename in priority_files:
        file_path = os.path.join(gen_dir, filename)
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content += f"\n\n--- FILE: {filename} ---\n"
                    content += f.read(4000)  # Limit per file
            except Exception as e:
                logger.warning(f"⚠️ Failed to read {file_path}: {e}")

    return content


async def analyze_dimension(
    agent: SwarmlordAgent, gen: int, dimension: str, description: str, content: str
) -> str:
    """Analyzes the content from the perspective of a specific Stigmergy Dimension."""
    prompt = f"""
    You are a **History Archivist** for Hive Fleet Obsidian.
    Your specific lens is **{dimension}** ({description}).

    **Task**: Analyze the provided archive data for **Generation {gen}** and extract ONLY information relevant to your dimension.

    **Archive Data**:
    {content[:10000]}

    **Output Format**:
    - Provide a bulleted list of findings.
    - Focus on FACTS found in the text.
    - If nothing is found, state "No specific data for {dimension}."
    - Be concise.
    """
    try:
        response = await agent.chat(prompt)
        return response
    except Exception as e:
        logger.error(f"Worker {dimension} failed: {e}")
        return f"Error analyzing {dimension}"


async def synthesize_generation(
    agent: SwarmlordAgent, gen: int, reports: Dict[str, str]
) -> str:
    """Synthesizes the 8 dimensional reports into a cohesive history entry."""

    reports_text = ""
    for dim, report in reports.items():
        reports_text += f"\n### {dim} Report\n{report}\n"

    prompt = f"""
    You are the **Swarmlord**.

    **Task**: Synthesize the following 8 Stigmergy Reports into a **Complete Historical Entry** for **Generation {gen}**.

    **Goal**: Create a "Near Complete Knowledge Transfer" document. Any AI reading this should be able to reconstruct the generation.

    **Input Reports**:
    {reports_text}

    **Required Output Format**:
    ## Generation {gen}: [Title]

    ### 1. The Octet Analysis (8 Stigmergy Dimensions)
    *   **Logos (Logic)**: ...
    *   **Nomos (Law)**: ...
    *   **Ontos (Essence)**: ...
    *   **Chronos (Time)**: ...
    *   **Pathos (Pain)**: ...
    *   **Ethos (Trust)**: ...
    *   **Topos (Structure)**: ...
    *   **Telos (Purpose)**: ...

    ### 2. The Reconstruction Guide
    *   **Key Files**: ...
    *   **Core Loop**: ...
    *   **Architecture**: ...

    ### 3. The Evolutionary Leap
    *   **From**: [Previous State]
    *   **To**: [New State]
    *   **The Gem**: [The core innovation]

    **Tone**: High-Fidelity, Technical, Evolutionary.
    """

    return await agent.chat(prompt)


async def process_generation(gen: int, semaphore: asyncio.Semaphore):
    async with semaphore:
        logger.info(f"🚀 Starting Swarm Analysis for Generation {gen}...")

        content = await get_archived_content(gen)
        if not content:
            logger.warning(f"⚠️ No content found for Gen {gen}. Skipping.")
            return None

        # Initialize Swarm (Simulated by 1 agent instance for now to save memory, or multiple if needed)
        # Ideally we use one agent per task, but let's reuse one to be polite to the API
        agent = SwarmlordAgent()
        await agent.initialize()

        # Map Phase: 8 Dimensions
        tasks = []
        for dim, desc in STIGMERGY_DIMENSIONS.items():
            tasks.append(analyze_dimension(agent, gen, dim, desc, content))

        results = await asyncio.gather(*tasks)
        reports = dict(zip(STIGMERGY_DIMENSIONS.keys(), results))

        # Reduce Phase: Synthesis
        logger.info(f"🧩 Synthesizing Consensus for Generation {gen}...")
        final_entry = await synthesize_generation(agent, gen, reports)

        await agent.close()
        logger.info(f"✅ Generation {gen} Complete.")
        return final_entry


async def main():
    logger.info("🔥 Igniting History Swarm (Octree Protocol)...")

    # Initialize Output File
    existing_gens = set()
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r") as f:
            content = f.read()
            import re

            matches = re.findall(r"## Generation (\d+)", content)
            existing_gens = set(map(int, matches))
            logger.info(f"Found existing generations: {sorted(list(existing_gens))}")
    else:
        with open(OUTPUT_FILE, "w") as f:
            f.write(
                "# 🌳 The Octree History of Evolution (Gen 1-53)\n\n> **Generated by the Council of 8 (Stigmergy Swarm)**\n\n---\n\n"
            )

    # Semaphore to limit concurrent generations (not concurrent workers per gen)
    # We process 1 generation at a time to avoid rate limits, but internally it does 8 parallel calls
    semaphore = asyncio.Semaphore(1)

    for gen in range(1, 54):
        if gen in existing_gens:
            logger.info(f"⏭️ Skipping Generation {gen} (Already exists)")
            continue

        entry = await process_generation(gen, semaphore)
        if entry:
            with open(OUTPUT_FILE, "a") as f:
                f.write(f"\n{entry}\n\n---\n")
                f.flush()


if __name__ == "__main__":
    asyncio.run(main())
