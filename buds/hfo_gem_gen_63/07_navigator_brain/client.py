"""
---
holon:
  id: hfo-navigator-client
  type: implementation
  file: client.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_navigator_temporal.md
---
"""
import asyncio
import logging
import sys
import os
import uuid

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))
# Add bud root to path for src imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from temporalio.client import Client

# Import Workflow Definition (only needed for type hints/name)
try:
    from .workflows import ResearchWorkflow
except ImportError:
    from workflows import ResearchWorkflow

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NavigatorClient")

async def main():
    """
    Submit a Research Workflow.
    """
    if len(sys.argv) < 2:
        print("Usage: python client.py <query>")
        sys.exit(1)
        
    query = sys.argv[1]
    
    logger.info("🔌 Connecting to Temporal...")
    try:
        client = await asyncio.wait_for(Client.connect("localhost:7233"), timeout=5.0)
    except asyncio.TimeoutError:
        logger.error("❌ Failed to connect to Temporal Server (Timeout 5s). Is it running?")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Connection Error: {e}")
        sys.exit(1)
    
    run_id = str(uuid.uuid4())[:8]
    workflow_id = f"research-{run_id}"
    
    logger.info(f"🚀 Submitting Workflow: '{query}' (ID: {workflow_id})")
    
    try:
        # Enforce 60s timeout on workflow execution
        result = await asyncio.wait_for(
            client.execute_workflow(
                ResearchWorkflow.run,
                query,
                id=workflow_id,
                task_queue="hfo-research-queue",
            ),
            timeout=60.0
        )
    except asyncio.TimeoutError:
        logger.error("❌ Workflow Execution Timed Out (60s). Worker might be stuck or missing.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"❌ Workflow Failed: {e}")
        sys.exit(1)
    
    print("\n\n=== 🕷️ RESEARCH REPORT (PREY 1181) ===\n")
    print(result)
    print("\n======================================\n")

if __name__ == "__main__":
    asyncio.run(main())
