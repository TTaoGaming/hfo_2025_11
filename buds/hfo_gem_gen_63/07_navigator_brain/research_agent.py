"""
---
holon:
  id: hfo-00e78944
  type: intent
  file: research_agent.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_navigator_temporal.md
---
"""
import asyncio
import logging
from temporalio.client import Client
from temporalio.worker import Worker

# Import Config via Proxy
from src.config import settings

# Import Workflow & Activities
# Handle numeric folder import issue
try:
    from .workflows import ResearchWorkflow
    from .activities import search_memory, search_web_activity, synthesize_report
except ImportError:
    # Fallback for when running with sys.path hack
    from workflows import ResearchWorkflow
    from activities import search_memory, search_web_activity, synthesize_report

logger = logging.getLogger("ResearchAgent")

class ResearchAgent:
    """
    The Research Agent (Navigator Client).
    Submits workflows to the Temporal Cluster.
    """
    def __init__(self):
        self.client = None

    async def connect(self):
        """Connect to Temporal Server."""
        # Default to localhost:7233
        self.client = await Client.connect("localhost:7233")
        logger.info("🔌 Connected to Temporal.")

    async def run_worker(self):
        """Run a local worker (for development/POC)."""
        if not self.client:
            await self.connect()
            
        worker = Worker(
            self.client,
            task_queue="hfo-research-queue",
            workflows=[ResearchWorkflow],
            activities=[search_memory, search_web_activity, synthesize_report],
        )
        logger.info("👷 Starting Temporal Worker...")
        await worker.run()

    async def research(self, query: str) -> str:
        """
        Submit a Research Workflow.
        """
        if not self.client:
            await self.connect()
            
        logger.info(f"🚀 Submitting Workflow: {query}")
        
        result = await self.client.execute_workflow(
            ResearchWorkflow.run,
            query,
            id=f"research-{query.replace(' ', '-').lower()[:30]}",
            task_queue="hfo-research-queue",
        )
        
        return result

if __name__ == "__main__":
    # Simple CLI for testing
    agent = ResearchAgent()
    
    async def main():
        # Start worker in background
        worker_task = asyncio.create_task(agent.run_worker())
        
        # Wait a bit for worker to spin up
        await asyncio.sleep(2)
        
        # Run query
        try:
            result = await agent.research("What is the Model Context Protocol?")
            print("\n\n=== 🕷️ RESEARCH REPORT ===\n")
            print(result)
            print("\n==========================\n")
        finally:
            # Cancel worker
            worker_task.cancel()
            try:
                await worker_task
            except asyncio.CancelledError:
                pass

    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
