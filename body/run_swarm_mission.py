"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: ded21914-7211-46f1-9c32-f1bc76c1548f
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.339920+00:00'
    generation: 51
  topos:
    address: body/run_swarm_mission.py
    links: []
  telos:
    viral_factor: 0.0
    meme: run_swarm_mission.py
"""

import asyncio
import uuid
from temporalio.client import Client
from body.temporal.swarm_workflow import ResearchSwarmWorkflow, run_worker
from body.config import Config
from dotenv import load_dotenv

# Load env vars
load_dotenv()


async def main():
    # 1. Start Temporal Worker in the background
    worker_task = asyncio.create_task(run_worker())

    # Give worker a moment to connect
    await asyncio.sleep(2)

    # 2. Submit Workflow
    client = await Client.connect(Config.TEMPORAL_ADDRESS)

    workflow_id = f"research-swarm-{uuid.uuid4()}"
    print(f"--- Submitting Workflow to Temporal (ID: {workflow_id}) ---")

    mission = "Research the future of AI Agents in 2025"

    handle = await client.start_workflow(
        ResearchSwarmWorkflow.run,
        mission,
        id=workflow_id,
        task_queue="research-swarm-queue",
    )

    print(f"Workflow ID: {handle.id}")
    print("Waiting for result (Timeout: 600s)...")

    # 3. Get Result with Monitoring
    async def monitor_progress():
        seconds = 0
        while True:
            print(f"[{seconds}s] Swarm is thinking...", end="\r", flush=True)
            await asyncio.sleep(5)
            seconds += 5

    monitor_task = asyncio.create_task(monitor_progress())

    try:
        result = await handle.result()
    finally:
        monitor_task.cancel()
        print("\n")  # Newline after progress monitoring

    print("\n================ FINAL DIGEST ================")
    print(result)
    print("==============================================")

    # Cancel worker
    worker_task.cancel()
    try:
        await worker_task
    except asyncio.CancelledError:
        pass


if __name__ == "__main__":
    asyncio.run(main())
