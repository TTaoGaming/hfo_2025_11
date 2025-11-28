"""
# ==================================================================
# 🕸⛰🔔 CHANT ASSIMILATOR (The Listener)
# ==================================================================
# Listens to the Octarchy. Verifies Truth. Reports Uptime.
"""

import asyncio
import logging
import os
import time
import hmac
import hashlib
import json
from datetime import datetime
from collections import defaultdict

# Import Canonical Chant
import sys

# Add path to Gen 55 Memory
sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../buds/hfo_gem_gen_55")
    )
)

# Fix for OMP Error
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

try:
    from memory.lancedb_store import HFOStigmergyMemory
except ImportError as e:
    logging.error(f"Failed to import HFOStigmergyMemory: {e}")
    sys.exit(1)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from body.constants_chant import CANONICAL_CHANT_TEXT, CHANT_SECRET_KEY
from hfo_sdk.stigmergy import StigmergyClient

# Configure Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("hfo.chant_assimilator")

REPORT_LOG_PATH = "audit_trail/logs/chant_report.log"
os.makedirs(os.path.dirname(REPORT_LOG_PATH), exist_ok=True)
DB_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../buds/hfo_gem_gen_55/memory/lancedb")
)


class ChantAssimilator:
    def __init__(self, nats_client: StigmergyClient):
        self.nats = nats_client
        self.stats = defaultdict(
            lambda: {"count": 0, "errors": 0, "hallucinations": 0, "last_seen": 0}
        )
        self.start_time = time.time()
        self.last_report_hour = datetime.now().hour

        # Initialize LanceDB
        try:
            logger.info(f"🔌 Connecting to LanceDB at {DB_PATH}...")
            self.memory = HFOStigmergyMemory(db_path=DB_PATH)
            logger.info("✅ LanceDB Connected.")
        except Exception as e:
            logger.error(f"❌ LanceDB Connection Failed: {e}")
            raise

    def verify_signature(self, payload: dict) -> bool:
        try:
            agent_id = payload["agent_id"]
            timestamp = str(payload["timestamp"])
            chant = payload["chant"]
            signature = payload["signature"]

            payload_str = f"{agent_id}:{timestamp}:{chant}"
            expected_sig = hmac.new(
                CHANT_SECRET_KEY.encode(), payload_str.encode(), hashlib.sha256
            ).hexdigest()

            return hmac.compare_digest(signature, expected_sig)
        except KeyError:
            return False

    def check_hallucination(self, chant: str) -> bool:
        # Normalize line endings and whitespace
        canonical = CANONICAL_CHANT_TEXT.strip().replace("\r\n", "\n")
        received = chant.strip().replace("\r\n", "\n")
        return canonical == received

    async def generate_report(self, report_type="HOURLY"):
        uptime_seconds = time.time() - self.start_time
        uptime_hours = uptime_seconds / 3600

        report = [
            f"--- {report_type} CHANT REPORT [{datetime.now().isoformat()}] ---",
            f"Uptime: {uptime_hours:.2f} hours",
            "Agent Stats:",
        ]

        total_chants = 0
        total_hallucinations = 0

        for agent_id, data in self.stats.items():
            count = data["count"]
            hallucinations = data["hallucinations"]
            last_seen_ago = time.time() - data["last_seen"]
            status = "🟢 Online" if last_seen_ago < 120 else "🔴 Offline"

            report.append(
                f"  - {agent_id}: {count} chants, {hallucinations} hallucinations. Status: {status} ({last_seen_ago:.1f}s ago)"
            )
            total_chants += count
            total_hallucinations += hallucinations

        report.append(f"Total Throughput: {total_chants} chants")
        report.append(
            f"System Integrity: {100 * (1 - (total_hallucinations / max(1, total_chants))):.2f}%"
        )
        report.append("---------------------------------------------------")

        report_str = "\n".join(report)
        logger.info(f"\n{report_str}")

        with open(REPORT_LOG_PATH, "a") as f:
            f.write(report_str + "\n")

    async def run(self):
        logger.info("👂 Assimilator Listening on hfo.chant.>")

        async def msg_handler(msg):
            try:
                data = json.loads(msg.data.decode())
                agent_id = data.get("agent_id", "unknown")

                # Update heartbeat
                self.stats[agent_id]["last_seen"] = time.time()
                self.stats[agent_id]["count"] += 1

                # Verify Crypto
                if not self.verify_signature(data):
                    logger.warning(f"⚠️ [SECURITY] Invalid Signature from {agent_id}")
                    self.stats[agent_id]["errors"] += 1
                    return

                # Verify Truth
                if not self.check_hallucination(data["chant"]):
                    logger.warning(
                        f"🍄 [HALLUCINATION] {agent_id} deviated from the Chant!"
                    )
                    self.stats[agent_id]["hallucinations"] += 1
                else:
                    logger.info(f"✅ {agent_id} verified.")

                    # Store in LanceDB (Cold Memory)
                    try:
                        # Add ID if missing
                        if "id" not in data:
                            data["id"] = f"{agent_id}_{time.time()}"

                        self.memory.store(
                            section="hfo_chant", payload=data, privilege_level=0
                        )
                        logger.info("   💾 Stored in LanceDB.")
                    except Exception as e:
                        logger.error(f"❌ LanceDB Store Failed: {e}")

                # Check for Hourly Report
                current_hour = datetime.now().hour
                if current_hour != self.last_report_hour:
                    await self.generate_report("HOURLY")
                    self.last_report_hour = current_hour

            except Exception as e:
                logger.error(f"Processing Error: {e}")

        await self.nats.js.subscribe("hfo.chant.>", cb=msg_handler)

        # Keep running
        while True:
            await asyncio.sleep(1)


async def main():
    nats_url = os.getenv("NATS_URL", "nats://localhost:4225")
    stigmergy = StigmergyClient(nats_url=nats_url)

    try:
        await stigmergy.connect()
    except Exception as e:
        logger.error(f"Critical NATS Failure: {e}")
        return

    assimilator = ChantAssimilator(stigmergy)

    try:
        await assimilator.run()
    except KeyboardInterrupt:
        logger.info("Stopping Assimilator...")
    finally:
        await stigmergy.close()


if __name__ == "__main__":
    asyncio.run(main())
