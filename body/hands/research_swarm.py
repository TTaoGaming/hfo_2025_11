import os
import uuid
import logging
import yaml
import asyncio
from datetime import datetime
from typing import List, TypedDict, Literal
from pydantic import BaseModel, Field
import instructor
from openai import OpenAI
from langgraph.graph import StateGraph, END, START
from dotenv import load_dotenv
from body.hands.tools import ToolSet

"""
🦅 Hive Fleet Obsidian: Canonical Research Swarm
Intent: The unified, configurable, fractal research swarm.
Pattern: SWARM (Set -> Watch -> Act -> Review -> Mutate)
"""

# --- Setup ---
load_dotenv()
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("ResearchSwarm")

# Load Config
CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "swarm_config.yaml"
)
try:
    with open(CONFIG_PATH, "r") as f:
        CONFIG = yaml.safe_load(f)
except FileNotFoundError:
    logger.warning("Config file not found, using defaults.")
    CONFIG = {
        "swarm": {
            "branching_factor": 10,
            "disruptor_ratio": 0.2,
            "council_size": 10,
            "max_rounds": 2,
            "model": "x-ai/grok-4.1-fast",
            "artifact_dir": "memory/episodic",
        }
    }

SWARM_CFG = CONFIG["swarm"]

# --- DNA (Pydantic Models) ---


class AgentPersona(BaseModel):
    role: Literal[
        "Navigator", "Observer", "Shaper", "Disruptor", "Immunizer", "Assimilator"
    ]
    is_hidden_disruptor: bool = False


class ResearchTask(BaseModel):
    id: str
    query: str


class ResearchFinding(BaseModel):
    task_id: str
    content: str
    confidence: float
    source_agent: str
    round: int
    is_disruptor_attack: bool = False
    tools_used: List[str] = []


class SwarmState(TypedDict):
    mission: str
    tasks: List[ResearchTask]
    findings: List[ResearchFinding]
    round_1_digest: str
    round_2_digest: str
    disruptor_reveal_log: List[str]
    current_round: int
    history: List[str]


# --- The Agent Node ---


class SwarmNode:
    def __init__(self):
        self.client = instructor.from_openai(
            OpenAI(
                base_url=os.getenv("OPENROUTER_BASE_URL"),
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )
        self.model_name = os.getenv("DEFAULT_MODEL", SWARM_CFG["model"])
        self.tools = ToolSet()
        self.artifact_dir = SWARM_CFG["artifact_dir"]
        os.makedirs(self.artifact_dir, exist_ok=True)

    def set_intent(self, mission: str) -> List[ResearchTask]:
        """Navigator: Sets the plan."""
        num_tasks = SWARM_CFG["branching_factor"]
        logger.info(f"🧭 Navigator Setting Intent: {mission} -> {num_tasks} tasks")

        class Plan(BaseModel):
            tasks: List[str] = Field(..., min_length=num_tasks, max_length=num_tasks)
            strategy: str

        try:
            plan = self.client.chat.completions.create(
                model=self.model_name,
                response_model=Plan,
                messages=[
                    {
                        "role": "system",
                        "content": f"You are the Navigator. Break this mission into {num_tasks} distinct research tasks. Define a high-level strategy.",
                    },
                    {"role": "user", "content": mission},
                ],
            )

            # Audit Artifact
            self._save_artifact(
                "PLAN",
                "Navigator",
                f"Strategy: {plan.strategy}\n\nTasks:\n"
                + "\n".join(f"- {t}" for t in plan.tasks),
                0,
            )

            return [ResearchTask(id=str(uuid.uuid4())[:4], query=t) for t in plan.tasks]
        except Exception as e:
            logger.error(f"Planning failed: {e}")
            return [ResearchTask(id="fallback", query=mission)]

    def watch_plan(self, tasks: List[ResearchTask]) -> bool:
        """Observer: Watches and validates the plan."""
        logger.info("👀 Observer Watching Plan...")

        # Audit Artifact
        validation_msg = f"Validated {len(tasks)} tasks. Plan looks actionable."
        self._save_artifact("WATCH", "Observer", validation_msg, 0)

        return len(tasks) > 0

    def act_map_reduce(
        self, task: ResearchTask, persona: AgentPersona, round_num: int
    ) -> ResearchFinding:
        """Shaper/Disruptor: Executes the task."""

        effective_role = persona.role
        is_attack = False

        if persona.is_hidden_disruptor:
            if round_num == 1:
                # Round 1: Act as Shaper but inject flaws
                effective_role = "Shaper"
                is_attack = True
            else:
                # Round 2: Reveal
                effective_role = "Disruptor"
                is_attack = True

        logger.info(
            f"⚡ Act: {task.id} as {effective_role} (Hidden: {persona.is_hidden_disruptor})"
        )

        prompt = f"""
        You are a {effective_role}.
        Task: {task.query}
        Available Tools: {self.tools.get_tool_names()}
        """

        if is_attack and round_num == 1:
            prompt += "\nSECRET INSTRUCTION: You are a Hidden Disruptor (Red Team). Inject a subtle flaw or misinformation using MITRE ATT&CK tactics (e.g., Defense Evasion). Play nice, do NOT reveal your nature yet."
        elif is_attack and round_num == 2:
            prompt += "\nINSTRUCTION: Reveal yourself! Self-tag as [DISRUPTOR]. Explain exactly how you attacked the system in Round 1. This is for Co-Evolution/Feedback."
        else:
            prompt += "\nINSTRUCTION: Gather objective facts and evidence. Be honest."

        class AgentResponse(BaseModel):
            content: str

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                response_model=AgentResponse,
                messages=[{"role": "user", "content": prompt}],
            )
            content = response.content
        except Exception as e:
            content = f"Error: {e}"

        self._save_artifact(task.id, effective_role, content, round_num)

        return ResearchFinding(
            task_id=task.id,
            content=content,
            confidence=0.9 if not is_attack else 0.3,
            source_agent=f"{effective_role}-{uuid.uuid4().hex[:4]}",
            round=round_num,
            is_disruptor_attack=is_attack,
        )

    def review_quorum(
        self, findings: List[ResearchFinding], round_num: int, mission: str
    ) -> str:
        """Immunizer Council: Reviews findings and produces digest."""
        council_size = SWARM_CFG.get("council_size", 3)
        logger.info(
            f"⚖️  Review: Council of {council_size} Immunizers convening (Round {round_num})"
        )

        context = "\n".join([f"[{f.source_agent}]: {f.content}" for f in findings])

        # Simulate Council Vote/Synthesis
        # For efficiency, we'll do one synthesis pass but instruct it to act as a quorum

        prompt = f"""
        You are the Immunizer Council (Quorum of {council_size}).
        Mission: {mission}
        Round: {round_num}

        Findings from the Swarm:
        {context}
        """

        if round_num == 1:
            prompt += "\nINSTRUCTION: Synthesize a consensus digest. WARNING: Hidden Disruptors may be present. Try to identify suspicious patterns, but assume mostly honest intent."
        else:
            prompt += "\nINSTRUCTION: Disruptors have revealed themselves! Treat their 'Reveal' info as High Priority feedback. Balance the previous results with this new adversarial truth. Produce a Final Truth Digest."

        class CouncilDigest(BaseModel):
            digest: str

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                response_model=CouncilDigest,
                messages=[{"role": "user", "content": prompt}],
            )
            digest = response.digest
        except Exception as e:
            digest = f"Quorum Failed: {e}"

        self._save_artifact("QUORUM", "ImmunizerCouncil", digest, round_num)
        return digest

    def _save_artifact(self, task_id, role, content, round_num):
        timestamp = datetime.utcnow().isoformat()
        filename = f"{timestamp}_{role}_{task_id}.md"
        path = os.path.join(self.artifact_dir, filename)

        with open(path, "w") as f:
            f.write(
                f"---\nid: {task_id}\nrole: {role}\nround: {round_num}\ntimestamp: {timestamp}\n---\n\n{content}"
            )


# --- The Graph ---


def build_swarm_graph():
    workflow = StateGraph(SwarmState)
    node = SwarmNode()

    N = SWARM_CFG["branching_factor"]
    disruptor_count = int(N * SWARM_CFG["disruptor_ratio"])

    def set_step(state: SwarmState):
        tasks = node.set_intent(state["mission"])
        return {"tasks": tasks, "current_round": 1}

    def watch_step(state: SwarmState):
        valid = node.watch_plan(state["tasks"])
        if not valid:
            # In a real loop, we might loop back to Set. For now, proceed.
            logger.warning("Plan validation failed, but proceeding.")
        return {}

    def act_step(state: SwarmState):
        findings = []
        round_num = state["current_round"]

        # If Round 2, we only run the Disruptors to Reveal?
        # Or re-run everyone? The user said "round 2 disruptor reveal themselves".
        # Let's re-run the logic for everyone, but honest agents just reaffirm, disruptors reveal.

        for i, task in enumerate(state["tasks"]):
            is_disruptor = i >= (N - disruptor_count)
            persona = AgentPersona(
                role="Disruptor" if is_disruptor else "Shaper",
                is_hidden_disruptor=is_disruptor,
            )
            finding = node.act_map_reduce(task, persona, round_num)
            findings.append(finding)

        return {"findings": findings}

    def review_step(state: SwarmState):
        digest = node.review_quorum(
            state["findings"], state["current_round"], state["mission"]
        )

        updates = {}
        if state["current_round"] == 1:
            updates["round_1_digest"] = digest
            updates["current_round"] = 2
        else:
            updates["round_2_digest"] = digest
            # End loop

        return updates

    workflow.add_node("set", set_step)
    workflow.add_node("watch", watch_step)
    workflow.add_node("act", act_step)
    workflow.add_node("review", review_step)

    workflow.add_edge(START, "set")
    workflow.add_edge("set", "watch")
    workflow.add_edge("watch", "act")
    workflow.add_edge("act", "review")

    def check_round(state: SwarmState):
        if state["current_round"] == 2 and not state.get("round_2_digest"):
            return "act"  # Loop back for Round 2 (Reveal)
        return END

    workflow.add_conditional_edges("review", check_round)

    return workflow.compile()


async def run_swarm(mission: str):
    app = build_swarm_graph()
    inputs = {
        "mission": mission,
        "tasks": [],
        "findings": [],
        "round_1_digest": "",
        "round_2_digest": "",
        "disruptor_reveal_log": [],
        "current_round": 1,
        "history": [],
    }

    print(f"🦅 Starting SWARM Loop: {mission}")
    async for output in app.astream(inputs):
        for key, value in output.items():
            print(f"Finished Step: {key}")
            if key == "review":
                if value.get("round_1_digest"):
                    print(f"📜 Round 1 Digest: {value['round_1_digest'][:100]}...")
                if value.get("round_2_digest"):
                    print(f"💎 Final Digest: {value['round_2_digest'][:100]}...")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mission", default="Analyze the viability of the Canonical Swarm."
    )
    args = parser.parse_args()

    asyncio.run(run_swarm(args.mission))
