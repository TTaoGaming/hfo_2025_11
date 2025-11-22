import os
import json
import asyncio
from pathlib import Path
from openai import AsyncOpenAI
from body.constants import DEFAULT_MODEL

# Load .env manually
env_path = Path(".env")
if env_path.exists():
    for line in env_path.read_text().splitlines():
        if "=" in line and not line.startswith("#"):
            key, value = line.split("=", 1)
            os.environ[key.strip()] = value.strip().strip('"').strip("'")

# 🏛️ THE CONSENSUS COUNCIL
# Role: Byzantine Fault Tolerance / Auditor
# Mission: Review the Weaver's graph and reach consensus on system health.

AUDIT_REPORT = Path("venom/audit_report.md")
GRAPH_FILE = Path("memory/semantic/knowledge_graph.json")
CONSENSUS_FILE = Path("memory/semantic/consensus_statement.md")


async def convene_council():
    print("🏛️  The Council is convening...")

    if not AUDIT_REPORT.exists() or not GRAPH_FILE.exists():
        print("❌ Missing audit artifacts. Run the Weaver first.")
        return

    report_content = AUDIT_REPORT.read_text()
    graph_data = json.loads(GRAPH_FILE.read_text())

    stats = {
        "nodes": len(graph_data["nodes"]),
        "edges": len(graph_data["links"]),
        "orphans": report_content.count("*   `"),  # Rough estimate from report
    }

    prompt = f"""
    You are the Byzantine Council of the Hive Fleet Obsidian.
    Your task is to audit the Knowledge Graph and declare its health status.

    ## Telemetry
    - Nodes: {stats['nodes']}
    - Edges: {stats['edges']}
    - Orphan Count (Approx): {stats['orphans']}

    ## Audit Report Excerpt
    {report_content[:2000]}...

    ## Mission
    1. Analyze the connectivity. Is the graph fragmented?
    2. Identify the biggest risk (e.g., high orphan count).
    3. Declare a "Consensus Status": HEALTHY, DEGRADED, or CRITICAL.
    4. Propose 3 remedial actions.

    Output in Markdown.
    """

    client = AsyncOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    print("🗳️  Casting votes...")
    try:
        response = await client.chat.completions.create(
            model=DEFAULT_MODEL,  # Fast, cheap auditor
            messages=[
                {
                    "role": "system",
                    "content": "You are the HFO Consensus Council. You are strict, logical, and biological.",
                },
                {"role": "user", "content": prompt},
            ],
        )

        verdict = response.choices[0].message.content

        CONSENSUS_FILE.write_text(verdict)
        print(f"📜 Consensus reached. Verdict saved to {CONSENSUS_FILE}")
        print(verdict)

    except Exception as e:
        print(f"🔥 Council failed to reach consensus: {e}")


if __name__ == "__main__":
    asyncio.run(convene_council())
