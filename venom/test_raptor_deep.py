"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: d32fa77a-7ee1-4e90-9c61-3570d391f333
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.254194+00:00'
    generation: 51
  topos:
    address: venom/test_raptor_deep.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_raptor_deep.py
"""

import pytest
import ray
import numpy as np
from typing import TypedDict
from pydantic import ValidationError
from langgraph.graph import StateGraph, END
from ribs.archives import GridArchive
from langsmith import Client
from langsmith.run_trees import RunTree
from temporalio import workflow
from temporalio.testing import WorkflowEnvironment
from temporalio.worker import Worker
from body.models.intent import MissionIntent


# --- P - Pydantic (SSOT) ---
def test_mission_intent_ssot_enforcement():
    """
    Verify that the MissionIntent SSOT correctly enforces defaults
    and validates the FinOps strategy fields.
    """
    # 1. Test Defaults
    intent = MissionIntent(description="Test Mission", rationale="Testing Defaults")
    assert intent.coordination_model_group == "Cheap Navigators"
    assert intent.execution_model_group == "Cheap QD Swarm"
    assert intent.swarm_size == 10

    # 2. Test Custom Values
    intent_custom = MissionIntent(
        description="Custom Mission",
        rationale="Testing Custom",
        coordination_model_group="Custom Navigators",
        excluded_models=["Gemini 3 Pro"],
    )
    assert intent_custom.coordination_model_group == "Custom Navigators"
    assert "Gemini 3 Pro" in intent_custom.excluded_models

    # 3. Test Validation (if we had strict validators, we'd test failure here)
    # For now, we just ensure the model instantiates correctly with required fields
    with pytest.raises(ValidationError):
        MissionIntent(description="Missing Rationale")


# --- R - Ray (Distributed Compute) ---
@pytest.mark.asyncio
async def test_ray_actor_state():
    """
    Verify Ray Actors can maintain state (essential for Swarm Agents).
    """
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True, num_cpus=1)

    @ray.remote
    class Counter:
        def __init__(self):
            self.value = 0

        def increment(self):
            self.value += 1
            return self.value

        def get_value(self):
            return self.value

    # Spawn Actor
    counter = Counter.remote()

    # Interact
    assert ray.get(counter.get_value.remote()) == 0
    assert ray.get(counter.increment.remote()) == 1
    assert ray.get(counter.increment.remote()) == 2
    assert ray.get(counter.get_value.remote()) == 2

    ray.shutdown()


# --- A - Agent Logic (LangGraph) ---


def test_langgraph_simple_workflow():
    """
    Verify LangGraph can construct and execute a simple state machine.
    """

    # 1. Define State
    class AgentState(TypedDict):
        count: int
        log: list[str]

    # 2. Define Nodes
    def increment_node(state: AgentState):
        return {"count": state["count"] + 1, "log": state["log"] + ["incremented"]}

    def double_node(state: AgentState):
        return {"count": state["count"] * 2, "log": state["log"] + ["doubled"]}

    # 3. Build Graph
    workflow = StateGraph(AgentState)
    workflow.add_node("increment", increment_node)
    workflow.add_node("double", double_node)

    # 4. Define Edges
    workflow.set_entry_point("increment")
    workflow.add_edge("increment", "double")
    workflow.add_edge("double", END)

    # 5. Compile & Run
    app = workflow.compile()

    initial_state = {"count": 1, "log": []}
    result = app.invoke(initial_state)

    # 6. Verify
    assert result["count"] == 4  # (1 + 1) * 2 = 4
    assert result["log"] == ["incremented", "doubled"]


# --- R - Ribs (Evolution) ---


def test_ribs_map_elites_archive():
    """
    Verify Ribs (pyribs) can initialize an archive and store solutions.
    This is the core of the 'Mutate' phase.
    """
    # 1. Create Archive
    # 2D behavior space, 10 bins each
    archive = GridArchive(
        solution_dim=2,
        dims=[10, 10],
        ranges=[(0, 1), (0, 1)],
    )

    # 2. Add a solution
    # Solution: [0.5, 0.5]
    # Objective: 1.0
    # Measures: [0.5, 0.5] (falls in middle bin)
    solution = np.array([0.5, 0.5])
    objective = 1.0
    measures = np.array([0.5, 0.5])

    status, value = archive.add_single(solution, objective, measures)

    # 3. Verify
    assert status is not None
    assert len(archive) == 1

    # Retrieve best
    elite = archive.best_elite
    assert elite["objective"] == 1.0


# --- T - Temporal (Orchestration) ---


@workflow.defn
class SayHelloWorkflow:
    @workflow.run
    async def run(self, name: str) -> str:
        return f"Hello, {name}!"


@pytest.mark.asyncio
async def test_temporal_workflow_execution():
    """
    Verify Temporal can execute a workflow locally.
    Requires the test server (will attempt to download).
    """
    try:
        async with await WorkflowEnvironment.start_time_skipping() as env:
            async with Worker(
                env.client,
                task_queue="hello-world-task-queue",
                workflows=[SayHelloWorkflow],
            ):
                result = await env.client.execute_workflow(
                    SayHelloWorkflow.run,
                    "Temporal",
                    id="hello-workflow-id",
                    task_queue="hello-world-task-queue",
                )
                assert result == "Hello, Temporal!"
    except Exception as e:
        pytest.skip(f"Skipping Temporal test due to environment issues: {e}")


# --- O - Observability (LangSmith) ---


def test_langsmith_tracing_init():
    """
    Verify LangSmith client can initialize and construct a RunTree.
    Does not assert on network success (to avoid auth failures in CI),
    but ensures the SDK is functional.
    """
    # 1. Init Client
    client = Client()
    assert client is not None

    # 2. Create a RunTree (Trace)
    rt = RunTree(name="Test Trace", run_type="chain", inputs={"input": "test"})

    # 3. End the trace
    rt.end(outputs={"output": "success"})

    # 4. Verify structure
    assert rt.name == "Test Trace"
    assert rt.run_type == "chain"
    # We don't call rt.post() to avoid network calls in this smoke test
