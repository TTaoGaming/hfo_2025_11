import sys
import os
import uuid

# Add the parent directory to sys.path to import the memory module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory


def ingest_lvl0():
    print("Initializing HFO Memory for Level 0 Ingestion...")
    # Initialize memory (this will load the embedding model)
    memory = HFOStigmergyMemory(db_path="memory/lancedb")

    # Level 0 Data: Atomic Agent Signals
    # These represent the "Prey" loop or simple "Observer" data.

    artifacts = [
        {
            "section": "chronos",
            "payload": {
                "id": str(uuid.uuid4()),
                "type": "heartbeat",
                "agent_id": "agent-007",
                "status": "active",
                "cpu_load": 0.45,
                "message": "System nominal. Awaiting orders.",
            },
        },
        {
            "section": "topos",
            "payload": {
                "id": str(uuid.uuid4()),
                "type": "location",
                "agent_id": "agent-007",
                "coordinates": {"x": 12, "y": 44, "z": 0},
                "message": "Arrived at sector 7G.",
            },
        },
        {
            "section": "pathos",
            "payload": {
                "id": str(uuid.uuid4()),
                "type": "sentiment",
                "agent_id": "agent-007",
                "mood": "alert",
                "urgency": 0.1,
                "message": "No threats detected in immediate vicinity.",
            },
        },
    ]

    print(f"Ingesting {len(artifacts)} Level 0 artifacts...")

    for artifact in artifacts:
        memory.store(
            section=artifact["section"],
            payload=artifact["payload"],
            privilege_level=0,  # Explicitly Level 0
        )

    print("✅ Level 0 Data Ingested.")


if __name__ == "__main__":
    ingest_lvl0()
