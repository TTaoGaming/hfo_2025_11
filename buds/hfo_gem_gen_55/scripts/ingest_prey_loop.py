import os

# Fix for OMP Error
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['OMP_NUM_THREADS'] = '1'

import sys

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory

def ingest_prey_loop():
    print("🦅 Ingesting 1-1-1-1 PREY Loop Intent into Lvl 0 Stigmergy...")

    # Initialize Memory
    # Note: Adjust db_path if necessary. The previous script used "memory/lancedb" relative to the root?
    # The previous script was in buds/hfo_gem_gen_55/scripts/ and used "memory/lancedb".
    # But HFOStigmergyMemory likely expects a path relative to where the script is run or absolute.
    # Let's assume running from repo root.
    memory = HFOStigmergyMemory(db_path="memory/lancedb")

    base_path = "buds/hfo_gem_gen_55"
    
    # 1. Read the Design Document
    design_path = os.path.join(base_path, "brain/design-markdown/design_prey_1111_loop.md")
    with open(design_path, "r") as f:
        design_content = f.read()

    # 2. Read the Feature File
    feature_path = os.path.join(base_path, "brain/intent-literate-gherkin/prey_1111_loop.feature")
    with open(feature_path, "r") as f:
        feature_content = f.read()

    # 3. Store in LanceDB (Lvl 0)
    artifacts = [
        {
            "section": "ontos", # Design/Knowledge
            "payload": {
                "id": "design_prey_1111_loop",
                "type": "markdown_design",
                "title": "Design: The 1-1-1-1 PREY Loop",
                "content": design_content,
                "status": "active",
            },
        },
        {
            "section": "telos", # Intent/Goal
            "payload": {
                "id": "intent_prey_1111_loop",
                "type": "gherkin_feature",
                "title": "The 1-1-1-1 PREY Loop Protocol",
                "content": feature_content,
                "status": "active",
            },
        },
    ]

    for artifact in artifacts:
        print(f"  -> Storing {artifact['payload']['title']}...")
        memory.store_artifact(
            section=artifact["section"],
            payload=artifact["payload"]
        )

    print("✅ Ingestion Complete.")

if __name__ == "__main__":
    ingest_prey_loop()
