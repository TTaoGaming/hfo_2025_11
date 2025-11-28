"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 550e8400-e29b-41d4-a716-446655440021
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-26T12:00:00.000000Z'
    generation: 51
  topos:
    address: body/hands/heartbeat_summary.py
    links: []
  telos:
    viral_factor: 0.0
    meme: heartbeat_summary.py
"""

import asyncio
import argparse
import json
import logging
from datetime import datetime, timedelta, timezone
import nats
from nats.js.api import ConsumerConfig, DeliverPolicy

# --- Configuration ---
NATS_URL = "nats://localhost:4225"
STREAM_NAME = "HIVE_MIND"
SUBJECT = "hfo.heartbeat.>"

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("HeartbeatSummary")


async def main():
    parser = argparse.ArgumentParser(description="Summarize HFO Heartbeat Activity")
    parser.add_argument(
        "--minutes", type=int, default=5, help="Minutes of history to analyze"
    )
    args = parser.parse_args()

    try:
        nc = await nats.connect(NATS_URL)
        js = nc.jetstream()
    except Exception as e:
        logger.error(f"Failed to connect to NATS: {e}")
        return

    # Calculate Start Time
    start_time = datetime.now(timezone.utc) - timedelta(minutes=args.minutes)
    logger.info(
        f"🔍 Analyzing Heartbeat Stream since {start_time.isoformat()} (Last {args.minutes}m)..."
    )

    # Create Ephemeral Consumer
    # We use an ordered consumer to get messages efficiently
    sub = await js.subscribe(
        SUBJECT,
        ordered_consumer=True,
        config=ConsumerConfig(
            deliver_policy=DeliverPolicy.BY_START_TIME,
            opt_start_time=start_time.isoformat(),
        ),
    )

    messages = []
    agents_seen = set()
    phases_counts = {}
    contents = set()
    quorum_statuses = []

    try:
        # Fetch messages until we catch up or timeout
        # Since we don't know exactly how many, we'll fetch for a short duration or until no new msgs
        # start_fetch = datetime.now() <-- Removed unused variable
        while True:
            try:
                msg = await sub.next_msg(timeout=1.0)
                data = json.loads(msg.data.decode())
                messages.append(data)

                # Aggregation
                agents_seen.add(data.get("agent_id"))

                phase = data.get("phase")
                phases_counts[phase] = phases_counts.get(phase, 0) + 1

                content = data.get("content")
                if content:
                    # Truncate long content for summary
                    short_content = (
                        content[:50] + "..." if len(content) > 50 else content
                    )
                    contents.add(short_content)

                q_status = data.get("quorum_status")
                if q_status:
                    quorum_statuses.append(q_status)

            except nats.errors.TimeoutError:
                # No more messages for now
                break

            # Safety break if too many messages (e.g. > 10000) to prevent hanging
            if len(messages) > 5000:
                logger.warning("⚠️ Limit reached (5000 msgs). Stopping fetch.")
                break

    except Exception as e:
        logger.error(f"Error during fetch: {e}")
    finally:
        await nc.close()

    # --- Report Generation ---
    print("\n" + "=" * 40)
    print(f"🦅 HFO HEARTBEAT SUMMARY (Last {args.minutes}m)")
    print("=" * 40)

    if not messages:
        print("❌ No heartbeat signals found in this window.")
        return

    print(f"📊 Total Signals: {len(messages)}")
    print(f"🤖 Active Agents: {len(agents_seen)} {sorted(list(agents_seen))}")

    print("\n🔄 PREY Loop Distribution:")
    for phase, count in phases_counts.items():
        print(f"  - {phase}: {count}")

    print("\n🗣️  Chant Samples (Unique Content):")
    for c in list(contents)[:5]:  # Show top 5 unique contents
        print(f"  - {c}")

    # Quorum Analysis
    reached_count = quorum_statuses.count("QUORUM_REACHED")
    # seeking_count = quorum_statuses.count("SEEKING_PEERS") <-- Removed unused variable
    total_q = len(quorum_statuses)
    if total_q > 0:
        consensus_rate = (reached_count / total_q) * 100
        print(
            f"\n🤝 Quorum Consensus Rate: {consensus_rate:.1f}% ({reached_count}/{total_q})"
        )
    else:
        print("\n🤝 Quorum Consensus: N/A")

    print("=" * 40 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
