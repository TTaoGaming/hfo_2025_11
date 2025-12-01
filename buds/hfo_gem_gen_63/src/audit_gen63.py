import asyncio
import logging
import sys
import os
import time

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings
from src.adapters.nats_adapter import NatsAdapter
from src.bridger import Bridger
from src.swarm import HydraSwarm

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("AuditGen63")

async def audit_system():
    """
    The Grand Audit of Gen 63.
    Verifies all organs of the Hydra.
    """
    logger.info("🔍 STARTING GEN 63 SYSTEM AUDIT...")
    report = {
        "config": False,
        "memory": False,
        "nerves": False,
        "brain": False,
        "heartbeat": False
    }

    # 1. Config Check
    try:
        if settings.ENV and settings.NATS_URL:
            logger.info("✅ [CONFIG] Environment loaded.")
            report["config"] = True
        else:
            logger.error("❌ [CONFIG] Settings missing.")
    except Exception as e:
        logger.error(f"❌ [CONFIG] Failed: {e}")

    # 2. Memory Check (Bridger)
    try:
        bridger = Bridger()
        # Quick write/read
        test_mem = f"Audit Timestamp {time.time()}"
        bridger.memorize(test_mem, source="audit", category="test")
        results = bridger.ask(test_mem, limit=1)
        if results and results[0]['text'] == test_mem:
            logger.info("✅ [MEMORY] Bridger (LanceDB) is active and recalling.")
            report["memory"] = True
        else:
            logger.error("❌ [MEMORY] Recall failed.")
    except Exception as e:
        logger.error(f"❌ [MEMORY] Failed: {e}")

    # 3. Nerves Check (NATS)
    try:
        bus = NatsAdapter(settings.NATS_URL)
        await bus.connect()
        logger.info("✅ [NERVES] NATS JetStream connected.")
        report["nerves"] = True
        await bus.close()
    except Exception as e:
        logger.error(f"❌ [NERVES] Failed: {e}")

    # 4. Brain Check (Swarm)
    try:
        swarm = HydraSwarm()
        # Simple research query (no council needed for quick check)
        res = swarm.researcher.research("Are you online?")
        if res and "❌" not in res:
            logger.info("✅ [BRAIN] Hydra Swarm (OpenRouter) is thinking.")
            report["brain"] = True
        else:
            logger.error(f"❌ [BRAIN] Failed: {res}")
    except Exception as e:
        logger.error(f"❌ [BRAIN] Failed: {e}")

    # 5. Heartbeat Check (Simulated Loop)
    # We assume the previous stigmergy_loop.py test passed if we are here, 
    # but let's verify the file exists as proof of life.
    if os.path.exists("buds/hfo_gem_gen_63/sandbox/hello_stigmergy.txt"):
        logger.info("✅ [HEARTBEAT] Stigmergy artifact found.")
        report["heartbeat"] = True
    else:
        logger.warning("⚠️ [HEARTBEAT] Stigmergy artifact missing (run stigmergy_loop.py first).")

    # Final Verdict
    if all(report.values()):
        logger.info("🏆 AUDIT PASSED: Gen 63 is READY for Deployment.")
        return True
    else:
        logger.error(f"🚫 AUDIT FAILED: {report}")
        return False

if __name__ == "__main__":
    success = asyncio.run(audit_system())
    sys.exit(0 if success else 1)
