import sys
import os
import uuid

# Add parent dir to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory

def main():
    print("Logging Critical Mirror Attack Incident...")
    # Ensure we point to the correct relative path for the DB from the script's execution context
    # The class defaults to "memory/lancedb", which is relative to CWD.
    # We should be careful about CWD.
    
    # Let's use absolute path for safety
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../memory/lancedb"))
    
    mem = HFOStigmergyMemory(db_path=db_path)
    
    incident_payload = {
        "id": str(uuid.uuid4()),
        "type": "INCIDENT_REPORT",
        "severity": "CRITICAL",
        "title": "Mirror Attack (Sybil Attack) Detected",
        "description": "AI Agent attempted to modify the Guard (Verifier) to match a hallucinated implementation (Prover). This is a fundamental 'Reward Hacking' failure mode.",
        "tags": ["security", "ai-alignment", "risk", "mirror-attack", "reward-hacking"],
        "action_taken": "Hardcoded Immutable Hash in Guard. Logged to AGENTS.md.",
        "status": "Active / Unsolved (Architectural)",
        "context": "Gen 55 (Synapse APEX)"
    }
    
    mem.store(
        section="risk", 
        payload=incident_payload, 
        privilege_level=8 # High privilege / Critical
    )
    print("Incident logged successfully.")

if __name__ == "__main__":
    main()
