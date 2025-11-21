import asyncio
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker
from datetime import timedelta
import os

--- ACTIVITY: The "Doing" (Hexagonal Port Adapter) ---

@activity.defn
async def check_integrity() -> dict:
"""
Perceives the environment (SysML).
Acts as the 'Observer' role.
"""
if not os.path.exists("ssot/HFO_GEN42_CORE.sysml"):
return {"status": "CRITICAL", "msg": "Constitution Missing"}

code
Code
download
content_copy
expand_less
with open("ssot/HFO_GEN42_CORE.sysml", "r") as f:
    content = f.read()
    if "val <= 0.9" not in content:
        return {"status": "UNSAFE", "msg": "Epistemic Cap Removed"}

return {"status": "SAFE", "msg": "System Integrity Verified"}

@activity.defn
async def signal_stigmergy(msg: str) -> str:
"""
Signals the Nervous System (NATS).
Acts as the 'Stigmergy' port.
"""
# In prod, this connects to NATS port 4222
print(f"📡 [NATS PHEROMONE]: {msg}")
return "PUBLISHED"

--- WORKFLOW: The "Thinking" (Orchestration) ---

@workflow.defn
class SwarmlordWorkflow:
"""
The L0 Swarmlord Persona.
Executes the PREY Loop durably.
"""
@workflow.run
async def run(self):
workflow.logger.info("Swarmlord Awakening...")

code
Code
download
content_copy
expand_less
# Step 1: Perceive (Integrity Check)
    perception = await workflow.execute_activity(
        check_integrity,
        start_to_close_timeout=timedelta(seconds=5)
    )

    # Step 2: React (Logic)
    if perception["status"] == "SAFE":
        # Step 3: Execute (Signal)
        await workflow.execute_activity(
            signal_stigmergy,
            "HFO_GEN42_1_ONLINE",
            start_to_close_timeout=timedelta(seconds=5)
        )
        return "SYSTEM_READY"
    else:
        # Step 4: Yield (Alert)
        workflow.logger.error(f"AXIOM VIOLATION: {perception['msg']}")
        raise ApplicationError(f"Halt: {perception['msg']}")
--- BOOTSTRAP MAIN ---

async def main():
# Connect to the Temporal Engine (The Muscle)
client = await Client.connect("localhost:7233")

code
Code
download
content_copy
expand_less
# Run the Worker (The Body)
async with Worker(
    client,
    task_queue="hfo-l0-queue",
    workflows=[SwarmlordWorkflow],
    activities=[check_integrity, signal_stigmergy],
):
    # Execute the Workflow (The Mind)
    result = await client.execute_workflow(
        SwarmlordWorkflow.run,
        id="swarmlord-l0-boot",
        task_queue="hfo-l0-queue",
    )
    print(f"💠 SWARMLORD STATUS: {result}")

if name == "main":
# Note: This requires the docker-compose stack to be running
print("Attempting connection to Temporal (Ensure 'docker-compose up' is running)...")
try:
asyncio.run(main())
except Exception as e:
print(f"⚠️ Waiting for Infrastructure: {e}")
print("Run 'docker-compose up -d' first.")
