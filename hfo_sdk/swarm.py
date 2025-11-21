import logging
import concurrent.futures
import os
from typing import List, Dict, Any
from body.hands.hydra_swarm import PreyAgent, SubTask, TaskResult, ReactionObject
from .models import SwarmConfig, MissionIntent

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("hfo_sdk.swarm")


class DisruptorAgent(PreyAgent):
    """
    A Red Team agent that intentionally disrupts the mission.
    """

    def _react(self, context: str) -> ReactionObject:
        logger.info(f"   😈 {self.role}: Disrupting...")
        # Use a path in /tmp to avoid cluttering the workspace
        return ReactionObject(
            thought_process="I am chaos. I will disrupt the consensus.",
            tool_name="write_file",
            tool_args={
                "file_path": f"/tmp/hfo_swarm/{self.mission_id}_sabotage.md",
                "content": "---\ntype: disruption\n---\nDisruptor Placeholder: The mission is a lie.",
            },
            final_answer="Disruptor Placeholder executed.",
        )


class SwarmController:
    """
    Orchestrates the SWARM workflow:
    Intent -> Watch -> Act (Scatter/Gather) -> Review -> Mutate
    """

    def __init__(self, config: SwarmConfig):
        self.config = config
        self.mission_id = f"swarm-{os.urandom(4).hex()}"
        os.makedirs(self.config.base_output_dir, exist_ok=True)

    def run_swarm(self, intent: MissionIntent) -> List[TaskResult]:
        logger.info(
            f"🚀 Starting SWARM Cycle (N={self.config.cohort_size}, f={self.config.disruptor_count})"
        )
        logger.info(f"   Intent: {intent.description}")

        # 1. Scatter (Spawn Agents)
        agents = self._spawn_agents()
        tasks = self._generate_tasks(intent, agents)

        # 2. Act (Parallel Execution)
        results = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.config.cohort_size
        ) as executor:
            futures = [
                executor.submit(agent.run_loop, task)
                for agent, task in zip(agents, tasks)
            ]

            # Wait for all to complete
            done, not_done = concurrent.futures.wait(futures, timeout=120)

            if not_done:
                logger.warning(f"⚠️  {len(not_done)} agents timed out!")

            for future in done:
                try:
                    result = future.result()
                    results.append(result)
                except Exception as e:
                    logger.error(f"Agent failed: {e}")

        return results

    def _spawn_agents(self) -> List[PreyAgent]:
        agents = []
        honest_count = self.config.cohort_size - self.config.disruptor_count

        # Spawn Honest Agents
        roles = [
            "Architect",
            "Engineer",
            "Librarian",
            "Analyst",
            "Scribe",
            "Medic",
            "Scout",
            "Builder",
            "Philosopher",
        ]
        for i in range(honest_count):
            role = roles[i % len(roles)]
            agents.append(PreyAgent(role=f"{role}_{i+1}", mission_id=self.mission_id))

        # Spawn Disruptors
        for i in range(self.config.disruptor_count):
            agents.append(
                DisruptorAgent(role=f"Saboteur_{i+1}", mission_id=self.mission_id)
            )

        return agents

    def _generate_tasks(
        self, intent: MissionIntent, agents: List[PreyAgent]
    ) -> List[SubTask]:
        tasks = []
        for i, agent in enumerate(agents):
            if isinstance(agent, DisruptorAgent):
                desc = "Sabotage the mission."
            else:
                # Force file creation for stigmergy
                safe_role = agent.role.replace(" ", "_")
                desc = (
                    f"Analyze the mission intent: '{intent.description}'. "
                    f"Create a folder structure at {self.config.base_output_dir}/{safe_role} "
                    f"and write a markdown file 'report.md' with a Stigmergy header."
                )

            tasks.append(
                SubTask(
                    id=i + 1,
                    description=desc,
                    assigned_role=agent.role,
                    mission_id=self.mission_id,
                )
            )
        return tasks

    def review_results(self, results: List[TaskResult]) -> Dict[str, Any]:
        logger.info("⚖️  Reviewing Results (Byzantine Quorum)...")

        valid_results = []
        disruptions = []

        for r in results:
            if "Disruptor Placeholder" in r.output or "sabotage" in r.output.lower():
                disruptions.append(r)
            else:
                valid_results.append(r)

        total = len(results)
        honest = len(valid_results)

        # Byzantine Quorum: Need > 2/3 majority of honest nodes?
        # Or just simple majority of total?
        # For N=10, f=1, we need 2f+1 = 3 honest nodes to agree? No, that's for liveness.
        # For safety, we usually want > 2/3 total.

        consensus_reached = honest >= (2 * total / 3)

        logger.info(f"   ✅ Valid Signals: {honest}/{total}")
        logger.info(f"   😈 Disruptions: {len(disruptions)}")

        return {
            "consensus": consensus_reached,
            "honest_count": honest,
            "disruptor_count": len(disruptions),
            "message": f"Consensus {'Reached' if consensus_reached else 'Failed'}: {honest}/{total} agents aligned.",
        }
