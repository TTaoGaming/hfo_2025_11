import asyncio
import nats
import os


async def main():
    try:
        nc = await nats.connect("nats://localhost:4225")
        print("Connected to NATS")

        async def cb(msg):
            print(f"Received: {msg.data.decode()}")
            # Exit after one message
            os._exit(0)

        await nc.subscribe("hfo.heartbeat.>", cb=cb)
        print("Subscribed. Waiting for message...")
        await asyncio.sleep(5)
        await nc.close()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
