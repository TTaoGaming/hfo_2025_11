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
