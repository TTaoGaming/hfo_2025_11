import asyncio
import sys
import os
import logging

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.brain.bridger_oracle import BridgerOracle
from buds.hfo_gem_gen_60.brain.prey_swarm import PreySwarm

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ObsidianTraversal")


async def run_traversal():
    oracle = BridgerOracle()
    swarm = PreySwarm()

    # 1. Define the 3 Anchors (The Spider Gait)
    anchors = {
        "past": "Case-Based Reasoning (CBR) for Multi-Agent Systems",
        "future": "Monte Carlo Tree Search (MCTS) in Latent Space",
        "present": "Social Spider Optimization (SSO) and Stigmergy",
    }

    print("\n🕷️  Initiating Obsidian Spider Traversal...")
    print("-------------------------------------------")

    # 2. Triangulate Position (Query Oracle for each Anchor)
    context = []
    for leg, query in anchors.items():
        print(f"\n🦵 Anchoring Leg: {leg.upper()} ({query})")
        results = oracle.ask(query, limit=2)
        for res in results:
            print(f"   - Found: {res['text'][:100]}...")
            context.append(res["text"])

    # 3. Search the Latent Space (Ask the Swarm to find SOTA equivalents)
    print("\n🕸️  Crawling the Web for SOTA Equivalents...")

    # We construct a prompt that asks the LLM to synthesize the context and find the SOTA match
    sota_query = f"""
    Based on the following HFO architectural context:
    {context[:3]}

    We are building a 'Hexagonal Hidden Byzantine Swarm' with 'Aggressive Apex Assimilation'.
    We want to adopt existing SOTA research that matches this pattern.

    Find the closest SOTA research equivalents for:
    1. A fractal architecture that combines MCTS and Stigmergy.
    2. A '0 Invention' system that uses hexagonal adapters to wrap tools.
    3. A biological 'Budding' pattern for software evolution.

    Return a list of specific papers, algorithms, or projects we should assimilate.
    """

    # Use the Swarm to "Think" (Simulated via simple chat for now, as full swarm is complex)
    # In a real run, this would dispatch to 8 agents. Here we use the Swarmlord (LLM) directly if possible,
    # but since we don't have a direct LLM chat tool exposed here, we will use the BridgerOracle to find if we ALREADY know this.

    # Actually, let's use the 'PreySwarm' to process this "Mission" if it supports it.
    # Looking at prey_swarm.py, it processes 'MemoryItems'.
    # Let's simulate the "Search" by querying the Oracle for "SOTA Multi-Agent Architecture"

    print("   - Querying Memory for 'SOTA Multi-Agent Architecture'...")
    sota_results = oracle.ask("SOTA Multi-Agent Architecture MCTS Stigmergy", limit=3)

    print("\n💎  Traversal Results (Potential SOTA Matches):")
    for res in sota_results:
        print(f"   - {res['text'][:200]}...")


if __name__ == "__main__":
    asyncio.run(run_traversal())
