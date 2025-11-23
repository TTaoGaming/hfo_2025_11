"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: aa9bac74-31bb-4233-b4d3-8a74b6961260
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.408282+00:00'
    generation: 51
  topos:
    address: body/hands/assimilator_agent.py
    links: []
  telos:
    viral_factor: 0.0
    meme: assimilator_agent.py
"""

import os
import time
import logging
import yaml
import glob
from datetime import datetime
from dotenv import load_dotenv
import instructor
from openai import OpenAI
from pydantic import BaseModel
from body.constants import DEFAULT_MODEL

"""
🦅 Hive Fleet Obsidian: Assimilator Agent
Intent: Watches the Stigmergy Layer (Artifacts) and produces periodic rollups.
"""

load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("Assimilator")

# Load Config
CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "swarm_config.yaml"
)
try:
    with open(CONFIG_PATH, "r") as f:
        CONFIG = yaml.safe_load(f)
except FileNotFoundError:
    CONFIG = {
        "assimilator": {"schedule_interval": 300, "min_artifacts": 5},
        "swarm": {"artifact_dir": "memory/episodic"},
    }

ASSIM_CFG = CONFIG["assimilator"]
ARTIFACT_DIR = CONFIG["swarm"]["artifact_dir"]
KNOWLEDGE_DIR = CONFIG["swarm"].get("knowledge_dir", "memory/semantic")

os.makedirs(KNOWLEDGE_DIR, exist_ok=True)


class KnowledgeArtifact(BaseModel):
    title: str
    summary: str
    key_insights: list[str]
    tags: list[str]


class Assimilator:
    def __init__(self):
        self.client = instructor.from_openai(
            OpenAI(
                base_url=os.getenv("OPENROUTER_BASE_URL"),
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )
        self.model_name = DEFAULT_MODEL

    def scan_artifacts(self):
        """Finds unprocessed artifacts."""
        # In a real system, we'd track processed files in a DB or state file.
        # Here we just grab all .md files in episodic memory.
        files = glob.glob(os.path.join(ARTIFACT_DIR, "*.md"))
        return files

    def digest(self, file_paths):
        """Reads and summarizes artifacts."""
        if not file_paths:
            return

        logger.info(f"🍽️  Digesting {len(file_paths)} artifacts...")

        content_buffer = ""
        for fp in file_paths:
            with open(fp, "r") as f:
                content_buffer += f"\n--- FILE: {os.path.basename(fp)} ---\n"
                content_buffer += f.read()

        # Synthesize
        try:
            artifact = self.client.chat.completions.create(
                model=self.model_name,
                response_model=KnowledgeArtifact,
                messages=[
                    {
                        "role": "system",
                        "content": "You are the Assimilator. Condense these episodic memories into a semantic knowledge artifact.",
                    },
                    {"role": "user", "content": content_buffer},
                ],
            )

            self._save_knowledge(artifact)

        except Exception as e:
            logger.error(f"Digestion failed: {e}")

    def _save_knowledge(self, artifact: KnowledgeArtifact):
        timestamp = datetime.utcnow().isoformat()
        filename = f"knowledge_{timestamp}.md"
        path = os.path.join(KNOWLEDGE_DIR, filename)

        content = f"""---
title: {artifact.title}
timestamp: {timestamp}
tags: {artifact.tags}
---

# {artifact.title}

## Summary
{artifact.summary}

## Key Insights
"""
        for insight in artifact.key_insights:
            content += f"- {insight}\n"

        with open(path, "w") as f:
            f.write(content)

        logger.info(f"💎 Knowledge Crystallized: {filename}")

    def run_loop(self):
        logger.info("👁️  Assimilator Watcher Started")
        while True:
            files = self.scan_artifacts()
            if len(files) >= ASSIM_CFG["min_artifacts"]:
                self.digest(files)
                # In a real system, move processed files to 'archive'
            else:
                logger.info("Not enough artifacts to digest. Sleeping.")

            time.sleep(ASSIM_CFG["schedule_interval"])


if __name__ == "__main__":
    agent = Assimilator()
    # For demo purposes, run once then exit
    files = agent.scan_artifacts()
    if files:
        agent.digest(files)
    else:
        logger.info("No artifacts found.")
