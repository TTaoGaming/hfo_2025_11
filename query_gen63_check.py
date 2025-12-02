import sys
import os

# Add the bud to the path so we can import src
sys.path.append(os.path.abspath("buds/hfo_gem_gen_63"))

from src.research_agent import ResearchAgent  # noqa: E402


def main():
    agent = ResearchAgent()
    query = "What is the recommended file structure for the Organ Registry or Fractal Octree in HFO? How should the 8 pillars be mapped to directories?"
    print(f"Querying Gen 63 Memory: '{query}'")
    result = agent.research(query)
    print("\n--- Result ---")
    print(result)


if __name__ == "__main__":
    main()
