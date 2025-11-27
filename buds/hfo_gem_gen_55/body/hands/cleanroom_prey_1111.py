"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: cleanroom-prey-1111-impl
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.8
    decay: 0.1
    created: '2025-11-26T12:00:00Z'
    generation: 55
  topos:
    address: buds/hfo_gem_gen_55/body/hands/cleanroom_prey_1111.py
    links: []
  telos:
    viral_factor: 0.0
    meme: cleanroom_prey_1111.py
"""

import asyncio
import logging
import uuid
import time
import os
import sys
import json
import hashlib

# Add project root to sys.path to allow importing 'body'
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "../../../../"))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from typing import List, Optional, Dict, Any, Literal
from collections import deque
from pydantic import BaseModel, Field, BeforeValidator
from typing import List, Optional, Dict, Any, Annotated
from body.hfo_sdk.stigmergy import StigmergyClient
import instructor
from openai import AsyncOpenAI

# Setup Logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("CleanroomPrey")

from datetime import datetime, timedelta, timezone

# --- Constants ---
OLLAMA_BASE_URL = "http://localhost:11434/v1"
MODEL_NAME = (
    "gemma3:270m"  # Using a slightly larger model for logic if available, else fallback
)
API_KEY = "ollama"
MANTRA = """I am the Node, the Earth, the Seed,
Swarmlord of Webs is the one I heed.
From Karmic Web, where Wisdom flows,
To Swarm Web, where the Willpower grows.
In Simulation Web, I Weave the state,
Obsidian Hourglass, the Engine of Fate.
A Prescient Path in State-Action Space,
One Mind, One Swarm, in time and place."""
MANTRA_HASH = hashlib.sha256(MANTRA.encode("utf-8")).hexdigest()

# 🧪 TEST CONFIGURATION
MOCK_MODE = False  # Set to True to bypass LLM for frequency testing


# --- Tools ---
class ToolSet:
    @staticmethod
    def list_dir(path: str) -> str:
        try:
            return str(os.listdir(path))
        except Exception as e:
            return f"Error: {e}"

    @staticmethod
    def read_file(path: str) -> str:
        try:
            with open(path, "r") as f:
                return f.read()[:2000]  # Truncate for context window
        except Exception as e:
            return f"Error: {e}"


def stringify_content(v: Any) -> str:
    if isinstance(v, dict) or isinstance(v, list):
        return json.dumps(v)
    return str(v)


def handle_list(v: Any) -> List[str]:
    if isinstance(v, str):
        return [v]
    if v is None:
        return []
    return v


def handle_float(v: Any) -> float:
    if isinstance(v, dict):
        return 0.5
    if v is None:
        return 0.5
    try:
        return float(v)
    except:
        return 0.5


# --- Stigmergy Models ---


class StigmergyPillars(BaseModel):
    ontos: Dict[str, Any] = Field(..., description="Being/Essence")
    chronos: Dict[str, Any] = Field(..., description="Time/Thermodynamics")
    topos: Dict[str, Any] = Field(..., description="Space/Location")
    telos: Dict[str, Any] = Field(..., description="Purpose/Goal")
    logos: Dict[str, Any] = Field(..., description="Logic/Protocol")
    pathos: Dict[str, Any] = Field(..., description="Emotion/Signal")
    ethos: Dict[str, Any] = Field(..., description="Ethics/Trust")
    techne: Dict[str, Any] = Field(..., description="Craft/Stack")


class HeartbeatSignal(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str
    phase: str  # Perceive, React, Execute, Yield
    pillars: StigmergyPillars
    content: str
    mantra_hash: str = Field(
        ..., description="SHA-256 hash of the HFO Gen 55 Mantra for integrity"
    )
    previous_signal_id: Optional[str] = Field(
        None, description="Chain link to previous heartbeat"
    )
    delta_seconds: float = Field(
        0.0, description="Time elapsed since previous heartbeat"
    )


# --- Pydantic Models (The DNA) ---


class PerceptionReport(BaseModel):
    loop_id: Optional[int] = None
    context_summary: Optional[str] = Field(default="No summary provided.")
    detected_artifacts: Optional[List[str]] = Field(default_factory=list)
    environment_scan: Optional[str] = Field(
        default="Scanning...", description="What do I see in the repo?"
    )
    cynefin_state: Literal[
        "Clear", "Complicated", "Complex", "Chaotic", "Confused"
    ] = Field(default="Clear", description="Cynefin Framework State")
    alert_level: Optional[str] = Field(
        default="Green", description="Green, Yellow, Red"
    )


class ReactionPlan(BaseModel):
    loop_id: Optional[int] = None
    intent: str = Field(default="Execute Mission")
    tool_calls: List[Dict[str, Any]] = Field(
        default_factory=list, description="List of {tool: name, args: dict}"
    )
    reasoning: str = Field(default="No reasoning provided.")


class ExecutionResult(BaseModel):
    loop_id: int
    status: str
    output: str
    tool_outputs: List[str]


class YieldArtifact(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    loop_id: Optional[int] = None
    content: Annotated[str, BeforeValidator(stringify_content)] = Field(
        default="", description="The synthesized output/summary of the loop."
    )
    parent_artifacts: Annotated[
        Optional[List[str]], BeforeValidator(handle_list)
    ] = Field(default_factory=list)
    timestamp: Annotated[Optional[float], BeforeValidator(handle_float)] = Field(
        default_factory=time.time
    )
    reflexion_score: Annotated[Optional[float], BeforeValidator(handle_float)] = Field(
        default=0.5, description="Self-audit score 0.0-1.0"
    )


# --- The Agent ---


class PreyAgent:
    def __init__(self, agent_id: str, stigmergy: StigmergyClient, mission: str):
        self.agent_id = agent_id
        self.stigmergy = stigmergy
        self.mission = mission
        self.memory: List[YieldArtifact] = []
        self.signal_buffer: deque = deque(
            maxlen=20
        )  # Short-Term Sensory Store (5 mins)
        self.current_cynefin_state = "Clear"
        self.client = instructor.patch(
            AsyncOpenAI(base_url=OLLAMA_BASE_URL, api_key=API_KEY),
            mode=instructor.Mode.JSON,
        )
        self.tools = ToolSet()

    def get_mountain_time(self) -> str:
        # Mountain Time (US) is UTC-7
        tz = timezone(timedelta(hours=-7))
        return datetime.now(tz).isoformat()

    def generate_pillars(self, phase: str) -> StigmergyPillars:
        return StigmergyPillars(
            ontos={
                "id": self.agent_id,
                "type": "agent",
                "owner": "Swarmlord",
                "generation": "55",
            },
            chronos={
                "status": "active",
                "urgency": 0.5,
                "decay": 0.1,
                "created": self.get_mountain_time(),
                "repo_gen": "52",
                "bud_gen": "55",
            },
            topos={
                "address": "buds/hfo_gem_gen_55/body/hands/cleanroom_prey_1111.py",
                "links": [],
            },
            telos={
                "viral_factor": 0.8,
                "meme": "stigmergy_heartbeat",
                "mission": self.mission,
            },
            logos={"protocol": "PREY", "format": "json", "phase": phase},
            pathos={"stress_level": 0.1, "validation": "self-audit"},
            ethos={"security_level": "high", "compliance": ["cleanroom"]},
            techne={
                "stack": ["python", "pydantic", "nats", "ollama"],
                "complexity": self.current_cynefin_state,
            },
        )

    async def emit_heartbeat(self, phase: str, content: str):
        pillars = self.generate_pillars(phase)
        # Append Mantra to content
        full_content = f"{MANTRA} | {content}"

        # Calculate Delta and Link to Previous Heartbeat
        now = datetime.fromisoformat(self.get_mountain_time())
        delta = 0.0
        prev_id = None

        if self.signal_buffer:
            last_sig = self.signal_buffer[-1]
            prev_id = last_sig.id
            try:
                last_time = datetime.fromisoformat(last_sig.timestamp)
                delta = (now - last_time).total_seconds()
            except Exception as e:
                logger.warning(f"Time calc error: {e}")
                delta = -1.0

        # Anomaly Detection (Simple Gap Check)
        if delta > 120:  # Warning if gap > 2 mins (even in resting state)
            logger.warning(f"💔 Heartbeat Gap Detected: {delta:.2f}s")

        signal = HeartbeatSignal(
            timestamp=self.get_mountain_time(),
            phase=phase,
            pillars=pillars,
            content=full_content,
            mantra_hash=MANTRA_HASH,
            previous_signal_id=prev_id,
            delta_seconds=delta,
        )

        # Update Local Buffer (Awareness)
        self.signal_buffer.append(signal)

        # Publish to NATS
        subject = f"hfo.heartbeat.{self.agent_id}.{phase.lower()}"
        try:
            await self.stigmergy.publish(subject, signal.model_dump())
            logger.info(
                f"💓 Heartbeat [{phase}]: {content[:50]}... (Delta: {delta:.2f}s)"
            )
        except Exception as e:
            logger.error(f"Failed to publish heartbeat: {e}")

    async def perceive(self, loop_id: int) -> PerceptionReport:
        logger.info(f"[{self.agent_id}] Loop {loop_id}: Perceiving...")

        if MOCK_MODE:
            # Mock Response
            response = PerceptionReport(
                loop_id=loop_id,
                environment_scan="Mock Scan",
                cynefin_state=self.current_cynefin_state,  # Keep state consistent
                alert_level="Green",
            )
            await self.emit_heartbeat(
                "Perceive",
                f"{response.environment_scan} (Alert: {response.alert_level})",
            )
            return response

        # Build Context from Memory & Signal Buffer
        context = f"Mission: {self.mission}\nLoop {loop_id} Start."
        artifacts = []
        if self.memory:
            last_artifact = self.memory[-1]
            context += f"\nPrevious Output: {last_artifact.content}"
            if last_artifact.id:
                artifacts.append(last_artifact.id)

        # Build Signal History (Awareness)
        history_summary = "Signal History (Last 5 mins):\n"
        if self.signal_buffer:
            for sig in list(self.signal_buffer)[
                -5:
            ]:  # Just show last 5 for prompt conciseness
                history_summary += f"- [{sig.timestamp}] {sig.phase}: {sig.content[:30]}... (Cynefin: {sig.pillars.techne.get('complexity', 'Unknown')})\n"
        else:
            history_summary += "No history yet."

        # Real LLM Call
        try:
            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                response_model=PerceptionReport,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an Observer Agent. Scan the environment and signal history. Classify the Cynefin state (Clear, Complicated, Complex, Chaotic, Confused) and Alert Level.",
                    },
                    {
                        "role": "user",
                        "content": f"Context: {context}\n\n{history_summary}\n\nWhat is the state of the mission and the system?",
                    },
                ],
                max_retries=3,
            )
            # Inject loop_id and artifacts since LLM might hallucinate them
            response.loop_id = loop_id
            response.detected_artifacts = artifacts

            # Update Internal State
            if response.cynefin_state:
                self.current_cynefin_state = response.cynefin_state

            # Emit Heartbeat
            await self.emit_heartbeat(
                "Perceive",
                f"{response.environment_scan} (Alert: {response.alert_level})",
            )

            return response
        except Exception as e:
            logger.error(f"Perception Failed: {e}")
            return PerceptionReport(
                loop_id=loop_id,
                context_summary="Error",
                detected_artifacts=artifacts,
                environment_scan="Error",
            )

    async def react(self, perception: PerceptionReport) -> ReactionPlan:
        logger.info(f"[{self.agent_id}] Loop {perception.loop_id}: Reacting...")

        try:
            response = await self.client.chat.completions.create(
                model=MODEL_NAME,
                response_model=ReactionPlan,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a Planner Agent. Available tools: list_dir(path), read_file(path). Return tool_calls as list of dicts like {'tool': 'list_dir', 'args': {'path': '.'}}.",
                    },
                    {
                        "role": "user",
                        "content": f"Perception: {perception.environment_scan}. Context: {perception.context_summary}. Plan the next step.",
                    },
                ],
                max_retries=3,
            )
            response.loop_id = perception.loop_id

            # Emit Heartbeat
            await self.emit_heartbeat("React", response.intent)

            return response
        except Exception as e:
            logger.error(f"Reaction Failed: {e}")
            return ReactionPlan(
                loop_id=perception.loop_id,
                intent="Error",
                tool_calls=[],
                reasoning=str(e),
            )

    async def execute(self, plan: ReactionPlan) -> ExecutionResult:
        logger.info(f"[{self.agent_id}] Loop {plan.loop_id}: Executing...")

        tool_outputs = []
        for call in plan.tool_calls:
            tool_name = call.get("tool")
            args = call.get("args")  # Now a dict
            try:
                if isinstance(args, str):
                    args = json.loads(args)

                if tool_name == "list_dir":
                    output = self.tools.list_dir(args.get("path", "."))
                elif tool_name == "read_file":
                    output = self.tools.read_file(args.get("path"))
                else:
                    output = f"Unknown tool: {tool_name}"
            except Exception as e:
                output = f"Tool Execution Failed: {e}"

            tool_outputs.append(f"Tool: {tool_name}, Output: {output}")
            logger.info(f"  -> Executed {tool_name}: {output[:50]}...")

        result = ExecutionResult(
            loop_id=plan.loop_id if plan.loop_id else 0,
            status="success",
            output="\n".join(tool_outputs),
            tool_outputs=tool_outputs,
        )

        # Emit Heartbeat
        await self.emit_heartbeat("Execute", f"Executed {len(tool_outputs)} tools")

        return result

    async def yield_phase(
        self, result: ExecutionResult, perception: PerceptionReport
    ) -> YieldArtifact:
        logger.info(f"[{self.agent_id}] Loop {result.loop_id}: Yielding...")

        # Self-Audit (Reflexion) via LLM
        try:
            audit = await self.client.chat.completions.create(
                model=MODEL_NAME,
                response_model=YieldArtifact,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an Assimilator Agent. Audit the execution result against the mission. Score it 0.0-1.0. Synthesize the result into the 'content' field.",
                    },
                    {
                        "role": "user",
                        "content": f"Mission: {self.mission}. Result: {result.output}. Synthesize the findings and fill the 'content' field with a summary.",
                    },
                ],
                max_retries=3,
            )

            # Enforce structure
            audit.loop_id = result.loop_id
            audit.parent_artifacts = perception.detected_artifacts

            logger.info(f"  -> Self-Audit Score: {audit.reflexion_score}")

            # Publish to NATS (Hot Stigmergy)
            # We use emit_heartbeat for the Yield phase too, but also keep the original publish if needed.
            # The user asked for "stigmergy heartbeat", so emit_heartbeat covers it.
            await self.emit_heartbeat("Yield", audit.content)

            # Update local memory (Short-term episodic)
            self.memory.append(audit)

            return audit
        except Exception as e:
            logger.error(f"Yield Failed: {e}")
            return YieldArtifact(
                loop_id=result.loop_id, content="Error in Yield", reflexion_score=0.0
            )

    async def run_loop(self, loop_id: int):
        # Anytime Robustness: Retry logic could be wrapped here
        try:
            perception = await self.perceive(loop_id)
            reaction = await self.react(perception)
            execution = await self.execute(reaction)
            artifact = await self.yield_phase(execution, perception)
            logger.info(
                f"[{self.agent_id}] Loop {loop_id} Complete. Artifact: {artifact.id}"
            )
            return artifact
        except Exception as e:
            logger.error(f"[{self.agent_id}] Loop {loop_id} Failed: {e}")
            # Don't raise, just log, so the loop continues
            pass


# --- Runner ---


async def run_agent_lifecycle(agent_id: str, stigmergy: StigmergyClient, mission: str):
    agent = PreyAgent(agent_id=agent_id, stigmergy=stigmergy, mission=mission)
    loop_count = 1
    logger.info(f"[{agent_id}] Starting Lifecycle...")

    while True:
        start_time = time.time()

        # Run the loop
        await agent.run_loop(loop_count)

        # Variable Frequency Logic based on Cynefin State
        cynefin = agent.current_cynefin_state
        if cynefin == "Chaotic":
            target_interval = 5
        elif cynefin == "Complex":
            target_interval = 15
        else:
            # Clear, Complicated, Confused -> 1 minute
            target_interval = 60

        elapsed = time.time() - start_time
        sleep_time = max(0, target_interval - elapsed)

        logger.info(
            f"[{agent_id}] Loop {loop_count} ({cynefin}) finished in {elapsed:.2f}s. Sleeping {sleep_time:.2f}s..."
        )
        await asyncio.sleep(sleep_time)
        loop_count += 1


async def main():
    # Ensure NATS URL is available
    if not os.getenv("NATS_URL"):
        os.environ["NATS_URL"] = "nats://localhost:4225"  # Default fallback

    stigmergy = StigmergyClient()
    try:
        await stigmergy.connect()
    except Exception as e:
        logger.warning(
            f"Could not connect to NATS: {e}. Proceeding in offline mode (local memory only)."
        )

    mission = "Explore the repository, maintain the heartbeat, and validate HFO state."

    # Create 8 Agents (Octarchy)
    tasks = []
    for i in range(8):
        agent_id = f"cleanroom_agent_{i+1}"
        tasks.append(run_agent_lifecycle(agent_id, stigmergy, mission))

    logger.info("🦅 HFO Heartbeat Swarm: Launching 8 Concurrent Agents (Octarchy)...")
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
