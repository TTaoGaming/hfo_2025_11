import os
import logging
import asyncio
from typing import TypedDict, Annotated, List, Union
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import operator

# Setup Logging
logger = logging.getLogger("HydraAgent")

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
    # In a real scenario, this would query the Oracle or read files
    return {"status": "perceiving", "messages": [SystemMessage(content="Perceived task context.")]}

async def node_plan(state: AgentState):
    logger.info("🗺️ Planning execution...")
    # Call LLM to plan (Mock for now)
    return {"status": "planning", "messages": [AIMessage(content="Plan: Execute step 1, then step 2.")]}

async def node_execute(state: AgentState):
    logger.info(f"⚙️ Executing (Iteration {state.get('iterations', 0) + 1})...")
    # Perform work
    await asyncio.sleep(1) # Simulate work
    return {"status": "executing", "iterations": state.get("iterations", 0) + 1}

async def node_evaluate(state: AgentState):
    logger.info("⚖️ Evaluating results...")
    # Check if done
    if state.get("iterations", 0) >= 3:
        return {"status": "complete", "result": "Task Completed Successfully."}
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
