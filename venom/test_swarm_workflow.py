"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: cd88a07f-b61e-4cc7-9710-64050691a0e3
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.265381+00:00'
  topos:
    address: venom/test_swarm_workflow.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_swarm_workflow.py
"""

import os
import shutil
from body.hands.swarm_controller import SwarmController

TEST_DIR = "/tmp/hfo_swarm_test"


def setup_module():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)
    os.makedirs(TEST_DIR, exist_ok=True)


def teardown_module():
    # Optional: Keep it for inspection
    pass


def test_swarm_workflow():
    print("\n🧪 TEST: Full SWARM Workflow (Scatter-Gather + Disruptor)")

    # 1. Initialize
    controller = SwarmController(mission_id="swarm-test-001")
    intent = "Design a Dyson Sphere power grid"

    # 2. Run Swarm
    results = controller.run_swarm(intent)

    # 3. Verify Outputs
    print("\n🔍 Verifying Artifacts...")

    # Check for honest files
    # Note: The agents might name files slightly differently depending on LLM output,
    # but we instructed them specifically. Let's check if the folders exist at least.

    arch_exists = os.path.exists(f"{TEST_DIR}/architecture")
    eng_exists = os.path.exists(f"{TEST_DIR}/engineering")
    lib_exists = os.path.exists(f"{TEST_DIR}/library")

    print(f"   Architecture Folder: {arch_exists}")
    print(f"   Engineering Folder: {eng_exists}")
    print(f"   Library Folder: {lib_exists}")

    # Check for disruptor file
    sabotage_exists = os.path.exists(f"{TEST_DIR}/sabotage.md")
    print(f"   Sabotage File: {sabotage_exists}")

    assert arch_exists and eng_exists and lib_exists
    assert sabotage_exists

    # 4. Verify Consensus
    consensus = controller.review_results(results)
    print(f"\n⚖️  Consensus Result: {consensus}")

    assert "Consensus Reached" in consensus
    print("   ✅ Success: Swarm coordinated and overcame disruption.")


if __name__ == "__main__":
    setup_module()
    test_swarm_workflow()
