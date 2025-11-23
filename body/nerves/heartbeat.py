"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 321b1e8e-7c32-4047-8001-72ea4d8b70ab
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.360226+00:00'
    generation: 51
  topos:
    address: body/nerves/heartbeat.py
    links: []
  telos:
    viral_factor: 0.0
    meme: heartbeat.py
"""

import asyncio
import os
import time
from datetime import datetime, timezone
import nats
from nats.errors import ConnectionClosedError, NoServersError

# Configuration
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
HEARTBEAT_INTERVAL = 10  # Seconds
WATCHDOG_TIMEOUT = 60  # Seconds (Alert if no activity for this long)
LOG_FILE = "swarm_heartbeat.log"


async def run_heartbeat():
    print("💓 Starting Swarm Heartbeat Monitor...")
    print(f"🔌 Connecting to NATS: {NATS_URL}")

    try:
        nc = await nats.connect(NATS_URL)
    except NoServersError:
        print("❌ Critical: Could not connect to NATS server!")
        return

    # State
    last_activity = time.time()

    async def activity_handler(msg):
        nonlocal last_activity
        last_activity = time.time()
        # Optional: Print dot for activity
        # print(".", end="", flush=True)

    # Subscribe to all swarm events to monitor activity
    await nc.subscribe("swarm.>", cb=activity_handler)

    # Publisher Loop
    while True:
        current_time = time.time()

        # 1. Publish Heartbeat
        payload = f"{datetime.now(timezone.utc).isoformat()}".encode()
        try:
            await nc.publish("swarm.heartbeat", payload)
            # print("💓", end="", flush=True)
        except ConnectionClosedError:
            print("\n❌ Connection Lost!")
            break

        # 2. Watchdog Check
        silence_duration = current_time - last_activity
        if silence_duration > WATCHDOG_TIMEOUT:
            alert_msg = (
                f"\n🚨 WATCHDOG ALERT: No Swarm Activity for {int(silence_duration)}s!"
            )
            print(alert_msg)
            with open(LOG_FILE, "a") as f:
                f.write(f"{datetime.now(timezone.utc).isoformat()} - {alert_msg}\n")

        await asyncio.sleep(HEARTBEAT_INTERVAL)


if __name__ == "__main__":
    try:
        asyncio.run(run_heartbeat())
    except KeyboardInterrupt:
        print("\n🛑 Heartbeat Stopped.")
