import asyncio
import logging
from temporalio.client import Client
from temporalio.worker import Worker
from body.config import Config

# Import Workflows and Activities
from body.temporal.swarm_workflow import (
    ResearchSwarmWorkflow,
    run_research_swarm_activity,
)
from body.temporal.header_workflow import HeaderSwarmWorkflow, run_header_swarm_activity

# from body.temporal.math_workflow import MathWorkflow, run_math_activity # If exists

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TemporalWorker")


async def main():
    logger.info("Connecting to Temporal server...")
    client = await Client.connect(Config.TEMPORAL_ADDRESS)

    # Create Worker
    worker = Worker(
        client,
        task_queue="header-swarm-queue",  # Using a shared queue or specific one?
        # Ideally we might want multiple workers or one worker listening to multiple queues
        # For simplicity, let's use one worker for now, but we need to make sure the queue matches
        # genesis.py uses "header-swarm-queue"
        # swarm_workflow.py uses "research-swarm-queue"
        # We can listen to multiple queues by creating multiple workers or just use one queue for all if we change the code.
        # Let's create a worker that listens to "header-swarm-queue" for now.
        workflows=[HeaderSwarmWorkflow],
        activities=[run_header_swarm_activity],
    )

    # We can also add the research swarm worker here if we want a unified worker
    research_worker = Worker(
        client,
        task_queue="research-swarm-queue",
        workflows=[ResearchSwarmWorkflow],
        activities=[run_research_swarm_activity],
    )

    logger.info(
        "Worker started. Listening on 'header-swarm-queue' and 'research-swarm-queue'..."
    )
    await asyncio.gather(worker.run(), research_worker.run())


if __name__ == "__main__":
    asyncio.run(main())
