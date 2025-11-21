import os
import ray
import json
from typing import List, Dict, TypedDict, Annotated
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, END
import operator

# --- Configuration ---
MODEL_NAME = "x-ai/grok-4-fast"  # As per docs
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# --- Data Models ---
class MathProblem(TypedDict):
    id: int
    question: str

class ResearchResult(TypedDict):
    problem_id: int
    agent_id: str
    answer: str
    reasoning: str
    confidence: float

class SwarmState(TypedDict):
    user_request: str
    problems: List[MathProblem]
    results: Annotated[List[ResearchResult], operator.add]
    quorum_report: str
    final_digest: str

# --- Ray Actors (The Researchers) ---
@ray.remote
class MathResearcher:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            openai_api_key=OPENROUTER_API_KEY,
            openai_api_base=OPENROUTER_BASE_URL,
            temperature=0.7
        )

    def solve(self, problem: MathProblem) -> ResearchResult:
        print(f"[{self.agent_id}] Solving: {problem['question']}")
        try:
            messages = [
                SystemMessage(content="You are a precise mathematician. Solve the problem and provide a confidence score (0.0-1.0). Format output as JSON with keys: 'answer', 'reasoning', 'confidence'."),
                HumanMessage(content=problem['question'])
            ]
            response = self.llm.invoke(messages)

            # Simple parsing (in production, use structured output parsers)
            content = response.content.strip()
            # Attempt to find JSON in markdown
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].split("```")[0].strip()

            data = json.loads(content)

            return {
                "problem_id": problem["id"],
                "agent_id": self.agent_id,
                "answer": str(data.get("answer", "Error")),
                "reasoning": data.get("reasoning", "No reasoning provided"),
                "confidence": float(data.get("confidence", 0.0))
            }
        except Exception as e:
            return {
                "problem_id": problem["id"],
                "agent_id": self.agent_id,
                "answer": "Error",
                "reasoning": str(e),
                "confidence": 0.0
            }

# --- LangGraph Nodes ---

def orchestrator_node(state: SwarmState):
    """Parses the user request into specific math problems."""
    print(f"Orchestrator received: {state['user_request']}")
    # For this simple test, we'll hardcode the breakdown or use a simple split
    # In a real app, an LLM would do this.

    # Simulating LLM breakdown of "Solve these: 2+2, 5*5, sqrt(16)"
    # We will just generate a fixed set for the test to ensure deterministic inputs for the swarm
    problems = [
        {"id": 1, "question": "What is the integral of x^2 dx?"},
        {"id": 2, "question": "Solve for x: 2x + 5 = 15"},
        {"id": 3, "question": "What is the 10th Fibonacci number?"}
    ]
    return {"problems": problems}

def scatter_gather_node(state: SwarmState):
    """Dispatches problems to Ray actors."""
    problems = state["problems"]
    futures = []

    # Create a pool of researchers (Ray Actors)
    researchers = [MathResearcher.remote(f"Researcher-{i}") for i in range(3)]

    for i, problem in enumerate(problems):
        # Assign each problem to a researcher (round-robin)
        researcher = researchers[i % len(researchers)]
        futures.append(researcher.solve.remote(problem))

    results = ray.get(futures)
    return {"results": results}

def byzantine_quorum_node(state: SwarmState):
    """Reviews results for consensus and quality."""
    results = state["results"]
    print(f"Quorum reviewing {len(results)} results...")

    # Simple logic: Check if confidence > 0.8
    valid_count = sum(1 for r in results if r["confidence"] > 0.8)
    total = len(results)

    if valid_count == total:
        status = "UNANIMOUS_CONSENSUS"
    elif valid_count > total / 2:
        status = "MAJORITY_CONSENSUS"
    else:
        status = "CONSENSUS_FAILED"

    report = f"Quorum Status: {status}. {valid_count}/{total} results passed confidence threshold."
    return {"quorum_report": report}

def synthesizer_node(state: SwarmState):
    """Synthesizes the final digest."""
    results = state["results"]
    report = state["quorum_report"]

    digest = f"# Final Swarm Digest\n\n## Quorum Report\n{report}\n\n## Findings\n"
    for r in results:
        digest += f"- **Problem {r['problem_id']}**: {r['answer']} (Confidence: {r['confidence']})\n"
        digest += f"  - *Reasoning*: {r['reasoning']}\n"
        digest += f"  - *Agent*: {r['agent_id']}\n"

    return {"final_digest": digest}

# --- Graph Construction ---
def build_swarm_graph():
    workflow = StateGraph(SwarmState)

    workflow.add_node("orchestrator", orchestrator_node)
    workflow.add_node("scatter_gather", scatter_gather_node)
    workflow.add_node("quorum", byzantine_quorum_node)
    workflow.add_node("synthesizer", synthesizer_node)

    workflow.set_entry_point("orchestrator")
    workflow.add_edge("orchestrator", "scatter_gather")
    workflow.add_edge("scatter_gather", "quorum")
    workflow.add_edge("quorum", "synthesizer")
    workflow.add_edge("synthesizer", END)

    return workflow.compile()
