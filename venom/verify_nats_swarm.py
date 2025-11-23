"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 5cc4cfcd-a6b1-4899-85ac-cbc44c4daa93
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.266597+00:00'
    generation: 51
  topos:
    address: venom/verify_nats_swarm.py
    links: []
  telos:
    viral_factor: 0.0
    meme: verify_nats_swarm.py
"""

import logging
import sys
import os

# Add workspace root to path
sys.path.append(os.getcwd())

from hfo_sdk import SwarmController, SwarmConfig, MissionIntent  # noqa: E402

logging.basicConfig(level=logging.INFO)


def test_nats_swarm():
    print("🧪 Testing NATS Swarm Integration...")

    # Use a smaller cohort for speed
    config = SwarmConfig(
        cohort_size=3,
        disruptor_count=0,
        base_output_dir="memory/episodic/test_run",
        nats_url="nats://localhost:4222",
    )

    controller = SwarmController(config)

    intent = MissionIntent(
        description="Verify NATS Stigmergy Layer connectivity.", domain="test"
    )

    try:
        results = controller.run_swarm(intent)
        print(f"\n✅ Swarm completed with {len(results)} results.")
        for res in results:
            print(f"   - {res.agent_id}: {res.output[:50]}...")

    except Exception as e:
        print(f"\n❌ Test Failed: {e}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    test_nats_swarm()
