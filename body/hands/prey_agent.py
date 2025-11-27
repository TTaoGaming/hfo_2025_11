"""
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: f1f21da2-647f-42fb-a2d4-da3db890dcd2
    type: py
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:21:31.376408+00:00'
    generation: 51
  topos:
    address: body/hands/prey_agent.py
    links: []
  telos:
    viral_factor: 0.0
    meme: prey_agent.py
"""

import os
import logging
import json
import asyncio
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field
import instructor
from openai import AsyncOpenAI
from langgraph.graph import StateGraph, END, START

from body.models.state import AgentState, PreyStep, AgentRole
from body.hands.tool_registry import ToolRegistry
from body.hands.evolutionary_memory import EvolutionaryMemory
from body.hfo_sdk.stigmergy import StigmergyClient
from body.constants import DEFAULT_MODEL
from body.config import Config

# Setup Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("prey_agent")

# --- Pydantic Models for Cognitive Steps ---


class Perception(BaseModel):
    """Phase 1: What do I see?"""

    context_summary: str = Field(
        ..., description="Summary of the current situation and task"
    )
    relevant_memories: List[str] = Field(
        default_factory=list, description="Key facts retrieved from memory"
    )
    environment_state: str = Field(
        ..., description="Description of the environment (files, tools)"
    )


class Reaction(BaseModel):
    """Phase 2: What should I do?"""

    thought_process: str = Field(..., description="Chain of thought reasoning")
    plan: List[str] = Field(..., description="Step-by-step plan")
    tool_calls: List[Dict[str, Any]] = Field(
        default_factory=list,
        description="List of tool calls to make. Format: {'tool': 'name', 'args': {...}}",
    )
    safety_check: bool = Field(
        ..., description="Does this plan violate any guardrails?"
    )


class Execution(BaseModel):
    """Phase 3: What did I do?"""

    tool_outputs: List[Dict[str, Any]] = Field(
        ..., description="Results from tool executions"
    )
    success: bool = Field(..., description="Did the execution succeed?")
    error_message: Optional[str] = None


class Yield(BaseModel):
    """Phase 4: What did I learn?"""

    final_result: str = Field(..., description="The final answer or output artifact")
    reflection: str = Field(..., description="Self-critique of the performance")
    lessons_learned: str = Field(
        ..., description="Specific improvements for the next iteration (RL Feedback)"
    )
    stigmergy_signal: Dict[str, Any] = Field(
        ..., description="Data to publish to the Hive Mind"
    )
    confidence_score: float = Field(..., ge=0.0, le=1.0)


# --- The PREY Agent ---


class PreyAgent:
    def __init__(
        self,
        agent_id: str,
        role: AgentRole,
        model_name: Optional[str] = None,
        nats_url: str = Config.NATS_URL,
    ):
        self.agent_id = agent_id
        self.role = role
        self.model_name = model_name or DEFAULT_MODEL

        # Initialize LLM Client (Instructor)
        base_url = os.getenv("LLM_BASE_URL", "https://openrouter.ai/api/v1")
        api_key = os.getenv("LLM_API_KEY", os.getenv("OPENROUTER_API_KEY"))

        self.client = instructor.from_openai(
            AsyncOpenAI(
                base_url=base_url,
                api_key=api_key,
            ),
            mode=instructor.Mode.JSON,
        )

        # Initialize Stigmergy
        self.stigmergy = StigmergyClient(nats_url)

        # Initialize Evolutionary Memory (Test-Time Compute)
        self.evolution = EvolutionaryMemory()

        # Initialize Tools
        self.tools = ToolRegistry()

        # Build the Graph
        self.graph = self._build_graph()

    def _build_graph(self):
        workflow = StateGraph(AgentState)

        # Add Nodes
        workflow.add_node("perceive", self.perceive_node)
        workflow.add_node("react", self.react_node)
        workflow.add_node("execute", self.execute_node)
        workflow.add_node("yield_node", self.yield_node)

        # Add Edges
        workflow.add_edge(START, "perceive")
        workflow.add_edge("perceive", "react")

        # Conditional Edge from React
        def check_safety(state: AgentState):
            # In a real implementation, we would check the Reaction object in the state
            # For now, we assume safety passes if we got here
            return "execute"

        workflow.add_edge("react", "execute")
        workflow.add_edge("execute", "yield_node")
        workflow.add_edge("yield_node", END)

        return workflow.compile()

    # --- Nodes ---

    async def perceive_node(self, state: AgentState):
        """Phase 1: Gather Context"""
        logger.info(f"[{self.agent_id}] 👀 PERCEIVE")

        # 1. Read Memory (Stigmergy)
        try:
            await self.stigmergy.connect()
            history = await self.stigmergy.fetch_history("hfo.mission.>", limit=5)
            memory_context = json.dumps(history, indent=2)
        except Exception as e:
            logger.warning(f"Failed to fetch stigmergy: {e}")
            memory_context = "No external memory available."

        # 2. LLM Call
        # Select Evolutionary Strategy
        strategy = self.evolution.select_strategy()
        state.active_strategy = strategy.strategy_name
        logger.info(f"   🧬 Strategy Selected: {strategy.strategy_name}")

        prompt = f"""
        You are {self.agent_id} ({self.role}).
        Task: {state.short_term_memory[-1] if state.short_term_memory else 'No task'}

        External Memory (Stigmergy):
        {memory_context}

        REASONING MODE: HIGH
        STRATEGY: {strategy.instruction}

        Analyze the situation deeply. Look for patterns in the External Memory.
        If previous agents failed, identify WHY.
        """

        perception = await self.client.chat.completions.create(
            model=self.model_name,
            response_model=Perception,
            messages=[{"role": "user", "content": prompt}],
        )

        # Update State
        state.current_step = PreyStep.PERCEIVE
        # We might store the perception in a temporary field or append to memory
        # For this simple implementation, we just log it
        logger.info(f"   Context: {perception.context_summary}")
        return state

    async def react_node(self, state: AgentState):
        """Phase 2: Plan & Decide"""
        logger.info(f"[{self.agent_id}] 🧠 REACT")

        tool_definitions = self.tools.get_definitions_str()

        prompt = f"""
        You are {self.agent_id} ({self.role}).
        Current State: {state.current_step}
        Task: {state.short_term_memory[-1]}

        REASONING MODE: HIGH
        Based on your perception, formulate a robust plan.
        Think step-by-step. Anticipate errors.
        Use 'sequential_thinking' if the problem is complex.

        Available Tools:
        {tool_definitions}
        """

        reaction = await self.client.chat.completions.create(
            model=self.model_name,
            response_model=Reaction,
            messages=[{"role": "user", "content": prompt}],
        )

        state.current_step = PreyStep.REACT
        # Store the plan in the state (we need to extend AgentState or use a dict)
        # For now, we'll hack it into short_term_memory or just pass it implicitly via the graph state if we extended it
        # Ideally AgentState should have a 'current_plan' field.
        # I will append the plan to short_term_memory as a JSON string for the next step
        state.short_term_memory.append(f"PLAN: {reaction.model_dump_json()}")
        return state

    async def execute_node(self, state: AgentState):
        """Phase 3: Run Tools"""
        logger.info(f"[{self.agent_id}] 🛠️ EXECUTE")

        # Retrieve Plan
        last_mem = state.short_term_memory[-1]
        if not last_mem.startswith("PLAN:"):
            logger.error("No plan found!")
            return state

        plan_json = last_mem.replace("PLAN: ", "")
        reaction = Reaction.model_validate_json(plan_json)

        outputs = []
        for tool_call in reaction.tool_calls:
            tool_name = tool_call.get("tool")
            args = tool_call.get("args", {})

            result = self.tools.execute(tool_name, args)

            outputs.append({"tool": tool_name, "result": result})
            logger.info(f"   Ran {tool_name}: {str(result)[:50]}...")

        execution = Execution(
            tool_outputs=outputs,
            success=True,  # Simplified
        )

        state.current_step = PreyStep.EXECUTE
        state.short_term_memory.append(f"EXECUTION: {execution.model_dump_json()}")
        return state

    async def yield_node(self, state: AgentState):
        """Phase 4: Reflect & Share"""
        logger.info(f"[{self.agent_id}] 📡 YIELD")

        # Retrieve Execution
        last_mem = state.short_term_memory[-1]
        exec_json = last_mem.replace("EXECUTION: ", "")

        prompt = f"""
        You are {self.agent_id} ({self.role}).
        Execution Results: {exec_json}

        REASONING MODE: HIGH
        Reflect on your performance.
        Did you succeed? If not, why?
        What should the next agent know to do better? (Reinforcement Learning)
        """

        yield_obj = await self.client.chat.completions.create(
            model=self.model_name,
            response_model=Yield,
            messages=[{"role": "user", "content": prompt}],
        )

        # Publish to Stigmergy
        try:
            # Include lessons learned in the signal
            signal = yield_obj.stigmergy_signal
            signal["lessons_learned"] = yield_obj.lessons_learned
            signal["confidence"] = yield_obj.confidence_score
            signal["strategy"] = state.active_strategy

            await self.stigmergy.publish(f"hfo.mission.{self.agent_id}.yield", signal)
            logger.info("   Signal emitted to NATS.")

            # Update Evolutionary Fitness
            if state.active_strategy:
                success = yield_obj.confidence_score > 0.7
                self.evolution.update_fitness(state.active_strategy, success)
                logger.info(
                    f"   🧬 Fitness Updated for {state.active_strategy} (Success: {success})"
                )

        except Exception as e:
            logger.error(f"Failed to publish signal: {e}")

        state.current_step = PreyStep.YIELD
        state.confidence_score = yield_obj.confidence_score
        state.final_output = yield_obj.final_result
        return state

    async def run(self, task: str):
        """Entry point to run the agent."""
        initial_state = AgentState(
            agent_id=self.agent_id,
            role=self.role,
            short_term_memory=[task],
            current_step=PreyStep.IDLE,
        )

        # Run the graph
        # Note: LangGraph invoke is synchronous or async depending on setup.
        # Since our nodes are async, we should use ainvoke
        final_state = await self.graph.ainvoke(initial_state)
        return final_state

    async def close(self):
        """Cleanup resources."""
        if self.stigmergy:
            await self.stigmergy.close()


# Example Usage
if __name__ == "__main__":

    async def main():
        agent = PreyAgent("scout-1", AgentRole.OBSERVER)
        result = await agent.run("Check the current directory for any markdown files.")
        print("Final State:", result)

    asyncio.run(main())
