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

def ingest_entropy_funnel():
    print("🦅 Ingesting Fractal Entropy Funnel Design...")

    # Initialize Memory
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
    db_path = os.path.join(root_dir, "memory/lancedb")
    memory = HFOStigmergyMemory(db_path=db_path)
    base_path = "buds/hfo_gem_gen_56"

    # Ingest the Design
    design_path = os.path.join(base_path, "brain/design-markdown/design_fractal_entropy_reduction.md")
    with open(design_path, "r") as f: content = f.read()

    memory.store("ontos", {
        "id": "design_fractal_entropy_funnel_v1",
        "type": "markdown_design",
        "title": "Design: The Fractal Entropy Funnel",
        "content": content,
        "status": "active"
    })

    print("✅ Entropy Funnel Ingestion Complete!")

if __name__ == "__main__":
    ingest_entropy_funnel()
