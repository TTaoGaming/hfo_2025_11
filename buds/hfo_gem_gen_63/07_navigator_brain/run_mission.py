"""
---
holon:
  id: hfo-bd53c3da
  type: intent
  file: run_mission.py
  status: active
---
"""
import asyncio
import sys
import os
import yaml
from typing import Optional

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.swarm import HydraSwarm
from forge.genesis import Genesis, HolonHeader

async def run_mission(intent_path: str):
    """
    Executes a Mission:
    1. Reads the Intent (Cold Stigmergy).
    2. Convenes the Council (Hot Processing).
    3. Writes the Design (Cold Crystallization).
    """
    
    if not os.path.exists(intent_path):
        print(f"❌ Intent file not found: {intent_path}")
        return

    print(f"📖 Reading Intent: {intent_path}")
    with open(intent_path, "r") as f:
        content = f.read()
        
    # Extract Title/Topic from Content (Simple parsing)
    # Assuming format "# 🎯 Intent: {Title}"
    topic = "Unknown Mission"
    for line in content.split("\n"):
        if line.startswith("# 🎯 Intent:"):
            topic = line.replace("# 🎯 Intent:", "").strip()
            break
            
    print(f"🚀 Launching Swarm for Topic: '{topic}'")
    
    # Initialize Swarm
    swarm = HydraSwarm()
    
    # Run Council
    print("🏛️  Convening the Council of 8...")
    result = await swarm.convene_council(topic)
    
    print(f"✅ Consensus Reached: {result.consensus}")
    
    # Generate Design File
    design_title = f"Design for {topic}"
    design_path = Genesis.create_design(design_title, intent_id=os.path.basename(intent_path))
    
    # Append Content to Design
    with open(design_path, "a") as f:
        f.write(f"\n## 🏛️ Council Consensus: {result.consensus}\n")
        f.write(f"\n### 📊 Voting Record\n")
        for op in result.opinions:
            f.write(f"- **{op.pillar}**: {op.vote}\n")
            f.write(f"  - *Reasoning*: {op.reasoning}\n")
            
        f.write(f"\n## 🛠️ Action Plan\n")
        f.write(result.action_plan)
        
    print(f"💾 Design Crystallized at: {design_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_mission.py <path_to_intent_file>")
        sys.exit(1)
        
    intent_file = sys.argv[1]
    asyncio.run(run_mission(intent_file))
