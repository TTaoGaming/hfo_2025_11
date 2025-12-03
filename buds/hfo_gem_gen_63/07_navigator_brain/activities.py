"""
---
holon:
  id: hfo-navigator-activities
  type: implementation
  file: activities.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_navigator_temporal.md
---
"""
from temporalio import activity
from typing import List, Dict, Any
import asyncio

# Import Proxies
from src.bridger import bridger
from src.search_tool import search_web
from src.config import settings
from openai import OpenAI

@activity.defn
async def search_memory(query: str) -> str:
    """
    Activity: Search Internal Memory (Bridger).
    """
    activity.logger.info(f"🧠 Searching Memory for: {query}")
    
    # Import the direct client
    # We do this inside the activity to ensure it runs in the worker process
    try:
        from .memory_client import search_memory_direct
    except ImportError:
        from memory_client import search_memory_direct
        
    return search_memory_direct(query)

@activity.defn
async def search_web_activity(query: str) -> str:
    """
    Activity: Search External Web (MCP).
    """
    activity.logger.info(f"🌍 Searching Web for: {query}")
    # We use the search_tool proxy
    return search_web(query)

@activity.defn
async def synthesize_report(context: str, query: str) -> str:
    """
    Activity: Synthesize Report using LLM.
    """
    activity.logger.info(f"✍️ Synthesizing Report for: {query}")
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.OPENROUTER_API_KEY,
    )
    
    prompt = f"""
    You are the Navigator of Hive Fleet Obsidian.
    
    QUERY: {query}
    
    CONTEXT:
    {context}
    
    TASK:
    Synthesize a concise research report based on the context.
    Focus on facts and actionable insights.
    """
    
    completion = client.chat.completions.create(
        model=settings.MODEL_REASONING,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return completion.choices[0].message.content

@activity.defn
async def run_cognitive_cycle(query: str) -> str:
    """
    Activity: Run the Prey 1181 Cognitive Cycle (LangGraph).
    Encapsulates the non-deterministic agent loop.
    """
    activity.logger.info(f"🕸️ Starting Prey 1181 Cycle for: {query}")
    
    # Import here to avoid circular deps or load issues
    try:
        from .intelligence import run_prey_cycle
    except ImportError:
        from intelligence import run_prey_cycle
        
    return run_prey_cycle(query)
