import asyncio
import ray
from temporalio.client import Client
from src.temporal.math_workflow import MathSwarmWorkflow, run_worker
from dotenv import load_dotenv

# Load env vars (API keys)
load_dotenv()

async def main():
    # 1. Start Ray
    if not ray.is_initialized():
        ray.init()
        
    # 2. Start Temporal Worker in the background (for this test script)
    # In production, workers run separately.
    worker_task = asyncio.create_task(run_worker())
    
    # Give worker a moment to connect
    await asyncio.sleep(2)
    
    # 3. Submit Workflow
    client = await Client.connect("localhost:7235")
    
    # Start the workflow
    import uuid
    workflow_id = f"math-swarm-test-{uuid.uuid4()}"
    print(f"--- Submitting Workflow to Temporal (ID: {workflow_id}) ---")
    
    user_request = "Solve these math problems for me."
    handle = await client.start_workflow(
        MathSwarmWorkflow.run,
        user_request,
        id=workflow_id,
        task_queue="math-swarm-queue",
    )
    
    print(f"Workflow ID: {handle.id}")
    print("Waiting for result (this triggers Ray actors)...")
    
    # 4. Get Result
    result = await handle.result()
    
    print("\n================ FINAL DIGEST ================")
    print(result)
    print("==============================================")
    
    # Cleanup
    worker_task.cancel()
    try:
        await worker_task
    except asyncio.CancelledError:
        pass
    ray.shutdown()

if __name__ == "__main__":
    asyncio.run(main())
