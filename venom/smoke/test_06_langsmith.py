"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: ade2792e-04e4-4ddd-8a95-ba3992ce79de
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.325552+00:00'
  topos:
    address: venom/smoke/test_06_langsmith.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_06_langsmith.py
"""

import os
import pytest
from langchain_core.tracers.context import tracing_v2_enabled
from langchain_openai import ChatOpenAI


def test_langsmith_smoke():
    print("\n🧪 SMOKE TEST: LangSmith Observability Layer")

    if not os.getenv("LANGCHAIN_API_KEY"):
        print("   ⚠️ LANGCHAIN_API_KEY not set. Skipping.")
        return

    try:
        # We just want to verify we can trace a simple call without error
        with tracing_v2_enabled(project_name="hfo-smoke-test"):
            llm = ChatOpenAI(
                model="x-ai/grok-4-fast",
                openai_api_key=os.getenv("OPENROUTER_API_KEY"),
                openai_api_base="https://openrouter.ai/api/v1",
            )
            llm.invoke("Hello")

        print("   ✅ LangSmith Trace: OK")
    except Exception as e:
        pytest.fail(f"LangSmith failed: {e}")


if __name__ == "__main__":
    test_langsmith_smoke()
