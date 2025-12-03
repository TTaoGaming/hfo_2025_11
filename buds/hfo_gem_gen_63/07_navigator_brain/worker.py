"""
---
holon:
  id: hfo-navigator-worker
  type: implementation
  file: worker.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_navigator_temporal.md
---
"""
import asyncio
import logging
import sys
import os

# FIX: OpenMP Runtime Error (Core Dump)
# LanceDB/PyTorch fights with Temporal Sandbox over thread affinity.
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
# Add bud root to path for src imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from temporalio.client import Client
from temporalio.worker import Worker
from temporalio.worker.workflow_sandbox import SandboxedWorkflowRunner

# Import Config via Proxy
from src.config import settings

# Import Workflow & Activities
try:
    from .workflows import ResearchWorkflow
    from .activities import search_memory, search_web_activity, synthesize_report, run_cognitive_cycle
except ImportError:
    from workflows import ResearchWorkflow
    from activities import search_memory, search_web_activity, synthesize_report, run_cognitive_cycle

# Setup Logging
# ARCHITECTURAL FIX: Force standard logging to avoid RichHandler inside Sandbox
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
    force=True # Overwrite any existing handlers (like Rich)
)
logger = logging.getLogger("NavigatorWorker")

async def main():
    """
    Start the Temporal Worker.
    """
    logger.info("🔌 Connecting to Temporal...")
    try:
        # Enforce 10s timeout on connection
        client = await asyncio.wait_for(Client.connect("localhost:7233"), timeout=10.0)
    except asyncio.TimeoutError:
        logger.error("❌ Failed to connect to Temporal Server (Timeout 10s). Is it running?")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Connection Error: {e}")
        sys.exit(1)
    
    # Configure Sandbox
    # ARCHITECTURAL NOTE: We do NOT pass 'rich' through. The Worker must be headless.
    # Observability is handled by OTel/Logging, not stdout.
    # This ensures determinism and prevents import deadlocks.

    worker = Worker(
        client,
        task_queue="hfo-research-queue",
        workflows=[ResearchWorkflow],
        activities=[search_memory, search_web_activity, synthesize_report, run_cognitive_cycle],
    )
    
    logger.info("👷 Navigator Worker Online. Listening on 'hfo-research-queue'...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
