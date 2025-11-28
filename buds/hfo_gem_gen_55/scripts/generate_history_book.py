import asyncio
import logging
import os
from typing import Optional
from dotenv import load_dotenv
from body.hands.swarmlord import SwarmlordAgent

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HistoryBook")

# Path to the Archives
ARCHIVE_ROOT = "eyes/archive/hfo_gem"

# Known History Data (Fallback)
HISTORY_DATA = {
    50: {
        "theme": "The Phoenix",
        "details": "System Reset. GitOps enforcement. Infrastructure-as-Code.",
    },
    51: {
        "theme": "Synapse APEX",
        "details": "Stigmergic GraphRAG. Hexagonal Holarchy. Mass Ingestion of KCS/Diataxis.",
    },
    52: {
        "theme": "Obsidian Horizon",
        "details": "The Hourglass Architecture. Intention Hyperdrive. Cooling & Refinement.",
    },
    53: {
        "theme": "The Symbiote",
        "details": "Current State. Integration with External Mind. Simulation Web active.",
    },
}

ERA_THEMES = {
    (1, 18): "Era 1: The Foundation (Zero Invention & Composition)",
    (19, 30): "Era 2a: The Infrastructure Shift (Ray & NATS)",
    (31, 49): "Era 2b: The Agentic Rise (LangGraph & Temporal)",
    (50, 53): "Era 3: The Crystallization (Cognitive Symbiosis)",
}


def get_archived_content(gen: int) -> Optional[str]:
    """Retrieves content from the archive for a specific generation."""
    gen_dir = os.path.join(ARCHIVE_ROOT, f"gen_{gen}")

    if not os.path.exists(gen_dir):
        # Try gen_X.X if needed, but for now stick to integers
        return None

    # Priority list of files to read
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
                    # Read first 4000 chars to get the gist without blowing context
                    return f.read(4000)
            except Exception as e:
                logger.warning(f"⚠️ Failed to read {file_path}: {e}")

    return None


async def generate_history_book():
    logger.info("🕷️ Waking the Swarmlord to write the TRUE History Book...")
    agent = SwarmlordAgent()
    await agent.initialize()

    output_path = "brain/history_of_evolution_full.md"

    # Check what's already done
    existing_gens = set()
    if os.path.exists(output_path):
        with open(output_path, "r") as f:
            content = f.read()
            # Look for "## Generation X" or "## Generation X:"
            import re

            matches = re.findall(r"## Generation (\d+)", content)
            existing_gens = set(map(int, matches))
            logger.info(f"Found existing generations: {sorted(list(existing_gens))}")
    else:
        # Initialize file with header
        with open(output_path, "w") as f:
            f.write(
                """# 🧬 History of Evolution: HFO Generations 1-53

> **The Chronicle of the Hive Fleet's Ascent.**
> *Based on the Original Gem Archives.*

---

"""
            )

    for gen in range(1, 54):
        if gen in existing_gens:
            logger.info(f"⏭️ Skipping Generation {gen} (Already exists)")
            continue

        logger.info(f"✍️ Writing Generation {gen}...")

        # Determine Era
        era = "Unknown Era"
        for r, name in ERA_THEMES.items():
            if r[0] <= gen <= r[1]:
                era = name
                break

        # Get content from Archive
        archived_content = get_archived_content(gen)

        if archived_content:
            source_type = "ARCHIVE (High Fidelity)"
            context_data = f"**Archived Content (Excerpt)**:\n{archived_content}..."
        else:
            # Fallback to manual data
            source_type = "EXTRAPOLATION (Low Fidelity)"
            specifics = HISTORY_DATA.get(gen, "")
            if specifics:
                specifics = f"Known Facts: {specifics}"
            else:
                specifics = "Details lost. Extrapolate based on Era Theme."
            context_data = f"**Specifics**: {specifics}"

        prompt = f"""
        Write a comprehensive **2-page summary** (approx 500 words) for **HFO Generation {gen}**.

        **Era**: {era}
        **Source Material**:
        {source_type}

        **Context Data**:
        {context_data}

        **Format**:
        ## Generation {gen}: [Thematic Title]

        **Structure**:
        1. **The Executive Summary**: High-level theme and objective.
        2. **The Architecture**: Technical details (Roles, Loops, Stacks).
        3. **The Pain Points**: What failed? What triggered the evolution?
        4. **The Innovation**: What was the "Gem" of this generation?
        5. **The Legacy**: What survived to the next generation?

        **Tone**:
        Epic, biological, evolutionary. Use HFO terminology (Stigmergy, Red Sand, Swarmlord).
        """

        # Generate content
        try:
            # Increased timeout for longer generation
            response = await asyncio.wait_for(agent.chat(prompt), timeout=120.0)

            # Append immediately to file
            with open(output_path, "a") as f:
                f.write(f"\n{response}\n\n---\n")
                f.flush()

            logger.info(f"✅ Generation {gen} written to disk.")

            # Brief pause to respect rate limits
            await asyncio.sleep(1)
        except Exception as e:
            logger.error(f"❌ Failed to generate Gen {gen}: {e}")
            # Don't write failure to disk so we can retry later
            # Or write a placeholder? Better to retry.
            continue

    logger.info("🎉 History Book generation complete!")

    await agent.close()


if __name__ == "__main__":
    asyncio.run(generate_history_book())
