import asyncio
import os
from src.config import settings, model_registry
from langchain_openai import ChatOpenAI
from langsmith import Client as LangSmithClient
from langchain_core.messages import HumanMessage

async def verify_openrouter():
    print(f"\n🧠 Testing OpenRouter Connection...")
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
            temperature=0
        )
        
        response = await llm.ainvoke([HumanMessage(content="Reply with 'Connection Successful'")])
        print(f"   ✅ Success! Response: {response.content}")
        return True
    except Exception as e:
        print(f"   ❌ Failed: {str(e)}")
        return False

def verify_langsmith():
    print(f"\n👁️ Testing LangSmith Connection...")
    print(f"   Endpoint: {settings.langchain_endpoint}")
    print(f"   Project: {settings.langchain_project}")

    if not settings.langchain_api_key or "lsv2_..." in settings.langchain_api_key:
        print("   ❌ Error: LANGCHAIN_API_KEY is missing or default.")
        return False

    try:
        client = LangSmithClient(
            api_key=settings.langchain_api_key,
            api_url=settings.langchain_endpoint
        )
        # Check if we can list projects (basic auth check)
        projects = list(client.list_projects(limit=1))
        print(f"   ✅ Success! Authenticated with LangSmith.")
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
