"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 2044466e-8f12-43d7-89b1-dbb8ab146a14
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:20:43.120797+00:00'
    generation: 51
  topos:
    address: verify_nats_connection.py
    links: []
  telos:
    viral_factor: 0.0
    meme: verify_nats_connection.py
"""

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
