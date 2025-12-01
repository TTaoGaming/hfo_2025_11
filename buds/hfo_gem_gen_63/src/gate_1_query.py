import sys
import os
import json
import hashlib
from datetime import datetime

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_63.src.research_agent import ResearchAgent

def main():
    query = "What is the recommended file structure for the Organ Registry or Fractal Octree in HFO? How should the 8 pillars be mapped to directories?"
    print(f"🔒 Gate 1: Querying Oracle for '{query}'...")
    
    agent = ResearchAgent()
    result = agent.research(query)
    
    # Create the Token
    timestamp = datetime.now().isoformat()
    token_data = {
        "query": query,
        "result": result,
        "timestamp": timestamp,
        "agent": "ResearchAgent_Gen63"
    }
    
    # Generate Hash
    token_str = json.dumps(token_data, sort_keys=True).encode('utf-8')
    token_hash = hashlib.sha256(token_str).hexdigest()[:8]
    token_data["hash"] = token_hash
    
    # Save to Short Term Memory
    filename = f"buds/hfo_gem_gen_63/memory/short_term/query_result_{token_hash}.json"
    with open(filename, "w") as f:
        json.dump(token_data, f, indent=2)
        
    print(f"✅ Gate 1 Passed. Token created: {filename}")
    print(f"🔑 Hash: {token_hash}")

if __name__ == "__main__":
    main()
