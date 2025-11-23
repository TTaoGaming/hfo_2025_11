"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: 4830d704-795c-4592-ab8b-1af69102b2d6
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.323582+00:00'
    generation: 51
  topos:
    address: venom/smoke/test_04_pydantic_instructor.py
    links: []
  telos:
    viral_factor: 0.0
    meme: test_04_pydantic_instructor.py
"""

import os
import pytest
import instructor
from pydantic import BaseModel
from openai import OpenAI


class UserInfo(BaseModel):
    name: str
    age: int


def test_instructor_smoke():
    print("\n🧪 SMOKE TEST: Instructor & Pydantic Layer")

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("   ⚠️ Skipped: OPENROUTER_API_KEY not set (Instructor test skipped)")
        return

    try:
        client = instructor.from_openai(
            OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
            ),
            mode=instructor.Mode.JSON,
        )

        resp = client.chat.completions.create(
            model="x-ai/grok-4-fast",  # Cheap & Fast
            messages=[
                {"role": "user", "content": "Extract: John Doe is 30 years old."}
            ],
            response_model=UserInfo,
        )

        assert resp.name == "John Doe"
        assert resp.age == 30
        print("   ✅ Instructor Extraction: OK")

    except Exception as e:
        pytest.fail(f"Instructor failed: {e}")


if __name__ == "__main__":
    test_instructor_smoke()
