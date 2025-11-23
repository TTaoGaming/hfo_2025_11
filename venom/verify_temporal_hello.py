"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: a1dafb17-740d-4c46-951b-5d1fdb955c20
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.259695+00:00'
  topos:
    address: venom/verify_temporal_hello.py
    links: []
  telos:
    viral_factor: 0.0
    meme: verify_temporal_hello.py
"""

import asyncio
from datetime import timedelta
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker


# --- 1. Define a Basic Activity ---
@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"


# --- 2. Define a Basic Workflow ---
@workflow.defn
class HelloWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, start_to_close_timeout=timedelta(seconds=5)
        )


# --- 3. Run the Test ---
async def main():
    print("🧪 TESTING: Temporal Hello World (Minimal)...")

    # Connect to the Temporal Server running in Docker
    client = await Client.connect("localhost:7235")
    print("   ✅ Connected to Temporal Server")

    # Create a Worker to process the workflow
    async with Worker(
        client,
        task_queue="hello-world-queue",
        workflows=[HelloWorkflow],
        activities=[say_hello],
    ):
        print("   ✅ Worker started")

        # Execute the workflow
        print("   🚀 Executing workflow...")
        result = await client.execute_workflow(
            HelloWorkflow.run,
            "World",
            id="hello-world-id",
            task_queue="hello-world-queue",
        )

        print(f"   ✅ RESULT: {result}")


if __name__ == "__main__":
    asyncio.run(main())
