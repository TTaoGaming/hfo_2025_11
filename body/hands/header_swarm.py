"""
🦅 Hive Fleet Obsidian: Header Swarm (Gen 51)
Intent: Generate "Deep Semantic" Stigmergy Headers using a 10-Agent Swarm.
Workflow: 10 -> 5 -> 1 Funnel (Generate -> Refine -> Consensus).
"""

import os
import asyncio
import logging
import yaml
import uuid
import datetime
from typing import List
from pathlib import Path
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Setup
load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("HeaderSwarm")

# Constants
MODEL = os.getenv("DEFAULT_MODEL", "google/gemini-2.0-flash-001")  # Fast & Cheap
SQUAD_SIZE = 10
REFINE_SIZE = 5

# --- Pydantic Models (The DNA) ---


class Ontos(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str = Field(..., description="Type of the file (doc, code, concept, pattern)")
    owner: str = Field(..., description="Owner/Steward of this concept")


class Chronos(BaseModel):
    status: str = Field(..., description="active, draft, archived, stable")
    urgency: float = Field(
        ..., ge=0.0, le=1.0, description="0.0 (Low) to 1.0 (Critical)"
    )
    decay: float = Field(..., ge=0.0, le=1.0, description="Relevance decay rate")
    created: str = Field(
        default_factory=lambda: datetime.datetime.utcnow().isoformat() + "Z"
    )


class Topos(BaseModel):
    address: str = Field(..., description="Virtual address (e.g., 1.2.3)")
    links: List[str] = Field(
        default_factory=list, description="Related file paths or IDs"
    )


class Telos(BaseModel):
    viral_factor: float = Field(..., ge=0.0, le=1.0, description="Potential for spread")
    meme: str = Field(..., description="Short, catchy meme/slogan for this file")


class Hexagon(BaseModel):
    ontos: Ontos
    chronos: Chronos
    topos: Topos
    telos: Telos


class Face(BaseModel):
    title: str = Field(..., description="Clear, descriptive title")
    bluf: str = Field(..., description="Bottom Line Up Front (Summary)")
    story: str = Field(..., description="Narrative context or 'The Why'")
    tags: List[str] = Field(default_factory=list)


class HolonHeader(BaseModel):
    face: Face
    hexagon: Hexagon


# --- The Swarm ---


class HeaderSwarm:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.content = file_path.read_text(encoding="utf-8")
        self.client = instructor.from_openai(
            AsyncOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )

    async def generate_header(self) -> HolonHeader:
        logger.info(f"🦅 Swarm initialized for {self.file_path.name}")

        # Round 1: Divergence (10 Agents)
        logger.info(f"🌊 Round 1: Divergence ({SQUAD_SIZE} Agents)...")
        candidates = await self._round_1_divergence()

        # Round 2: Convergence (5 Agents)
        logger.info(f"🌪️ Round 2: Convergence ({REFINE_SIZE} Agents)...")
        refined = await self._round_2_convergence(candidates)

        # Round 3: Consensus (1 Swarmlord)
        logger.info("👑 Round 3: Consensus (Swarmlord)...")
        final_header = await self._round_3_consensus(refined)

        return final_header

    async def _round_1_divergence(self) -> List[HolonHeader]:
        """10 Agents analyze the file independently."""
        tasks = []
        for i in range(SQUAD_SIZE):
            tasks.append(self._analyze_file(i))
        return await asyncio.gather(*tasks)

    async def _analyze_file(self, agent_id: int) -> HolonHeader:
        prompt = f"""
        You are Agent {agent_id} of the Obsidian Swarm.
        Analyze the following file content and generate a 'Holon Header' (Face + Hexagon).

        Context:
        - File: {self.file_path}
        - Goal: Deep Semantic Understanding.

        Content:
        {self.content[:5000]} # Truncate for context window if needed
        """
        return await self.client.chat.completions.create(
            model=MODEL,
            response_model=HolonHeader,
            messages=[{"role": "user", "content": prompt}],
        )

    async def _round_2_convergence(
        self, candidates: List[HolonHeader]
    ) -> List[HolonHeader]:
        """5 Agents review the 10 candidates and synthesize better versions."""
        # Split candidates into chunks for reviewers
        chunk_size = len(candidates) // REFINE_SIZE
        tasks = []
        for i in range(REFINE_SIZE):
            chunk = candidates[i * chunk_size : (i + 1) * chunk_size]
            tasks.append(self._refine_candidates(i, chunk))
        return await asyncio.gather(*tasks)

    async def _refine_candidates(
        self, agent_id: int, chunk: List[HolonHeader]
    ) -> HolonHeader:
        prompt = f"""
        You are Reviewer {agent_id}.
        Review the following {len(chunk)} header candidates.
        Synthesize the BEST attributes of each into a single, superior header.

        Candidates:
        {chunk}
        """
        return await self.client.chat.completions.create(
            model=MODEL,
            response_model=HolonHeader,
            messages=[{"role": "user", "content": prompt}],
        )

    async def _round_3_consensus(self, refined: List[HolonHeader]) -> HolonHeader:
        """The Swarmlord makes the final decision."""
        prompt = f"""
        You are the Swarmlord.
        Review the following {len(refined)} refined headers.
        Create the FINAL CONSENSUS header.
        Ensure the 'Hexagon' metrics (urgency, viral_factor) are realistic.
        Ensure the 'Face' (BLUF, Story) is compelling and accurate.

        Refined Candidates:
        {refined}
        """
        return await self.client.chat.completions.create(
            model=MODEL,
            response_model=HolonHeader,
            messages=[{"role": "user", "content": prompt}],
        )


# --- CLI Entrypoint ---


async def main_async(file_path_str: str):
    path = Path(file_path_str)
    if not path.exists():
        print(f"❌ File not found: {path}")
        return

    swarm = HeaderSwarm(path)
    header = await swarm.generate_header()

    print("\n💎 FINAL CONSENSUS HEADER 💎")
    print("=============================")
    print(header.model_dump_json(indent=2))

    # Write back to file
    try:
        # Reconstruct YAML
        face_dict = header.face.model_dump()
        hexagon_dict = header.hexagon.model_dump()
        face_dict["hexagon"] = hexagon_dict

        new_yaml = yaml.dump(face_dict, sort_keys=False, allow_unicode=True)

        # Add comments
        new_yaml = new_yaml.replace(
            "hexagon:",
            "\n# ==================================================================\n# 🤖 THE HEXAGON (Swarm Generated)\n# ==================================================================\nhexagon:",
        )

        # Read original body
        content = path.read_text(encoding="utf-8")
        parts = content.split("---", 2)
        if len(parts) >= 3:
            body = parts[2]
        else:
            body = content  # Fallback if no frontmatter

        new_content = f"---\n{new_yaml}---\n{body}"
        path.write_text(new_content, encoding="utf-8")
        print(f"\n✅ Swarm Crystallization Complete: {path}")

    except Exception as e:
        print(f"\n❌ Error writing to file: {e}")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python header_swarm.py <file_path>")
    else:
        asyncio.run(main_async(sys.argv[1]))
