"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: ecff7e3f-6cb1-4d8f-8bb8-0cdad3faa7ac
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.435044+00:00'
  topos:
    address: body/digestion/swarm_spinner.py
    links: []
  telos:
    viral_factor: 0.0
    meme: swarm_spinner.py
"""

import os
import asyncio
import json
import logging
from datetime import datetime
from typing import List, Dict, Any
from pathlib import Path
import yaml
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from body.digestion.crystal_spinner import CrystalSpinner
from hfo_sdk.stigmergy import StigmergyClient
from body.constants import DEFAULT_MODEL
from body.config import Config

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("swarm_spinner")


class SwarmlordDigest(BaseModel):
    """
    The Final Output: A summary of the entire mission.
    """

    mission_name: str = Field(..., description="Name of the mission")
    total_files_processed: int = Field(..., description="Total files processed")
    success_count: int = Field(..., description="Number of successful files")
    failure_count: int = Field(..., description="Number of failed files")
    domain_breakdown: Dict[str, int] = Field(
        ..., description="Count of files per domain"
    )
    top_concepts: List[str] = Field(
        ..., description="Top 10 most frequent concepts found"
    )
    emergent_patterns: List[str] = Field(
        ..., description="3-5 emergent patterns or insights observed across the corpus"
    )
    executive_summary: str = Field(
        ..., description="A high-level summary of the ingested knowledge"
    )


class Synthesizer:
    """
    The Swarmlord's Eye. Aggregates signals and produces the final digest.
    """

    def __init__(self, nats_url: str, total_expected: int):
        self.stigmergy = StigmergyClient(nats_url)
        self.total_expected = total_expected
        self.processed_count = 0
        self.success_count = 0
        self.failure_count = 0
        self.domains: Dict[str, Any] = {}
        self.concepts: Dict[str, Any] = {}
        self.running = True
        self.client = instructor.from_openai(
            AsyncOpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )
        self.model = DEFAULT_MODEL

    async def start(self):
        await self.stigmergy.connect()
        logger.info("👁️  Synthesizer Online. Watching the Swarm...")

        async def on_crystal(msg):
            try:
                data = json.loads(msg.data.decode())
                self.processed_count += 1
                self.success_count += 1

                meta = data.get("metadata", {})
                domain = meta.get("domain", "Unsorted")
                self.domains[domain] = self.domains.get(domain, 0) + 1

                for concept in meta.get("concepts", []):
                    self.concepts[concept] = self.concepts.get(concept, 0) + 1

                if self.processed_count % 10 == 0:
                    logger.info(
                        f"📊 Progress: {self.processed_count}/{self.total_expected}"
                    )

                await msg.ack()
            except Exception as e:
                logger.error(f"Synthesizer Error: {e}")

        await self.stigmergy.subscribe_queue(
            "hfo.memory.crystallized", "synthesizer", on_crystal
        )

        # Wait for completion
        while self.processed_count < self.total_expected:
            await asyncio.sleep(1)
            # Timeout safety could be added here

        logger.info("✅ All tasks accounted for. Generating Digest...")
        await self.generate_digest()
        self.running = False

    async def generate_digest(self):
        """Generates the Swarmlord of Webs Digest from the physical memory."""

        logger.info("🧠 Aggregating total memory state from disk...")

        # Reset stats to ensure we capture the final state on disk
        final_domains = {}
        final_concepts = {}
        total_files = 0

        library_path = Path("memory/semantic/library")
        if library_path.exists():
            for f in library_path.rglob("*.md"):
                total_files += 1
                try:
                    content = f.read_text(encoding="utf-8")
                    if content.startswith("---"):
                        parts = content.split("---", 2)
                        if len(parts) >= 3:
                            meta = yaml.safe_load(parts[1])
                            if meta:
                                domain = meta.get("domain", "Unsorted")
                                final_domains[domain] = final_domains.get(domain, 0) + 1
                                for concept in meta.get("concepts", []):
                                    final_concepts[concept] = (
                                        final_concepts.get(concept, 0) + 1
                                    )
                except Exception:
                    continue

        # Prepare context for LLM
        top_concepts = sorted(final_concepts.items(), key=lambda x: x[1], reverse=True)[
            :50
        ]
        domain_summary = json.dumps(final_domains, indent=2)
        concept_summary = json.dumps(dict(top_concepts), indent=2)

        prompt = f"""
        The Hive Mind Memory currently contains {total_files} crystallized artifacts.

        Domain Breakdown:
        {domain_summary}

        Top Concepts (Frequency):
        {concept_summary}

        Generate a 'Swarmlord of Webs Digest' summarizing the state of the Hive's knowledge.
        Focus on the emergent patterns, the convergence of ideas, and the overall shape of the knowledge base.
        """

        try:
            digest = await self.client.chat.completions.create(
                model=self.model,
                response_model=SwarmlordDigest,
                messages=[
                    {
                        "role": "system",
                        "content": "You are the Swarmlord. Synthesize the mission results.",
                    },
                    {"role": "user", "content": prompt},
                ],
            )

            # Save to file with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            output_path = Path(f"Swarmlord_of_Webs_Digest_{timestamp}.md")

            with open(output_path, "w") as f:
                f.write(f"# 🦅 {digest.mission_name}\n\n")
                f.write(f"**Date**: {timestamp}\n")
                f.write(f"**Executive Summary**: {digest.executive_summary}\n\n")
                f.write("## 📊 Stats\n")
                f.write(f"- **Total Processed**: {digest.total_files_processed}\n")
                f.write(f"- **Success**: {digest.success_count}\n")
                f.write(f"- **Failure**: {digest.failure_count}\n\n")
                f.write("## 🌐 Domain Breakdown\n")
                for d, c in digest.domain_breakdown.items():
                    f.write(f"- **{d}**: {c}\n")
                f.write("\n## 🧠 Top Concepts\n")
                for c in digest.top_concepts:
                    f.write(f"- {c}\n")
                f.write("\n## ✨ Emergent Patterns\n")
                for p in digest.emergent_patterns:
                    f.write(f"- {p}\n")

            logger.info(f"📜 Digest saved to {output_path}")

        except Exception as e:
            logger.error(f"Failed to generate digest: {e}")


class SwarmSpinner:
    """
    A Swarm-enabled version of the Crystal Spinner.
    Uses NATS Queue Groups to distribute work among multiple workers.
    """

    def __init__(self, worker_id: str, nats_url: str = Config.NATS_URL):
        self.worker_id = worker_id
        self.spinner = CrystalSpinner(nats_url)
        self.running = True

    async def start_worker(self):
        """Starts the worker loop."""
        await self.spinner.connect()
        logger.info(
            f"🕷️  Worker {self.worker_id} Online. Listening on 'hfo.task.spin'..."
        )

        async def process_msg(msg):
            try:
                data = json.loads(msg.data.decode())
                file_path = data.get("file_path")

                if not file_path:
                    await msg.ack()
                    return

                logger.info(f"[{self.worker_id}] 📥 Received: {file_path}")

                # Read File
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    logger.error(f"[{self.worker_id}] ❌ Read Error: {e}")
                    await msg.ack()
                    return

                # Spin (LLM)
                metadata = await self.spinner.spin(content, Path(file_path).name)

                # Harden (YAML)
                new_content = self.spinner.harden(content, metadata)

                # Weave (Save & Signal)
                await self.spinner.weave(Path(file_path), new_content, metadata)

                logger.info(f"[{self.worker_id}] ✅ Done: {file_path}")
                await msg.ack()

            except Exception as e:
                logger.error(f"[{self.worker_id}] 💥 Processing Error: {e}")
                # Don't ack if we want retry, but for now ack to prevent loop
                await msg.ack()

        # Subscribe to the queue group "spinners"
        # This ensures only ONE worker gets each message
        await self.spinner.stigmergy.subscribe_queue(
            subject="hfo.task.spin", queue="spinners", callback=process_msg
        )

        # Keep alive
        while self.running:
            await asyncio.sleep(1)

    async def stop(self):
        self.running = False
        await self.spinner.close()


async def run_dispatcher(nats_url: str = Config.NATS_URL) -> int:
    """Scans files and dispatches tasks to the swarm. Returns count."""
    logger.info("👑 Dispatcher Online. Scanning for Gems...")

    client = StigmergyClient(nats_url)
    await client.connect()

    source_dir = Path("eyes/archive/hfo_gem")
    files = list(source_dir.rglob("*.md"))

    # Check for existing crystallized artifacts to avoid re-processing
    library_dir = Path("memory/semantic/library")
    existing_filenames = set()
    if library_dir.exists():
        existing_filenames = {f.name for f in library_dir.rglob("*.md")}

    files_to_process = []
    for f in files:
        # Replicate naming logic from CrystalSpinner.weave
        parent_name = f.parent.name
        if "gen_" in parent_name or f.name.lower() in [
            "readme.md",
            "summary.md",
            "deep_dive.md",
        ]:
            expected_name = f"{parent_name}_{f.name}"
        else:
            expected_name = f.name

        if expected_name not in existing_filenames:
            files_to_process.append(f)

    logger.info(
        f"Found {len(files)} gems. {len(existing_filenames)} already crystallized. Dispatching {len(files_to_process)} tasks..."
    )

    for i, file_path in enumerate(files_to_process):
        payload = {"file_path": str(file_path)}
        await client.publish("hfo.task.spin", payload)
        if i % 50 == 0:
            print(f"   🚀 Dispatched {i}/{len(files_to_process)} tasks...")

    logger.info("✅ All tasks dispatched.")
    await client.close()
    return len(files_to_process)


async def main():
    nats_url = Config.NATS_URL

    # 1. Start Dispatcher
    total_tasks = await run_dispatcher(nats_url)

    # 2. Start Synthesizer (The Swarmlord's Eye)
    synthesizer = Synthesizer(nats_url, total_tasks)
    synth_task = asyncio.create_task(synthesizer.start())

    # 3. Start Swarm (50 Workers)
    workers = []
    for i in range(50):
        worker = SwarmSpinner(f"worker-{i+1}", nats_url)
        workers.append(worker)

    logger.info("🔥 Swarm Activated (50 Workers). Processing in parallel...")

    try:
        # Run workers in background
        worker_tasks = [asyncio.create_task(w.start_worker()) for w in workers]

        # Wait for Synthesizer to finish (it tracks progress)
        await synth_task

        logger.info("🏁 Mission Complete. Shutting down Swarm...")

    except KeyboardInterrupt:
        logger.info("🛑 Stopping Swarm...")
    finally:
        for w in workers:
            await w.stop()
        # Cancel worker tasks
        for t in worker_tasks:
            t.cancel()


if __name__ == "__main__":
    # Ensure PYTHONPATH is set
    import sys

    sys.path.append(os.getcwd())
    asyncio.run(main())
