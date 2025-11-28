"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: migration-swarm-001
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T13:00:00+00:00'
    generation: 53
  topos:
    address: body/hands/migration_swarm.py
    links: []
  telos:
    viral_factor: 1.0
    meme: The Grand Migration Swarm
"""

import asyncio
import os
import logging
from typing import List
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Configure Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("MigrationSwarm")

# Load Env
load_dotenv()

# Constants
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "x-ai/grok-4.1-fast")
CONCURRENCY = 50
ROUNDS = 3


class DigestArtifact(BaseModel):
    """The output of a single agent's analysis."""

    file_path: str
    pattern_name: str
    bluf: str = Field(..., description="Bottom Line Up Front summary")
    topics: List[str] = Field(..., description="Core keywords and topics found")
    conflicts: List[str] = Field(
        ..., description="Evolutionary conflicts or contradictions detected"
    )
    key_insights: List[str] = Field(..., description="Bullet points of wisdom")
    code_snippet: str = Field(
        ..., description="The most critical code block or text excerpt"
    )
    quality_score: float = Field(
        ..., description="0.0 to 1.0 rating of the content value"
    )


class SwarmConsensus(BaseModel):
    """The final merged digest."""

    title: str
    executive_summary: str
    core_topics: List[str]
    evolutionary_conflicts: List[str]
    patterns: List[DigestArtifact]
    migration_advice: str


async def analyze_file(client, file_path: str, model: str) -> DigestArtifact:
    """Worker Function: Reads a file and extracts wisdom (Iterative Loop)."""
    try:
        with open(file_path, "r") as f:
            content = f.read()

        logger.info(f"🕷️ Agent scanning: {file_path}")

        # Round 1: Initial Scan
        artifact = await client.chat.completions.create(
            model=model,
            response_model=DigestArtifact,
            messages=[
                {
                    "role": "system",
                    "content": "You are a HFO Historian & Researcher. Analyze this file to extract Core Keywords, Research Topics, and Evolutionary Conflicts. We are migrating from Gen 52 to 53. Look for 'Obsidian', 'Octet', 'Stigmergy', 'Fractal' concepts.",
                },
                {"role": "user", "content": f"Analyze this file:\n\n{content[:8000]}"},
            ],
        )

        # Round 2 & 3: Refinement Loop (Self-Correction)
        for i in range(ROUNDS - 1):
            logger.info(f"🔄 Refinement Round {i+2} for {file_path}")
            artifact = await client.chat.completions.create(
                model=model,
                response_model=DigestArtifact,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Senior Editor. Refine the Topics and Conflicts. Ensure keywords are specific (e.g., 'NATS JetStream' not just 'NATS'). Identify contradictions between old and new versions.",
                    },
                    {
                        "role": "user",
                        "content": f"Original Content:\n{content[:2000]}...\n\nCurrent Analysis:\n{artifact.model_dump_json()}\n\nImprove this analysis.",
                    },
                ],
            )

        return artifact
    except Exception as e:
        logger.error(f"❌ Failed to analyze {file_path}: {e}")
        return DigestArtifact(
            file_path=file_path,
            pattern_name="Error",
            bluf=f"Failed to analyze: {str(e)}",
            key_insights=[],
            code_snippet="",
            quality_score=0.0,
        )


async def synthesize_digest(
    client, artifacts: List[DigestArtifact], model: str
) -> SwarmConsensus:
    """Synthesizer Function: Merges artifacts into a final report."""
    logger.info("🧠 Synthesizing Swarm Consensus...")

    # Convert artifacts to text summary
    summary_text = "\n".join(
        [f"- {a.pattern_name}: {a.bluf}" for a in artifacts if a.quality_score > 0.5]
    )

    return await client.chat.completions.create(
        model=model,
        response_model=SwarmConsensus,
        messages=[
            {
                "role": "system",
                "content": "You are the Swarmlord. Synthesize these findings into a Master Migration Digest.",
            },
            {
                "role": "user",
                "content": f"Here are the findings from 50 agents:\n\n{summary_text}",
            },
        ],
    )


async def main():
    logger.info(f"🚀 Launching Migration Swarm (N={CONCURRENCY}, Rounds={ROUNDS})")

    # 1. Setup Client
    client = instructor.from_openai(
        AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        ),
        mode=instructor.Mode.JSON,
    )

    # 2. Scan Target Files (AGENTS.md, Brain, Body)
    files = []

    # Priority 1: The Blackboard
    if os.path.exists("AGENTS.md"):
        files.append("AGENTS.md")

    # Priority 2: The Brain (Strategy & Intents)
    for root, _, filenames in os.walk("brain"):
        for filename in filenames:
            if filename.endswith(".md") or filename.endswith(".feature"):
                files.append(os.path.join(root, filename))

    # Priority 3: The Body (Code)
    for root, _, filenames in os.walk("body"):
        for filename in filenames:
            if filename.endswith(".py") and "test" not in filename:
                files.append(os.path.join(root, filename))

    # Limit to CONCURRENCY
    files = files[:CONCURRENCY]
    logger.info(f"📂 Found {len(files)} target files (Prioritizing AGENTS.md & Brain).")

    # 3. Scatter (Parallel Analysis)
    tasks = [analyze_file(client, f, DEFAULT_MODEL) for f in files]
    artifacts = await asyncio.gather(*tasks)

    # 4. Gather (Synthesis)
    consensus = await synthesize_digest(client, artifacts, DEFAULT_MODEL)

    # 5. Output
    output_path = "buds/hfo_gem_gen_53/memory/library/reference/digest_hfo_discovery.md"

    # Ensure directory exists (Stigmergy Safety)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    markdown = f"""# 🦅 Swarmlord Discovery Digest: HFO Evolution
> **Date**: 2025-11-24
> **Swarm Size**: {len(artifacts)} Agents
> **Consensus**: {consensus.title}

## 1. Executive Summary
{consensus.executive_summary}

## 2. Core Topics & Keywords
{", ".join(consensus.core_topics)}

## 3. Evolutionary Conflicts Detected
{", ".join(consensus.evolutionary_conflicts)}

## 4. Migration Advice
{consensus.migration_advice}

## 5. Detailed Findings
"""
    for art in artifacts:
        if art.quality_score > 0.6:
            markdown += f"\n### {art.pattern_name} (`{art.file_path}`)\n"
            markdown += f"**BLUF**: {art.bluf}\n\n"
            markdown += f"**Topics**: {', '.join(art.topics)}\n\n"
            markdown += f"**Conflicts**: {', '.join(art.conflicts)}\n\n"
            markdown += "**Insights**:\n"
            for insight in art.key_insights:
                markdown += f"- {insight}\n"
            markdown += f"\n```text\n{art.code_snippet}\n```\n"

    with open(output_path, "w") as f:
        f.write(markdown)

    logger.info(f"✅ Migration Digest written to {output_path}")


if __name__ == "__main__":
    asyncio.run(main())
