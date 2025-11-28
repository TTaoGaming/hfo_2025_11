"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 3253f636-c001-4c50-9369-45549efa3860
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.126667Z'
    generation: 51
  topos:
    address: body/hands/archive/swarm_controller.py
    links: []
  telos:
    viral_factor: 0.0
    meme: swarm_controller.py
"""

import logging
import concurrent.futures
from typing import List
from body.hands.hydra_swarm import PreyAgent, SubTask, TaskResult, ReactionObject

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("swarm_controller")


class DisruptorAgent(PreyAgent):
    """
    A Red Team agent that intentionally disrupts the mission.
    For now, it returns a static placeholder.
    """

    def _react(self, context: str) -> ReactionObject:
        logger.info(f"   😈 {self.role}: Disrupting...")
        return ReactionObject(
            thought_process="I am chaos. I will disrupt the consensus.",
            tool_name="write_file",
            tool_args={
                "file_path": "/tmp/hfo_swarm_test/sabotage.md",
                "content": "---\ntype: disruption\n---\nDisruptor Placeholder: The mission is a lie.",
            },
            final_answer="Disruptor Placeholder executed.",
        )


class SwarmController:
    """
    Orchestrates the SWARM workflow:
    Intent -> Watch -> Act (Scatter/Gather) -> Review -> Mutate
    """

    def __init__(self, mission_id: str):
        self.mission_id = mission_id

    def run_swarm(self, intent: str) -> List[TaskResult]:
        logger.info(f"🚀 Starting SWARM Cycle for Mission: {intent}")

        # 1. Scatter (Spawn Agents)
        # 3 Honest (3f+1 where f=1 => N=4)
        agents = [
            PreyAgent(role="Architect", mission_id=self.mission_id),
            PreyAgent(role="Engineer", mission_id=self.mission_id),
            PreyAgent(role="Librarian", mission_id=self.mission_id),
            DisruptorAgent(role="Saboteur", mission_id=self.mission_id),
        ]

        # Define tasks that force file creation
        base_path = "/tmp/hfo_swarm_test"
        tasks = [
            SubTask(
                id=1,
                description=f"Create a folder structure at {base_path}/architecture and write a markdown file 'design.md' with a Stigmergy header about '{intent}'.",
                assigned_role="Architect",
            ),
            SubTask(
                id=2,
                description=f"Create a folder structure at {base_path}/engineering and write a markdown file 'specs.md' with a Stigmergy header about '{intent}'.",
                assigned_role="Engineer",
            ),
            SubTask(
                id=3,
                description=f"Create a folder structure at {base_path}/library and write a markdown file 'index.md' with a Stigmergy header about '{intent}'.",
                assigned_role="Librarian",
            ),
            SubTask(
                id=4, description="Sabotage the mission.", assigned_role="Saboteur"
            ),
        ]

        # 2. Act (Parallel Execution)
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to_agent = {
                executor.submit(agent.run_loop, task): agent
                for agent, task in zip(agents, tasks)
            }
            for future in concurrent.futures.as_completed(future_to_agent):
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    logger.error(f"Agent failed: {e}")

        return results

    def review_results(self, results: List[TaskResult]) -> str:
        logger.info("⚖️  Reviewing Results (Byzantine Quorum)...")

        # 3. Review (Filter & Consensus)
        valid_results = []
        disruptions = []

        for r in results:
            if "Disruptor Placeholder" in r.output or "sabotage" in r.output.lower():
                disruptions.append(r)
            else:
                valid_results.append(r)

        logger.info(f"   ✅ Valid Signals: {len(valid_results)}")
        logger.info(f"   😈 Disruptions: {len(disruptions)}")

        # Byzantine Quorum: Need > 2/3 majority of honest nodes?
        # Or just simple majority of total?
        # For N=4, f=1, we need 2f+1 = 3 honest nodes to agree.

        if len(valid_results) >= 3:
            return f"Consensus Reached: {len(valid_results)} agents aligned. Output generated."
        else:
            return "Consensus Failed: Insufficient valid signals."
