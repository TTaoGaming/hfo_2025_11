"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 7707f45e-c6c3-4a0c-a0b3-4285bf9feaca
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-24T14:30:05.042007Z'
    generation: 51
  topos:
    address: body/hands/octarchy_swarm.py
    links: []
  telos:
    viral_factor: 0.0
    meme: octarchy_swarm.py

# ==================================================================
# 🤖 THE OCTAGON (System Generated)
# ==================================================================
octagon:
  ontos:
    id: octarchy-swarm-v1
    type: py
    owner: Swarmlord
  logos:
    protocol: Morphic Octet
    format: python
  techne:
    stack: [python, instructor, pydantic, asyncio]
    complexity: medium
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-23T15:00:00Z'
  pathos:
    stress_level: 0.1
    validation: self-verified
  ethos:
    security_level: internal
    compliance: [hfo-standard]
  topos:
    address: body/hands/octarchy_swarm.py
    links: [hfo_stigmergic_schema_v0.2.json]
  telos:
    viral_factor: 1.0
    meme: The 8-Fold Path of the Hive.

🦅 Hive Fleet Obsidian: Octarchy Swarm (Gen 52)
Intent: Generate "Octarchy Headers" (8 Dimensions) using a Morphic Octet Swarm.
Workflow: 8 -> 1 (Generate -> Consensus).
"""

import os
import asyncio
import logging
import yaml
import uuid
import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from dotenv import load_dotenv
from body.constants import DEFAULT_MODEL
from body.hfo_sdk.stigmergy import StigmergyClient

# Setup
load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("OctarchySwarm")

# Constants
MODEL = DEFAULT_MODEL
OCTET_SIZE = 1  # Sequential execution as requested

# --- Pydantic Models (The DNA) ---


class Ontos(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = Field(..., description="Type of the file (doc, code, concept, pattern)")
    owner: str = Field(..., description="Owner/Steward of this concept")


class Logos(BaseModel):
    protocol: str = Field(..., description="Communication protocol or pattern used")
    format: str = Field(..., description="File format or data structure")


class Techne(BaseModel):
    stack: List[str] = Field(..., description="Tech stack or tools used")
    complexity: str = Field(..., description="low, medium, high")


class Chronos(BaseModel):
    status: str = Field(..., description="active, draft, archived, stable")
    urgency: float = Field(
        ..., ge=0.0, le=1.0, description="0.0 (Low) to 1.0 (Critical)"
    )
    decay: float = Field(..., ge=0.0, le=1.0, description="Relevance decay rate")
    created: str = Field(
        default_factory=lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
    )


class Pathos(BaseModel):
    stress_level: float = Field(..., ge=0.0, le=1.0, description="Current stress/load")
    validation: str = Field(
        ..., description="Validation status (e.g., verified, pending)"
    )


class Ethos(BaseModel):
    security_level: str = Field(..., description="public, internal, confidential")
    compliance: List[str] = Field(
        default_factory=list, description="Compliance standards met"
    )


class Topos(BaseModel):
    address: str = Field(..., description="Virtual address (e.g., path/to/file)")
    links: List[str] = Field(
        default_factory=list, description="Related file paths or IDs"
    )


class Telos(BaseModel):
    viral_factor: float = Field(..., ge=0.0, le=1.0, description="Potential for spread")
    meme: str = Field(..., description="Short, catchy meme/slogan for this file")


class Octagon(BaseModel):
    ontos: Ontos
    logos: Logos
    techne: Techne
    chronos: Chronos
    pathos: Pathos
    ethos: Ethos
    topos: Topos
    telos: Telos


# --- PREY Loop Models ---


class Perception(BaseModel):
    """Phase 1: Perceive"""

    file_path: str
    detected_header: str = Field(..., description="None, Hexagon, or Octagon")
    content_summary: str = Field(..., description="Brief summary of file intent")


class Reaction(BaseModel):
    """Phase 2: React"""

    action: str = Field(..., enum=["upgrade", "skip", "repair"], description="Decision")
    reasoning: str = Field(..., description="Why this action?")


class Execution(BaseModel):
    """Phase 3: Execute"""

    generated_header: Optional[Octagon] = Field(
        None, description="The new header if upgrading"
    )


class Yield(BaseModel):
    """Phase 4: Yield"""

    stigmergy_signal: Dict[str, Any] = Field(
        ..., description="Signal to publish to NATS"
    )
    reflexion: str = Field(..., description="Self-critique")


class PreyLoop(BaseModel):
    """The Full PREY Cycle"""

    perception: Perception
    reaction: Reaction
    execution: Execution
    yield_: Yield = Field(..., alias="yield")


# --- The Swarm ---


class OctarchySwarm:
    def __init__(self, model: str = MODEL):
        api_key = os.getenv("OPENAI_API_KEY")
        base_url = os.getenv("OPENAI_BASE_URL")

        if not api_key:
            api_key = os.getenv("OPENROUTER_API_KEY")
            if api_key:
                base_url = "https://openrouter.ai/api/v1"
                logger.info("Using OpenRouter API Key")

        if not api_key:
            raise ValueError(
                "No API Key found. Please set OPENAI_API_KEY or OPENROUTER_API_KEY in .env"
            )

        self.client = instructor.from_openai(
            AsyncOpenAI(api_key=api_key, base_url=base_url)
        )
        self.model = model
        self.stigmergy = StigmergyClient()

    async def run_prey_loop(self, file_path: str, content: str) -> PreyLoop:
        """
        Executes the full PREY loop for a single file.
        """
        logger.info(f"🦅 PREY Loop: Perceiving {file_path}...")

        prompt = f"""
        You are the Swarmlord of Webs (Gen 52).
        Execute the PREY Loop (Perceive-React-Execute-Yield) to upgrade this file to the Octarchy.

        Target: {file_path}

        Task:
        1. Perceive: Analyze the file. Is it missing a header? Is it Hexagonal (Legacy)?
        2. React: Decide to 'upgrade' (if Hexagon/None) or 'skip' (if Octagon).
        3. Execute: Generate the full 'Octagon' header (8 Dimensions) if upgrading.
        4. Yield: Create a Stigmergy signal confirming the action.

        Content Snippet:
        {content[:3000]}
        """

        return await self.client.chat.completions.create(
            model=self.model,
            response_model=PreyLoop,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert metadata architect. Output the full PREY loop.",
                },
                {"role": "user", "content": prompt},
            ],
        )

    async def process_file(self, file_path: str):
        """
        Processes a single file through the PREY loop.
        """
        try:
            with open(file_path, "r") as f:
                content = f.read()

            # Run PREY Loop
            result = await self.run_prey_loop(file_path, content)

            # Handle Execution
            if (
                result.reaction.action == "upgrade"
                and result.execution.generated_header
            ):
                self.apply_header(file_path, content, result.execution.generated_header)
                logger.info(f"✅ Executed Upgrade on {file_path}")
            else:
                logger.info(f"⏭️ Skipped {file_path}: {result.reaction.reasoning}")

            # Handle Yield (Stigmergy)
            await self.publish_stigmergy(result.yield_.stigmergy_signal)

        except Exception as e:
            logger.error(f"❌ Failed to process {file_path}: {e}")

    def apply_header(self, file_path: str, original_content: str, header: Octagon):
        """
        Writes the header to disk.
        """
        # Strip existing header if present
        body = original_content
        if original_content.startswith("---"):
            parts = original_content.split("---", 2)
            if len(parts) >= 3:
                body = parts[2]

        # Create YAML
        header_dict = header.model_dump()
        yaml_header = yaml.dump({"octagon": header_dict}, sort_keys=False)

        new_content = f"---\n{yaml_header}---\n{body}"

        with open(file_path, "w") as f:
            f.write(new_content)

    async def publish_stigmergy(self, signal: Dict[str, Any]):
        """
        Publishes the Yield signal to NATS.
        """
        try:
            # Attempt to connect if not connected
            # Note: In a real run, we'd manage connection lifecycle better
            # But for this script, we try-connect on demand or assume it's handled
            await self.stigmergy.publish("hfo.mission.octarchy", signal)
        except Exception as e:
            logger.warning(f"⚠️ Stigmergy Publish Failed (NATS offline?): {e}")

    async def run(self, target_dir: str = "."):
        """
        Main loop: Sequential Processing.
        """
        # Try connecting to NATS once at start
        try:
            await self.stigmergy.connect()
        except Exception:
            logger.warning(
                "⚠️ Could not connect to NATS. Stigmergy will be local-only (logs)."
            )

        all_files = []
        for root, dirs, files in os.walk(target_dir):
            if ".git" in dirs:
                dirs.remove(".git")
            if "venv" in dirs:
                dirs.remove("venv")
            if "__pycache__" in dirs:
                dirs.remove("__pycache__")

            for file in files:
                if (
                    file.endswith((".md", ".py", ".yaml", ".json"))
                    and file != "octarchy_swarm.py"
                ):
                    all_files.append(os.path.join(root, file))

        logger.info(f"Found {len(all_files)} files. Starting Sequential PREY Loop...")

        for i, fp in enumerate(all_files):
            logger.info(f"[{i+1}/{len(all_files)}] Processing {fp}...")
            await self.process_file(fp)


if __name__ == "__main__":
    import sys

    target = sys.argv[1] if len(sys.argv) > 1 else "."
    swarm = OctarchySwarm()
    asyncio.run(swarm.run(target))
