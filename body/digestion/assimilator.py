import asyncio
import logging
import os
from nats.aio.client import Client as NATS
from body.models.stigmergy import StigmergySignal

# Configure Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Assimilator")

NATS_URL = os.getenv("NATS_URL", "nats://localhost:4225")
STREAM_NAME = "hfo_artifacts"
SUBJECT = "hfo.signal.artifact.>"
DURABLE_NAME = "assimilator_consumer"


class Assimilator:
    def __init__(self):
        self.nc = NATS()
        self.js = None

    async def connect(self):
        await self.nc.connect(NATS_URL)
        self.js = self.nc.jetstream()
        logger.info(f"✅ Connected to NATS at {NATS_URL}")

        # Ensure Stream Exists
        try:
            await self.js.add_stream(name=STREAM_NAME, subjects=[SUBJECT])
            logger.info(f"✅ Stream '{STREAM_NAME}' created.")
        except Exception as e:
            logger.warning(f"Stream check warning (likely exists): {e}")

    async def process_signal(self, msg):
        try:
            data = msg.data.decode()
            signal = StigmergySignal.model_validate_json(data)

            # Use metadata.type as the signal type, and producer_id as source
            logger.info(
                f"📥 Received Signal: {signal.metadata.type} from {signal.producer_id}"
            )
            logger.info(f"   📍 Claim Check: {signal.claim_check.pointer}")

            # TODO: In the future, this is where we read the file and write to Postgres/Graph
            # For now, we just verify the file exists
            if os.path.exists(signal.claim_check.pointer):
                logger.info("   ✅ Payload Verified on Disk.")
                # Simulate "Assimilation"
                with open(signal.claim_check.pointer, "r") as f:
                    content = f.read()
                    logger.info(f"   📄 Content Length: {len(content)} chars")
            else:
                logger.error(f"   ❌ Payload NOT FOUND at {signal.claim_check.pointer}")

            await msg.ack()

        except Exception as e:
            logger.error(f"Error processing message: {e}")
            await msg.nak()

    async def run(self):
        await self.connect()

        # Create Durable Consumer
        try:
            await self.js.subscribe(
                SUBJECT, durable=DURABLE_NAME, cb=self.process_signal, manual_ack=True
            )
            logger.info(f"🎧 Listening on {SUBJECT}...")
        except Exception as e:
            logger.error(f"Subscription failed: {e}")
            # Fallback to queue group if durable fails
            await self.js.subscribe(
                SUBJECT,
                queue="assimilator_queue",
                cb=self.process_signal,
                manual_ack=True,
            )
            logger.info(f"🎧 Listening on {SUBJECT} (Queue Mode)...")

        # Keep running
        while True:
            await asyncio.sleep(1)


if __name__ == "__main__":
    assimilator = Assimilator()
    try:
        asyncio.run(assimilator.run())
    except KeyboardInterrupt:
        print("Assimilator Stopped.")
