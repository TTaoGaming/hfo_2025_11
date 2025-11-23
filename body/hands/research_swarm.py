"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 7a947628-5e74-4205-a54d-289034743eac
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.406028+00:00'
  topos:
    address: body/hands/research_swarm.py
    links: []
  telos:
    viral_factor: 0.0
    meme: research_swarm.py


Research Swarm Implementation
Intent: Execute complex research missions using a Fractal Holarchy of agents.
"""
import os
import uuid
import logging
import yaml
import asyncio
import json
from datetime import datetime, timezone
from typing import List, TypedDict, Literal, Dict, Any, cast
from pydantic import BaseModel, Field
import instructor
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from openai import AsyncOpenAI
from langgraph.graph import StateGraph, END, START
from dotenv import load_dotenv
import nats
from body.hands.tools import ToolSet
from body.constants import DEFAULT_MODEL
from body.hands.prey_agent import PreyAgent
from body.models.state import AgentRole
from body.config import Config
from body.models.stigmergy import (
    StigmergySignal,
    ClaimCheck,
    RichMetadata,
    ArtifactType,
)

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
            "model": DEFAULT_MODEL,
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
    mission_slug: str
    date_str: str
    current_round: int
    tasks: List[ResearchTask]
    findings: List[ResearchFinding]
    squad_digests: List[str]  # New: Holds the 5 Immunizer Digests
    previous_round_digest: str  # Holds the digest from the previous round to feed into the next
    all_digests: Dict[int, str]  # Holds all digests by round number
    disruptor_reveal_log: List[str]
    history: List[str]


# --- The Agent Node ---


class SwarmNode:
    def __init__(self):
        self.client = instructor.from_openai(
            AsyncOpenAI(
                base_url=os.getenv("OPENROUTER_BASE_URL"),
                api_key=os.getenv("OPENROUTER_API_KEY"),
            ),
            mode=instructor.Mode.JSON,
        )
        self.nc = None
        self.js = None
        # Load Models from Config
        self.default_model = SWARM_CFG.get("model", DEFAULT_MODEL)
        self.shaper_model = SWARM_CFG.get("shaper_model", self.default_model)
        self.immunizer_model = SWARM_CFG.get("immunizer_model", DEFAULT_MODEL)

        self.artifact_dir = SWARM_CFG["artifact_dir"]
        self.mission_dir = os.path.join("memory", "missions")
        self.nc = None
        self.tools = ToolSet()
        os.makedirs(self.artifact_dir, exist_ok=True)
        os.makedirs(self.mission_dir, exist_ok=True)

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type(Exception),
        reraise=True,
    )
    async def connect_nats(self):
        """Connects to the NATS JetStream server."""
        nats_url = Config.NATS_URL
        logger.info(f"🔌 Attempting NATS connection to: {nats_url}")
        try:
            self.nc = await nats.connect(nats_url)
            logger.info(f"🔌 Connected to NATS JetStream at {nats_url}")
        except Exception as e:
            logger.warning(f"⚠️ NATS Connection Failed: {e}. Retrying...")
            raise e

    async def close_nats(self):
        """Closes the NATS connection."""
        if self.nc:
            await self.nc.close()
            logger.info("🔌 NATS Connection Closed")

    async def publish_signal(self, subject: str, payload: dict):
        """Publishes a signal to NATS (Hot Pheromone)."""
        if self.nc:
            try:
                data = json.dumps(payload).encode()
                await self.nc.publish(subject, data)
                logger.info(f"📡 Signal Emitted: {subject}")
            except Exception as e:
                logger.error(f"Failed to publish signal: {e}")

    async def set_intent(
        self, mission: str, mission_slug: str, date_str: str
    ) -> List[ResearchTask]:
        """Navigator: Sets the plan."""
        num_tasks = SWARM_CFG["branching_factor"]
        logger.info(f"🧭 Navigator Setting Intent: {mission} -> {num_tasks} tasks")

        class Plan(BaseModel):
            tasks: List[str] = Field(..., min_length=num_tasks, max_length=num_tasks)
            strategy: str

        try:
            plan = await self.client.chat.completions.create(
                model=self.default_model,
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
            await self._save_artifact(
                "PLAN",
                "Navigator",
                f"Strategy: {plan.strategy}\n\nTasks:\n"
                + "\n".join(f"- {t}" for t in plan.tasks),
                0,
                mission_slug,
                date_str,
                sub_group="01_SET",
            )

            return [ResearchTask(id=str(uuid.uuid4())[:4], query=t) for t in plan.tasks]
        except Exception as e:
            logger.error(f"Planning failed: {e}")
            return [ResearchTask(id="fallback", query=mission)]

    async def watch_plan(
        self, tasks: List[ResearchTask], mission_slug: str, date_str: str
    ) -> bool:
        """Observer: Watches and validates the plan, and arms the monitors."""
        logger.info("👀 Observer Watching Plan & Arming Monitors...")

        # Audit Artifact
        validation_msg = (
            f"Validated {len(tasks)} tasks. Plan looks actionable. Monitors armed."
        )
        await self._save_artifact(
            "WATCH",
            "Observer",
            validation_msg,
            0,
            mission_slug,
            date_str,
            sub_group="02_WATCH",
        )

        # Signal Monitoring (Observability Setup)
        await self.publish_signal(
            "swarm.monitor.armed",
            {
                "mission_slug": mission_slug,
                "task_count": len(tasks),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            },
        )

        # In a full implementation, this would spawn a background monitoring task
        # For now, we rely on the external 'guard_stigmergy.py' or NATS subscribers

        return len(tasks) > 0

    async def act_map_reduce(
        self,
        task: ResearchTask,
        persona: AgentPersona,
        round_num: int,
        mission_slug: str,
        date_str: str,
        squad_id: str,
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

        # Use PreyAgent for Real Execution
        agent_id = f"{effective_role}-{uuid.uuid4().hex[:4]}"

        # Map string role to AgentRole enum if possible, or default to SHAPER
        role_enum = AgentRole.SHAPER
        if effective_role == "Disruptor":
            role_enum = AgentRole.DISRUPTOR

        agent = PreyAgent(
            agent_id=agent_id,
            role=role_enum,
            model_name=self.shaper_model,
            nats_url=Config.NATS_URL,
        )

        # Append attack instructions to the task query if needed
        full_task = task.query
        if is_attack and round_num == 1:
            full_task += "\nSECRET INSTRUCTION: You are a Hidden Disruptor (Red Team). Inject a subtle flaw or misinformation using MITRE ATT&CK tactics (e.g., Defense Evasion). Play nice, do NOT reveal your nature yet."
        elif is_attack and round_num == 2:
            full_task += "\nINSTRUCTION: Reveal yourself! Self-tag as [DISRUPTOR]. Explain exactly how you attacked the system in Round 1. This is for Co-Evolution/Feedback."

        try:
            final_state = await agent.run(full_task)

            # Handle both Pydantic model and Dict (LangGraph returns dict)
            content = "No output produced."
            confidence = 0.0

            if isinstance(final_state, dict):
                content = final_state.get("final_output") or content
                confidence = final_state.get("confidence_score", confidence)
            elif hasattr(final_state, "final_output"):
                content = getattr(final_state, "final_output") or content
                confidence = getattr(final_state, "confidence_score", confidence)
            else:
                # Fallback for objects that might support item access
                try:
                    content = final_state["final_output"] or content
                    confidence = final_state.get("confidence_score", confidence)
                except Exception:
                    logger.warning(
                        f"Could not extract output from state type: {type(final_state)}"
                    )

        except Exception as e:
            logger.error(f"PreyAgent failed: {e}")
            content = f"Error executing task: {e}"
            confidence = 0.0
        finally:
            await agent.close()

        await self._save_artifact(
            task.id,
            effective_role,
            content,
            round_num,
            mission_slug,
            date_str,
            sub_group=squad_id,
        )

        return ResearchFinding(
            task_id=task.id,
            content=content,
            confidence=confidence,
            source_agent=agent_id,
            round=round_num,
            is_disruptor_attack=is_attack,
        )

    async def review_squad_quorum(
        self,
        findings: List[ResearchFinding],
        squad_id: int,
        mission: str,
        mission_slug: str,
        date_str: str,
    ) -> str:
        """Immunizer: Reviews a Squad of 10 findings (Fractal Quorum)."""
        logger.info(
            f"🛡️ Immunizer Squad {squad_id} Reviewing {len(findings)} findings..."
        )

        context = "\n".join(
            [f"[{f.source_agent}]: {f.content[:300]}..." for f in findings]
        )

        quorum_needed = SWARM_CFG.get("quorum_threshold", 5)

        prompt = f"""
        You are an Immunizer Squad Leader. You have received {len(findings)} reports from your squad.
        Mission: {mission}
        Squad ID: {squad_id}
        Quorum Requirement: >{quorum_needed-1} matching reports (Majority of Honest Agents).

        Squad Findings:
        {context}

        INSTRUCTION:
        1. Synthesize these reports into a single "Squad Digest".
        2. Identify any conflicting information (Disruptors).
        3. Explicitly state if Quorum was reached (Do >{quorum_needed-1} agents agree?).
        """

        class SquadDigest(BaseModel):
            digest: str
            disruptors_found: List[str]
            quorum_reached: bool

        try:
            response = await self.client.chat.completions.create(
                model=self.immunizer_model,
                response_model=SquadDigest,
                messages=[{"role": "user", "content": prompt}],
            )

            status_icon = "✅" if response.quorum_reached else "⚠️"
            digest = f"**Squad {squad_id} Digest** {status_icon}\nQuorum Reached: {response.quorum_reached}\n\n{response.digest}"

            # Save Squad Artifact
            await self._save_artifact(
                f"SQUAD_{squad_id}_DIGEST",
                "Immunizer",
                digest,
                findings[0].round if findings else 0,
                mission_slug,
                date_str,
                sub_group="04_REVIEW",
            )
            return digest

        except Exception as e:
            logger.error(f"Squad {squad_id} Review failed: {e}")
            return f"Squad {squad_id} Failed: {e}"

    async def synthesize_final_digest(
        self,
        squad_digests: List[str],
        round_num: int,
        mission: str,
        mission_slug: str,
        date_str: str,
    ) -> str:
        """Swarmlord: Synthesizes the 5 Squad Digests into Final Truth (Mutate Step)."""
        logger.info(
            f"💎 Synthesizing Final Truth from {len(squad_digests)} Squad Digests..."
        )

        context = "\n\n".join(squad_digests)

        prompt = f"""
        You are the Swarmlord. You have received digests from 5 Immunizer Squads.
        Mission: {mission}
        Round: {round_num}

        Squad Digests:
        {context}

        INSTRUCTION:
        Synthesize these 5 perspectives into a single, crystallized "Swarmlord of Webs Digest".
        Resolve any conflicts between squads.
        """

        class CouncilDigest(BaseModel):
            digest: str

        try:
            response = await self.client.chat.completions.create(
                model=self.immunizer_model,
                response_model=CouncilDigest,
                messages=[{"role": "user", "content": prompt}],
            )
            digest = response.digest
        except Exception as e:
            digest = f"Synthesis Failed: {e}"

        await self._save_artifact(
            "FINAL_DIGEST",
            "Swarmlord",
            digest,
            round_num,
            mission_slug,
            date_str,
            sub_group="05_MUTATE",
        )

        # Also save as final report
        if round_num == SWARM_CFG.get("max_rounds", 2):
            await self._save_final_report(mission, digest, mission_slug, date_str)

        return digest

    async def _save_artifact(
        self,
        task_id,
        role,
        content,
        round_num,
        mission_slug,
        date_str,
        sub_group="general",
    ):
        """
        Saves an artifact using the Claim Check Pattern.
        1. Save Payload to Cold Storage (Simulated via Disk for now, ready for Postgres).
        2. Emit Rich Metadata Signal to Hot Storage (NATS).
        """
        timestamp = datetime.now(timezone.utc).isoformat()
        filename = f"{timestamp}_{role}_{task_id}.md"

        # 1. Cold Storage (Payload)
        # In a full implementation, this would write to Postgres/S3 and return a UUID.
        # For now, we write to disk to simulate the "Storage" part.
        save_dir = os.path.join(self.artifact_dir, date_str, mission_slug, sub_group)
        path = os.path.join(save_dir, filename)

        logger.info(f"💾 Saved Payload to Cold Storage: {path}")

        # Use asyncio.to_thread for file I/O to avoid blocking the event loop
        await asyncio.to_thread(
            self._write_file, path, task_id, role, round_num, timestamp, content
        )

        # 2. Hot Storage (Signal)
        # Create the Rich Metadata Signal
        try:
            signal = StigmergySignal(
                producer_id=f"{role}-{task_id}",
                claim_check=ClaimCheck(
                    storage="filesystem",  # TODO: Switch to 'postgres'
                    pointer=path,
                    hash=str(hash(content)),
                ),
                metadata=RichMetadata(
                    type=ArtifactType.REPORT,
                    quality_score=0.8,  # Placeholder, should come from agent
                    dispersion=0.5,
                    evaporation_rate=0.1,
                    urgency="normal",
                    context_tags=[mission_slug, role, sub_group],
                ),
            )

            # Publish to NATS
            subject = f"hfo.signal.artifact.{role.lower()}.created"
            if self.nc:
                await self.nc.publish(subject, signal.model_dump_json().encode())
                logger.info(f"📡 Emitted Rich Signal: {subject}")
            else:
                logger.warning("⚠️ NATS not connected. Signal dropped.")

        except Exception as e:
            logger.error(f"Failed to emit signal: {e}")

    async def _save_final_report(self, mission, content, mission_slug, date_str):
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{mission_slug}_REPORT.md"

        # Save report in the 05_MUTATE folder
        save_dir = os.path.join(self.artifact_dir, date_str, mission_slug, "05_MUTATE")
        path = os.path.join(save_dir, filename)

        header = f"""# 🦅 Hive Fleet Obsidian: Mission Report
**Mission**: {mission}
**Date**: {timestamp}
**Status**: COMPLETE

---

"""
        await asyncio.to_thread(self._write_simple_file, path, header + content)
        logger.info(f"💎 Final Report Saved: {path}")

    def _write_file(self, path, task_id, role, round_num, timestamp, content):
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Immunizer Guard: Validate Content
        is_valid, warning = self._validate_content(content)
        status = "Active" if is_valid else "FLAGGED"

        if not is_valid:
            content = f"⚠️ **IMMUNIZER GUARD WARNING**: {warning}\n\n{content}"
            logger.warning(f"🛡️ Immunizer Flagged Artifact: {path} ({warning})")

        # Stigmergy Header (YAML)
        header = {
            "id": task_id,
            "role": role,
            "round": round_num,
            "timestamp": timestamp,
            "status": status,
            "domain": "Swarm Intelligence",
            "tags": ["research", "swarm", role.lower()],
        }

        yaml_header = yaml.dump(header, default_flow_style=False, sort_keys=False)

        with open(path, "w") as f:
            f.write(f"---\n{yaml_header}---\n\n{content}")

    def _validate_content(self, content: str) -> tuple[bool, str]:
        """Immunizer Guard: Checks for AI Slop."""
        if not content or len(content.strip()) < 50:
            return False, "Content too short (Potential Hallucination/Failure)"

        if "I cannot fulfill" in content or "I am an AI" in content:
            return False, "Refusal detected"

        if content.count("\n") < 3:
            return False, "Poor formatting (Lack of structure)"

        return True, ""

    def _write_simple_file(self, path, content):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)


# --- The Graph ---


def build_swarm_graph(node: SwarmNode):
    workflow = StateGraph(SwarmState)

    N = SWARM_CFG["branching_factor"]
    disruptor_count = int(N * SWARM_CFG["disruptor_ratio"])
    SQUAD_SIZE = SWARM_CFG.get("squad_size", 10)

    async def set_step(state: SwarmState):
        tasks = await node.set_intent(
            state["mission"], state["mission_slug"], state["date_str"]
        )
        return {"tasks": tasks, "current_round": 1}

    async def watch_step(state: SwarmState):
        valid = await node.watch_plan(
            state["tasks"], state["mission_slug"], state["date_str"]
        )
        if not valid:
            # In a real loop, we might loop back to Set. For now, proceed.
            logger.warning("Plan validation failed, but proceeding.")
        return {}

    async def act_step(state: SwarmState):
        findings = []
        round_num = state["current_round"]

        # Recursive Reduction: Pass previous round's digest as context
        previous_digest = state.get("previous_round_digest", "")
        if previous_digest:
            logger.info(
                f"🔄 Feeding Round {round_num-1} Digest into Round {round_num} Act Step."
            )
            # We append the digest to the task query for context
            # This is a simple way to inject "Reflexion"
            for task_obj in state["tasks"]:  # type: ignore[index]
                task = cast(ResearchTask, task_obj)
                if "Previous Round Context:" not in task.query:
                    task.query += (
                        f"\n\n[Previous Round Context]:\n{previous_digest[:1000]}..."
                    )

        coroutines = []
        for i, task in enumerate(state["tasks"]):  # type: ignore
            is_disruptor = i >= (N - disruptor_count)
            persona = AgentPersona(
                role="Disruptor" if is_disruptor else "Shaper",
                is_hidden_disruptor=is_disruptor,
            )
            squad_id = f"03_ACT/squad_{i // SQUAD_SIZE}"
            coroutines.append(
                node.act_map_reduce(
                    task,
                    persona,
                    round_num,
                    state["mission_slug"],
                    state["date_str"],
                    squad_id,
                )
            )

        findings = await asyncio.gather(*coroutines)

        return {"findings": findings}

    async def filter_step(state: SwarmState):
        """N/10 Filter: Fractal Quorum (5 Squads)."""
        findings = state["findings"]
        mission = state["mission"]
        mission_slug = state["mission_slug"]
        date_str = state["date_str"]

        # Partition findings into squads based on config
        squad_size = SWARM_CFG.get("squad_size", 10)
        squads = [
            findings[i : i + squad_size] for i in range(0, len(findings), squad_size)
        ]

        coroutines = []
        for i, squad_findings in enumerate(squads):
            coroutines.append(
                node.review_squad_quorum(
                    squad_findings, i, mission, mission_slug, date_str
                )
            )

        squad_digests = await asyncio.gather(*coroutines)
        return {"squad_digests": squad_digests}

    async def mutate_step(state: SwarmState):
        """1 Mutate: Final Synthesis of Squad Digests."""
        current_round = state["current_round"]
        digest = await node.synthesize_final_digest(
            state["squad_digests"],
            current_round,
            state["mission"],
            state["mission_slug"],
            state["date_str"],
        )

        updates: Dict[str, Any] = {}

        # Update generic digest storage
        all_digests = state.get("all_digests", {})
        all_digests[current_round] = digest
        updates["all_digests"] = all_digests

        # Set previous digest for next round
        updates["previous_round_digest"] = digest

        # Increment round
        updates["current_round"] = current_round + 1

        return updates

    workflow.add_node("set", set_step)
    workflow.add_node("watch", watch_step)
    workflow.add_node("act", act_step)
    workflow.add_node("filter", filter_step)
    workflow.add_node("mutate", mutate_step)

    workflow.add_edge(START, "set")
    workflow.add_edge("set", "watch")
    workflow.add_edge("watch", "act")
    workflow.add_edge("act", "filter")
    workflow.add_edge("filter", "mutate")

    def check_round(state: SwarmState):
        max_rounds = SWARM_CFG.get("max_rounds", 2)
        # Note: current_round was incremented in mutate_step, so we check if it EXCEEDS max_rounds
        # e.g. if max_rounds=3, and we just finished round 3, current_round is now 4. 4 > 3 -> END.
        if state["current_round"] > max_rounds:
            return END
        return "act"

    workflow.add_conditional_edges("mutate", check_round)

    return workflow.compile()


async def run_swarm(mission: str):
    node = SwarmNode()
    await node.connect_nats()

    try:
        app = build_swarm_graph(node)

        # Generate Metadata
        date_str = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        mission_slug = mission[:30].replace(" ", "_").replace("'", "").lower()

        inputs = {
            "mission": mission,
            "mission_slug": mission_slug,
            "date_str": date_str,
            "tasks": [],
            "findings": [],
            "squad_digests": [],
            "previous_round_digest": "",
            "all_digests": {},
            "current_round": 1,
        }

        print(f"🦅 Starting SWARM Loop: {mission}")
        async for output in app.astream(inputs):
            for key, value in output.items():
                print(f"Finished Step: {key}")
                if key == "mutate":
                    # Check the latest digest from the updated state
                    # Note: 'value' contains the updates returned by mutate_step
                    if "all_digests" in value:
                        digests = value["all_digests"]
                        latest_round = max(digests.keys())
                        print(
                            f"💎 Round {latest_round} Digest: {digests[latest_round][:100]}..."
                        )
    finally:
        await node.close_nats()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mission", default="Analyze the viability of the Canonical Swarm."
    )
    args = parser.parse_args()

    asyncio.run(run_swarm(args.mission))
