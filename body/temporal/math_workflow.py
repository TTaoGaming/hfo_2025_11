from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker


# --- Activities ---
@activity.defn
async def run_math_swarm_activity(user_request: str) -> str:
    """
    Executes the LangGraph Swarm.
    """
    print(f"Activity started for: {user_request}")

    # Import here to avoid Temporal Sandbox issues with Ray/Filelock
    import ray
    from body.nerves.math_swarm import build_swarm_graph, SwarmState

    # Initialize Ray if needed (it might be running globally, but safe to check)
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True)

    app = build_swarm_graph()

    initial_state = SwarmState(
        user_request=user_request,
        problems=[],
        results=[],
        quorum_report="",
        final_digest="",
    )

    # Run the graph
    final_state = await app.ainvoke(initial_state)

    return final_state["final_digest"]


# --- Workflow ---
@workflow.defn
class MathSwarmWorkflow:
    @workflow.run
    async def run(self, user_request: str) -> str:
        return await workflow.execute_activity(
            run_math_swarm_activity,
            user_request,
            start_to_close_timeout_seconds=300,  # 5 minutes timeout
        )


# --- Worker Helper ---
async def run_worker():
    client = await Client.connect("localhost:7235")
    worker = Worker(
        client,
        task_queue="math-swarm-queue",
        workflows=[MathSwarmWorkflow],
        activities=[run_math_swarm_activity],
    )
    print("Temporal Worker started on queue 'math-swarm-queue'...")
    await worker.run()
