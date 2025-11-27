import asyncio
import logging
import json
import os
import hashlib
from datetime import datetime
import nats

# --- Configuration ---
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
MANTRA = """I am the Node, the Earth, the Seed,
Swarmlord of Webs is the one I heed.
From Karmic Web, where Wisdom flows,
To Swarm Web, where the Willpower grows.
In Simulation Web, I Weave the state,
Obsidian Hourglass, the Engine of Fate.
A Prescient Path in State-Action Space,
One Mind, One Swarm, in time and place."""
EXPECTED_HASH = hashlib.sha256(MANTRA.encode("utf-8")).hexdigest()
REQUIRED_PILLARS = {
    "ontos",
    "chronos",
    "topos",
    "telos",
    "logos",
    "pathos",
    "ethos",
    "techne",
}

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("HiveGuard")


class HeartbeatGuard:
    def __init__(self):
        self.agent_timestamps = {}

    async def validate_signal(self, msg):
        try:
            data = json.loads(msg.data.decode())
            subject = msg.subject
            agent_id = data.get("agent_id", "unknown")

            # 1. Check Mantra Hash
            if data.get("mantra_hash") != EXPECTED_HASH:
                logger.warning(f"⚠️ [Integrity] Invalid Mantra Hash from {agent_id}!")
                return

            # 2. Check Pillars
            pillars = data.get("pillars", {})
            missing_pillars = REQUIRED_PILLARS - pillars.keys()
            if missing_pillars:
                logger.warning(
                    f"⚠️ [Structure] Missing Pillars from {agent_id}: {missing_pillars}"
                )
                return

            # 3. Check Time Regression
            timestamp_str = data.get("timestamp")
            try:
                # Handle ISO format with potential timezone info
                current_ts = datetime.fromisoformat(timestamp_str)
                last_ts = self.agent_timestamps.get(agent_id)

                if last_ts and current_ts < last_ts:
                    logger.error(
                        f"🚨 [Chronos] Time Regression detected for {agent_id}! {current_ts} < {last_ts}"
                    )

                self.agent_timestamps[agent_id] = current_ts
            except Exception as e:
                logger.warning(f"⚠️ [Chronos] Time parse error for {agent_id}: {e}")

            # 4. Log Success (Verbose only if needed, keeping it clean for now)
            # logger.info(f"✅ Validated Heartbeat from {agent_id}")

        except json.JSONDecodeError:
            logger.error(f"❌ [Format] Invalid JSON on {msg.subject}")
        except Exception as e:
            logger.error(f"❌ [Unknown] Validation Error: {e}")


async def main():
    logger.info("🛡️ Hive Guard: Initializing Heartbeat Monitor...")

    try:
        nc = await nats.connect(NATS_URL)
        logger.info(f"✅ Connected to NATS at {NATS_URL}")
    except Exception as e:
        logger.error(f"❌ Failed to connect to NATS: {e}")
        return

    guard = HeartbeatGuard()

    async def message_handler(msg):
        await guard.validate_signal(msg)

    # Subscribe to all heartbeats
    await nc.subscribe("hfo.heartbeat.>", cb=message_handler)
    logger.info("👀 Watching 'hfo.heartbeat.>' for anomalies...")
    logger.info("   (Ctrl+C to stop)")

    # Keep alive
    while True:
        await asyncio.sleep(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
