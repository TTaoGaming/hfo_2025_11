"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: aaf395a2-8c44-463b-9296-0191fd8a4b97
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.302852+00:00'
  topos:
    address: venom/test_cognitive_tools.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_cognitive_tools.py
"""

from body.hands.tool_registry import ToolRegistry


def test_sequential_thinking():
    registry = ToolRegistry()

    # 1. Test Registration
    assert "sequential_thinking" in registry.tools

    # 2. Test Execution
    result = registry.execute(
        "sequential_thinking",
        {
            "thought": "I need to break this down.",
            "needs_more_time": True,
            "next_step_hint": "Analyze the file structure.",
        },
    )

    assert "Thought recorded" in result
    assert "Total steps: 1" in result

    # 3. Test History
    history = registry.thinking_tool.get_thought_process()
    assert "1. I need to break this down." in history


def test_basic_tools():
    registry = ToolRegistry()

    # Test list_directory
    result = registry.execute("list_directory", {"path": "."})
    assert "Makefile" in result


if __name__ == "__main__":
    test_sequential_thinking()
    test_basic_tools()
    print("✅ Cognitive Tools Verified")
