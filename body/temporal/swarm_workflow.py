"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 9f203b16-2125-47f3-8be2-bde71401fd0d
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.352643+00:00'
  topos:
    address: body/temporal/swarm_workflow.py
    links: []
  telos:
    viral_factor: 0.0
    meme: swarm_workflow.py
"""

from datetime import timedelta
from temporalio import activity, workflow
from temporalio.common import RetryPolicy
from body.config import Config


@activity.defn
async def run_research_swarm_activity(mission: str) -> str:
    """
    Executes the Research Swarm (Fractal Holarchy).
    """
    # Import inside activity to avoid serialization issues
    from body.hands.research_swarm import SwarmNode, build_swarm_graph
    from datetime import datetime, timezone

    node = SwarmNode()
    await node.connect_nats()

    try:
        app = build_swarm_graph(node)

        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        mission_slug = mission[:30].replace(" ", "_").replace("'", "").lower()

        inputs = {
            "mission": mission,
            "mission_slug": mission_slug,
            "date_str": date_str,
            "tasks": [],
            "findings": [],
            "squad_digests": [],
            "round_1_digest": "",
            "round_2_digest": "",
            "disruptor_reveal_log": [],
            "current_round": 1,
            "history": [],
        }

        final_state = await app.ainvoke(inputs)

        # Return the final digest (Round 2 or Round 1)
        return (
            final_state.get("round_2_digest")
            or final_state.get("round_1_digest")
            or "Mission Failed"
        )

    finally:
        await node.close_nats()


@workflow.defn
class ResearchSwarmWorkflow:
    @workflow.run
    async def run(self, mission: str) -> str:
        return await workflow.execute_activity(
            run_research_swarm_activity,
            mission,
            start_to_close_timeout=timedelta(seconds=Config.SWARM_TIMEOUT),
            retry_policy=RetryPolicy(
                initial_interval=timedelta(seconds=5),
                maximum_interval=timedelta(seconds=60),
                maximum_attempts=3,
            ),
        )


async def run_worker():
    from temporalio.client import Client
    from temporalio.worker import Worker

    client = await Client.connect(Config.TEMPORAL_ADDRESS)
    worker = Worker(
        client,
        task_queue="research-swarm-queue",
        workflows=[ResearchSwarmWorkflow],
        activities=[run_research_swarm_activity],
    )
    print("Temporal Worker started on queue 'research-swarm-queue'...")
    await worker.run()
