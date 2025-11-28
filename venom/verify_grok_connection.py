"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 5819b6a3-26b2-4a87-820b-2be5969247e8
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.257013+00:00'
    generation: 51
  topos:
    address: venom/verify_grok_connection.py
    links: []
  telos:
    viral_factor: 0.0
    meme: verify_grok_connection.py
"""

import os
import time
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage


def test_grok_connection():
    print("🧪 TESTING: OpenRouter Connection (x-ai/grok-4-fast)...")

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ ERROR: OPENROUTER_API_KEY is not set.")
        return

    try:
        llm = ChatOpenAI(
            model="x-ai/grok-4-fast",
            openai_api_key=api_key,
            openai_api_base="https://openrouter.ai/api/v1",
            temperature=0.7,
        )

        start_time = time.time()
        print("   Sending request: 'What is 2 + 2?'")
        response = llm.invoke(
            [HumanMessage(content="What is 2 + 2? Answer in one word.")]
        )
        duration = time.time() - start_time

        print(f"✅ SUCCESS: Response received in {duration:.2f}s")
        print(f"   Output: {response.content}")

    except Exception as e:
        print(f"❌ FAILED: {str(e)}")


if __name__ == "__main__":
    test_grok_connection()
