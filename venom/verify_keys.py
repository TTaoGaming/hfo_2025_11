"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: e0688afd-b110-474b-9911-7b355368be4d
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.257892+00:00'
  topos:
    address: venom/verify_keys.py
    links: []
  telos:
    viral_factor: 0.0
    meme: verify_keys.py
"""

import asyncio
from body.blood import settings, model_registry
from langchain_openai import ChatOpenAI
from langsmith import Client as LangSmithClient
from langchain_core.messages import HumanMessage


async def verify_openrouter():
    print("\n🧠 Testing OpenRouter Connection...")
    print(f"   Base URL: {settings.openrouter_base_url}")

    if not settings.openrouter_api_key or "sk-or-..." in settings.openrouter_api_key:
        print("   ❌ Error: OPENROUTER_API_KEY is missing or default.")
        return False

    try:
        # Use a cheap/fast model for testing
        model_name = "openai/gpt-4o-mini"
        # Fallback if registry is empty or key missing
        if model_registry and model_registry.models.get("fast"):
            model_name = model_registry.models["fast"][0]

        print(f"   Model: {model_name}")

        llm = ChatOpenAI(
            base_url=settings.openrouter_base_url,
            api_key=settings.openrouter_api_key,
            model=model_name,
            temperature=0,
        )

        response = await llm.ainvoke(
            [HumanMessage(content="Reply with 'Connection Successful'")]
        )
        print(f"   ✅ Success! Response: {response.content}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {str(e)}")
        return False


def verify_langsmith():
    print("\n👁️ Testing LangSmith Connection...")
    print(f"   Endpoint: {settings.langchain_endpoint}")
    print(f"   Project: {settings.langchain_project}")

    if not settings.langchain_api_key or "lsv2_..." in settings.langchain_api_key:
        print("   ❌ Error: LANGCHAIN_API_KEY is missing or default.")
        return False

    try:
        client = LangSmithClient(
            api_key=settings.langchain_api_key, api_url=settings.langchain_endpoint
        )
        # Check if we can list projects (basic auth check)
        _ = list(client.list_projects(limit=1))
        print("   ✅ Success! Authenticated with LangSmith.")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {str(e)}")
        return False


async def main():
    print("🦅 Hive Fleet Obsidian: Key Verification Protocol")
    print("-----------------------------------------------")

    ls_ok = verify_langsmith()
    or_ok = await verify_openrouter()

    if ls_ok and or_ok:
        print("\n🟢 All Systems Operational. Ready for Swarm Deployment.")
    else:
        print("\n🔴 Verification Failed. Check .env file.")


if __name__ == "__main__":
    asyncio.run(main())
