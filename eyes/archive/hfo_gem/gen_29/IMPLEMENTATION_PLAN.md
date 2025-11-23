---
hexagon:
  ontos:
    id: 431d0ea5-0584-427f-8624-cf2cf14d516d
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.991117Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_29/IMPLEMENTATION_PLAN.md
    links: []
  telos:
    viral_factor: 0.0
    meme: IMPLEMENTATION_PLAN.md
---
# Gen 29 → Production: Phased Implementation Plan

**Date**: 2025-11-11
**Goal**: Incrementally add OBSIDIAN roles + Hourglass to working Gen 29 swarm
**Principle**: Each phase is independently valuable and testable

---

## Current State Analysis

### ✅ What Already Exists (Gen 29 Code)

**Working Components**:
- `PREYOrchestrator` class with LangGraph StateGraph
- 4 specialized agent classes with distinct system prompts
- Artifact management (`SwarmRunArtifacts`)
- Swarmlord digest generation (`generate_swarmlord_digest`)
- Database integration (PostgreSQL + pgvector)
- Parallel execution (ThreadPoolExecutor)

**Agent Classes**:
```python
InterpreterAgent    # SENSE: Extract mission intent (temp=0.3, precise)
ResearcherAgent     # ACT: Execute research (temp=0.8, creative)
ValidatorAgent      # YIELD: Quorum + hallucination detection (temp=0.3, objective)
SynthesizerAgent    # YIELD: Generate digest (temp=0.5, structured)
```

**Entry Point**:
```python
orchestrator = PREYOrchestrator()
digest = orchestrator.execute(
    intent="Research Kubernetes best practices",
    constraints="Focus on production deployments"
)
```

---

## OBSIDIAN Role Mapping (Current → Target)

| OBSIDIAN Role | Current Agent | Status | Phase |
|---------------|---------------|--------|-------|
| **B** Bridger (Intent translation) | InterpreterAgent | ✅ Exists | Phase 1 (rename) |
| **S** Shaper (Execution) | ResearcherAgent | ✅ Exists | Phase 1 (rename) |
| **I₂** Immunizer (Blue team) | ValidatorAgent | ✅ Exists | Phase 1 (rename) |
| **A** Assimilator (Synthesis) | SynthesizerAgent | ✅ Exists | Phase 1 (rename) |
| **O** Observer (Telemetry) | *Missing* | ❌ Need to create | Phase 1 (new) |
| **N** Navigator (Strategy/C2) | *Missing* | ❌ Need to create | Phase 2 (orchestrator wrapper) |
| **I₁** Injector (Resources) | *Missing* | ❌ Need to create | Phase 3 (cost management) |
| **D** Disruptor (Red team) | *Missing* | ❌ Need to create | Phase 3 (adversarial) |

---

## Phase 1: OBSIDIAN Role Integration (Week 1)

**Goal**: Add OBSIDIAN role abstraction to existing agents + create Observer

**Effort**: 4-6 hours
**Value**: Use OBSIDIAN playbook terminology, enable telemetry collection

### Changes Required

#### 1.1 Create `hfo_swarm/obsidian_roles.py` (NEW FILE)

Base class for all OBSIDIAN roles:

```python
"""
OBSIDIAN Role Abstraction Layer

Maps Gen 29 agents to OBSIDIAN 8-role framework (JADC2-aligned)
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from datetime import datetime
import json


class OBSIDIANRole(ABC):
    """
    Base class for all OBSIDIAN roles.

    JADC2 Mapping:
    - Sense → Perceive (PREY)
    - Make Sense → React (PREY)
    - Act → Execute (PREY)
    - Feedback → Yield (PREY)
    """

    def __init__(self, role_code: str, role_name: str):
        self.role_code = role_code  # "B", "S", "O", etc.
        self.role_name = role_name  # "Bridger", "Shaper", etc.
        self.telemetry = []  # Observer will collect this

    @abstractmethod
    def execute_role(self, **kwargs) -> Dict[str, Any]:
        """Execute this role's primary function."""
        pass

    def log_telemetry(self, phase: str, data: Dict[str, Any]):
        """Log telemetry for Observer role to collect."""
        self.telemetry.append({
            "timestamp": datetime.utcnow().isoformat(),
            "role": self.role_code,
            "phase": phase,
            "data": data
        })


class BridgerRole(OBSIDIANRole):
    """
    Bridger (B): Intent Translation
    JADC2: Sense → Make Sense (convert natural language to mission structure)
    """
    def __init__(self, interpreter_agent):
        super().__init__("B", "Bridger")
        self.interpreter = interpreter_agent

    def execute_role(self, user_input: str) -> Dict[str, Any]:
        """Translate user intent into structured mission."""
        self.log_telemetry("sense", {"input_length": len(user_input)})

        result = self.interpreter.interpret(user_input)

        self.log_telemetry("react", {
            "mission_intent": result.get("mission_intent"),
            "has_constraints": bool(result.get("constraints"))
        })

        return result


class ShaperRole(OBSIDIANRole):
    """
    Shaper (S): Execution
    JADC2: Act (dispatch and coordinate swarm workers)
    """
    def __init__(self, researcher_agent):
        super().__init__("S", "Shaper")
        self.researcher = researcher_agent

    def execute_role(self, prompt: str, worker_id: int) -> str:
        """Execute research mission."""
        self.log_telemetry("act", {"worker_id": worker_id, "prompt_length": len(prompt)})

        result = self.researcher.research(prompt, worker_id)

        self.log_telemetry("yield", {"response_length": len(result)})

        return result


class ImmunizerRole(OBSIDIANRole):
    """
    Immunizer (I₂): Blue Team / Quality Validation
    JADC2: Feedback (validate quality, detect threats)
    """
    def __init__(self, validator_agent):
        super().__init__("I2", "Immunizer")
        self.validator = validator_agent

    def execute_role(self, responses: list, mode: str) -> Dict[str, Any]:
        """Validate swarm outputs (quorum or hallucinations)."""
        self.log_telemetry("sense", {"num_responses": len(responses), "mode": mode})

        if mode == "quorum":
            result = self.validator.analyze_quorum(responses)
        elif mode == "hallucinations":
            result = self.validator.detect_hallucinations(responses)
        else:
            result = {"error": f"Unknown mode: {mode}"}

        self.log_telemetry("yield", {"result_keys": list(result.keys())})

        return result


class AssimilatorRole(OBSIDIANRole):
    """
    Assimilator (A): Knowledge Fusion
    JADC2: Feedback (synthesize learnings into actionable artifacts)
    """
    def __init__(self, synthesizer_agent):
        super().__init__("A", "Assimilator")
        self.synthesizer = synthesizer_agent

    def execute_role(self, mission_data: Dict[str, Any]) -> str:
        """Synthesize swarm outputs into digest."""
        self.log_telemetry("sense", {"data_keys": list(mission_data.keys())})

        result = self.synthesizer.synthesize(mission_data)

        self.log_telemetry("yield", {"digest_length": len(result)})

        return result


class ObserverRole(OBSIDIANRole):
    """
    Observer (O): Telemetry Collection
    JADC2: Sense (collect all signals across swarm execution)
    """
    def __init__(self):
        super().__init__("O", "Observer")
        self.collected_telemetry = []

    def execute_role(self, roles: list) -> Dict[str, Any]:
        """Collect telemetry from all roles."""
        self.log_telemetry("sense", {"num_roles": len(roles)})

        for role in roles:
            if hasattr(role, 'telemetry'):
                self.collected_telemetry.extend(role.telemetry)

        summary = self._analyze_telemetry()

        self.log_telemetry("yield", summary)

        return {
            "telemetry": self.collected_telemetry,
            "summary": summary
        }

    def _analyze_telemetry(self) -> Dict[str, Any]:
        """Basic telemetry analysis."""
        if not self.collected_telemetry:
            return {}

        phases = {}
        for entry in self.collected_telemetry:
            phase = entry.get("phase", "unknown")
            phases[phase] = phases.get(phase, 0) + 1

        return {
            "total_events": len(self.collected_telemetry),
            "phase_counts": phases,
            "roles_active": len(set(e.get("role") for e in self.collected_telemetry))
        }
```

#### 1.2 Update `hfo_swarm/prey_orchestrator.py`

Add OBSIDIAN role wrappers (minimal changes):

```python
# Add import at top
from hfo_swarm.obsidian_roles import (
    BridgerRole, ShaperRole, ImmunizerRole, AssimilatorRole, ObserverRole
)

# In PREYOrchestrator.__init__, after creating agents:
class PREYOrchestrator:
    def __init__(self):
        # Existing agent creation
        self.interpreter = InterpreterAgent()
        self.researcher = ResearcherAgent()
        self.validator = ValidatorAgent()
        self.synthesizer = SynthesizerAgent()

        # NEW: OBSIDIAN role wrappers
        self.bridger = BridgerRole(self.interpreter)        # B
        self.shaper = ShaperRole(self.researcher)           # S
        self.immunizer = ImmunizerRole(self.validator)      # I₂
        self.assimilator = AssimilatorRole(self.synthesizer) # A
        self.observer = ObserverRole()                      # O

        # Track roles for telemetry
        self.active_roles = [self.bridger, self.shaper, self.immunizer, self.assimilator]
```

Update `_sense` node to use Bridger:

```python
def _sense(self, state: PREYState) -> PREYState:
    """PREY: Sense/Perceive - Extract mission intent (Bridger role)"""
    print("🔍 PREY Phase: SENSE (Bridger)")

    # Use OBSIDIAN Bridger role
    interpretation = self.bridger.execute_role(user_input=state["user_input"])

    return {
        **state,
        "mission_intent": interpretation.get("mission_intent"),
        "constraints": interpretation.get("constraints"),
        "orchestration_prompt": interpretation.get("orchestration_prompt"),
        "timestamp_sense": datetime.now(timezone.utc).isoformat()
    }
```

Update worker dispatch to use Shaper:

```python
def _execute_worker(self, worker_id: int, prompt: str) -> Dict[str, Any]:
    """Execute single worker using Shaper role."""
    start_time = time.time()

    # Use OBSIDIAN Shaper role
    response = self.shaper.execute_role(prompt=prompt, worker_id=worker_id)

    elapsed = time.time() - start_time

    return {
        "worker_id": worker_id,
        "response": response,
        "execution_time": elapsed
    }
```

Update validation to use Immunizer:

```python
def _yield_phase(self, state: PREYState) -> PREYState:
    """PREY: Yield/Feedback - Validate and synthesize (Immunizer + Assimilator roles)"""
    print("📊 PREY Phase: YIELD (Immunizer + Assimilator)")

    responses = [r["response"] for r in state["research_results"]]

    # Use OBSIDIAN Immunizer for validation
    quorum_analysis = self.immunizer.execute_role(responses=responses, mode="quorum")
    hallucinations = self.immunizer.execute_role(responses=responses, mode="hallucinations")

    # Collect telemetry using Observer
    telemetry = self.observer.execute_role(roles=self.active_roles)

    # ... rest of synthesis logic ...
```

### Validation Criteria (Phase 1)

- [ ] All existing tests pass (no regression)
- [ ] New `obsidian_roles.py` file created with 5 role classes
- [ ] `PREYOrchestrator` uses role wrappers (backward compatible)
- [ ] Telemetry collection works (Observer captures events)
- [ ] Run existing mission → verify OBSIDIAN roles in logs

**Test Command**:
```bash
python -c "
from hfo_swarm.prey_orchestrator import PREYOrchestrator
orch = PREYOrchestrator()
result = orch.execute('Test OBSIDIAN roles', 'None')
print('Roles active:', [r.role_code for r in orch.active_roles])
print('Telemetry events:', len(orch.observer.collected_telemetry))
"
```

---

## Phase 2: Simple Hourglass Flip (Week 2)

**Goal**: Implement single forward flip (PAST → PRESENT → FUTURE)

**Effort**: 6-8 hours
**Value**: Precedent retrieval improves research quality

### Changes Required

#### 2.1 Create `hfo_swarm/hourglass_components.py` (NEW FILE)

```python
"""
Obsidian Horizon Hourglass Components (Phase 2: Simple Flip)

Implements:
- PAST Cone: Precedent retrieval (pgvector search)
- PRESENT Diameter: Existing swarm execution
- FUTURE Cone: Simplified projection (statistics on outcomes)
"""

from typing import List, Dict, Any, Optional
import psycopg2
from psycopg2.extras import Json
import os


class PastCone:
    """
    PAST Cone: Hunt for precedents in pgvector archive.

    Simplified Phase 2 version: Just pgvector similarity search.
    Phase 3 will add: Internet search, CYNEFIN, CBR.
    """

    def __init__(self):
        self.db_conn = psycopg2.connect(os.getenv("DATABASE_URL"))

    def search_precedents(self, mission_intent: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """
        Search PAST cone for similar missions.

        Returns precedents with:
        - mission_intent
        - outcome summary
        - consensus score
        - artifacts
        """
        # Simple pgvector search (Phase 2)
        # Phase 3 will add decomposition, Internet, CYNEFIN

        cursor = self.db_conn.cursor()

        # Get embedding for mission intent (placeholder - use actual embedding model)
        # For Phase 2, use simple text search as fallback

        cursor.execute("""
            SELECT
                mission_intent,
                outcome_summary,
                consensus_score,
                artifacts_path
            FROM missions
            WHERE status = 'completed'
              AND mission_intent ILIKE %s
            ORDER BY created_at DESC
            LIMIT %s
        """, (f"%{mission_intent}%", top_k))

        results = cursor.fetchall()
        cursor.close()

        precedents = []
        for row in results:
            precedents.append({
                "mission_intent": row[0],
                "outcome_summary": row[1],
                "consensus_score": row[2],
                "artifacts_path": row[3]
            })

        return precedents


class FutureCone:
    """
    FUTURE Cone: Project outcomes based on precedents.

    Simplified Phase 2 version: Statistical projection.
    Phase 3 will add: Monte Carlo, A*, VM experiments.
    """

    def project_outcomes(self, precedents: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Project future outcomes based on past precedents.

        Phase 2: Simple statistics (average success rate)
        Phase 3: Monte Carlo simulation, risk analysis
        """
        if not precedents:
            return {
                "confidence": 0.5,  # No data, 50/50
                "projected_success_rate": 0.5,
                "recommendation": "No precedents found - proceed with caution"
            }

        # Calculate average consensus from precedents
        avg_consensus = sum(p.get("consensus_score", 0.5) for p in precedents) / len(precedents)

        return {
            "confidence": avg_consensus,
            "projected_success_rate": avg_consensus,
            "precedents_used": len(precedents),
            "recommendation": self._generate_recommendation(avg_consensus)
        }

    def _generate_recommendation(self, success_rate: float) -> str:
        if success_rate > 0.7:
            return "High confidence - proceed with standard approach"
        elif success_rate > 0.5:
            return "Medium confidence - review precedents carefully"
        else:
            return "Low confidence - consider alternative approaches"


class HourglassFlip:
    """
    Hourglass Flip Coordinator (Phase 2: Single Forward Flip)

    Implements: PAST → PRESENT → FUTURE
    Phase 3 will add: FUTURE → PAST (reverse flip), recursive flipping
    """

    def __init__(self, past_cone: PastCone, future_cone: FutureCone):
        self.past_cone = past_cone
        self.future_cone = future_cone

    def forward_flip(self, mission_intent: str, constraints: Optional[str] = None) -> Dict[str, Any]:
        """
        Single forward flip: PAST → (inject to PRESENT) → FUTURE

        Returns enriched mission data with precedents + projections
        """
        # PAST: Search for precedents
        precedents = self.past_cone.search_precedents(mission_intent, top_k=5)

        # FUTURE: Project outcomes
        projections = self.future_cone.project_outcomes(precedents)

        # Enrich orchestration prompt with precedents
        enriched_prompt = self._enrich_with_precedents(mission_intent, precedents)

        return {
            "mission_intent": mission_intent,
            "constraints": constraints,
            "precedents": precedents,
            "projections": projections,
            "enriched_prompt": enriched_prompt,
            "flip_type": "forward"
        }

    def _enrich_with_precedents(self, base_prompt: str, precedents: List[Dict[str, Any]]) -> str:
        """Inject precedents into orchestration prompt."""
        if not precedents:
            return base_prompt

        precedent_summary = "\n\n**PRECEDENTS FROM PAST MISSIONS:**\n"
        for i, p in enumerate(precedents, 1):
            precedent_summary += f"{i}. {p.get('mission_intent')} (consensus: {p.get('consensus_score', 0):.0%})\n"
            precedent_summary += f"   Outcome: {p.get('outcome_summary', 'N/A')}\n"

        precedent_summary += "\n**YOUR RESEARCH ANGLE:**\n"
        precedent_summary += "Focus on aspects NOT fully covered by precedents above.\n"

        return base_prompt + precedent_summary
```

#### 2.2 Create Navigator Role (Orchestrator Wrapper)

Add to `obsidian_roles.py`:

```python
class NavigatorRole(OBSIDIANRole):
    """
    Navigator (N): Strategic C2 / Campaign Management
    JADC2: All phases (orchestrates entire PREY loop + Hourglass flips)

    This is the "Swarmlord of Webs" - the master orchestrator.
    """
    def __init__(self, prey_orchestrator, hourglass_flip):
        super().__init__("N", "Navigator")
        self.orchestrator = prey_orchestrator
        self.hourglass = hourglass_flip

    def execute_role(self, mission_intent: str, constraints: Optional[str] = None, use_hourglass: bool = False) -> Dict[str, Any]:
        """
        Navigate mission execution (optionally using Hourglass).

        Phase 2: Single forward flip
        Phase 3: Recursive flipping with convergence detection
        """
        self.log_telemetry("sense", {"mission_intent": mission_intent, "use_hourglass": use_hourglass})

        if use_hourglass:
            # HOURGLASS FLIP: PAST → PRESENT → FUTURE
            flip_result = self.hourglass.forward_flip(mission_intent, constraints)

            self.log_telemetry("react", {
                "precedents_found": len(flip_result["precedents"]),
                "projected_confidence": flip_result["projections"]["confidence"]
            })

            # Execute swarm with enriched prompt
            digest = self.orchestrator.execute(
                intent=flip_result["enriched_prompt"],
                constraints=constraints
            )

            # Add hourglass metadata to result
            digest["hourglass"] = {
                "flip_type": "forward",
                "precedents": flip_result["precedents"],
                "projections": flip_result["projections"]
            }
        else:
            # Standard execution (no hourglass)
            digest = self.orchestrator.execute(
                intent=mission_intent,
                constraints=constraints
            )

        self.log_telemetry("yield", {"digest_generated": bool(digest)})

        return digest
```

#### 2.3 Update Entry Point

Add Hourglass option to `run_swarm.py`:

```python
from hfo_swarm.hourglass_components import PastCone, FutureCone, HourglassFlip
from hfo_swarm.obsidian_roles import NavigatorRole

# Create components
orchestrator = PREYOrchestrator()
past_cone = PastCone()
future_cone = FutureCone()
hourglass = HourglassFlip(past_cone, future_cone)

# Create Navigator (Swarmlord of Webs)
navigator = NavigatorRole(orchestrator, hourglass)

# Execute with Hourglass
result = navigator.execute_role(
    mission_intent="Research Kubernetes best practices",
    constraints="Focus on production",
    use_hourglass=True  # NEW: Enable Hourglass flip
)
```

### Validation Criteria (Phase 2)

- [ ] Precedent search returns similar past missions
- [ ] Orchestration prompt includes precedent summary
- [ ] Projections show confidence based on past success
- [ ] Navigator role coordinates Hourglass flip
- [ ] All Phase 1 tests still pass

**Test Command**:
```bash
python -c "
from hfo_swarm.prey_orchestrator import PREYOrchestrator
from hfo_swarm.hourglass_components import PastCone, FutureCone, HourglassFlip
from hfo_swarm.obsidian_roles import NavigatorRole

orch = PREYOrchestrator()
past = PastCone()
future = FutureCone()
hourglass = HourglassFlip(past, future)
navigator = NavigatorRole(orch, hourglass)

result = navigator.execute_role(
    mission_intent='Test Hourglass flip',
    use_hourglass=True
)

print('Precedents found:', len(result.get('hourglass', {}).get('precedents', [])))
print('Confidence:', result.get('hourglass', {}).get('projections', {}).get('confidence'))
"
```

---

## Phase 3: Full Hourglass (Week 3-4)

**Goal**: Recursive flipping, convergence detection, remaining OBSIDIAN roles

**Effort**: 12-16 hours
**Value**: Full state-action space exploration with anytime stopping

### Changes Required

1. **Reverse Flip** (FUTURE → PAST):
   - Postmortem analysis of swarm results
   - Archive learnings as new precedents
   - Retroflip outcomes into past cone

2. **Recursive Flipping**:
   - Convergence detection (probability distribution stability)
   - Multiple flip algorithms (Thompson, MCTS, A*)
   - Anytime stopping criteria

3. **Remaining OBSIDIAN Roles**:
   - Injector (I₁): Cost/resource management
   - Disruptor (D): Adversarial red-team testing

4. **Diameter Constraints**:
   - Calculate `d_present = min(budget/cost, time×throughput, √(energy×compute))`
   - Enforce limits on parallel workers

---

## Implementation Sequence (Step-by-Step)

### Week 1: Phase 1 (OBSIDIAN Roles)

**Day 1-2**:
1. Create `hfo_swarm/obsidian_roles.py`
2. Implement 5 role classes (Bridger, Shaper, Immunizer, Assimilator, Observer)
3. Write unit tests for each role

**Day 3-4**:
1. Update `PREYOrchestrator.__init__` to create role wrappers
2. Update `_sense` to use Bridger
3. Update `_execute_worker` to use Shaper
4. Update `_yield_phase` to use Immunizer + Assimilator + Observer

**Day 5**:
1. Integration testing (run full mission with OBSIDIAN roles)
2. Verify telemetry collection
3. Document role usage in code comments

### Week 2: Phase 2 (Simple Hourglass)

**Day 1-2**:
1. Create `hfo_swarm/hourglass_components.py`
2. Implement `PastCone` (pgvector search)
3. Implement `FutureCone` (statistical projection)
4. Implement `HourglassFlip` (forward flip only)

**Day 3-4**:
1. Create `NavigatorRole` in `obsidian_roles.py`
2. Update `run_swarm.py` entry point
3. Test precedent retrieval and prompt enrichment

**Day 5**:
1. Integration testing (compare with/without Hourglass)
2. Measure quality improvement from precedents
3. Document Hourglass usage

### Week 3-4: Phase 3 (Full Hourglass)

**Day 1-3**:
1. Implement reverse flip (FUTURE → PAST)
2. Add recursive flipping loop
3. Add convergence detection

**Day 4-5**:
1. Create Injector and Disruptor roles
2. Add diameter constraint enforcement
3. Full integration testing

**Day 6-7**:
1. Performance optimization
2. Documentation updates
3. User guide

---

## File Structure (After All Phases)

```
hfo_swarm/
├── __init__.py
├── prey_orchestrator.py          # Main orchestrator (updated)
├── obsidian_roles.py              # NEW: 8 OBSIDIAN role classes
├── hourglass_components.py        # NEW: Past/Future cones + flip logic
├── artifact_manager.py            # Existing (unchanged)
├── swarmlord_digest_format.py     # Existing (unchanged)
└── basic_swarm.py                 # Existing (legacy)

tests/
├── test_obsidian_roles.py         # NEW: Role unit tests
├── test_hourglass_components.py   # NEW: Hourglass unit tests
└── test_prey_orchestrator.py      # Existing (updated)

run_swarm.py                       # Entry point (updated)
```

---

## Success Metrics

### Phase 1
- [ ] All OBSIDIAN roles instantiated and callable
- [ ] Telemetry collection captures 10+ events per mission
- [ ] No regression in existing tests

### Phase 2
- [ ] Precedent search returns 3+ relevant past missions
- [ ] Enriched prompts improve consensus score by 5-10%
- [ ] Projections reflect historical success rates

### Phase 3
- [ ] Multi-flip convergence within 3-5 iterations
- [ ] Diameter constraints enforce budget limits
- [ ] Full OBSIDIAN role integration (all 8 roles active)

---

## Migration Path (Minimal Disruption)

**Backward Compatibility**:
- Existing `PREYOrchestrator.execute()` works unchanged
- OBSIDIAN roles wrap existing agents (no rewrite needed)
- Hourglass is opt-in via `use_hourglass=True` flag

**Progressive Enhancement**:
1. Phase 1: Add role abstraction (no behavior change)
2. Phase 2: Add precedent retrieval (optional improvement)
3. Phase 3: Add full flipping (advanced users only)

**Rollback Strategy**:
- Each phase is feature-flagged
- Can disable Hourglass with single flag
- All changes in new files (minimal edit to existing code)

---

**Next Step**: Start with Phase 1, Day 1 - create `obsidian_roles.py` with base class and 5 role implementations.
