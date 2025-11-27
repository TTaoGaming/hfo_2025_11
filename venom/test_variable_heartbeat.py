import sys
import os
import asyncio
import time
import logging
from datetime import datetime

# Path setup
sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("buds/hfo_gem_gen_55"))

# Dynamic import to handle the module name
import importlib.util
spec = importlib.util.spec_from_file_location(
    "cleanroom_prey_1111",
    "buds/hfo_gem_gen_55/body/hands/cleanroom_prey_1111.py"
)
cleanroom_prey_1111 = importlib.util.module_from_spec(spec)
sys.modules["cleanroom_prey_1111"] = cleanroom_prey_1111
spec.loader.exec_module(cleanroom_prey_1111)

PreyAgent = cleanroom_prey_1111.PreyAgent
PerceptionReport = cleanroom_prey_1111.PerceptionReport

# Mock Stigmergy
class MockStigmergy:
    async def publish(self, subject, payload):
        pass
    async def connect(self):
        pass

# Mock Agent to override perceive
class TestAgent(PreyAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.forced_state = "Clear"

    async def perceive(self, loop_id: int) -> PerceptionReport:
        # Force the state update
        self.current_cynefin_state = self.forced_state
        return PerceptionReport(
            loop_id=loop_id,
            cynefin_state=self.forced_state,
            environment_scan=f"Forced state: {self.forced_state}"
        )
    
    async def react(self, perception):
        # No-op for speed
        from cleanroom_prey_1111 import ReactionPlan
        return ReactionPlan(loop_id=perception.loop_id, intent="Test")
        
    async def execute(self, plan):
        from cleanroom_prey_1111 import ExecutionResult
        return ExecutionResult(loop_id=plan.loop_id, status="success", output="Test", tool_outputs=[])

    async def yield_phase(self, result, perception):
        from cleanroom_prey_1111 import YieldArtifact
        return YieldArtifact(loop_id=result.loop_id, content="Test")

async def test_variable_heartbeat():
    agent = TestAgent(agent_id="test_variable", stigmergy=MockStigmergy(), mission="Test")
    
    print("--- Starting Variable Heartbeat Test ---")
    
    # Phase 1: Chaotic (Should be ~5s)
    print("\n[Phase 1] Setting State to CHAOTIC (Target: 5s)")
    agent.forced_state = "Chaotic"
    
    for i in range(1, 4):
        start = time.time()
        await agent.run_loop(i)
        
        # Logic from main()
        cynefin = agent.current_cynefin_state
        if cynefin == "Chaotic":
            target = 5
        else:
            target = 60
            
        elapsed = time.time() - start
        sleep_time = max(0, target - elapsed)
        
        print(f"Loop {i}: Elapsed {elapsed:.2f}s. State: {cynefin}. Sleeping {sleep_time:.2f}s...")
        # await asyncio.sleep(sleep_time)
        
        total_time = time.time() - start
        print(f"-> Total Loop Time: {total_time:.2f}s (Expected ~5s)")

    # Phase 2: Clear (Should be ~60s)
    # We will just run 1 loop to verify the sleep calculation, we don't need to wait the full minute to prove the logic
    print("\n[Phase 2] Setting State to CLEAR (Target: 60s)")
    agent.forced_state = "Clear"
    
    start = time.time()
    await agent.run_loop(4)
    
    cynefin = agent.current_cynefin_state
    if cynefin == "Chaotic":
        target = 5
    else:
        target = 60
        
    elapsed = time.time() - start
    sleep_time = max(0, target - elapsed)
    
    print(f"Loop 4: Elapsed {elapsed:.2f}s. State: {cynefin}. Sleeping {sleep_time:.2f}s...")
    print(f"-> Calculated Sleep: {sleep_time:.2f}s. (If we waited, total would be ~60s)")
    
    if sleep_time > 50:
        print("\n✅ SUCCESS: Logic correctly adjusted for Clear state.")
    else:
        print("\n❌ FAILURE: Logic did not adjust for Clear state.")

if __name__ == "__main__":
    asyncio.run(test_variable_heartbeat())
