import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import sys
import json
import uuid

# Add parent directory to path to import memory module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory

def ingest():
    gherkin_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../brain/intent/hydra_antifragile.feature"))
    
    if not os.path.exists(gherkin_path):
        print(f"Error: File not found at {gherkin_path}")
        return

    with open(gherkin_path, "r") as f:
        content = f.read()
        
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../memory/lancedb"))
    print(f"Connecting to LanceDB at: {db_path}")
    
    try:
        mem = HFOStigmergyMemory(db_path=db_path)
        
        payload = {
            "id": str(uuid.uuid4()),
            "type": "gherkin_intent",
            "title": "Hydra Antifragile and Self-Healing Principle",
            "content": content,
            "tags": ["hydra", "antifragile", "biomimetic", "fractal", "octet", "holonic", "hfo"]
        }
        
        # Storing in 'telos' (Purpose) and 'ontos' (Being)
        mem.store("telos", payload, privilege_level=8) # High privilege as it's core intent
        mem.store("ontos", payload, privilege_level=8)
        
        print("Successfully ingested Hydra Intent into LanceDB.")
        
    except Exception as e:
        print(f"Error during ingestion: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    ingest()
