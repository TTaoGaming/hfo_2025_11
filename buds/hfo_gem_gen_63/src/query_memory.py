import sys
import os

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_63.src.research_agent import ResearchAgent

def main():
    if len(sys.argv) < 2:
        print("Usage: python query_memory.py <query>")
        sys.exit(1)
        
    query = sys.argv[1]
    print(f"🔍 Querying Gen 63 Memory: '{query}'")
    
    agent = ResearchAgent()
    result = agent.research(query)
    
    print("\n" + "="*40)
    print("🧠 MEMORY RESULT:")
    print("="*40)
    print(result)
    print("="*40)

if __name__ == "__main__":
    main()
