"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440023
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-26T12:00:00.000000Z'
    generation: 51
  topos:
    address: body/hands/handoff_note.py
    links: []
  telos:
    viral_factor: 0.0
    meme: handoff_note.py
"""

import sys
import os
import time
import uuid

# Fix for OMP Error: Must be set before importing libraries that use OpenMP
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

# Add the Gen 55 path to sys.path to import lancedb_store
gen_55_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../buds/hfo_gem_gen_55")
)
sys.path.append(gen_55_path)

try:
    from memory.lancedb_store import HFOStigmergyMemory
except ImportError as e:
    print(f"Error importing HFOStigmergyMemory: {e}")
    print(f"Sys Path: {sys.path}")
    sys.exit(1)


def main():
    # Initialize Memory
    # Pointing to the root memory/lancedb as seen in other scripts
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    db_path = os.path.join(root_dir, "memory/lancedb")

    print(f"Connecting to LanceDB at: {db_path}")
    memory = HFOStigmergyMemory(db_path=db_path)

    # Define Handoff Payload
    handoff_id = str(uuid.uuid4())
    payload = {
        "id": handoff_id,
        "type": "handoff_note",
        "event": "Cloud Heartbeat Pivot",
        "status": "Implemented (Pending Verification)",
        "details": "Pivoted swarm heartbeat from local Gemma to OpenRouter Grok 4.1 Fast. Updated octarchy_heartbeat.py. Logs indicate fallback usage, suggesting missing API Key.",
        "next_steps": [
            "Verify OPENROUTER_API_KEY in .env",
            "Restart Swarm (make heartbeat)",
            "Proceed to Octree Integration (14 Pillars)",
        ],
        "author": "GitHub Copilot (Gemini 3 Pro)",
        "timestamp": time.time(),
    }

    # Store in LanceDB
    # Using 'chronos' section for temporal status updates
    memory.store(section="chronos", payload=payload, privilege_level=0)

    print("Handoff note stored successfully.")


if __name__ == "__main__":
    main()
