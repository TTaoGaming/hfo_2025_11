import asyncio
import sys
import os

# Add the parent directory to sys.path to import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from nerves.bus.nats_client import HFOStigmergyBus  # noqa: E402
from memory.lancedb_store import HFOStigmergyMemory  # noqa: E402


async def main():
    print("--- Setting up HFO Stigmergy System ---")

    # 1. Setup NATS
    print("\n[1/2] Setting up NATS JetStream...")
    bus = HFOStigmergyBus()
    try:
        await bus.connect()
        await bus.setup_streams()
        print("NATS setup complete.")
    except Exception as e:
        print(f"NATS setup failed: {e}")
    finally:
        await bus.close()

    # 2. Setup LanceDB
    print("\n[2/2] Setting up LanceDB...")
    try:
        # Assuming running from buds/hfo_gem_gen_55
        HFOStigmergyMemory(db_path="memory/lancedb")
        print("LanceDB setup complete.")
    except Exception as e:
        print(f"LanceDB setup failed: {e}")

    print("\n--- Setup Finished ---")


if __name__ == "__main__":
    asyncio.run(main())
