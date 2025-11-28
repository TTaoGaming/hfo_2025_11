import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from memory.lancedb_store import HFOStigmergyMemory


def ingest_hybrid_intent():
    print("🦅 Ingesting Hybrid Swarm Intent into Lvl 0 Stigmergy...")

    # Initialize Memory
    memory = HFOStigmergyMemory(db_path="memory/lancedb")

    # 1. Read the Feature File (The Intent)
    feature_path = "brain/intent-literate-gherkin/hybrid_swarm_architecture.feature"
    with open(os.path.join(os.path.dirname(__file__), "..", feature_path), "r") as f:
        feature_content = f.read()

    # 2. Read the Registry (The Config)
    config_path = "blood/config/local_model_registry.yaml"
    with open(os.path.join(os.path.dirname(__file__), "..", config_path), "r") as f:
        config_content = f.read()

    # 3. Store in LanceDB (Lvl 0)
    # We store this as "Nomos" (Law/Config) and "Telos" (Goal/Intent)

    artifacts = [
        {
            "section": "telos",
            "payload": {
                "id": "intent_hybrid_swarm_gen55",
                "type": "gherkin_feature",
                "title": "Hybrid Swarm Architecture",
                "content": feature_content,
                "status": "active",
            },
        },
        {
            "section": "nomos",
            "payload": {
                "id": "config_local_model_registry",
                "type": "yaml_config",
                "title": "Weekly Local Champion Registry",
                "content": config_content,
                "update_cycle": "weekly",
            },
        },
    ]

    for artifact in artifacts:
        memory.store(
            section=artifact["section"],
            payload=artifact["payload"],
            privilege_level=0,  # Explicitly Lvl 0 as requested
        )

    print("✅ Hybrid Intent & Config Ingested to Lvl 0.")


if __name__ == "__main__":
    ingest_hybrid_intent()
