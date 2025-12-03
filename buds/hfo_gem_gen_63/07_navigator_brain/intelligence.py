"""
---
holon:
  id: hfo-navigator-intelligence
  type: implementation
  file: intelligence.py
  status: active
  intent: buds/hfo_gem_gen_63/brain/intent_intelligence_langgraph.md
---
"""
import operator
from typing import Annotated, List, TypedDict, Union
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
import logging

logger = logging.getLogger("NavigatorIntelligence")

# Import Proxies
from src.config import settings
from src.search_tool import search_web
# We'll simulate memory for now as the MCP is not fully ready for direct python call without async
# But we can use the same logic as activities.

# --- 1. State Definition ---
class AgentState(TypedDict):
    query: str
    messages: Annotated[List[BaseMessage], operator.add]
    context: str
    plan: List[str]
    results: List[str]
    final_report: str

# --- 2. Nodes (The Prey 1181 Cycle) ---

def perceive(state: AgentState):
    """
    Phase 1: Perceive.
    Gather context from Internal Memory and External Web.
    """
    query = state["query"]
    logger.info(f"👁️ [PERCEIVE] Scanning for: {query}")
    
    # 1. Web Search (Real)
    web_data = search_web(query)
    
    # 2. Memory Search (Simulated/Placeholder until MCP is fully linked)
    memory_data = f"[MEMORY] No specific stigmergic records found for {query}."
    
    context = f"--- WEB DATA ---\n{web_data}\n\n--- MEMORY DATA ---\n{memory_data}"
    
    return {
        "context": context,
        "messages": [SystemMessage(content=f"Context gathered:\n{context}")]
    }

def react(state: AgentState):
    """
    Phase 2: React.
    Formulate a plan based on the context.
    """
    logger.info(f"🧠 [REACT] Formulating Plan...")
    query = state["query"]
    context = state["context"]
    
    # We use the LLM to generate a plan
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.OPENROUTER_API_KEY,
        model=settings.MODEL_REASONING,
        temperature=0.7
    )
    
    prompt = f"""
    You are the Navigator of Hive Fleet Obsidian.
    User Query: {query}
    Context: {context}
    
    Generate a concise list of 3-5 specific execution steps to answer this query fully.
    Return ONLY the steps as a bulleted list.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    plan_text = response.content
    
    # Simple parsing of the plan (splitting by newlines)
    plan = [line.strip() for line in plan_text.split('\n') if line.strip().startswith('-') or line.strip().startswith('*') or line.strip()[0].isdigit()]
    
    return {
        "plan": plan,
        "messages": [AIMessage(content=f"Plan formulated: {plan}")]
    }

def execute(state: AgentState):
    """
    Phase 3: Execute.
    Run the plan. (Simulating the 8-agent swarm).
    """
    logger.info(f"⚔️ [EXECUTE] Swarm 186481 Engaging...")
    plan = state["plan"]
    results = []
    
    # In a full implementation, this would spawn parallel Temporal Activities or Ray tasks.
    # For now, we simulate the execution loop.
    for step in plan:
        # We assume the step is self-contained enough for the LLM to "simulate" execution or we just record it.
        # Ideally, we would have a tool router here.
        # For this iteration, we will just append the step as "Executed".
        results.append(f"Executed: {step}")
        
    return {
        "results": results,
        "messages": [SystemMessage(content=f"Execution complete. Results: {len(results)} steps processed.")]
    }

def yield_node(state: AgentState):
    """
    Phase 4: Yield.
    Synthesize the final report.
    """
    print(f"💎 [YIELD] Crystallizing Insight...")
    query = state["query"]
    context = state["context"]
    results = "\n".join(state["results"])
    
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=settings.OPENROUTER_API_KEY,
        model=settings.MODEL_REASONING,
        temperature=0.7
    )
    
    prompt = f"""
    You are the Swarmlord.
    Query: {query}
    Context: {context}
    Execution Results: {results}
    
    Synthesize a final, comprehensive report.
    """
    
    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "final_report": response.content,
        "messages": [AIMessage(content=response.content)]
    }

# --- 3. Graph Construction ---

def build_prey_1181_graph():
    workflow = StateGraph(AgentState)
    
    # Add Nodes
    workflow.add_node("perceive", perceive)
    workflow.add_node("react", react)
    workflow.add_node("execute", execute)
    workflow.add_node("yield", yield_node)
    
    # Add Edges (Linear 1-1-8-1 Cycle)
    workflow.set_entry_point("perceive")
    workflow.add_edge("perceive", "react")
    workflow.add_edge("react", "execute")
    workflow.add_edge("execute", "yield")
    workflow.add_edge("yield", END)
    
    return workflow.compile()

# Entry point for the Temporal Activity
def run_prey_cycle(query: str) -> str:
    app = build_prey_1181_graph()
    initial_state = {
        "query": query,
        "messages": [],
        "context": "",
        "plan": [],
        "results": [],
        "final_report": ""
    }
    
    # Run the graph
    final_state = app.invoke(initial_state)
    return final_state["final_report"]
