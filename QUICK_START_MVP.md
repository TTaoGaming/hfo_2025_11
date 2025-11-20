# 🚀 Quick Start: Building the Byzantine Scatter-Gather MVP

**Status:** Actionable Roadmap  
**Priority:** Execute these in order  
**Timeline:** 2-3 weeks for minimal viable system

---

## 🎯 Goal: Working End-to-End Demo

By the end of this roadmap, you should have:
- ✅ 1 working PREY agent that can process a task
- ✅ 10 agents running in parallel via Ray
- ✅ Byzantine voting with disruptor detection
- ✅ A simple synthesis artifact returned to the user

**Success Metric:** `python demo.py "What is 2+2?"` → Returns consensus with 70-90% confidence

---

## 📅 Week 1: Foundation (PREY Loop)

### Day 1-2: Single Agent Implementation
**File:** `src/agents/prey_agent.py`

```python
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from src.models import AgentState, PreyStep

def build_prey_loop(model_name: str = "x-ai/grok-4.1-fast"):
    """
    Builds a LangGraph state machine for the PREY loop.
    
    States: Perceive → React → Execute → Yield
    """
    
    # Initialize LLM
    llm = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        model=model_name,
        temperature=0.7
    )
    
    # Define workflow
    workflow = StateGraph(AgentState)
    
    # Node: Perceive (Read mission context)
    def perceive_node(state: AgentState):
        mission = state.current_mission
        context = f"Mission: {mission.description}"
        state.short_term_memory.append(f"[PERCEIVE] {context}")
        state.current_step = PreyStep.PERCEIVE
        return state
    
    # Node: React (Plan approach)
    def react_node(state: AgentState):
        # Use LLM to generate plan
        prompt = f"Mission: {state.current_mission.description}\nYour plan:"
        response = llm.invoke(prompt)
        state.short_term_memory.append(f"[REACT] {response.content}")
        state.current_step = PreyStep.REACT
        return state
    
    # Node: Execute (Generate response)
    def execute_node(state: AgentState):
        # Use LLM to execute
        context = "\n".join(state.short_term_memory[-3:])
        response = llm.invoke(context)
        state.short_term_memory.append(f"[EXECUTE] {response.content}")
        state.current_step = PreyStep.EXECUTE
        return state
    
    # Node: Yield (Format output)
    def yield_node(state: AgentState):
        result = state.short_term_memory[-1]
        state.current_step = PreyStep.YIELD
        state.confidence_score = 0.85  # TODO: Calculate actual confidence
        return state
    
    # Build graph
    workflow.add_node("perceive", perceive_node)
    workflow.add_node("react", react_node)
    workflow.add_node("execute", execute_node)
    workflow.add_node("yield_results", yield_node)
    
    workflow.set_entry_point("perceive")
    workflow.add_edge("perceive", "react")
    workflow.add_edge("react", "execute")
    workflow.add_edge("execute", "yield_results")
    workflow.add_edge("yield_results", END)
    
    return workflow.compile()

# Test it
if __name__ == "__main__":
    from src.models import MissionIntent
    
    mission = MissionIntent(
        description="What is 2 + 2?",
        rationale="Test single agent"
    )
    
    agent = AgentState(
        agent_id="test-agent-0",
        role=AgentRole.SHAPER,
        current_mission=mission
    )
    
    workflow = build_prey_loop()
    result = workflow.invoke(agent)
    
    print(f"Agent {result.agent_id} completed mission!")
    print(f"Confidence: {result.confidence_score}")
    print(f"Memory: {result.short_term_memory}")
```

**Deliverable:** `pytest tests/test_prey_agent.py` passes

---

## 📅 Week 2: Scatter-Gather (Parallelization)

### Day 3-5: Ray Scatter-Gather
**File:** `src/orchestrator/scatter_gather.py`

```python
import ray
from typing import List
from src.agents.prey_agent import build_prey_loop
from src.models import MissionIntent, AgentState, AgentRole

@ray.remote
class PreyActor:
    """
    Ray actor wrapper for PREY agent.
    Each actor runs independently in parallel.
    """
    
    def __init__(self, agent_id: str, role: AgentRole):
        self.agent_id = agent_id
        self.role = role
        self.workflow = build_prey_loop()
    
    def execute_mission(self, mission: MissionIntent) -> dict:
        """Run PREY loop and return result"""
        agent_state = AgentState(
            agent_id=self.agent_id,
            role=self.role,
            current_mission=mission
        )
        
        result = self.workflow.invoke(agent_state)
        
        return {
            "agent_id": result.agent_id,
            "role": result.role.value,
            "response": result.short_term_memory[-1],
            "confidence": result.confidence_score
        }

def scatter_gather(mission: MissionIntent) -> List[dict]:
    """
    Main scatter-gather orchestrator.
    
    1. Spawn N Ray actors
    2. Scatter mission to all actors
    3. Gather results
    """
    
    # Initialize Ray
    if not ray.is_initialized():
        ray.init(ignore_reinit_error=True)
    
    # Spawn agents
    n_agents = mission.swarm_size
    n_disruptors = mission.disruptor_min  # Simplify for MVP
    
    actors = []
    for i in range(n_agents):
        role = AgentRole.DISRUPTOR if i < n_disruptors else AgentRole.SHAPER
        actor = PreyActor.remote(f"agent-{i}", role)
        actors.append(actor)
    
    # Scatter
    futures = [actor.execute_mission.remote(mission) for actor in actors]
    
    # Gather
    results = ray.get(futures)
    
    return results

# Test it
if __name__ == "__main__":
    mission = MissionIntent(
        description="What is 2 + 2?",
        rationale="Test scatter-gather",
        swarm_size=10,
        disruptor_min=1
    )
    
    results = scatter_gather(mission)
    
    print(f"Gathered {len(results)} responses:")
    for r in results[:3]:
        print(f"  - {r['agent_id']} ({r['role']}): confidence={r['confidence']}")
```

**Deliverable:** 10 agents run in parallel, complete in <30 seconds

---

## 📅 Week 3: Byzantine Quorum (Consensus)

### Day 6-8: Voting & Synthesis
**File:** `src/review/byzantine_quorum.py`

```python
from typing import List, Dict
from collections import Counter

def byzantine_vote(
    results: List[dict],
    max_confidence: float = 0.90
) -> Dict[str, any]:
    """
    Simple majority voting with confidence capping.
    
    TODO: Upgrade to actual Byzantine algorithm (PBFT, etc.)
    """
    
    # Extract responses
    responses = [r["response"] for r in results]
    
    # Count occurrences
    vote_counts = Counter(responses)
    consensus = vote_counts.most_common(1)[0][0]
    
    # Calculate confidence
    raw_confidence = vote_counts[consensus] / len(responses)
    capped_confidence = min(raw_confidence, max_confidence)
    
    # Detect disruptors (agents voting against consensus)
    disruptors = [
        r["agent_id"] for r in results 
        if r["response"] != consensus
    ]
    
    return {
        "consensus": consensus,
        "confidence": capped_confidence,
        "total_votes": len(results),
        "disruptors_detected": len(disruptors),
        "disruptor_ids": disruptors,
        "quorum_met": capped_confidence >= 0.66
    }

def synthesize_final_artifact(
    mission: MissionIntent,
    scatter_results: List[dict],
    vote_results: Dict[str, any]
) -> Dict[str, any]:
    """
    Create final artifact for user.
    
    TODO: Use Navigator LLM for synthesis
    """
    
    return {
        "mission": mission.description,
        "answer": vote_results["consensus"],
        "confidence": vote_results["confidence"],
        "evidence": {
            "swarm_size": mission.swarm_size,
            "disruptors_injected": mission.disruptor_min,
            "disruptors_detected": vote_results["disruptors_detected"],
            "quorum_met": vote_results["quorum_met"]
        },
        "status": "complete" if vote_results["quorum_met"] else "failed"
    }
```

**Deliverable:** End-to-end demo works

---

## 🎬 Final Demo Script
**File:** `demo.py`

```python
#!/usr/bin/env python3
"""
Byzantine Scatter-Gather MVP Demo

Usage: python demo.py "What is the capital of France?"
"""

import sys
from src.models import MissionIntent
from src.orchestrator.scatter_gather import scatter_gather
from src.review.byzantine_quorum import byzantine_vote, synthesize_final_artifact

def main(question: str):
    print("=" * 70)
    print("🦅 HIVE FLEET OBSIDIAN: Byzantine Scatter-Gather")
    print("=" * 70)
    print()
    
    # 1. Create mission
    mission = MissionIntent(
        description=question,
        rationale="User query",
        swarm_size=10,
        disruptor_min=1,
        disruptor_max=3
    )
    
    print(f"📋 Mission: {mission.description}")
    print(f"🦅 Swarm Size: {mission.swarm_size}")
    print()
    
    # 2. Scatter-Gather
    print("⏳ Scattering to agents...")
    results = scatter_gather(mission)
    print(f"✅ Gathered {len(results)} responses")
    print()
    
    # 3. Byzantine Vote
    print("⚖️  Conducting Byzantine vote...")
    vote = byzantine_vote(results)
    print(f"   Consensus: {vote['consensus'][:100]}...")
    print(f"   Confidence: {vote['confidence']:.1%}")
    print(f"   Disruptors Detected: {vote['disruptors_detected']}")
    print()
    
    # 4. Synthesize
    artifact = synthesize_final_artifact(mission, results, vote)
    
    print("✅ FINAL ANSWER:")
    print(f"   {artifact['answer']}")
    print(f"   Confidence: {artifact['confidence']:.1%}")
    print(f"   Status: {artifact['status']}")
    print()
    print("=" * 70)

if __name__ == "__main__":
    question = sys.argv[1] if len(sys.argv) > 1 else "What is 2 + 2?"
    main(question)
```

**Run:**
```bash
python demo.py "What is the capital of France?"
```

---

## 🧪 Testing Strategy

Create these test files:

### `tests/test_prey_agent.py`
```python
def test_prey_agent_completes_mission():
    """Verify single agent can complete PREY loop"""
    # ... test code

def test_prey_agent_uses_correct_model():
    """Verify FinOps model selection works"""
    # ... test code
```

### `tests/test_scatter_gather.py`
```python
def test_scatter_creates_n_agents():
    """Verify Ray spawns correct number of agents"""
    # ... test code

def test_gather_collects_all_responses():
    """Verify no responses are lost"""
    # ... test code
```

### `tests/test_byzantine_quorum.py`
```python
def test_vote_detects_disruptors():
    """Verify voting identifies minority"""
    # ... test code

def test_confidence_capped_at_90():
    """Verify confidence never exceeds 90%"""
    # ... test code
```

---

## 📊 Success Metrics

**Week 1 Checkpoint:**
- [ ] Single PREY agent works
- [ ] Agent uses Grok model from OpenRouter
- [ ] Confidence score calculated

**Week 2 Checkpoint:**
- [ ] 10 agents run in parallel
- [ ] Ray cluster functional
- [ ] All responses gathered correctly

**Week 3 Checkpoint:**
- [ ] Byzantine vote works
- [ ] Disruptors detected
- [ ] End-to-end demo runs

**MVP Complete:**
- [ ] `demo.py` works for any question
- [ ] Response time < 60 seconds
- [ ] Confidence typically 70-90%
- [ ] Costs < $0.05 per query

---

## 💰 Cost Estimate

**Per Query (10 agents, Grok model):**
- Input: ~100 tokens × 10 agents = 1,000 tokens
- Output: ~200 tokens × 10 agents = 2,000 tokens
- Cost: (1,000 × $0.00028/1K + 2,000 × $0.00028/1K) ≈ **$0.001 per query**

**At scale:**
- 1,000 queries/day = $1/day = $30/month ✅ Affordable
- 10,000 queries/day = $10/day = $300/month ⚠️ Monitor

---

## 🔄 Next Steps After MVP

1. **Add NATS Stigmergy** - Agents communicate via blackboard
2. **Integrate Temporal** - Durable workflows for long-running tasks
3. **Add MAP-Elites** - Evolve swarm parameters
4. **Optimize with DSPy** - Auto-tune prompts
5. **Scale to 100+ agents** - Stress test Byzantine quorum
6. **Production monitoring** - LangSmith + Grafana dashboard

---

**Document Version:** 1.0  
**Last Updated:** 2025-11-20  
**Status:** Ready for execution
