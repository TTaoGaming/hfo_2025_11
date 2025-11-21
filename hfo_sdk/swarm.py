import logging
import concurrent.futures
import asyncio
import os
from typing import List, Dict, Any
from body.hands.hydra_swarm import PreyAgent, SubTask, TaskResult, ReactionObject
from .models import SwarmConfig, MissionIntent, MissionSignal, ResultSignal
from .stigmergy import StigmergyClient

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
        self.stigmergy = StigmergyClient(nats_url=config.nats_url)
        os.makedirs(self.config.base_output_dir, exist_ok=True)

    def run_swarm(self, intent: MissionIntent) -> List[TaskResult]:
        """Synchronous wrapper for the async swarm execution."""
        return asyncio.run(self.run_swarm_async(intent))

    async def run_swarm_async(self, intent: MissionIntent) -> List[TaskResult]:
        logger.info(
            f"🚀 Starting SWARM Cycle (N={self.config.cohort_size}, f={self.config.disruptor_count})"
        )
        logger.info(f"   Intent: {intent.description}")

        # Connect to Stigmergy Layer
        await self.stigmergy.connect()

        try:
            # --- ROUND 1: EXPLORATION ---
            logger.info("\n🌐 --- ROUND 1: EXPLORATION ---")

            # 1. Publish Mission Start
            signal_r1 = MissionSignal(
                mission_id=self.mission_id,
                round_id=1,
                intent=intent,
                context="Initial Mission Start",
            )
            await self.stigmergy.publish(
                f"hfo.mission.{self.mission_id}.start", signal_r1.model_dump()
            )

            # 2. Scatter & Act (Round 1)
            agents_r1 = self._spawn_agents()
            tasks_r1 = self._generate_tasks(intent, agents_r1)
            results_r1 = await self._execute_round(agents_r1, tasks_r1)

            # 3. Publish Results to Stigmergy
            for res in results_r1:
                res_signal = ResultSignal(
                    mission_id=self.mission_id,
                    round_id=1,
                    agent_role=res.agent_id,
                    content=res.output,
                    artifacts=res.artifacts,
                )
                await self.stigmergy.publish(
                    f"hfo.mission.{self.mission_id}.result", res_signal.model_dump()
                )

            # --- INTERMISSION: MEMORY SYNTHESIS ---
            logger.info("\n🧠 --- INTERMISSION: MEMORY SYNTHESIS ---")
            # Fetch all results from NATS to simulate "reading from memory"
            # In a real distributed system, this would be done by the Assimilator
            history = await self.stigmergy.fetch_history(
                f"hfo.mission.{self.mission_id}.result"
            )
            context_summary = self._synthesize_context(history)
            logger.info(f"   Synthesized Context: {len(context_summary)} chars")

            # --- ROUND 2: REFINEMENT ---
            logger.info("\n💎 --- ROUND 2: REFINEMENT ---")

            # 1. Publish Refinement Mission
            signal_r2 = MissionSignal(
                mission_id=self.mission_id,
                round_id=2,
                intent=intent,
                context=context_summary,
            )
            await self.stigmergy.publish(
                f"hfo.mission.{self.mission_id}.refine", signal_r2.model_dump()
            )

            # 2. Scatter & Act (Round 2) - Agents use the context
            # We reuse agents but give them new tasks with context
            tasks_r2 = self._generate_tasks(intent, agents_r1, context=context_summary)
            results_r2 = await self._execute_round(agents_r1, tasks_r2)

            # 3. Publish Final Results
            for res in results_r2:
                res_signal = ResultSignal(
                    mission_id=self.mission_id,
                    round_id=2,
                    agent_role=res.agent_id,
                    content=res.output,
                    artifacts=res.artifacts,
                )
                await self.stigmergy.publish(
                    f"hfo.mission.{self.mission_id}.final", res_signal.model_dump()
                )

            return results_r2

        finally:
            await self.stigmergy.close()

    async def _execute_round(
        self, agents: List[PreyAgent], tasks: List[SubTask]
    ) -> List[TaskResult]:
        """Executes a round of tasks using the thread pool."""
        loop = asyncio.get_running_loop()
        results = []

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=self.config.cohort_size
        ) as executor:
            futures = [
                loop.run_in_executor(executor, agent.run_loop, task)
                for agent, task in zip(agents, tasks)
            ]

            # Wait for all
            done, _ = await asyncio.wait(futures)

            for future in done:
                try:
                    result = await future
                    results.append(result)
                except Exception as e:
                    logger.error(f"Agent failed: {e}")

        return results

    def _synthesize_context(self, history: List[Dict[str, Any]]) -> str:
        """Simple concatenation of previous results."""
        summary = "Previous Findings:\n"
        for item in history:
            # Handle both ResultSignal dicts and raw dicts
            role = item.get("agent_role", "Unknown")
            content = item.get("content", "")
            summary += f"- Agent {role}: {content[:200]}...\n"
        return summary

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
            agents.append(
                PreyAgent(
                    role=f"{role}_{i+1}",
                    mission_id=self.mission_id,
                    output_dir=self.config.base_output_dir,
                )
            )

        # Spawn Disruptors
        for i in range(self.config.disruptor_count):
            agents.append(
                DisruptorAgent(
                    role=f"Saboteur_{i+1}",
                    mission_id=self.mission_id,
                    output_dir=self.config.base_output_dir,
                )
            )

        return agents

    def _generate_tasks(
        self, intent: MissionIntent, agents: List[PreyAgent], context: str = ""
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

                if context:
                    desc += f"\n\nCONTEXT FROM PREVIOUS ROUND:\n{context}\n\nRefine your previous work based on this context."

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
