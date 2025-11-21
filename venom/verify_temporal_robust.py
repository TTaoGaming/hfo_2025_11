import asyncio
import uuid
import time
from datetime import timedelta
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker

# --- Definitions ---
@activity.defn
async def robust_hello(name: str) -> str:
    print(f"   [Activity] Executing robust_hello for {name}")
    return f"Hello, {name}!"

@workflow.defn
class RobustWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        print(f"   [Workflow] Started for {name}")
        return await workflow.execute_activity(
            robust_hello, name, start_to_close_timeout=timedelta(seconds=10)
        )

# --- Test Script ---
async def test_temporal_robust():
    run_id = str(uuid.uuid4())[:8]
    wf_id = f"robust-test-{run_id}"
    queue = f"queue-{run_id}"
    
    print(f"🧪 TESTING: Temporal Robust (ID: {wf_id})")
    
    try:
        # 1. Connect
        print("   [1/4] Connecting to Temporal...")
        client = await Client.connect("localhost:7235")
        print("   ✅ Connected.")

        # 2. Start Worker in Background Task
        print(f"   [2/4] Starting Worker on queue '{queue}'...")
        worker = Worker(
            client,
            task_queue=queue,
            workflows=[RobustWorkflow],
            activities=[robust_hello],
        )
        
        # Run worker in a separate task so we can submit workflow
        worker_task = asyncio.create_task(worker.run())
        print("   ✅ Worker task scheduled.")

        # 3. Submit Workflow
        print("   [3/4] Submitting Workflow...")
        handle = await client.start_workflow(
            RobustWorkflow.run,
            "Phoenix",
            id=wf_id,
            task_queue=queue,
            execution_timeout=timedelta(seconds=30)
        )
        print(f"   ✅ Workflow submitted. Run ID: {handle.result_run_id}")

        # 4. Wait for Result
        print("   [4/4] Waiting for result (timeout 10s)...")
        try:
            result = await asyncio.wait_for(handle.result(), timeout=10.0)
            print(f"✅ SUCCESS: Workflow result: '{result}'")
        except asyncio.TimeoutError:
            print("❌ TIMEOUT: Workflow did not complete in 10s.")
            print("   Checking workflow history...")
            async for event in handle.fetch_history_events():
                print(f"   - {event.event_type}")
        
        # Cleanup
        worker_task.cancel()
        try:
            await worker_task
        except asyncio.CancelledError:
            pass

    except Exception as e:
        print(f"❌ FAILED: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_temporal_robust())
