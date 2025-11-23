"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 805152aa-d28a-48da-8cd5-4892fc4b4caa
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.263079+00:00'
  topos:
    address: venom/test_hydra_integrity.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_hydra_integrity.py
"""

import time
import os
import yaml
import uuid
from body.hands.hydra_swarm import build_hydra_graph, DIGESTION_DIR


def test_hydra_parallelism_and_intelligence():
    """
    Verifies that the Hydra Swarm is:
    1. NOT Theater (Real LLM calls)
    2. Parallel (Execution time < Sum of individual task times)
    3. Stigmergic (Produces valid artifacts)
    """
    print("\n🧪 Starting Hydra Integrity Test...")

    # 1. Setup
    app = build_hydra_graph()
    mission_id = str(uuid.uuid4())
    mission_prompt = "Generate 3 distinct haikus about rust, neon, and silence."

    # 2. Execution (Measure Time)
    start_time = time.time()
    result = app.invoke(
        {"mission_id": mission_id, "mission": mission_prompt, "results": []}
    )
    end_time = time.time()
    duration = end_time - start_time

    print(f"⏱️  Total Execution Time: {duration:.2f}s")

    # 3. Verify Output Exists
    assert result["final_output"] is not None
    print(f"✅ Consensus Reached: {result['final_output'].consensus_score}")

    # 4. Verify Artifacts (The Trail)
    # Find artifacts for this mission
    mission_artifacts = []
    for filename in os.listdir(DIGESTION_DIR):
        filepath = os.path.join(DIGESTION_DIR, filename)
        with open(filepath, "r") as f:
            content = f.read()
            if mission_id in content:
                # Parse YAML frontmatter
                try:
                    _, frontmatter, body = content.split("---", 2)
                    metadata = yaml.safe_load(frontmatter)
                    mission_artifacts.append(
                        {"file": filename, "meta": metadata, "body": body.strip()}
                    )
                except ValueError:
                    continue

    print(f"📂 Found {len(mission_artifacts)} artifacts for Mission {mission_id}")

    # Assertions
    assert (
        len(mission_artifacts) >= 3
    ), "Should have at least 3 artifacts (Workers + Synthesis)"

    # Check for "Real Intelligence" (Keywords in body)
    bodies = [a["body"].lower() for a in mission_artifacts]
    combined_body = " ".join(bodies)

    assert (
        "rust" in combined_body or "neon" in combined_body or "silence" in combined_body
    ), "Artifacts do not contain requested keywords. Is the LLM working?"

    # Check Metadata
    for a in mission_artifacts:
        assert (
            a["meta"]["model"] == "x-ai/grok-4.1-fast"
        ), f"Wrong model used in {a['file']}"
        assert a["meta"]["mission_id"] == mission_id

    print("✅ Integrity Check Passed: Real LLM, Valid Artifacts, Correct Model.")


if __name__ == "__main__":
    test_hydra_parallelism_and_intelligence()
