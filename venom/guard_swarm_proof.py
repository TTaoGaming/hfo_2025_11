import asyncio
import os
import json
from datetime import datetime, timedelta, timezone
import nats
from nats.js.api import ConsumerConfig, DeliverPolicy

# --- Configuration ---
NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
STREAM_NAME = "HIVE_MIND"
SUBJECT = "hfo.heartbeat.>"
REQUIRED_AGENTS = 8
REQUIRED_UPTIME_PERCENT = 80.0
WINDOW_HOURS = 24


async def verify_swarm_proof():
    """
    Verifies HFO Level 1 Status via NATS JetStream Proof-of-Work.
    1. Connects to NATS.
    2. Consumes the entire 24h history of 'hfo.heartbeat.>'.
    3. Buckets heartbeats by Agent ID.
    4. Calculates coverage (uptime) for the swarm.
    """
    try:
        nc = await nats.connect(NATS_URL, connect_timeout=2)
        js = nc.jetstream()
    except Exception:
        # If NATS is down, uptime is 0
        print("0.00")
        return

    try:
        # Create an ephemeral consumer to read ALL messages in the stream
        # We use an ordered consumer to get them sequentially
        sub = await js.subscribe(
            SUBJECT,
            ordered_consumer=True,
            config=ConsumerConfig(
                deliver_policy=DeliverPolicy.ALL,  # Read from beginning
                ack_policy="none",  # Faster, no acks needed for analysis
            ),
        )
    except Exception:
        print("0.00")
        await nc.close()
        return

    # Analysis Buckets
    agent_timestamps = {f"cleanroom_agent_{i+1}": [] for i in range(REQUIRED_AGENTS)}
    now = datetime.now(timezone.utc)
    window_start = now - timedelta(hours=WINDOW_HOURS)

    msg_count = 0

    try:
        while True:
            try:
                # Fetch batch of messages
                msg = await sub.next_msg(timeout=1.0)
                msg_count += 1

                try:
                    data = json.loads(msg.data.decode())

                    # Extract Timestamp
                    ts_str = data.get("timestamp")
                    if not ts_str:
                        continue

                    # Parse ISO (handling offset)
                    ts = datetime.fromisoformat(ts_str)

                    # Normalize to UTC for comparison
                    if ts.tzinfo is None:
                        ts = ts.replace(tzinfo=timezone.utc)
                    else:
                        ts = ts.astimezone(timezone.utc)

                    # Filter by Window
                    if ts < window_start:
                        continue

                    # Extract Agent ID
                    # The subject is hfo.heartbeat.<agent_id>.<phase>
                    # But the payload might have it in 'pillars.ontos.id' or we infer from subject
                    subject_parts = msg.subject.split(".")
                    if len(subject_parts) >= 3:
                        agent_id = subject_parts[2]
                        if agent_id in agent_timestamps:
                            agent_timestamps[agent_id].append(ts)

                except Exception:
                    continue

            except nats.errors.TimeoutError:
                # No more messages
                break
    except Exception:
        pass
    finally:
        await nc.close()

    # Calculate Uptime per Agent
    total_uptime_seconds = 0
    max_possible_seconds = WINDOW_HOURS * 3600

    for agent_id, timestamps in agent_timestamps.items():
        if not timestamps:
            continue

        timestamps.sort()
        agent_uptime = 0

        # Sum gaps < 2 mins
        for i in range(1, len(timestamps)):
            gap = (timestamps[i] - timestamps[i - 1]).total_seconds()
            if gap <= 120:  # 2 min tolerance
                agent_uptime += gap

        # Add last segment if recent
        if timestamps:
            last_gap = (now - timestamps[-1]).total_seconds()
            if last_gap <= 120:
                agent_uptime += last_gap

        # Cap at max window
        if agent_uptime > max_possible_seconds:
            agent_uptime = max_possible_seconds

        total_uptime_seconds += agent_uptime

    # Average Swarm Uptime
    # If we have 8 agents, total possible is 8 * 24h
    # But we want the "Swarm Uptime" to be the average of the agents?
    # Or the intersection?
    # Let's use Average Uptime across the Octarchy.

    avg_uptime_seconds = total_uptime_seconds / REQUIRED_AGENTS
    percent = (avg_uptime_seconds / max_possible_seconds) * 100

    if percent > 100.0:
        percent = 100.0

    print(f"{percent:.2f}")


if __name__ == "__main__":
    asyncio.run(verify_swarm_proof())
