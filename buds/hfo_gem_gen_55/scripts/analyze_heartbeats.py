import asyncio
import os
import json
from datetime import datetime, timedelta, timezone
import nats

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


async def analyze_heartbeats():
    # Connect to NATS
    nc = await nats.connect("nats://localhost:4225")
    js = nc.jetstream()

    print("💓 Analyzing Heartbeat Stream (Last 24 Hours)...")

    # We need to find the stream that stores heartbeats.
    # Based on cleanroom_prey_1111.py, subject is hfo.heartbeat.*
    # We assume a stream exists for 'hfo.>'. Let's check streams.

    try:
        streams = await js.streams_info()
        target_stream = None
        for s in streams:
            if (
                "hfo" in s.config.subjects
                or "hfo.>" in s.config.subjects
                or "hfo.heartbeat.>" in s.config.subjects
            ):
                target_stream = s.config.name
                break

        if not target_stream:
            # Fallback: try 'swarm' or 'hfo_stigmergy'
            for s in streams:
                if s.config.name in ["swarm", "hfo_stigmergy", "hfo"]:
                    target_stream = s.config.name
                    break

        if not target_stream:
            print("❌ Could not find a relevant NATS Stream for heartbeats.")
            await nc.close()
            return

        print(f"   Target Stream: {target_stream}")

        # Create a consumer to read all messages
        # We'll use an ephemeral consumer to read from the stream
        # Since we want last 24h, we can try to filter by time if supported,
        # or just read last N messages and filter in python.

        # Let's get the last 10,000 messages (should cover a day if 1/min * 8 agents * 60 * 24 = ~11k)
        # If it was 5s interval, it would be much more.

        # We will iterate backwards or just fetch a batch.
        # Ordered consumer is easiest.

        sub = await js.subscribe("hfo.heartbeat.>", ordered_consumer=True)

        heartbeats = []
        start_time = datetime.now(timezone.utc) - timedelta(hours=24)

        print("   Fetching messages...")

        try:
            while True:
                try:
                    msg = await sub.next_msg(timeout=1.0)
                    data = json.loads(msg.data.decode())

                    # Check timestamp
                    # Assuming data['timestamp'] is ISO format
                    ts_str = data.get("timestamp")
                    if ts_str:
                        # Handle potential timezone issues
                        ts = datetime.fromisoformat(ts_str)
                        if ts.tzinfo is None:
                            ts = ts.replace(tzinfo=timezone.utc)

                        if ts > start_time:
                            heartbeats.append(
                                {
                                    "agent": data["pillars"]["ontos"]["id"],
                                    "timestamp": ts,
                                    "phase": data.get("phase"),
                                    "delta": data.get("delta_seconds", 0.0),
                                }
                            )
                except nats.errors.TimeoutError:
                    # No more messages currently available
                    break
                except Exception:
                    # print(f"Skipping malformed msg: {e}")
                    pass

        except Exception as e:
            print(f"   Stream read ended: {e}")

        print(f"   Total Heartbeats Found (Last 24h): {len(heartbeats)}")

        if not heartbeats:
            print("   No heartbeats found in the window.")
            await nc.close()
            return

        # Sort by time
        heartbeats.sort(key=lambda x: x["timestamp"])

        # Analyze Intervals
        # Group by Agent
        agents = {}
        for hb in heartbeats:
            aid = hb["agent"]
            if aid not in agents:
                agents[aid] = []
            agents[aid].append(hb)

        print("\n📊 Analysis by Agent:")
        for aid, hbs in agents.items():
            if len(hbs) < 2:
                continue

            intervals = []
            for i in range(1, len(hbs)):
                delta = (hbs[i]["timestamp"] - hbs[i - 1]["timestamp"]).total_seconds()
                intervals.append(delta)

            avg_int = sum(intervals) / len(intervals)
            min_int = min(intervals)
            max_int = max(intervals)

            # Detect "Fast Mode" (approx 5s) vs "Steady Mode" (approx 60s)
            fast_count = sum(1 for x in intervals if 4 <= x <= 10)
            steady_count = sum(1 for x in intervals if 50 <= x <= 70)
            gaps = sum(1 for x in intervals if x > 120)

            print(f"   👾 {aid}: {len(hbs)} beats")
            print(f"      Avg Interval: {avg_int:.2f}s")
            print(f"      Fast Beats (~5s): {fast_count}")
            print(f"      Steady Beats (~60s): {steady_count}")
            print(f"      Lapses (>2m): {gaps}")

            if gaps > 0:
                print("      ⚠️ Lapses detected (System Restarts/Sleep):")
                for i, val in enumerate(intervals):
                    if val > 120:
                        t = hbs[i]["timestamp"].strftime("%H:%M:%S")
                        print(f"         - At {t}: Gap of {val:.1f}s")

    except Exception as e:
        print(f"❌ Error: {e}")

    await nc.close()


if __name__ == "__main__":
    asyncio.run(analyze_heartbeats())
