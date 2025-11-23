"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 3fbe57b0-2431-4c8b-b713-177869f5ec29
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.329277+00:00'
  topos:
    address: venom/smoke/test_hydra_swarm.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_hydra_swarm.py
"""

import pytest
from body.hands.hydra_swarm import build_hydra_graph


def test_hydra_swarm_smoke():
    print("\n🧪 SMOKE TEST: Hydra Scatter-Gather Pattern")

    try:
        app = build_hydra_graph()

        initial_state = {
            "mission": "Analyze the viability of a Dyson Sphere",
            "results": [],
        }

        print("   🚀 Launching Swarm...")
        final = app.invoke(initial_state)

        # Assertions
        assert final is not None
        assert "plan" in final
        assert len(final["plan"]) > 0
        assert "results" in final
        assert len(final["results"]) == len(final["plan"])  # Gathered all
        assert "final_output" in final
        assert final["final_output"].consensus_score > 0.0

        print(f"   ✅ Plan Generated: {len(final['plan'])} tasks")
        print(f"   ✅ Results Gathered: {len(final['results'])} outputs")
        print(f"   ✅ Synthesis: {final['final_output'].summary[:50]}...")

    except Exception as e:
        pytest.fail(f"Hydra Swarm failed: {e}")


if __name__ == "__main__":
    test_hydra_swarm_smoke()
