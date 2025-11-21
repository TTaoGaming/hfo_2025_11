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
        base_output_dir="/tmp/hfo_nats_test",
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
