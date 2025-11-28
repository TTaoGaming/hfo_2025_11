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

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory

def ingest_holarchy():
    print("🦅 Ingesting Nested Octree Holarchy Design...")

    # Initialize Memory
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    db_path = os.path.join(root_dir, "memory/lancedb")
    memory = HFOStigmergyMemory(db_path=db_path)
    base_path = "buds/hfo_gem_gen_56"

    # 1. Ingest the Holarchy Design
    design_path = os.path.join(base_path, "brain/design-markdown/design_octree_fractal_holarchy_v2.md")
    with open(design_path, "r") as f: content = f.read()

    memory.store("ontos", {
        "id": "design_octree_holarchy_v2",
        "type": "markdown_design",
        "title": "Design: The Nested Octree Fractal Holarchy",
        "content": content,
        "status": "active"
    })

    # 2. Re-ingest PREY 8888 (Updated)
    print("  -> Updating PREY 8888 with Fractal Link...")
    p8_path = os.path.join(base_path, "brain/design-markdown/design_prey_8888_loop.md")
    with open(p8_path, "r") as f: p8_content = f.read()
    
    memory.store("ontos", {
        "id": "design_prey_8888_loop",
        "type": "markdown_design",
        "title": "Design: The 8-8-8-8 PREY Loop",
        "content": p8_content,
        "status": "active"
    })

    print("✅ Holarchy Ingestion Complete!")

if __name__ == "__main__":
    ingest_holarchy()
