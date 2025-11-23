"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 3f564d77-f063-4f23-8b3c-d9834ff2d02e
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.258878+00:00'
  topos:
    address: venom/verify_ray_local.py
    links: []
  telos:
    viral_factor: 0.0
    meme: verify_ray_local.py
"""

import ray
import time


@ray.remote
class TestActor:
    def ping(self):
        return "pong"


def test_ray_local():
    print("🧪 TESTING: Ray Local Cluster...")

    try:
        if ray.is_initialized():
            ray.shutdown()

        print("   Initializing Ray...")
        ray.init(ignore_reinit_error=True)

        print("   Creating Actor...")
        actor = TestActor.remote()

        print("   Calling Actor...")
        start_time = time.time()
        result = ray.get(actor.ping.remote())
        duration = time.time() - start_time

        print(f"✅ SUCCESS: Ray Actor returned '{result}' in {duration:.4f}s")
        ray.shutdown()

    except Exception as e:
        print(f"❌ FAILED: {str(e)}")


if __name__ == "__main__":
    test_ray_local()
