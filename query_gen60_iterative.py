import sys
import os

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_60.brain.bridger_oracle import BridgerOracle  # noqa: E402


def run_iterative_loops():
    oracle = BridgerOracle()

    # Loop 1: Broad Definition
    print("\n=== LOOP 1: DEFINITION ===")
    query_1 = (
        "What is Hive Fleet Obsidian (HFO) Gen 60 and what is the Obsidian Spider?"
    )
    print(f"Query: {query_1}")
    results_1 = oracle.ask(query_1, limit=3)
    for res in results_1:
        print(f"- [{res['score']:.2f}] {res['text'][:200]}...")

    # Loop 2: Architecture & Structure
    print("\n=== LOOP 2: ARCHITECTURE ===")
    query_2 = "What are the 8 Pillars of HFO and the Fractal Octree architecture?"
    print(f"Query: {query_2}")
    results_2 = oracle.ask(query_2, limit=3)
    for res in results_2:
        print(f"- [{res['score']:.2f}] {res['text'][:200]}...")

    # Loop 3: Specific Mechanisms (Hexagonal & Assimilation)
    print("\n=== LOOP 3: MECHANISMS ===")
    query_3 = "Explain 'Hexagonal Composition' and 'Apex Assimilation' in HFO."
    print(f"Query: {query_3}")
    results_3 = oracle.ask(query_3, limit=3)
    for res in results_3:
        print(f"- [{res['score']:.2f}] {res['text'][:200]}...")


if __name__ == "__main__":
    run_iterative_loops()
