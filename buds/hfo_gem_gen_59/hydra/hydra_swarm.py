import asyncio
import json
import logging
import sys
import os
import argparse
from typing import Dict

# Add root to path
sys.path.append(os.getcwd())

from buds.hfo_gem_gen_59.nerves.stigmergy_client import StigmergyClient
from buds.hfo_gem_gen_59.hydra.agent_graph import build_hydra_graph

# Setup Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("HydraSwarm")

class HydraSwarm:
    def __init__(self):
        self.stigmergy = StigmergyClient()
        self.graph = build_hydra_graph()
        self.active_tasks: Dict[str, asyncio.Task] = {}
        self.stop_signals: Dict[str, bool] = {}

    async def start(self):
        await self.stigmergy.connect()
        
        # Subscribe to Task Dispatch
        await self.stigmergy.subscribe("hfo.task.dispatch", self.handle_dispatch)
        # Subscribe to Stop Signals
        await self.stigmergy.subscribe("hfo.task.stop", self.handle_stop)
        
        logger.info("🐉 Hydra Swarm Active. Waiting for tasks...")
        
        # Keep alive
        while True:
            await asyncio.sleep(1)

    async def handle_dispatch(self, msg):
        try:
            data = json.loads(msg.data.decode())
            task_id = data.get("task_id")
            task_desc = data.get("task")
            
            if not task_id or not task_desc:
                logger.error("Invalid task dispatch received.")
                return

            logger.info(f"📥 Received Task {task_id}: {task_desc}")
            
            # Start Task in Background
            self.stop_signals[task_id] = False
            task_coro = self.run_agent(task_id, task_desc)
            self.active_tasks[task_id] = asyncio.create_task(task_coro)
            
        except Exception as e:
            logger.error(f"Error handling dispatch: {e}")

    async def handle_stop(self, msg):
        try:
            data = json.loads(msg.data.decode())
            task_id = data.get("task_id")
            if task_id in self.active_tasks:
                logger.info(f"🛑 Received Stop Signal for Task {task_id}")
                self.stop_signals[task_id] = True
                # We can also cancel the task if we want hard stop
                # self.active_tasks[task_id].cancel()
        except Exception as e:
            logger.error(f"Error handling stop: {e}")

    async def run_agent(self, task_id: str, task_desc: str):
        logger.info(f"🚀 Starting Agent for Task {task_id}")
        
        initial_state = {
            "task": task_desc,
            "messages": [],
            "status": "start",
            "iterations": 0
        }
        
        # Run the graph step by step to allow for "Anytime" stopping
        config = {"recursion_limit": 50}
        final_result = None
        
        try:
            async for event in self.graph.astream(initial_state, config=config):
                # Check for Stop Signal
                if self.stop_signals.get(task_id):
                    logger.info(f"⚠️ Task {task_id} Interrupted by User (Anytime Stop).")
                    await self.stigmergy.publish_ingest(json.dumps({
                        "task_id": task_id,
                        "status": "interrupted",
                        "result": "Partial Result (Interrupted)"
                    }))
                    break
                
                # Log Event
                for key, value in event.items():
                    logger.info(f"Task {task_id} - Node {key}: {value.get('status', 'running')}")
                    if 'result' in value:
                        final_result = value['result']
            
            if not self.stop_signals.get(task_id):
                logger.info(f"✅ Task {task_id} Completed.")
                await self.stigmergy.publish_ingest(json.dumps({
                    "task_id": task_id,
                    "status": "completed",
                    "result": final_result or "Task Completed Successfully (No Result)"
                }))
                
        except Exception as e:
            logger.error(f"Task {task_id} Failed: {e}")
        finally:
            if task_id in self.active_tasks:
                del self.active_tasks[task_id]
            if task_id in self.stop_signals:
                del self.stop_signals[task_id]

if __name__ == "__main__":
    swarm = HydraSwarm()
    try:
        asyncio.run(swarm.start())
    except KeyboardInterrupt:
        logger.info("Hydra Swarm Stopped.")
