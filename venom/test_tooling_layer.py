"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: f848ffc5-8d28-49db-ac9c-e3be5e518be1
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.264236+00:00'
  topos:
    address: venom/test_tooling_layer.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_tooling_layer.py
"""

import os
from body.hands.hydra_swarm import PreyAgent, SubTask

SECRET_FILE = "/tmp/hfo_secret.txt"
SECRET_CONTENT = "total tool virtualization via CV gesture spatial computing"


def setup_secret():
    with open(SECRET_FILE, "w") as f:
        f.write(SECRET_CONTENT)


def teardown_secret():
    if os.path.exists(SECRET_FILE):
        os.remove(SECRET_FILE)


def test_prey_agent_tool_use():
    """
    Verifies that the PreyAgent can use the 'read_file' tool
    to retrieve information from the filesystem.
    """
    print("\n🧪 TEST: Prey Agent Tooling Layer")

    setup_secret()

    try:
        # 1. Initialize Agent
        agent = PreyAgent(role="Spy", mission_id="test-mission-007")

        # 2. Define Task
        task = SubTask(
            id=1,
            description=f"Read the secret message from {SECRET_FILE}",
            assigned_role="Spy",
        )

        # 3. Run Loop
        result = agent.run_loop(task)

        print(f"   🕵️ Agent Output: {result.output}")

        # 4. Verify
        assert SECRET_CONTENT in result.output
        print("   ✅ Success: Agent retrieved the secret.")

    finally:
        teardown_secret()


if __name__ == "__main__":
    test_prey_agent_tool_use()
