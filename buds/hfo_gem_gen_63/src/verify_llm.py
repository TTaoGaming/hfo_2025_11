import os
import sys
from openai import OpenAI

# Add root to path to import config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.config import settings

def verify_llm():
    """Verify OpenRouter Connection."""
    print("🧠 Verifying OpenRouter Connection...")
    
    api_key = settings.OPENROUTER_API_KEY
    if not api_key:
        # Try getting from os.environ directly if pydantic missed it
        api_key = os.environ.get("OPENROUTER_API_KEY")
        
    if not api_key:
        print("❌ Verification FAILED: OPENROUTER_API_KEY not found in settings or environment.")
        return

    print(f"🔑 API Key found: {api_key[:4]}...{api_key[-4:]}")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    try:
        completion = client.chat.completions.create(
            model=settings.OPENROUTER_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": "Are you online? Reply with 'I am the Obsidian Spider'."
                }
            ]
        )
        response = completion.choices[0].message.content
        print(f"🤖 Response: {response}")
        
        if "Obsidian Spider" in response:
             print("✅ Verification SUCCESS: LLM is responsive.")
        else:
             print("⚠️ Verification WARNING: Response received but content unexpected.")
             
    except Exception as e:
        print(f"❌ Verification FAILED: {e}")

if __name__ == "__main__":
    verify_llm()
