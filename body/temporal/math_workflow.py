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
    import uuid
    from body.hands.hydra_swarm import build_hydra_graph, HydraState

    # Initialize Ray if needed (it might be running globally, but safe to check)
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True)

    app = build_hydra_graph()

    mission_id = str(uuid.uuid4())
    initial_state = HydraState(
        mission_id=mission_id,
        mission=user_request,
        plan=[],
        results=[],
        final_output=None,
    )

    # Run the graph
    final_state = await app.ainvoke(initial_state)

    if final_state.get("final_output"):
        return final_state["final_output"].summary
    return "Mission Failed: No output generated."


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
