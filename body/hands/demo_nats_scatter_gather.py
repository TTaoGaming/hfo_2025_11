"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: c54c11ea-1d18-4005-a36c-50f130e8f733
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.369324+00:00'
  topos:
    address: body/hands/demo_nats_scatter_gather.py
    links: []
  telos:
    viral_factor: 0.0
    meme: demo_nats_scatter_gather.py


🦅 Hive Fleet Obsidian: NATS Scatter-Gather Demo
Intent: Demonstrate NATS Scatter-Gather pattern.
Intent: Demonstrates the Async Swarm Pattern using NATS.
Linked to: brain/pattern_async_swarm.feature
"""
import asyncio
import json
import logging
import random
from datetime import datetime
from typing import List
import nats
from nats.js.api import StreamConfig, RetentionPolicy
from dotenv import load_dotenv
from pydantic import UUID4
from body.config import Config

# Import our SSOT models
from body.models.intent import MissionIntent
from body.models.signals import MissionSignal, ResultSignal
from body.models.state import AgentRole


# Setup
load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("NATS-Hydra")

# Configuration
NATS_URL = Config.NATS_URL
STREAM_NAME = "HIVE_MIND"
SUBJECT_MISSION = "hfo.mission.new"
SUBJECT_RESULT = "hfo.mission.result"

# Constants
NATS_CONNECT_TIMEOUT = 5
WORKER_FETCH_TIMEOUT = 5
ASSIMILATOR_TIMEOUT = 2
ASSIMILATOR_MAX_WAIT = 10


async def setup_jetstream(nc):
    """Ensures the JetStream stream exists with 'Evaporating' TTL."""
    js = nc.jetstream()

    try:
        # Create a stream that auto-deletes messages after 1 hour (TTL)
        # This implements the "Evaporating Blackboard"
        await js.add_stream(
            name=STREAM_NAME,
            subjects=["hfo.mission.*"],
            config=StreamConfig(
                retention=RetentionPolicy.LIMITS,
                max_age=3600,  # 1 hour TTL
                storage="file",
            ),
        )
        logger.info(f"✅ JetStream '{STREAM_NAME}' configured with 1h TTL.")
    except Exception as e:
        logger.warning(f"Stream might already exist: {e}")

    return js


async def swarmlord_publisher(js, mission_text: str) -> UUID4:
    """Acts as the Swarmlord: Creates and publishes a mission."""

    # 1. Define Intent (The 'Set' Phase)
    intent = MissionIntent(
        description=mission_text,
        rationale="Testing the NATS Scatter-Gather Protocol",
        swarm_size=3,
    )

    # 2. Wrap in Signal
    signal = MissionSignal(
        producer_id="Swarmlord-01", mission=intent, target_roles=[AgentRole.SHAPER]
    )

    # 3. Publish to NATS
    payload = signal.model_dump_json().encode()
    ack = await js.publish(SUBJECT_MISSION, payload)

    logger.info(f"👑 Swarmlord: Published Mission {intent.id} (Seq: {ack.seq})")
    return intent.id


async def agent_worker(nc, agent_id: str, role: AgentRole):
    """Acts as a Worker Agent: Listens for missions, executes, and replies."""
    js = nc.jetstream()

    # Create a durable consumer so we don't miss messages if we blink
    psub = await js.pull_subscribe(SUBJECT_MISSION, durable=f"worker_{agent_id}")

    logger.info(f"🐜 Agent {agent_id} ({role.value}): Online and listening...")

    try:
        while True:
            try:
                # Fetch 1 message
                msgs = await psub.fetch(1, timeout=WORKER_FETCH_TIMEOUT)
                for msg in msgs:
                    data = json.loads(msg.data.decode())
                    signal = MissionSignal(**data)

                    logger.info(
                        f"   ⚡ {agent_id}: Received Mission: '{signal.mission.description}'"
                    )

                    # --- SIMULATED WORK (The 'Act' Phase) ---
                    # In a real scenario, this would call the LLM via Instructor
                    await asyncio.sleep(random.uniform(0.5, 2.0))  # Thinking time

                    answer = f"Analysis from {agent_id}: {signal.mission.description[::-1]} (Reversed)"
                    confidence = random.uniform(0.7, 0.99)
                    # ----------------------------------------

                    # Reply with Result
                    result = ResultSignal(
                        producer_id=agent_id,
                        mission_id=signal.mission.id,
                        content=answer,
                        confidence=confidence,
                    )

                    await js.publish(SUBJECT_RESULT, result.model_dump_json().encode())
                    logger.info(f"   📤 {agent_id}: Published Result.")

                    await msg.ack()

            except nats.errors.TimeoutError:
                # No new missions, just wait
                continue
            except Exception as e:
                logger.error(f"❌ {agent_id} Error: {e}")
                await asyncio.sleep(1)  # Backoff
    except asyncio.CancelledError:
        logger.info(f"🛑 Agent {agent_id} shutting down.")


async def assimilator_collector(js, target_mission_id: UUID4, expected_count: int):
    """Acts as the Assimilator: Gathers results and forms consensus."""
    logger.info(
        f"🧠 Assimilator: Waiting for {expected_count} results for Mission {target_mission_id}..."
    )

    sub = await js.subscribe(SUBJECT_RESULT)
    results: List[ResultSignal] = []

    start_time = datetime.now()

    while len(results) < expected_count:
        try:
            msg = await sub.next_msg(timeout=ASSIMILATOR_TIMEOUT)
            data = json.loads(msg.data.decode())
            signal = ResultSignal(**data)

            if signal.mission_id == target_mission_id:
                results.append(signal)
                logger.info(
                    f"   📥 Assimilator: Collected result from {signal.producer_id}"
                )
        except nats.errors.TimeoutError:
            pass

        # Timeout safety
        if (datetime.now() - start_time).seconds > ASSIMILATOR_MAX_WAIT:
            logger.warning("⚠️  Assimilator: Timeout waiting for results.")
            break

    logger.info(
        f"✅ Assimilator: Collection Complete. {len(results)}/{expected_count} received."
    )

    # Simple Consensus (Concatenation for now)
    print("\n--- 🏁 FINAL REPORT ---")
    for r in results:
        print(f"Agent {r.producer_id} ({r.confidence:.2f}): {r.content}")
    print("-----------------------\n")


async def main():
    # Connect to NATS
    nc = None
    workers = []
    try:
        try:
            nc = await nats.connect(NATS_URL, connect_timeout=NATS_CONNECT_TIMEOUT)
        except Exception:
            logger.error(
                f"Could not connect to NATS at {NATS_URL}. Is it running? (Check docker-compose)"
            )
            return

        js = await setup_jetstream(nc)

        # 1. Start the Assimilator (Listener)
        # We need to know the mission ID ahead of time or have it listen generically.
        # For this demo, we'll start the workers first.

        # 2. Start Workers in background
        workers = [
            asyncio.create_task(agent_worker(nc, "Alpha", AgentRole.SHAPER)),
            asyncio.create_task(agent_worker(nc, "Beta", AgentRole.SHAPER)),
            asyncio.create_task(agent_worker(nc, "Gamma", AgentRole.DISRUPTOR)),
        ]

        # 3. Swarmlord publishes mission
        await asyncio.sleep(1)  # Let workers settle
        mission_id = await swarmlord_publisher(js, "What is the meaning of life?")

        # 4. Assimilator collects
        await assimilator_collector(js, mission_id, expected_count=3)

    except KeyboardInterrupt:
        logger.info("👋 User interrupted.")
    except Exception as e:
        logger.error(f"💥 Fatal Error: {e}")
    finally:
        # Cleanup
        logger.info("🧹 Cleaning up...")
        for w in workers:
            w.cancel()

        if workers:
            await asyncio.gather(*workers, return_exceptions=True)

        if nc:
            await nc.close()
        logger.info("👋 Done.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
