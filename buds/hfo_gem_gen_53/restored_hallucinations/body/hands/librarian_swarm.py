"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: librarian-swarm-001
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 1.0
    decay: 0.0
    created: '2025-11-24T15:00:00+00:00'
    generation: 53
  topos:
    address: body/hands/librarian_swarm.py
    links: []
  telos:
    viral_factor: 1.0
    meme: The Librarian Swarm (Ledger Based)
"""

import asyncio
import os
import json
import logging
from typing import List, Dict, Optional
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Configure Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("LibrarianSwarm")

# Load Env
load_dotenv()

# Constants
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "x-ai/grok-4.1-fast")
LEDGER_PATH = "buds/hfo_gem_gen_53/migration_ledger.json"
ROUNDS = 3


class LedgerEntry(BaseModel):
    path: str
    status: str = "PENDING"  # PENDING, IN_PROGRESS, MIGRATED, ERROR
    cluster: str = "Unclassified"
    last_touched: Optional[str] = None


class MigrationLedger(BaseModel):
    entries: Dict[str, LedgerEntry]


class DigestOption(BaseModel):
    """A strategic choice for the Overmind."""

    option_name: str
    pros: str
    cons: str
    alignment_score: float = Field(
        ..., description="0-1 score on alignment with Fractal Holarchy"
    )


class LibrarianDigest(BaseModel):
    """The output of the Librarian Swarm."""

    title: str
    bluf: str
    matrix_data: List[Dict[str, str]] = Field(
        ..., description="Key-Value pairs for the Matrix"
    )
    evolutionary_conflicts: List[str] = Field(
        ..., description="High-level contradictions found"
    )
    strategic_options: List[DigestOption] = Field(
        ..., description="Choices for the Overmind"
    )
    mermaid_diagram: str = Field(..., description="Mermaid code for the Map")
    gherkin_intent: str = Field(..., description="Draft Gherkin spec")


async def initialize_ledger():
    """Scans the repo and creates the ledger."""
    if os.path.exists(LEDGER_PATH):
        logger.info("📜 Ledger already exists. Skipping initialization.")
        return

    entries = {}
    # Scan Brain, Body, Memory
    for root_dir in ["brain", "body", "memory"]:
        for root, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith((".py", ".md", ".feature", ".yaml")):
                    path = os.path.join(root, filename)
                    # Simple Clustering Logic
                    cluster = "Unclassified"
                    if "infrastructure" in filename or "nats" in filename:
                        cluster = "Infrastructure"
                    elif "biology" in filename or "organ" in filename:
                        cluster = "Biology"
                    elif "strategy" in filename or "intent" in filename:
                        cluster = "Strategy"

                    entries[path] = LedgerEntry(path=path, cluster=cluster)

    ledger = MigrationLedger(entries=entries)
    os.makedirs(os.path.dirname(LEDGER_PATH), exist_ok=True)
    with open(LEDGER_PATH, "w") as f:
        f.write(ledger.model_dump_json(indent=2))
    logger.info(f"✅ Ledger initialized with {len(entries)} files.")


async def process_cluster(client, cluster_name: str, files: List[str], model: str):
    """Runs the 3-Round Loop on a cluster of files."""
    logger.info(f"📚 Processing Cluster: {cluster_name} ({len(files)} files)")

    # Read Content
    combined_content = ""
    for fpath in files:
        try:
            with open(fpath, "r") as f:
                combined_content += (
                    f"\n--- FILE: {fpath} ---\n{f.read()[:4000]}"  # Truncate
                )
        except Exception:
            pass

    # Round 1: Scan
    logger.info(f"🔄 Round 1: Scanning {cluster_name}...")
    digest = await client.chat.completions.create(
        model=model,
        response_model=LibrarianDigest,
        messages=[
            {
                "role": "system",
                "content": "You are the Librarian. Analyze these files. Identify the Core Concept, the Evolution (Gen 51->53), and Conflicts. Focus on 'Fractal Holarchy' and 'Obsidian Stigmergy'.",
            },
            {
                "role": "user",
                "content": combined_content[:30000],
            },  # Context Limit Check
        ],
    )

    # Round 2 & 3: Refine
    for i in range(ROUNDS - 1):
        logger.info(f"🔄 Round {i+2}: Refining {cluster_name}...")
        digest = await client.chat.completions.create(
            model=model,
            response_model=LibrarianDigest,
            messages=[
                {
                    "role": "system",
                    "content": "You are the Swarmlord. Refine this digest. Present 'Conflicting Opinions' as 'Strategic Options'. Ensure the Mermaid diagram is valid. Align with 'Obsidian Melt-Glass-Refinement' metaphor.",
                },
                {
                    "role": "user",
                    "content": f"Current Digest:\n{digest.model_dump_json()}\n\nImprove this.",
                },
            ],
        )

    # Output Literate Spec
    output_filename = f"intent_{cluster_name.lower().replace(' ', '_')}.md"
    output_path = f"buds/hfo_gem_gen_53/brain/intents/{output_filename}"

    markdown = f"""# 🦅 Intent: {digest.title}

> **Status**: Draft (Librarian Generated)
> **Cluster**: {cluster_name}

## 1. BLUF & Matrix
**BLUF**: {digest.bluf}

### The Matrix
| Key | Value |
| :--- | :--- |
"""
    for item in digest.matrix_data:
        markdown += f"| {list(item.keys())[0]} | {list(item.values())[0]} |\n"

    markdown += f"""
---

## 2. Visual Architecture
```mermaid
{digest.mermaid_diagram}
```

---

## 3. Cognitive Digest
### Evolutionary Conflicts
"""
    for conflict in digest.evolutionary_conflicts:
        markdown += f"*   {conflict}\n"

    markdown += "\n### Strategic Options (For Overmind Decision)\n"
    for opt in digest.strategic_options:
        markdown += f"#### Option: {opt.option_name}\n"
        markdown += f"*   **Pros**: {opt.pros}\n"
        markdown += f"*   **Cons**: {opt.cons}\n"
        markdown += f"*   **Alignment**: {opt.alignment_score}\n\n"

    markdown += f"""
---

## 4. Declarative Intent (Draft)
```gherkin
{digest.gherkin_intent}
```
"""
    with open(output_path, "w") as f:
        f.write(markdown)

    logger.info(f"✅ Generated Spec: {output_path}")
    return files


async def main():
    # 1. Init Ledger
    await initialize_ledger()

    # 2. Load Ledger
    with open(LEDGER_PATH, "r") as f:
        data = json.load(f)
        ledger = MigrationLedger(**data)

    # 3. Group Pending by Cluster
    clusters = {}
    for path, entry in ledger.entries.items():
        if entry.status == "PENDING":
            if entry.cluster not in clusters:
                clusters[entry.cluster] = []
            clusters[entry.cluster].append(path)

    # 4. Process Clusters (Limit to 3 for demo)
    client = instructor.from_openai(
        AsyncOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPENROUTER_API_KEY"),
        ),
        mode=instructor.Mode.JSON,
    )

    processed_files = []
    target_clusters = ["Infrastructure", "Biology", "Strategy"]

    for cluster in target_clusters:
        if cluster in clusters:
            files = clusters[cluster][:10]  # Limit to 10 files per cluster for context
            if files:
                processed = await process_cluster(client, cluster, files, DEFAULT_MODEL)
                processed_files.extend(processed)

    # 5. Update Ledger
    for path in processed_files:
        ledger.entries[path].status = "MIGRATED"

    with open(LEDGER_PATH, "w") as f:
        f.write(ledger.model_dump_json(indent=2))


if __name__ == "__main__":
    asyncio.run(main())
