import asyncio
from datetime import timedelta
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker
import pytest


@activity.defn
async def smoke_activity(name: str) -> str:
    return f"Smoke, {name}!"


@workflow.defn
class SmokeWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            smoke_activity, name, start_to_close_timeout=timedelta(seconds=5)
        )


@pytest.mark.asyncio
async def test_temporal_smoke():
    print("\n🧪 SMOKE TEST: Temporal Orchestration Layer")
    try:
        client = await Client.connect("localhost:7235")
        async with Worker(
            client,
            task_queue="smoke-queue",
            workflows=[SmokeWorkflow],
            activities=[smoke_activity],
        ):
            result = await client.execute_workflow(
                SmokeWorkflow.run,
                "Test",
                id="smoke-test-id",
                task_queue="smoke-queue",
            )
            assert result == "Smoke, Test!"
            print("   ✅ Temporal Workflow: OK")
    except Exception as e:
        pytest.fail(f"Temporal failed: {e}")


if __name__ == "__main__":
    asyncio.run(test_temporal_smoke())
