import asyncio
import nats
import os
from dotenv import load_dotenv

load_dotenv()


async def main():
    nats_url = os.getenv("NATS_URL", "nats://localhost:4225")
    print(f"Attempting to connect to NATS at: {nats_url}")

    try:
        nc = await nats.connect(nats_url)
        print("✅ Connection Successful!")
        nc.jetstream()
        print("✅ JetStream Context Retrieved")
        await nc.close()
    except Exception as e:
        print(f"❌ Connection Failed: {e}")


if __name__ == "__main__":
    asyncio.run(main())
