import os
import operator
import logging
import uuid
import datetime
import asyncio
from typing import Annotated, List, TypedDict, Optional, Dict, Any
from pydantic import BaseModel, Field
import instructor
from openai import OpenAI
from langgraph.graph import StateGraph, END, START
from langgraph.types import Send
from dotenv import load_dotenv
from body.hands.tools import ToolSet

"""
🦅 Hive Fleet Obsidian: Hydra Swarm
Intent: Implements the LangGraph-based Scatter-Gather workflow.
Linked to: brain/infrastructure_hydra.feature
"""

# 1. Setup & Config
load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger("hydra")

# Ray Suspended per User Request (2025-11-21)
# Reverting to AsyncIO for stability.


DIGESTION_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "digestion")
os.makedirs(DIGESTION_DIR, exist_ok=True)


def save_artifact(
    mission_id: str,
    agent_role: str,
    step_type: str,
    content: str,
    metadata: dict,
    output_dir: str = DIGESTION_DIR,
):
    """Saves a Stigmergy Artifact with YAML frontmatter."""
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.datetime.utcnow().isoformat()
    filename = (
        f"{timestamp.replace(':', '-')}_{step_type}_{agent_role.replace(' ', '_')}.md"
    )
    filepath = os.path.join(output_dir, filename)

    yaml_header = f"""---
mission_id: {mission_id}
timestamp: {timestamp}
agent_role: {agent_role}
step_type: {step_type}
model: {metadata.get('model', 'unknown')}
confidence: {metadata.get('confidence', 'N/A')}
---
"""
    with open(filepath, "w") as f:
        f.write(yaml_header + "\n" + content)

    logger.info(f"   📄 Artifact dropped: {filename}")
    return filepath


# --- DNA (Pydantic Models) ---


class SubTask(BaseModel):
    id: int
    description: str = Field(..., description="The specific sub-task to execute")
    assigned_role: str = Field(..., description="The role best suited for this task")
    mission_id: Optional[str] = None  # Added for context passing


class ReactionObject(BaseModel):
    thought_process: str = Field(..., description="Reasoning behind the action")
    tool_name: Optional[str] = Field(
        None, description="Name of the tool to use (read_file, write_file, search_web)"
    )
    tool_args: Optional[Dict[str, Any]] = Field(
        None, description="Arguments for the tool as a dictionary"
    )
    final_answer: Optional[str] = Field(
        None, description="Direct answer if no tool is needed"
    )


class Plan(BaseModel):
    tasks: List[SubTask] = Field(
        ..., description="List of sub-tasks to execute in parallel"
    )


class TaskResult(BaseModel):
    task_id: int
    output: str = Field(..., description="The result of the task")
    confidence: float = Field(..., description="Confidence score 0.0-1.0")
    is_valid: bool = Field(
        default=True, description="Whether this result passed the filter"
    )
    agent_id: Optional[str] = Field(None, description="The ID/Role of the agent")
    artifacts: List[str] = Field(
        default_factory=list, description="List of file paths created"
    )


class FinalSynthesis(BaseModel):
    summary: str
    consensus_score: float


# --- State Definition ---


class HydraState(TypedDict):
    mission_id: str
    mission: str
    plan: List[SubTask]
    # We use a reducer to collect results from parallel execution
    results: Annotated[List[TaskResult], operator.add]
    final_output: Optional[FinalSynthesis]


# --- The Agents (Nodes) ---


class PreyAgent:
    """
    Implements the Level 0 PREY Loop:
    - Perceive: Ingest context/task.
    - React: Plan/Decide (Select Tool).
    - Execute: Act (Run Tool).
    - Yield: Return.
    """

    def __init__(self, role: str, mission_id: str, output_dir: Optional[str] = None):
        self.role = role
        self.mission_id = mission_id
        self.client = get_client()
        self.output_dir = output_dir or DIGESTION_DIR

    def run_loop(self, task: SubTask) -> TaskResult:
        # 1. Perceive
        context = self._perceive(task)

        # 2. React
        reaction = self._react(context)

        # 3. Execute
        result = self._execute(reaction)

        # 4. Yield
        return self._yield(task.id, result)

    def _perceive(self, task: SubTask) -> str:
        logger.info(f"   👁️  {self.role}: Perceiving Task {task.id}...")
        # In future, this would read files or query memory
        return f"Task Description: {task.description}\nRole: {self.role}"

    def _react(self, context: str) -> ReactionObject:
        logger.info(f"   🧠 {self.role}: Reacting/Planning...")

        return self.client.chat.completions.create(
            model="x-ai/grok-4.1-fast",
            response_model=ReactionObject,
            messages=[
                {
                    "role": "system",
                    "content": f"""You are a {self.role}. Analyze the task and decide on an action.
                    Available Tools:
                    - read_file(file_path): Read content of a file.
                    - write_file(file_path, content): Write content to a file.
                    - search_web(query): Search the internet.

                    If you need to use a tool, specify tool_name and tool_args.
                    If you can answer directly, provide final_answer.
                    """,
                },
                {"role": "user", "content": context},
            ],
        )

    def _execute(self, reaction: ReactionObject) -> TaskResult:
        logger.info(f"   ⚡ {self.role}: Executing...")

        output = ""
        if reaction.tool_name:
            logger.info(
                f"      🛠️ Tool Call: {reaction.tool_name}({reaction.tool_args})"
            )

            # Ensure args is a dict (handle None case)
            args = reaction.tool_args or {}

            if reaction.tool_name == "read_file":
                file_path = args.get("file_path")
                if file_path:
                    output = ToolSet.read_file(file_path)
                else:
                    output = "Error: read_file requires 'file_path' argument"

            elif reaction.tool_name == "write_file":
                file_path = args.get("file_path")
                content = args.get("content")
                if file_path and content:
                    output = ToolSet.write_file(file_path, content)
                else:
                    output = (
                        "Error: write_file requires 'file_path' and 'content' arguments"
                    )

            elif reaction.tool_name == "search_web":
                query = args.get("query")
                if query:
                    output = ToolSet.search_web(query)
                else:
                    output = "Error: search_web requires 'query' argument"
            else:
                output = f"Error: Unknown tool {reaction.tool_name}"
        else:
            output = reaction.final_answer or "No action taken."

        # Wrap in TaskResult
        return TaskResult(
            task_id=0,  # Will be set in yield
            output=output,
            confidence=0.9,  # Mock confidence
            is_valid=True,
        )

    def _yield(self, task_id: int, result: TaskResult) -> TaskResult:
        logger.info(f"   ✅ {self.role}: Yielding Result...")
        result.task_id = task_id
        result.agent_id = self.role

        # Save Artifact (Stigmergy)
        artifact_path = save_artifact(
            mission_id=self.mission_id,
            agent_role=self.role,
            step_type="execution",
            content=result.output,
            metadata={"confidence": result.confidence, "model": "x-ai/grok-4.1-fast"},
            output_dir=self.output_dir,
        )
        result.artifacts.append(artifact_path)
        return result


class MockClient:
    def create(self, response_model, messages, **kwargs):
        if response_model == Plan:
            return Plan(
                tasks=[
                    SubTask(
                        id=1, description="Analyze sector A", assigned_role="Analyst"
                    ),
                    SubTask(
                        id=2, description="Analyze sector B", assigned_role="Analyst"
                    ),
                ]
            )
        elif response_model == TaskResult:
            return TaskResult(
                task_id=0, output="Mock Data", confidence=0.9, is_valid=True
            )
        elif response_model == FinalSynthesis:
            return FinalSynthesis(summary="Mock Consensus", consensus_score=0.99)

    @property
    def chat(self):
        return self

    @property
    def completions(self):
        return self


def get_client():
    api_key = os.getenv("OPENROUTER_API_KEY")
    base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")

    if not api_key:
        logger.warning("⚠️  OPENROUTER_API_KEY not set. Using Mock Client.")
        return MockClient()

    return instructor.from_openai(
        OpenAI(base_url=base_url, api_key=api_key), mode=instructor.Mode.JSON
    )


# 1. Orchestrator (Planner)
def planner_node(state: HydraState):
    logger.info(f"🧠 Brain: Planning mission '{state['mission']}'...")
    client = get_client()

    # Using a cheap/fast model for planning
    plan = client.chat.completions.create(
        model="x-ai/grok-4.1-fast",
        response_model=Plan,
        messages=[
            {
                "role": "system",
                "content": "You are the Swarmlord. Break the mission into 2-4 distinct, parallelizable subtasks.",
            },
            {"role": "user", "content": state["mission"]},
        ],
    )

    # Inject mission_id into tasks
    for task in plan.tasks:
        task.mission_id = state.get("mission_id", "unknown")

    logger.info(f"   📋 Plan: Generated {len(plan.tasks)} tasks.")
    return {"plan": plan.tasks}


# 2. Map (Worker)
async def worker_task(task_data: dict) -> dict:
    """
    Async worker logic (Replaces Ray Actor).
    """
    # Reconstruct SubTask from dict
    task = SubTask(**task_data)

    mission_id = task.mission_id or "unknown_in_map"
    # Instantiate agent
    agent = PreyAgent(role=task.assigned_role, mission_id=mission_id)

    # Run loop (blocking call wrapped in async if needed, but run_loop is sync here)
    # To make it truly async, we should make run_loop async or run in executor.
    # For now, we run it directly as this is a demo of structure.
    # In production, use asyncio.to_thread for blocking I/O.
    result = await asyncio.to_thread(agent.run_loop, task)

    # Return as dict for serialization
    return {"results": [result]}


async def worker_node(state: SubTask):
    # Note: Receives a single SubTask but we need mission_id context.
    # LangGraph map passes the item. To pass context, we'd need a wrapper or rely on the item having it.
    # For simplicity in this demo, we'll assume the SubTask *is* the state passed here,
    # but we can't easily access the global state mission_id without passing it in the map.
    # Let's hack it: The planner should inject mission_id into SubTask if we want it here.
    # Or we just use a placeholder if missing.

    # Offload to AsyncIO (No Ray)
    result_dict = await worker_task(state.model_dump())

    # Return the result
    return result_dict


# 3. Reduce (Synthesizer) with Filter Logic
def synthesizer_node(state: HydraState):
    # Filter logic included here for simplicity of the graph
    valid_results = [r for r in state["results"] if r.confidence >= 0.5]
    logger.info(
        f"   ⚡ Nerves: Synthesizing {len(valid_results)} valid results (Filtered from {len(state['results'])})"
    )

    if not valid_results:
        return {
            "final_output": FinalSynthesis(
                summary="Mission Failed: No valid results.", consensus_score=0.0
            )
        }

    client = get_client()
    synthesis = client.chat.completions.create(
        model="x-ai/grok-4.1-fast",  # High context window
        response_model=FinalSynthesis,
        messages=[
            {
                "role": "system",
                "content": "Synthesize these task results into a cohesive final report.",
            },
            {"role": "user", "content": str([r.model_dump() for r in valid_results])},
        ],
    )

    save_artifact(
        mission_id=state.get("mission_id", "unknown"),
        agent_role="Synthesizer",
        step_type="synthesis",
        content=synthesis.summary,
        metadata={
            "confidence": synthesis.consensus_score,
            "model": "x-ai/grok-4.1-fast",
        },
    )

    return {"final_output": synthesis}


# --- Graph Construction ---


def map_tasks(state: HydraState):
    return [Send("worker", task) for task in state["plan"]]


def build_hydra_graph():
    workflow = StateGraph(HydraState)

    workflow.add_node("planner", planner_node)
    workflow.add_node("worker", worker_node)
    workflow.add_node("synthesizer", synthesizer_node)

    workflow.add_edge(START, "planner")
    workflow.add_conditional_edges("planner", map_tasks, ["worker"])
    workflow.add_edge("worker", "synthesizer")  # Gather
    workflow.add_edge("synthesizer", END)

    return workflow.compile()


if __name__ == "__main__":
    app = build_hydra_graph()
    print("🦅 Hydra Swarm Activated.")

    mission_id = str(uuid.uuid4())
    print(f"🆔 Mission ID: {mission_id}")

    result = app.invoke(
        {
            "mission_id": mission_id,
            "mission": "Identify 3 key trends in AI Agent orchestration for late 2025",
            "results": [],
        }
    )

    if result["final_output"]:
        print(f"\n🏁 Consensus ({result['final_output'].consensus_score}):")
        print(result["final_output"].summary)
        print(f"\n📄 Artifacts saved to: {DIGESTION_DIR}")
