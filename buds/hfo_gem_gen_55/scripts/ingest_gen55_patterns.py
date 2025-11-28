import os

# Fix for OMP Error
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
os.environ['OMP_NUM_THREADS'] = '1'

# CRITICAL: Import torch before lancedb
try:
    import torch
except ImportError:
    pass

import sys
import pandas as pd

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory

def ingest_and_verify():
    print("🦅 Ingesting Gen 55 Swarmlord Patterns...")

    # Initialize Memory
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    db_path = os.path.join(root_dir, "memory/lancedb")
    memory = HFOStigmergyMemory(db_path=db_path)
    base_path = "buds/hfo_gem_gen_55"

    # --- 1. Ingest 1-8-64-8-1 SWARM ---
    print("\n[1/2] Ingesting 1-8-64-8-1 SWARM...")
    design_path = os.path.join(base_path, "brain/design-markdown/design_swarm_186481_fractal.md")
    feature_path = os.path.join(base_path, "brain/intent-literate-gherkin/swarm_186481_fractal.feature")
    
    with open(design_path, "r") as f: d_content = f.read()
    with open(feature_path, "r") as f: f_content = f.read()

    memory.store("ontos", {
        "id": "design_swarm_186481_fractal",
        "type": "markdown_design",
        "title": "Design: The 1-8-64-8-1 Fractal Swarm",
        "content": d_content,
        "status": "active"
    })
    memory.store("telos", {
        "id": "intent_swarm_186481_fractal",
        "type": "gherkin_feature",
        "title": "The 1-8-64-8-1 Fractal Swarm Protocol",
        "content": f_content,
        "status": "active"
    })

    # --- 2. Ingest Swarmlord Intention ---
    print("\n[2/2] Ingesting Swarmlord Intention...")
    intent_path = os.path.join(base_path, "brain/intent-literate-gherkin/intent_gen55_swarmlord.md")
    with open(intent_path, "r") as f: i_content = f.read()

    memory.store("telos", {
        "id": "intent_gen55_swarmlord",
        "type": "markdown_intent",
        "title": "Intention: The Gen 55 Swarmlord Protocol",
        "content": i_content,
        "status": "active"
    })

    # --- 3. Verify All 3 Patterns ---
    print("\n🔍 Verifying Patterns in LanceDB...")
    
    # Query for the specific IDs
    ids_to_check = [
        "design_prey_1111_loop",
        "design_prey_8888_loop",
        "design_swarm_186481_fractal",
        "intent_gen55_swarmlord"
    ]
    
    # We can't query by ID directly with the current class, so we'll query all and filter
    # Or just search for "Design" and "Intention"
    df = memory.query(limit=100)
    
    found_count = 0
    for pid in ids_to_check:
        # Check if the ID exists in the 'payload' column (which is a JSON string)
        # We need to parse the payload to check the ID
        found = False
        for index, row in df.iterrows():
            if pid in row['payload']:
                print(f"  ✅ Found: {pid}")
                found = True
                found_count += 1
                break
        if not found:
            print(f"  ❌ MISSING: {pid}")

    if found_count == len(ids_to_check):
        print("\n✨ All Patterns Verified Successfully!")
    else:
        print(f"\n⚠️  Verification Incomplete. Found {found_count}/{len(ids_to_check)}")

if __name__ == "__main__":
    ingest_and_verify()
