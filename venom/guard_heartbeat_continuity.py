import asyncio
import os
import sys
import json
from datetime import datetime, timedelta, timezone
import nats
from nats.js.api import ConsumerConfig, DeliverPolicy

# --- Configuration ---
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
SUBJECT = "hfo.heartbeat.>"
MAX_SILENCE_MINUTES = 3  # Warn if silence > 3 minutes (since interval is 1m)


async def check_heartbeat():
    print(
        f"🛡️  [GUARD] Checking HFO Heartbeat Continuity (Max Silence: {MAX_SILENCE_MINUTES}m)..."
    )

    try:
        nc = await nats.connect(NATS_URL, connect_timeout=2)
        js = nc.jetstream()
    except Exception as e:
        print(f"❌ [GUARD] NATS Connection Failed: {e}")
        print("   👉 Is the NATS server running? (docker-compose up -d)")
        return False

    try:
        # Get the last message from the stream
        sub = await js.subscribe(
            SUBJECT, config=ConsumerConfig(deliver_policy=DeliverPolicy.LAST)
        )

        try:
            msg = await sub.next_msg(timeout=3.0)
            data = json.loads(msg.data.decode())
            timestamp_str = data.get("timestamp")
            agent_id = data.get("agent_id", "unknown")

            if not timestamp_str:
                print("❌ [GUARD] Malformed Heartbeat Signal (No timestamp).")
                return False

            # Parse timestamp (ISO format with offset)
            last_beat = datetime.fromisoformat(timestamp_str)

            # Get current time in the same timezone (or UTC for comparison)
            if last_beat.tzinfo is None:
                now = datetime.now()
            else:
                now = datetime.now(timezone.utc)

            # Calculate difference
            diff = now - last_beat

            if diff > timedelta(minutes=MAX_SILENCE_MINUTES):
                print(
                    f"⚠️  [GUARD] HEARTBEAT OFFLINE! Last signal was {diff.total_seconds()/60:.1f} minutes ago."
                )
                print(f"   Last Agent: {agent_id}")
                print(f"   Last Time:  {timestamp_str}")
                print("   👉 Restart the swarm: 'make heartbeat'")
                return False

            print(
                f"✅ [GUARD] Heartbeat Active. Last signal {diff.total_seconds():.1f}s ago from {agent_id}."
            )
            return True

        except nats.errors.TimeoutError:
            print("⚠️  [GUARD] No Heartbeat signals found in stream history.")
            return False

    except Exception as e:
        print(f"❌ [GUARD] Error checking stream: {e}")
        return False
    finally:
        await nc.close()


if __name__ == "__main__":
    try:
        success = asyncio.run(check_heartbeat())
        if not success:
            sys.exit(1)
        sys.exit(0)
    except KeyboardInterrupt:
        sys.exit(1)
