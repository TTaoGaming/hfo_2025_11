import asyncio
import sys
import os
import logging

# Add root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import the Agent (which imports workflows/activities)
# We need to handle the numeric folder import again if we run this from src/
# But research_agent.py is in 07_navigator_brain.
# Let's try to import it via the file path or sys.path hack.

try:
    # Hack for numeric folders
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../07_navigator_brain")))
    # We also need to add the root to sys.path so that research_agent can import src.config
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    
    from research_agent import ResearchAgent
except ImportError as e:
    print(f"❌ Failed to import ResearchAgent: {e}")
    sys.exit(1)

async def smoke_test_temporal():
    print("🕷️ Smoke Testing Temporal Navigator...")
    
    agent = ResearchAgent()
    
    # We assume Temporal Server is running locally.
    # If not, this will fail with a connection error, which is expected if the user hasn't started it.
    try:
        print("🔌 Connecting to Temporal...")
        await agent.connect()
        print("✅ Connected to Temporal.")
        
        # We won't run the full workflow in the smoke test to avoid blocking/cost,
        # unless the user explicitly asked for it. 
        # But the user DID ask to "set up temporal and then smoke test".
        # So we should try to run a minimal workflow.
        
        print("🚀 Starting Worker & Workflow...")
        worker_task = asyncio.create_task(agent.run_worker())
        await asyncio.sleep(2) # Wait for worker
        
        result = await agent.research("What is the capital of France?")
        print(f"✅ Workflow Result: {result[:100]}...")
        
        worker_task.cancel()
        try:
            await worker_task
        except asyncio.CancelledError:
            pass
            
    except Exception as e:
        print(f"⚠️ Temporal Smoke Test Failed (Is the server running?): {e}")
        print("👉 Run 'temporal server start-dev' in a separate terminal.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(smoke_test_temporal())
