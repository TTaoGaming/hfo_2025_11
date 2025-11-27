import sys
import os
import time
import json
from datetime import datetime

# Path setup to import from buds/hfo_gem_gen_55
sys.path.append(os.path.abspath("buds/hfo_gem_gen_55"))

# Fix for OMP Error
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# CRITICAL: Import torch before sentence_transformers/lancedb to prevent OMP error
import torch

try:
    from memory.lancedb_store import HFOStigmergyMemory
except ImportError as e:
    print(f"Error importing HFOStigmergyMemory: {e}")
    sys.exit(1)

def log_activity():
    print("Initializing LanceDB connection...")
    # Use the standard path
    mem = HFOStigmergyMemory(db_path="memory/lancedb")
    
    timestamp = datetime.now().isoformat()
    payload = {
        "activity": "Testing variable heartbeat logic",
        "agents": [
            "cleanroom_prey_1111.py (Heartbeat Generator)",
            "guard_heartbeat_chain.py (Chain Monitor)"
        ],
        "status": "Active",
        "context": "Verifying 5s (Chaotic) vs 60s (Clear) heartbeat intervals and chain integrity.",
        "timestamp": timestamp
    }
    
    section = "hfo_lvl0_timestamp"
    privilege_level = 0
    
    print(f"Logging activity to section '{section}'...")
    mem.store(section, payload, privilege_level)
    print("✅ Activity logged successfully.")

if __name__ == "__main__":
    log_activity()
