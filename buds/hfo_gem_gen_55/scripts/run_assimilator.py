import asyncio
import json
import sys
import os
import signal

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from nerves.bus.nats_client import HFOStigmergyBus  # noqa: E402
from memory.lancedb_store import HFOStigmergyMemory  # noqa: E402


async def run_assimilator():
    print("--- Starting HFO Assimilator (Cold Stigmergy) ---")

    bus = HFOStigmergyBus()
    # Assuming running from buds/hfo_gem_gen_55
    mem = HFOStigmergyMemory(db_path="memory/lancedb")

    await bus.connect()

    async def message_handler(msg):
        subject = msg.subject
        data = msg.data.decode()
        print(f"Received on {subject}: {data}")

        try:
            payload = json.loads(data)
            # Extract section from subject (hfo.ontos -> ontos)
            section = subject.split(".")[1]

            mem.store(section, payload)
            await msg.ack()
        except Exception as e:
            print(f"Error processing message: {e}")

    # Subscribe to all HFO stigmergy events
    await bus.subscribe("hfo.>", message_handler)

    print("Listening for Stigmergy signals...")

    # Keep running until interrupted
    stop_event = asyncio.Event()

    def signal_handler():
        stop_event.set()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, signal_handler)

    await stop_event.wait()

    print("Shutting down...")
    await bus.close()


if __name__ == "__main__":
    asyncio.run(run_assimilator())
