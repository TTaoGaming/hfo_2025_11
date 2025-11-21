import ray
import time
import pytest

@ray.remote
class SmokeActor:
    def ping(self):
        return "pong"

def test_ray_smoke():
    print("\n🧪 SMOKE TEST: Ray Compute Layer")

    if ray.is_initialized():
        ray.shutdown()

    try:
        ray.init(ignore_reinit_error=True, logging_level="ERROR")
        actor = SmokeActor.remote()
        result = ray.get(actor.ping.remote())
        assert result == "pong"
        print("   ✅ Ray Actor: OK")
    except Exception as e:
        pytest.fail(f"Ray failed: {e}")
    finally:
        ray.shutdown()

if __name__ == "__main__":
    test_ray_smoke()
