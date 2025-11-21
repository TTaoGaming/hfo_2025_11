from typing import TypedDict
from langgraph.graph import StateGraph, END
import pytest

class State(TypedDict):
    count: int

def increment(state: State):
    return {"count": state["count"] + 1}

def test_langgraph_smoke():
    print("\n🧪 SMOKE TEST: LangGraph Logic Layer")
    try:
        workflow = StateGraph(State)
        workflow.add_node("increment", increment)
        workflow.set_entry_point("increment")
        workflow.add_edge("increment", END)
        
        app = workflow.compile()
        
        result = app.invoke({"count": 0})
        assert result["count"] == 1
        print("   ✅ LangGraph Execution: OK")
    except Exception as e:
        pytest.fail(f"LangGraph failed: {e}")

if __name__ == "__main__":
    test_langgraph_smoke()
