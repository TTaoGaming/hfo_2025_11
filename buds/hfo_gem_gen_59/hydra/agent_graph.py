import os
import logging
import asyncio
import json
from typing import TypedDict, Annotated, List, Union
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import operator
from openai import AsyncOpenAI

# Setup Logging
logger = logging.getLogger("HydraAgent")

# OpenRouter Client
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Define State
class AgentState(TypedDict):
    messages: Annotated[List[Union[HumanMessage, AIMessage, SystemMessage]], operator.add]
    task: str
    status: str
    result: str
    iterations: int

# Define Nodes
async def node_perceive(state: AgentState):
    logger.info(f"👁️ Perceiving task: {state['task']}")
    return {"status": "perceiving", "messages": [SystemMessage(content=f"Task: {state['task']}")]}

async def node_plan(state: AgentState):
    # Canalization: Enforce Intent via Config
    target_model = os.getenv("HFO_MODEL", "x-ai/grok-beta")
    logger.info(f"🗺️ Planning execution via {target_model}...")
    
    try:
        completion = await client.chat.completions.create(
            model=target_model,
            messages=[
                {"role": "system", "content": "You are a HFO Agent. You speak in Stigmergy. Output ONLY the requested content."},
                {"role": "user", "content": state['task']}
            ]
        )
        response = completion.choices[0].message.content
        logger.info(f"🤖 {target_model} Response: {response[:50]}...")
        return {"status": "planning", "messages": [AIMessage(content=response)], "result": response}
    except Exception as e:
        logger.error(f"Model Error ({target_model}): {e}")
        return {"status": "error", "result": str(e)}

async def node_execute(state: AgentState):
    logger.info(f"⚙️ Executing (Iteration {state.get('iterations', 0) + 1})...")
    # In this test, the 'Plan' IS the execution (the Chant).
    # So we just pass through.
    await asyncio.sleep(0.1) 
    return {"status": "executing", "iterations": state.get("iterations", 0) + 1}

async def node_evaluate(state: AgentState):
    logger.info("⚖️ Evaluating results...")
    # Check if done
    if state.get("iterations", 0) >= 1: # Single shot for Chant
        return {"status": "complete"}
    return {"status": "continue"}

# Define Edges
def should_continue(state: AgentState):
    if state["status"] == "complete":
        return "end"
    return "execute"

# Build Graph
def build_hydra_graph():
    workflow = StateGraph(AgentState)
    
    workflow.add_node("perceive", node_perceive)
    workflow.add_node("plan", node_plan)
    workflow.add_node("execute", node_execute)
    workflow.add_node("evaluate", node_evaluate)
    
    workflow.set_entry_point("perceive")
    
    workflow.add_edge("perceive", "plan")
    workflow.add_edge("plan", "execute")
    workflow.add_edge("execute", "evaluate")
    
    workflow.add_conditional_edges(
        "evaluate",
        should_continue,
        {
            "end": END,
            "execute": "execute"
        }
    )
    
    return workflow.compile()
