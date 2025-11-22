import os
import logging
import asyncio
import yaml
from pathlib import Path
from typing import List
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from body.hfo_sdk.stigmergy import StigmergyClient
from body.constants import DEFAULT_MODEL
from body.config import Config

# --- 1. Setup ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CrystalSpinner")

# --- 2. The DNA (Pydantic Models) ---


class CrystalMetadata(BaseModel):
    """
    The structured essence extracted from raw information.
    This is the 'Liquid Memory' before it hardens.
    """

    title: str = Field(..., description="A clear, concise title for the artifact")
    summary: str = Field(
        ..., description="A 1-sentence executive summary of the content"
    )
    domain: str = Field(
        ...,
        description="The primary domain (e.g., Strategy, Infrastructure, Biology, Memory)",
    )
    concepts: List[str] = Field(..., description="List of 3-5 key concepts or tags")
    owner: str = Field(
        ...,
        description="The role responsible for this knowledge (e.g., Swarmlord, Architect)",
    )
    actionable: bool = Field(
        ...,
        description="True if this contains tasks or directives, False if pure knowledge",
    )
    related_files: List[str] = Field(
        default_factory=list,
        description="List of potential related filenames mentioned",
    )


# --- 3. The Organ (Crystal Spinner Class) ---


class CrystalSpinner:
    def __init__(self, nats_url: str = Config.NATS_URL):
        self.client = instructor.from_openai(
            AsyncOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )
        self.stigmergy = StigmergyClient(nats_url)
        self.model = DEFAULT_MODEL

    async def connect(self):
        await self.stigmergy.connect()

    async def close(self):
        await self.stigmergy.close()

    async def spin(self, content: str, filename: str) -> CrystalMetadata:
        """
        Phase 1: The Spin (Digestion)
        Extracts structured metadata from raw text using the LLM.
        """
        logger.info(f"🕸️  Spinning: {filename}...")

        # Stigmergy Read: Fetch recent context to help linking
        try:
            recent_signals = await self.stigmergy.fetch_history(
                "hfo.memory.crystallized", limit=5
            )
            context_str = "\n".join(
                [
                    f"- {s.get('metadata', {}).get('title', 'Unknown')}"
                    for s in recent_signals
                ]
            )
        except Exception:
            context_str = "No recent context available."

        try:
            metadata = await self.client.chat.completions.create(
                model=self.model,
                response_model=CrystalMetadata,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are The Crystal-Spinner, a specialized HFO agent. "
                            "Your task is to digest raw text and extract structured metadata "
                            "to organize the Hive Mind's memory."
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"""Analyze this file content and extract metadata.

                        STIGMERGY CONTEXT (Recently Processed):
                        {context_str}

                        Filename: {filename}

                        Content:
                        {content[:10000]}""",  # Truncate for safety
                    },
                ],
                max_retries=3,
            )
            return metadata
        except Exception as e:
            logger.error(f"❌ Failed to spin {filename}: {e}")
            # Return a fallback if LLM fails
            return CrystalMetadata(
                title=filename,
                summary="Processing failed.",
                domain="Unsorted",
                concepts=["error"],
                owner="System",
                actionable=False,
            )

    def harden(self, content: str, metadata: CrystalMetadata) -> str:
        """
        Phase 2: The Harden (Crystallization)
        Injects the Stigmergic Header (YAML) into the content.
        """
        # Convert Pydantic to dict, exclude None
        meta_dict = metadata.model_dump(exclude_none=True)

        # Add system fields
        meta_dict["type"] = "crystallized_memory"
        meta_dict["status"] = "active"
        meta_dict["last_verified"] = "2025-11-21"  # In real system, use dynamic date

        # Create YAML block
        yaml_block = yaml.dump(meta_dict, sort_keys=False, default_flow_style=False)

        # Check if file already has a header (simple check)
        if content.strip().startswith("---"):
            # Remove existing header if present (naive implementation)
            parts = content.split("---", 2)
            if len(parts) >= 3:
                body = parts[2].strip()
            else:
                body = content
        else:
            body = content

        return f"---\n{yaml_block}---\n\n{body}"

    async def weave(
        self, original_path: Path, new_content: str, metadata: CrystalMetadata
    ):
        """
        Phase 3: The Weave (Integration)
        Saves the file to the Semantic Library and emits a Stigmergy Signal.
        """
        # 1. Determine Destination
        # Structure: memory/semantic/library/{domain}/{filename}
        dest_dir = Path(
            f"memory/semantic/library/{metadata.domain.lower().replace(' ', '_')}"
        )
        dest_dir.mkdir(parents=True, exist_ok=True)

        # Prevent Overwriting: Prepend parent folder name if filename is generic
        # or if it comes from a specific generation folder (e.g. gen_23)
        parent_name = original_path.parent.name
        if "gen_" in parent_name or original_path.name.lower() in [
            "readme.md",
            "summary.md",
            "deep_dive.md",
        ]:
            new_name = f"{parent_name}_{original_path.name}"
        else:
            new_name = original_path.name

        dest_file = dest_dir / new_name

        # 2. Write File
        with open(dest_file, "w", encoding="utf-8") as f:
            f.write(new_content)

        logger.info(f"💎 Crystallized: {dest_file}")

        # 3. Emit Signal (The Stigmergy)
        # This allows other assimilators (Vectorizer, GraphWeaver) to react
        signal = {
            "type": "memory_crystallized",
            "file_path": str(dest_file),
            "metadata": metadata.model_dump(),
            "timestamp": "2025-11-21T12:00:00Z",
        }

        await self.stigmergy.publish("hfo.memory.crystallized", signal)
        logger.info(f"📡 Signal Emitted: hfo.memory.crystallized -> {metadata.title}")


# --- 4. The Main Loop ---


async def main():
    logger.info("🕷️  Crystal-Spinner Online. Initializing Digestion Protocol...")

    spinner = CrystalSpinner()
    await spinner.connect()

    source_dir = Path("eyes/archive/hfo_gem")
    if not source_dir.exists():
        logger.error(f"❌ Source directory not found: {source_dir}")
        return

    # Gather files
    files = list(source_dir.rglob("*.md"))
    logger.info(f"Found {len(files)} raw gems to process.")

    for file_path in files:
        # Read
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            logger.warning(f"Skipping {file_path}: {e}")
            continue

        # Spin (LLM)
        metadata = await spinner.spin(content, file_path.name)

        # Harden (YAML)
        new_content = spinner.harden(content, metadata)

        # Weave (Save & Signal)
        await spinner.weave(file_path, new_content, metadata)

        # Rate limit slightly to be polite to API
        await asyncio.sleep(0.5)

    await spinner.close()
    logger.info("✅ Digestion Complete. The Web is stronger.")


if __name__ == "__main__":
    asyncio.run(main())
