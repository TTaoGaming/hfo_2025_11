import pytest
import ray
from typing import TypedDict, List, Dict
from langgraph.graph import StateGraph, END
import time


# --- Mock Data Structures ---
class ResearchResult(TypedDict):
    agent_id: str
    finding: str
    confidence: float


class SwarmState(TypedDict):
    user_request: str
    research_tasks: List[str]
    raw_findings: List[ResearchResult]
    quorum_decision: str
    final_digest: str


# --- Ray Actors for Scatter-Gather ---
@ray.remote
def perform_research_task(task: str, agent_id: str) -> ResearchResult:
    """
    Simulates a heavy research task running in parallel on Ray.
    """
    # Simulate work
    time.sleep(0.1)
    return {
        "agent_id": agent_id,
        "finding": f"Found evidence for {task}",
        "confidence": 0.95,
    }


# --- LangGraph Nodes ---


def orchestrator_node(state: SwarmState) -> Dict:
    """
    Phase 1: Orchestrator parses user request and generates tasks.
    """
    print(f"\n[Orchestrator] Processing: {state['user_request']}")
    # In a real app, an LLM would generate these based on the request
    tasks = [f"Aspect {i} of {state['user_request']}" for i in range(1, 4)]
    return {"research_tasks": tasks}


def scatter_gather_node(state: SwarmState) -> Dict:
    """
    Phase 2: Scatter tasks to Ray, Gather results.
    """
    tasks = state["research_tasks"]
    print(f"[Scatter] Dispatching {len(tasks)} tasks to Ray swarm...")

    # SCATTER: Launch parallel tasks
    futures = [
        perform_research_task.remote(task, f"Agent-{i}") for i, task in enumerate(tasks)
    ]

    # GATHER: Wait for all results
    results = ray.get(futures)
    print(f"[Gather] Collected {len(results)} research findings.")
    return {"raw_findings": results}


def byzantine_quorum_node(state: SwarmState) -> Dict:
    """
    Phase 3: Review findings and reach consensus.
    """
    findings = state["raw_findings"]
    print(f"[Quorum] Reviewing {len(findings)} findings for consensus...")

    # Simulate Byzantine Fault Tolerance check (simple majority for this test)
    valid_findings = [f for f in findings if f["confidence"] > 0.8]

    if len(valid_findings) >= len(findings) * 0.66:
        decision = "CONSENSUS_REACHED"
    else:
        decision = "CONSENSUS_FAILED"

    return {"quorum_decision": decision}


def synthesis_digest_node(state: SwarmState) -> Dict:
    """
    Phase 4: Synthesize final answer for the user.
    """
    decision = state["quorum_decision"]
    findings = state["raw_findings"]

    if decision == "CONSENSUS_REACHED":
        digest = f"Swarm confirms: {state['user_request']}. Evidence: {', '.join([f['finding'] for f in findings])}"
    else:
        digest = "Swarm could not reach consensus."

    print(f"[Synthesis] Final Digest: {digest}")
    return {"final_digest": digest}


# --- The Test ---


@pytest.mark.asyncio
async def test_user_journey_simulation():
    """
    Simulates the full User -> Orchestrator -> Scatter-Gather -> Quorum -> Digest flow.
    """
    # 1. Initialize Ray (if not already running)
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True)

    # 2. Build the Graph
    workflow = StateGraph(SwarmState)

    workflow.add_node("orchestrator", orchestrator_node)
    workflow.add_node("scatter_gather", scatter_gather_node)
    workflow.add_node("quorum", byzantine_quorum_node)
    workflow.add_node("synthesis", synthesis_digest_node)

    # Define Flow
    workflow.set_entry_point("orchestrator")
    workflow.add_edge("orchestrator", "scatter_gather")
    workflow.add_edge("scatter_gather", "quorum")
    workflow.add_edge("quorum", "synthesis")
    workflow.add_edge("synthesis", END)

    app = workflow.compile()

    # 3. Execute the Workflow
    initial_state = SwarmState(
        user_request="Analyze the viability of Warp Drives",
        research_tasks=[],
        raw_findings=[],
        quorum_decision="",
        final_digest="",
    )

    print("\n--- Starting Simulation ---")
    final_state = await app.ainvoke(initial_state)

    # 4. Assertions
    assert len(final_state["research_tasks"]) == 3
    assert len(final_state["raw_findings"]) == 3
    assert final_state["quorum_decision"] == "CONSENSUS_REACHED"
    assert "Warp Drives" in final_state["final_digest"]

    print("\n--- Simulation Complete ---")
    ray.shutdown()


if __name__ == "__main__":
    # Allow running directly with python
    import asyncio

    asyncio.run(test_user_journey_simulation())
