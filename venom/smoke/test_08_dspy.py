"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 24e4af45-5b6c-4055-a0bb-4389542e980d
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.327252+00:00'
  topos:
    address: venom/smoke/test_08_dspy.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_08_dspy.py
"""

import dspy
import pytest
import os


def test_dspy_smoke():
    print("\n🧪 SMOKE TEST: DSPy Evolution Layer")

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        pytest.skip("OPENROUTER_API_KEY not set")

    try:
        # Configure DSPy with OpenRouter (using OpenAI client compatibility)
        lm = dspy.LM(
            model="openai/x-ai/grok-4-fast",  # DSPy uses 'openai/' prefix for custom providers often, or just the model name
            api_key=api_key,
            api_base="https://openrouter.ai/api/v1",
            temperature=0.7,
        )
        dspy.configure(lm=lm)

        # Define a simple signature
        class BasicQA(dspy.Signature):
            """Answer questions with short factoid answers."""

            question = dspy.InputField()
            answer = dspy.OutputField(desc="often between 1 and 5 words")

        # Predict
        predict = dspy.Predict(BasicQA)
        response = predict(question="What is the capital of France?")

        print("   Question: What is the capital of France?")
        print(f"   Answer: {response.answer}")

        assert "Paris" in response.answer
        print("   ✅ DSPy Prediction: OK")

    except Exception as e:
        pytest.fail(f"DSPy failed: {e}")


if __name__ == "__main__":
    test_dspy_smoke()
