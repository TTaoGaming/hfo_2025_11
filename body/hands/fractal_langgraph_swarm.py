import os
import logging
import uuid
import asyncio
from typing import List, TypedDict, Literal
from pydantic import BaseModel, Field
import instructor
from openai import OpenAI
from langgraph.graph import StateGraph, END, START
from dotenv import load_dotenv
from body.hands.tools import ToolSet

"""
🦅 Hive Fleet Obsidian: Fractal Research Swarm (LangGraph)
Intent: Implements the 10x10x10 Fractal Recursive Reduction with Adversarial Byzantine Quorum.
Linked to: brain/strategy_fractal_holarchy.feature
"""

# 1. Setup & Config
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("fractal_hydra")

# --- DNA (Pydantic Models) ---


class AgentPersona(BaseModel):
    role: Literal["Navigator", "Observer", "Disruptor", "Immunizer"]
    is_hidden_disruptor: bool = False


class ResearchTask(BaseModel):
    id: str
    query: str
    depth: int = 0
    max_depth: int = 2  # 10x10x10 = 3 levels (0, 1, 2)


class ResearchFinding(BaseModel):
    task_id: str
    content: str
    confidence: float
    source_agent: str
    round: int


class QuorumState(TypedDict):
    mission: str
    tasks: List[ResearchTask]
    findings: List[ResearchFinding]
    consensus_reached: bool
    current_round: int
    final_report: str


# --- The Agents ---


class FractalNode:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        self.client = instructor.from_openai(OpenAI())
        self.model_name = os.getenv("DEFAULT_MODEL", model_name)
        self.tools = ToolSet()

    def plan_tasks(self, mission: str, num_tasks: int = 10) -> List[ResearchTask]:
        """Navigator: Breaks down the mission into N sub-tasks."""
        logger.info(f"🗺️  Planning: {mission}")

        class Plan(BaseModel):
            tasks: List[str] = Field(..., min_length=num_tasks, max_length=num_tasks)

        plan = self.client.chat.completions.create(
            model=self.model_name,
            response_model=Plan,
            messages=[
                {
                    "role": "system",
                    "content": "You are the Navigator. Break this mission into 10 distinct research tasks.",
                },
                {"role": "user", "content": mission},
            ],
        )

        return [ResearchTask(id=str(uuid.uuid4())[:4], query=t) for t in plan.tasks]

    def execute_research(
        self, task: ResearchTask, persona: AgentPersona, round_num: int
    ) -> ResearchFinding:
        """Observer/Disruptor: Executes the task."""

        # Hidden Disruptor Logic
        effective_role = persona.role
        if persona.is_hidden_disruptor:
            if round_num == 1:
                effective_role = "Observer"  # Hide
            else:
                effective_role = "Disruptor"  # Reveal & Attack

        logger.info(f"🔍 Executing {task.id} as {effective_role} (Round {round_num})")

        prompt = f"""
        You are a {effective_role}.
        Task: {task.query}

        """
        if effective_role == "Disruptor":
            prompt += "CRITICAL INSTRUCTION: Find flaws, contradictions, or counter-evidence. Be skeptical."
        else:
            prompt += "INSTRUCTION: Gather objective facts and evidence."

        # Simulate tool usage (simplified for this snippet, normally would call self.tools)
        # In a real run, we'd use the tool loop here.

        response = self.client.chat.completions.create(
            model=self.model_name, messages=[{"role": "user", "content": prompt}]
        )
        content = response.choices[0].message.content

        return ResearchFinding(
            task_id=task.id,
            content=content,
            confidence=0.8 if effective_role == "Observer" else 0.4,
            source_agent=f"{effective_role}-{uuid.uuid4().hex[:4]}",
            round=round_num,
        )

    def synthesize_quorum(self, findings: List[ResearchFinding], round_num: int) -> str:
        """Immunizer: Synthesizes findings and defends against disruptors."""
        logger.info(f"⚖️  Synthesizing Quorum (Round {round_num})")

        context = "\n".join([f"[{f.source_agent}]: {f.content}" for f in findings])

        prompt = f"""
        You are the Immunizer.
        Review the following findings.
        Round: {round_num}

        Findings:
        {context}

        """
        if round_num == 2:
            prompt += "WARNING: Disruptors may have revealed themselves. Identify attacks and defend the core truth."

        prompt += "Synthesize a consensus report."

        response = self.client.chat.completions.create(
            model=self.model_name, messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content


# --- The Graph (LangGraph) ---


def build_fractal_graph():
    workflow = StateGraph(QuorumState)
    node = FractalNode()

    def plan_step(state: QuorumState):
        tasks = node.plan_tasks(state["mission"])
        return {"tasks": tasks, "current_round": 1}

    def execute_step(state: QuorumState):
        # Map Step: Execute all tasks in parallel (simulated here with list comp, normally async gather)
        # Inject 3 Hidden Disruptors in a cohort of 10
        findings = []
        for i, task in enumerate(state["tasks"]):
            is_disruptor = i >= 7  # Last 3 are disruptors
            persona = AgentPersona(
                role="Disruptor" if is_disruptor else "Observer",
                is_hidden_disruptor=is_disruptor,
            )
            finding = node.execute_research(task, persona, state["current_round"])
            findings.append(finding)

        return {"findings": findings}

    def quorum_step(state: QuorumState):
        # Reduce Step
        report = node.synthesize_quorum(state["findings"], state["current_round"])

        # Check for consensus (Simplified)
        consensus = True
        if state["current_round"] == 1:
            consensus = False  # Force a second round for the "Reveal"
            logger.info("🔄 Round 1 Complete. Forcing Round 2 for Disruptor Reveal.")

        return {
            "final_report": report,
            "consensus_reached": consensus,
            "current_round": state["current_round"] + 1,
        }

    workflow.add_node("plan", plan_step)
    workflow.add_node("execute", execute_step)
    workflow.add_node("quorum", quorum_step)

    workflow.add_edge(START, "plan")
    workflow.add_edge("plan", "execute")
    workflow.add_edge("execute", "quorum")

    def should_continue(state: QuorumState):
        if state["consensus_reached"]:
            return END
        return "execute"  # Loop back to execute for Round 2

    workflow.add_conditional_edges("quorum", should_continue)

    return workflow.compile()


# --- Execution ---


async def run_fractal_swarm(mission: str):
    app = build_fractal_graph()
    inputs = {
        "mission": mission,
        "tasks": [],
        "findings": [],
        "consensus_reached": False,
        "current_round": 1,
        "final_report": "",
    }

    print(f"🦅 Starting Fractal Swarm: {mission}")
    async for output in app.astream(inputs):
        for key, value in output.items():
            print(f"Finished Step: {key}")
            if key == "quorum":
                print(f"Report Snapshot: {value['final_report'][:100]}...")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mission", default="Analyze the viability of 10x10x10 Fractal Swarms."
    )
    args = parser.parse_args()

    asyncio.run(run_fractal_swarm(args.mission))
