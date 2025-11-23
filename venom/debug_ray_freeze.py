"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 8537435c-ec08-4038-bb4b-90f7047576be
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.277849+00:00'
  topos:
    address: venom/debug_ray_freeze.py
    links: []
  telos:
    viral_factor: 0.0
    meme: debug_ray_freeze.py
"""

import ray
import time
import sys
import logging

# Configure logging to print to stdout immediately
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("ray_debug")


def debug_ray():
    logger.info("1. Starting Ray Debug Protocol...")

    if ray.is_initialized():
        logger.info("   Ray was already initialized. Shutting down...")
        ray.shutdown()

    logger.info("2. Initializing Ray (minimal config)...")
    try:
        # Minimal config, no dashboard, log to driver
        ray.init(
            ignore_reinit_error=True,
            include_dashboard=False,
            log_to_driver=True,
            num_cpus=1,  # Restrict to 1 CPU to minimize resource contention
        )
        logger.info("   ✅ Ray Initialized.")
        logger.info(f"   Ray Version: {ray.__version__}")
        logger.info(f"   Cluster Resources: {ray.cluster_resources()}")
    except Exception as e:
        logger.error(f"   ❌ Ray Init Failed: {e}")
        return

    logger.info("3. Defining Remote Actor...")

    @ray.remote
    class EchoActor:
        def __init__(self):
            print("   [Actor] Initialized.")

        def echo(self, msg):
            print(f"   [Actor] Received: {msg}")
            return f"Echo: {msg}"

    logger.info("4. Instantiating Actor...")
    try:
        start = time.time()
        actor = EchoActor.remote()
        logger.info(f"   Actor created in {time.time() - start:.4f}s")
    except Exception as e:
        logger.error(f"   ❌ Actor Instantiation Failed: {e}")
        ray.shutdown()
        return

    logger.info("5. Calling Actor (Timeout 5s)...")
    try:
        start = time.time()
        # Use a timeout to prevent infinite freeze
        ref = actor.echo.remote("Hello Ray")
        result = ray.get(ref, timeout=5.0)
        logger.info(f"   ✅ Actor returned: '{result}' in {time.time() - start:.4f}s")
    except Exception as e:
        logger.error(f"   ❌ Actor Call Failed/Timed Out: {e}")

    logger.info("6. Shutting down Ray...")
    ray.shutdown()
    logger.info("✅ Debug Protocol Complete.")


if __name__ == "__main__":
    debug_ray()
