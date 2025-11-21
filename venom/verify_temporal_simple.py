import asyncio
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker


@activity.defn
async def say_hello(name: str) -> str:
    return f"Hello, {name}!"


@workflow.defn
class HelloWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return await workflow.execute_activity(
            say_hello, name, start_to_close_timeout_seconds=5
        )


async def test_temporal():
    print("🧪 TESTING: Temporal Workflow...")
    try:
        client = await Client.connect("localhost:7235")
        print("   Connected to Temporal Server.")

        async with Worker(
            client,
            task_queue="smoke-test-queue",
            workflows=[HelloWorkflow],
            activities=[say_hello],
        ):
            print("   Worker started. Submitting workflow...")
            result = await client.execute_workflow(
                HelloWorkflow.run,
                "Phoenix",
                id="smoke-test-workflow-id",
                task_queue="smoke-test-queue",
            )
            print(f"✅ SUCCESS: Workflow result: '{result}'")

    except Exception as e:
        print(f"❌ FAILED: {str(e)}")


if __name__ == "__main__":
    asyncio.run(test_temporal())
