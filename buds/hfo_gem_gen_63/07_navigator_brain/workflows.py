"""
---
holon:
  id: hfo-navigator-workflows
  type: implementation
  file: workflows.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_navigator_temporal.md
---
"""
from datetime import timedelta
from temporalio import workflow

# Import Activities
# We need to import the definition, not the implementation, for the workflow
with workflow.unsafe.imports_passed_through():
    try:
        from .activities import search_memory, search_web_activity, synthesize_report, run_cognitive_cycle
    except (ImportError, TypeError):
        from activities import search_memory, search_web_activity, synthesize_report, run_cognitive_cycle

@workflow.defn
class ResearchWorkflow:
    """
    The Research Workflow (Navigator).
    Orchestrates the Sense -> Make Sense -> Act loop.
    Now upgraded to use Prey 1181 (LangGraph).
    """
    @workflow.run
    async def run(self, query: str) -> str:
        workflow.logger.info(f"🚀 Starting Research Workflow (Prey 1181) for: {query}")
        
        # The entire cognitive cycle is now encapsulated in a single activity
        # to allow LangGraph to handle the complex state transitions.
        # Temporal handles the reliability of the *entire* thought process.
        
        report = await workflow.execute_activity(
            run_cognitive_cycle,
            query,
            start_to_close_timeout=timedelta(minutes=5)
        )
        
        workflow.logger.info("✅ Research Workflow Complete.")
        return report
