# 🔬 Technical Deep Dive: Implementation Roadmap
## HFO Gen 50 - From Blueprint to Reality

**Companion to**: EXECUTIVE_DIGEST.md  
**Audience**: Implementation Team  
**Focus**: Code-level guidance for Phase 1

---

## 🎯 Phase 1 Implementation Guide

### Goal
Build a **minimal viable Byzantine quorum system** that actually runs:
- User provides intent
- Navigator spawns 3 agents via Ray
- Each agent calls OpenRouter API
- Results gathered and voted on via simple quorum
- Final synthesis returned

### Timeline
**2 weeks** (conservative estimate)

---

## 📝 Step-by-Step Implementation

### Step 1: OpenRouter API Client (Day 1-2)

**File**: `src/api/openrouter_client.py`

```python
"""
OpenRouter API Client
Wraps LangChain's ChatOpenAI to use OpenRouter models.
"""
from typing import Dict, Any, Optional
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from src.config.settings import settings
from src.models.intent import MissionIntent

class OpenRouterClient:
    def __init__(self, model: str, temperature: float = 0.7):
        self.model = model
        self.client = ChatOpenAI(
            model=model,
            openai_api_base=settings.openrouter_base_url,
            openai_api_key=settings.openrouter_api_key,
            temperature=temperature,
        )
    
    def generate(self, prompt: str, system_prompt: Optional[str] = None) -> str:
        messages = []
        if system_prompt:
            messages.append(SystemMessage(content=system_prompt))
        messages.append(HumanMessage(content=prompt))
        
        response = self.client.invoke(messages)
        return response.content
    
    @classmethod
    def from_intent(cls, intent: MissionIntent, role: str = "execution"):
        """Create client from mission intent."""
        if role == "coordination":
            # Use navigator models
            model = "x-ai/grok-4.1-fast"
        else:
            # Use swarm models
            model = "google/gemini-2.5-flash-lite-sep"
        
        return cls(model=model)
```

**Test**: `tests/test_openrouter_client.py`

```python
import pytest
from src.api.openrouter_client import OpenRouterClient
from src.models.intent import MissionIntent

@pytest.mark.skipif(not os.getenv("OPENROUTER_API_KEY"), reason="No API key")
def test_openrouter_basic_call():
    client = OpenRouterClient(model="google/gemini-2.5-flash-lite-sep")
    response = client.generate("What is 2+2?")
    assert "4" in response or "four" in response.lower()

def test_openrouter_from_intent():
    intent = MissionIntent(description="Test", rationale="Test")
    client = OpenRouterClient.from_intent(intent, role="execution")
    assert client.model in ["google/gemini-2.5-flash-lite-sep", "qwen/qwen3-next-80b-a3b-instruct"]
```

---

### Step 2: Ray-Based Scatter Pattern (Day 3-5)

**File**: `src/swarm/scatter.py`

```python
"""
Scatter-Gather Pattern using Ray
Spawns N agents as Ray actors, each making independent API calls.
"""
import ray
from typing import List, Dict, Any
from dataclasses import dataclass
from src.api.openrouter_client import OpenRouterClient
from src.models.intent import MissionIntent

@dataclass
class AgentResult:
    agent_id: str
    response: str
    model_used: str
    confidence: float = 0.0

@ray.remote
class ResearchAgent:
    def __init__(self, agent_id: str, model: str):
        self.agent_id = agent_id
        self.model = model
        self.client = OpenRouterClient(model=model)
    
    def execute(self, prompt: str) -> AgentResult:
        response = self.client.generate(prompt)
        return AgentResult(
            agent_id=self.agent_id,
            response=response,
            model_used=self.model,
            confidence=0.8  # Mock for now
        )

class SwarmScatter:
    def __init__(self, intent: MissionIntent):
        self.intent = intent
        self.agents = []
    
    def spawn_agents(self, n: int = 3) -> List:
        """Spawn N Ray actors."""
        if not ray.is_initialized():
            ray.init(ignore_reinit_error=True)
        
        models = ["google/gemini-2.5-flash-lite-sep", "qwen/qwen3-next-80b-a3b-instruct", "deepseek/deepseek-v3.2-exp"]
        
        self.agents = [
            ResearchAgent.remote(agent_id=f"agent-{i}", model=models[i % len(models)])
            for i in range(n)
        ]
        return self.agents
    
    def scatter(self, prompt: str) -> List[ray.ObjectRef]:
        """Send same prompt to all agents."""
        return [agent.execute.remote(prompt) for agent in self.agents]
    
    def gather(self, object_refs: List[ray.ObjectRef]) -> List[AgentResult]:
        """Wait for all agents to complete."""
        return ray.get(object_refs)
```

**Test**: `tests/test_scatter.py`

```python
import ray
from src.swarm.scatter import SwarmScatter, AgentResult
from src.models.intent import MissionIntent

def test_scatter_spawn():
    intent = MissionIntent(description="Test", rationale="Test")
    swarm = SwarmScatter(intent)
    agents = swarm.spawn_agents(n=3)
    assert len(agents) == 3

@pytest.mark.skipif(not os.getenv("OPENROUTER_API_KEY"), reason="No API key")
def test_scatter_gather_flow():
    intent = MissionIntent(description="Research task", rationale="Test scatter-gather")
    swarm = SwarmScatter(intent)
    swarm.spawn_agents(n=3)
    
    refs = swarm.scatter("What is the capital of France?")
    results = swarm.gather(refs)
    
    assert len(results) == 3
    assert all("Paris" in r.response for r in results)
```

---

### Step 3: Mock Byzantine Quorum (Day 6-8)

**File**: `src/swarm/quorum.py`

```python
"""
Byzantine Quorum - Mock Implementation
Uses simple majority voting and similarity checking.
"""
from typing import List, Dict, Any, Tuple
from collections import Counter
from dataclasses import dataclass
from src.swarm.scatter import AgentResult

@dataclass
class QuorumDecision:
    approved: bool
    consensus_response: str
    confidence: float
    vote_distribution: Dict[str, int]
    participating_agents: int

class ByzantineQuorum:
    def __init__(self, min_quorum: float = 0.67):
        """
        Args:
            min_quorum: Minimum agreement ratio (e.g., 0.67 = 2/3 majority)
        """
        self.min_quorum = min_quorum
    
    def vote(self, results: List[AgentResult]) -> QuorumDecision:
        """
        Perform simple voting based on response similarity.
        
        Algorithm:
        1. Group similar responses (using first 100 chars as proxy)
        2. Find majority cluster
        3. Check if majority >= min_quorum
        4. Cap confidence at 90% (persistent green is a code smell)
        """
        if not results:
            return QuorumDecision(
                approved=False,
                consensus_response="",
                confidence=0.0,
                vote_distribution={},
                participating_agents=0
            )
        
        # Simple grouping by response prefix (mock similarity)
        response_groups = Counter()
        response_map = {}
        
        for result in results:
            key = result.response[:100]  # First 100 chars as "fingerprint"
            response_groups[key] += 1
            if key not in response_map:
                response_map[key] = result.response
        
        # Find majority
        most_common_key, count = response_groups.most_common(1)[0]
        consensus_response = response_map[most_common_key]
        
        # Calculate agreement ratio
        agreement_ratio = count / len(results)
        approved = agreement_ratio >= self.min_quorum
        
        # Cap confidence at 90%
        confidence = min(0.90, agreement_ratio)
        
        return QuorumDecision(
            approved=approved,
            consensus_response=consensus_response,
            confidence=confidence,
            vote_distribution=dict(response_groups),
            participating_agents=len(results)
        )
```

**Test**: `tests/test_quorum.py`

```python
from src.swarm.quorum import ByzantineQuorum, QuorumDecision
from src.swarm.scatter import AgentResult

def test_unanimous_vote():
    results = [
        AgentResult("a1", "Paris is the capital", "model1", 0.9),
        AgentResult("a2", "Paris is the capital", "model2", 0.9),
        AgentResult("a3", "Paris is the capital", "model3", 0.9),
    ]
    
    quorum = ByzantineQuorum(min_quorum=0.67)
    decision = quorum.vote(results)
    
    assert decision.approved == True
    assert decision.confidence == 0.90  # Capped at 90%
    assert "Paris" in decision.consensus_response

def test_split_vote_fails():
    results = [
        AgentResult("a1", "Paris", "model1", 0.9),
        AgentResult("a2", "London", "model2", 0.9),
        AgentResult("a3", "Berlin", "model3", 0.9),
    ]
    
    quorum = ByzantineQuorum(min_quorum=0.67)
    decision = quorum.vote(results)
    
    assert decision.approved == False
    assert decision.confidence < 0.67

def test_two_thirds_majority_passes():
    results = [
        AgentResult("a1", "Paris", "model1", 0.9),
        AgentResult("a2", "Paris", "model2", 0.9),
        AgentResult("a3", "London", "model3", 0.9),  # Disruptor
    ]
    
    quorum = ByzantineQuorum(min_quorum=0.67)
    decision = quorum.vote(results)
    
    assert decision.approved == True
    assert decision.confidence >= 0.67
    assert decision.confidence <= 0.90
```

---

### Step 4: End-to-End Orchestrator (Day 9-10)

**File**: `src/orchestrator/navigator.py`

```python
"""
Navigator - Top-level orchestrator
Implements user → orchestrator → scatter → gather → review → synthesis pattern.
"""
from src.models.intent import MissionIntent
from src.swarm.scatter import SwarmScatter
from src.swarm.quorum import ByzantineQuorum, QuorumDecision
from src.api.openrouter_client import OpenRouterClient
from dataclasses import dataclass

@dataclass
class SynthesisArtifact:
    intent: MissionIntent
    decision: QuorumDecision
    final_output: str
    swarm_size: int

class Navigator:
    def __init__(self, intent: MissionIntent):
        self.intent = intent
        self.swarm = SwarmScatter(intent)
        self.quorum = ByzantineQuorum(min_quorum=0.67)
    
    def execute(self) -> SynthesisArtifact:
        """
        Main execution flow:
        1. Set - Load intent (already done)
        2. Watch - Log to LangSmith (TODO)
        3. Act - Scatter-gather
        4. Review - Byzantine quorum
        5. Mutate - Evolution (TODO)
        """
        # Act - Scatter
        self.swarm.spawn_agents(n=self.intent.swarm_size)
        prompt = f"Task: {self.intent.description}\n\nRationale: {self.intent.rationale}"
        
        refs = self.swarm.scatter(prompt)
        results = self.swarm.gather(refs)
        
        # Review - Quorum
        decision = self.quorum.vote(results)
        
        # Synthesis
        if decision.approved:
            final_output = self._synthesize(decision.consensus_response)
        else:
            final_output = "QUORUM FAILED - No consensus reached"
        
        return SynthesisArtifact(
            intent=self.intent,
            decision=decision,
            final_output=final_output,
            swarm_size=len(results)
        )
    
    def _synthesize(self, consensus: str) -> str:
        """Use Navigator model to synthesize final output."""
        client = OpenRouterClient(model="x-ai/grok-4.1-fast")
        
        synthesis_prompt = f"""
You are the Navigator AI synthesizing results from a swarm of {self.intent.swarm_size} agents.

Original Intent: {self.intent.description}
Rationale: {self.intent.rationale}

Swarm Consensus Output:
{consensus}

Provide a final, polished synthesis that addresses the original intent.
"""
        return client.generate(synthesis_prompt)
```

**Integration Test**: `tests/test_end_to_end.py`

```python
import pytest
from src.models.intent import MissionIntent
from src.orchestrator.navigator import Navigator

@pytest.mark.skipif(not os.getenv("OPENROUTER_API_KEY"), reason="No API key")
def test_full_pipeline():
    intent = MissionIntent(
        description="What are the key features of Python 3.12?",
        rationale="Research for technical blog post",
        swarm_size=3
    )
    
    navigator = Navigator(intent)
    artifact = navigator.execute()
    
    assert artifact.decision.approved == True
    assert artifact.decision.confidence >= 0.67
    assert len(artifact.final_output) > 100
    assert "Python" in artifact.final_output
```

---

## 📊 Validation Checklist

After Phase 1 implementation, verify:

- [ ] OpenRouter client makes successful API calls
- [ ] Ray spawns multiple agents concurrently
- [ ] Scatter pattern distributes work correctly
- [ ] Gather pattern collects all results
- [ ] Byzantine quorum votes correctly
- [ ] 2/3 majority passes, 1/3 fails
- [ ] Confidence capped at 90%
- [ ] Synthesis produces coherent output
- [ ] End-to-end test passes
- [ ] FinOps: 3 agents × 1 call ≈ $0.001 per run

---

## 🔄 Phase 2 Preview

Once Phase 1 works, add:

1. **NATS Messaging**: Replace Python lists with JetStream
2. **LangSmith Tracing**: Add observability to all steps
3. **Temporal Workflows**: Make it durable and retryable
4. **PREY Loop**: Add Perceive-React-Execute-Yield per agent
5. **Disruptor Injection**: Randomly inject 1-2 bad agents
6. **Immunizer Detection**: Blue team tries to catch disruptors

---

## 🎯 Success Metrics

Phase 1 is complete when:

1. ✅ User can provide `MissionIntent` object
2. ✅ Navigator spawns N agents (3-10)
3. ✅ Each agent calls OpenRouter API
4. ✅ Results aggregated via Byzantine quorum
5. ✅ Final synthesis returned
6. ✅ End-to-end test passes
7. ✅ Cost per run < $0.01

**Time to Value**: ~10 days (conservative)

---

## 💡 Pro Tips

1. **Start with n=3 agents**: Faster iteration, cheaper costs
2. **Use free models first**: `servicenow/apriel` is free on OpenRouter
3. **Mock similarity detection**: First 100 chars is good enough for MVP
4. **Skip NATS initially**: Python lists work fine for 3-10 agents
5. **Log everything**: Add print statements liberally
6. **Test incrementally**: Don't write all code then test
7. **Use pytest markers**: Skip expensive API tests in CI

---

## 📚 References

- **Ray Actors**: https://docs.ray.io/en/latest/ray-core/actors.html
- **LangChain ChatOpenAI**: https://python.langchain.com/docs/integrations/chat/openai
- **OpenRouter API**: https://openrouter.ai/docs
- **Byzantine Quorum**: Lamport et al. (1982) - Byzantine Generals Problem

---

**Generated**: 2025-11-20  
**Target Audience**: Implementation Team  
**Estimated Effort**: 2 weeks (Phase 1 only)
