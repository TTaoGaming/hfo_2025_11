import asyncio
import nats
import json
import os

NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")


async def main():
    print(f"🎧 Connecting to NATS at {NATS_URL} to verify Chant Content...")
    nc = await nats.connect(NATS_URL)

    print("👀 Listening for 'Yield' artifacts (The Chant)...")
    print("-" * 60)

    async def cb(msg):
        try:
            data = json.loads(msg.data.decode())
            phase = data.get("phase")
            agent_id = data.get("agent_id")
            content = data.get("content")

            if phase == "Yield":
                print(f"📦 [{agent_id}] YIELDED ARTIFACT:")
                print(f"   {content}")
                print("-" * 60)
        except Exception as e:
            print(f"Error parsing message: {e}")

    # Subscribe to all heartbeats
    await nc.subscribe("hfo.heartbeat.>", cb=cb)

    # Keep running for a bit to capture some chants
    await asyncio.sleep(30)
    await nc.close()


if __name__ == "__main__":
    asyncio.run(main())
