import asyncio
import logging
import os
import json
from pathlib import Path
from body.digestion.crystal_spinner import CrystalSpinner
from hfo_sdk.stigmergy import StigmergyClient

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("swarm_spinner")


class SwarmSpinner:
    """
    A Swarm-enabled version of the Crystal Spinner.
    Uses NATS Queue Groups to distribute work among multiple workers.
    """

    def __init__(self, worker_id: str, nats_url: str = "nats://localhost:4222"):
        self.worker_id = worker_id
        self.spinner = CrystalSpinner(nats_url)
        self.running = True

    async def start_worker(self):
        """Starts the worker loop."""
        await self.spinner.connect()
        logger.info(
            f"🕷️  Worker {self.worker_id} Online. Listening on 'hfo.task.spin'..."
        )

        async def process_msg(msg):
            try:
                data = json.loads(msg.data.decode())
                file_path = data.get("file_path")

                if not file_path:
                    await msg.ack()
                    return

                logger.info(f"[{self.worker_id}] 📥 Received: {file_path}")

                # Read File
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except Exception as e:
                    logger.error(f"[{self.worker_id}] ❌ Read Error: {e}")
                    await msg.ack()
                    return

                # Spin (LLM)
                metadata = await self.spinner.spin(content, Path(file_path).name)

                # Harden (YAML)
                new_content = self.spinner.harden(content, metadata)

                # Weave (Save & Signal)
                await self.spinner.weave(Path(file_path), new_content, metadata)

                logger.info(f"[{self.worker_id}] ✅ Done: {file_path}")
                await msg.ack()

            except Exception as e:
                logger.error(f"[{self.worker_id}] 💥 Processing Error: {e}")
                # Don't ack if we want retry, but for now ack to prevent loop
                await msg.ack()

        # Subscribe to the queue group "spinners"
        # This ensures only ONE worker gets each message
        await self.spinner.stigmergy.subscribe_queue(
            subject="hfo.task.spin", queue="spinners", callback=process_msg
        )

        # Keep alive
        while self.running:
            await asyncio.sleep(1)

    async def stop(self):
        self.running = False
        await self.spinner.close()


async def run_dispatcher(nats_url: str = "nats://localhost:4222"):
    """Scans files and dispatches tasks to the swarm."""
    logger.info("👑 Dispatcher Online. Scanning for Gems...")

    client = StigmergyClient(nats_url)
    await client.connect()

    source_dir = Path("eyes/archive/hfo_gem")
    files = list(source_dir.rglob("*.md"))

    logger.info(f"Found {len(files)} gems. Dispatching to Swarm...")

    for i, file_path in enumerate(files):
        payload = {"file_path": str(file_path)}
        await client.publish("hfo.task.spin", payload)
        if i % 10 == 0:
            print(f"   🚀 Dispatched {i}/{len(files)} tasks...")

    logger.info("✅ All tasks dispatched.")
    await client.close()


async def main():
    # 1. Start Dispatcher
    await run_dispatcher()

    # 2. Start Swarm (20 Workers)
    workers = []
    for i in range(20):
        worker = SwarmSpinner(f"worker-{i+1}")
        workers.append(worker)

    logger.info("🔥 Swarm Activated (20 Workers). Processing in parallel...")

    try:
        await asyncio.gather(*[w.start_worker() for w in workers])
    except KeyboardInterrupt:
        logger.info("🛑 Stopping Swarm...")
        for w in workers:
            await w.stop()


if __name__ == "__main__":
    # Ensure PYTHONPATH is set
    import sys

    sys.path.append(os.getcwd())
    asyncio.run(main())
