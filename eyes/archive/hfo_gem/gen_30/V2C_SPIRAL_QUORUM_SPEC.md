---
hexagon:
  ontos:
    id: 37f1f7d0-1e7f-4376-aa3e-5795aea119ca
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.703591Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_30/V2C_SPIRAL_QUORUM_SPEC.md
    links: []
  telos:
    viral_factor: 0.0
    meme: V2C_SPIRAL_QUORUM_SPEC.md
---
# V²C-SPIRAL-QUORUM Protocol Specification

**Version**: 1.0.0
**Date**: 2025-11-12
**Status**: 🎯 FORMAL SPECIFICATION

---

## 📋 Executive Summary

**V²C-SPIRAL-QUORUM** is a hierarchical verification-validation-consensus protocol for iterative multi-agent research swarms with bidirectional feedback.

**Key Innovation**: Transforms unreliable LLM agents into reliable research systems through nested holonic loops, confidence-weighted quorum consensus, and Thompson Sampling-driven annealing schedules.

---

## 🔤 Acronym Breakdown (12-Letter Mnemonic)

### SPIRAL (Outer Loop - Strategic)
- **S** - **Scatter**: Disperse N researchers (10+ parallel agents)
- **P** - **Perceive**: (Sense) phase with precedent retrieval
- **I** - **Iterate**: Multi-round refinement (max_rounds parameter)
- **R** - **Refine**: Convergence toward HIGH consensus
- **A** - **Anneal**: Thompson Sampling temperature schedules
- **L** - **Loops**: Nested holonic PREY structure

### QUORUM (Inner Loop - Validation)
- **Q** - **Quality**: Quality Diversity (QD) algorithms (MAP-Elites)
- **U** - **Uncertainty**: Confidence-weighted epistemic scoring
- **O** - **Orchestrate**: Strategic coordination across scales
- **R** - **Recursive**: Self-similar PREY within PREY
- **U** - **Unify**: Quorum consensus synthesis
- **M** - **Multi-agent**: Swarm verification & validation

### V²C (Meta-Pattern)
- **Verification**: Chain-of-Verification (Meta AI 2023)
- **Validation**: Cross-researcher contradiction detection
- **Consensus**: Confidence-weighted quorum (not simple majority)

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   V²C-SPIRAL-QUORUM                         │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           SPIRAL (Strategic Orchestrator)           │   │
│  │                                                     │   │
│  │  Round 1: High temp (explore, 10 researchers)      │   │
│  │  Round 2: Medium temp (refine gaps, weighted)      │   │
│  │  Round 3: Low temp (HIGH consensus, stable)        │   │
│  │                                                     │   │
│  │  ┌──────────────────────────────────────────────┐  │   │
│  │  │      QUORUM (Validation & Consensus)         │  │   │
│  │  │                                              │  │   │
│  │  │  • Confidence scoring per claim              │  │   │
│  │  │  • Epistemic uncertainty quantification      │  │   │
│  │  │  • Weighted voting (not simple majority)     │  │   │
│  │  │  • Hallucination detection (contradiction)   │  │   │
│  │  │  • Quorum thresholds (HIGH/MEDIUM/LOW)       │  │   │
│  │  │                                              │  │   │
│  │  │  ┌───────────────────────────────────────┐  │  │   │
│  │  │  │    PREY (Worker Execution Loop)      │  │  │   │
│  │  │  │                                       │  │  │   │
│  │  │  │  (Sense) → (Make Sense) → (Execute)  │  │  │   │
│  │  │  │       ↑            ↓                  │  │  │   │
│  │  │  │       └──(Feedback)──┘                │  │  │   │
│  │  │  └───────────────────────────────────────┘  │  │   │
│  │  └──────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Three Nested Holonic Loops

### Level 1: SPIRAL Loop (Strategic - Minutes)

**State**: `PREYState`
```python
@dataclass
class PREYState:
    round_number: int
    mission_intent: str
    mission_constraints: str
    previous_digest: Optional[Dict]  # Bidirectional feedback
    researcher_outputs: List[Dict]
    validation_result: Dict
    synthesis_result: Dict
    convergence_status: str  # "HIGH" | "MEDIUM" | "LOW"
```

**Nodes**:
1. `_sense_node()`: Parse intent + retrieve precedents + incorporate previous round
2. `_make_sense_node()`: Generate research strategy based on gaps
3. `_execute_node()`: Scatter-gather N researchers (QUORUM loop)
4. `_feedback_node()`: Validate + Synthesize + Check convergence

**Edges**:
```python
def _should_continue(state: PREYState) -> bool:
    if state.round_number >= max_rounds:
        return False  # Max rounds reached
    if state.convergence_status == "HIGH":
        return False  # Consensus achieved
    if _findings_stable(state):
        return False  # 80%+ overlap with previous round
    return True  # Continue iterating
```

**Temperature Schedule** (Thompson Sampling):
```python
def get_temperature(round_num: int, max_rounds: int) -> float:
    # Annealing schedule: High → Low
    # Round 1: 0.8 (exploration)
    # Round 2: 0.5 (balanced)
    # Round 3: 0.3 (exploitation)
    return 0.8 - (0.5 * (round_num / max_rounds))
```

---

### Level 2: QUORUM Loop (Validation - Seconds)

**Purpose**: Transform N unreliable agent outputs into 1 reliable consensus

**Input**: List[ResearcherOutput]
**Output**: QuorumResult

```python
@dataclass
class ResearcherOutput:
    researcher_id: str
    findings: str
    confidence_scores: Dict[str, float]  # Per claim
    verified_claims: List[str]  # [VERIFIED] tags
    sources: List[str]
```

@dataclass
class QuorumResult:
    consensus_level: str  # "HIGH" | "MEDIUM" | "LOW"
    agreed_findings: List[str]  # 50%+ researchers agree
    contested_claims: List[str]  # <50% agreement
    hallucinations: List[str]  # Fabricated facts detected
    outliers: List[str]  # Researchers with unique perspectives
    confidence_weighted_summary: str
```

**Validation Steps**:

1. **Confidence Scoring**:
```python
# Each researcher self-scores claims
claim = "Kubernetes 1.28 supports cgroups v2"
confidence = 0.85  # 85% sure
verification = "[VERIFIED]" if has_source else ""
```

2. **Cross-Researcher Contradiction Detection**:
```python
# Compare all researchers for conflicts
R1: "Kubernetes 1.28 released in Aug 2023"
R2: "Kubernetes 1.28 released in Sep 2023" ← CONTRADICTION
R3: "Kubernetes 1.28 released in Aug 2023"
# Flag R2 as potential hallucination
```

3. **Weighted Quorum Calculation**:
```python
def calculate_quorum(claims: List[Claim]) -> float:
    # Not simple majority - weight by confidence
    total_weight = sum(c.confidence for c in claims)
    agreement_weight = sum(
        c.confidence for c in claims
        if c.text == dominant_claim
    )
    return agreement_weight / total_weight

# HIGH: >80% weighted agreement
# MEDIUM: 60-80%
# LOW: <60%
```

4. **Hallucination Detection**:
```python
# Flag claims that:
# - Have 100% confidence but no source
# - Contradict multiple other researchers
# - Include specific numbers without verification
# - Reference non-existent entities (fake papers, URLs)
```

---

### Level 3: PREY Loop (Worker Execution - Milliseconds)

**Standard 4-phase loop** (runs inside each researcher):

```python
class ResearcherAgent:
    def research(self, topic: str, constraints: str) -> ResearcherOutput:
        # SENSE: Understand research angle
        angle = self._sense(topic, constraints)

        # MAKE SENSE: Choose search strategy
        strategy = self._make_sense(angle)

        # EXECUTE: Web search with tools
        findings = self._execute(strategy)

        # FEEDBACK: Self-validate findings
        validated = self._feedback(findings)

        return validated
```

---

## 🌡️ Annealing Schedule (Thompson Sampling)

**Core Idea**: Start with high exploration (diversity), converge to exploitation (precision)

### Round 1: High Temperature (Exploration)
```python
temperature = 0.8
num_researchers = 10
diversity_bonus = True  # Reward unique perspectives
prompt_template = "Explore diverse angles on {topic}..."
```

**Goal**: Generate quality-diverse solution space (MAP-Elites)

### Round 2: Medium Temperature (Refinement)
```python
temperature = 0.5
num_researchers = 8
focus_gaps = True  # Address Round 1 gaps
prompt_template = """
Based on Round 1 findings:
{previous_digest}

Research specifically:
{identified_gaps}
"""
```

**Goal**: Fill knowledge gaps, resolve contradictions

### Round 3: Low Temperature (Convergence)
```python
temperature = 0.3
num_researchers = 5
precision_mode = True
prompt_template = """
Validate and refine:
{high_confidence_claims_from_round_2}

Provide sources and verification.
"""
```

**Goal**: Achieve HIGH consensus, stable findings

---

## 📊 Convergence Criteria

**Auto-stop when ANY condition met**:

### 1. Max Rounds Reached
```python
if state.round_number >= max_rounds:
    return STOP
```

### 2. HIGH Consensus Achieved
```python
if quorum_result.consensus_level == "HIGH":
    # >80% weighted agreement
    return STOP
```

### 3. Findings Stable
```python
def findings_stable(current, previous) -> bool:
    overlap = jaccard_similarity(
        current.agreed_findings,
        previous.agreed_findings
    )
    return overlap >= 0.8  # 80%+ overlap
```

### 4. Diminishing Returns
```python
if (new_findings_count < 2) and (round_number > 1):
    # Less than 2 new insights
    return STOP
```

---

## 🎯 Quality Metrics

### Hallucination Rate
```python
hallucination_rate = len(hallucinations) / total_claims
# Target: <5% with tools, <20% without
```

### Quorum Strength
```python
quorum_strength = agreement_weight / total_weight
# HIGH: >80%, MEDIUM: 60-80%, LOW: <60%
```

### Verification Rate
```python
verification_rate = len([VERIFIED] tags) / total_claims
# Target: >70% with web search tools
```

### Confidence Calibration
```python
# Are 90% confidence claims actually 90% accurate?
calibration_error = abs(
    stated_confidence - actual_accuracy
)
# Target: <10% calibration error
```

---

## 🔧 Implementation Checklist

### Phase 1: Core Loop (Week 1)
- [ ] `PREYState` with `previous_digest` field
- [ ] `_sense_node()` incorporates previous round
- [ ] `_feedback_node()` feeds forward to next round
- [ ] `_should_continue()` checks convergence
- [ ] Temperature schedule per round

### Phase 2: QUORUM Validation (Week 2)
- [ ] Confidence scoring per claim
- [ ] Weighted quorum calculation
- [ ] Cross-researcher contradiction detection
- [ ] Hallucination detection (100% confidence flags)
- [ ] Outlier identification

### Phase 3: Chain-of-Verification (Week 3)
- [ ] Generate verification questions
- [ ] Answer with web search
- [ ] Tag [VERIFIED] claims
- [ ] Self-consistency checks

### Phase 4: Thompson Sampling (Week 4)
- [ ] Beta distribution priors
- [ ] Model selection based on cost/quality
- [ ] Dynamic allocation (best models get more runs)
- [ ] Convergence tracking

---

## 📚 Research Foundations

### V²C Pattern
- **Verification**: Chain-of-Verification (Meta AI, 2023)
- **Validation**: Ensemble uncertainty estimation (Lakshminarayanan 2017)
- **Consensus**: Byzantine fault tolerance quorum (Lamport 1982)

### SPIRAL Pattern
- **Scatter-Gather**: MapReduce (Dean & Ghemawat 2004)
- **Iterative Refinement**: Expectation-Maximization (Dempster 1977)
- **Annealing**: Simulated Annealing (Kirkpatrick 1983)
- **Nested Loops**: Holonic Systems (Koestler 1967)

### QUORUM Pattern
- **Quality Diversity**: MAP-Elites (Mouret & Clune 2015)
- **Uncertainty Quantification**: Bayesian Deep Learning (Kendall 2017)
- **Multi-Agent**: Swarm Intelligence (Bonabeau 1999)

---

## 🚀 Usage Example

```python
from hfo_swarm.v2c_spiral_quorum import V2CSpiralQuorumOrchestrator

# Create orchestrator
orch = V2CSpiralQuorumOrchestrator(
    llm_provider="openrouter",
    model_tier="balanced",  # Uses Thompson Sampling portfolio
    enable_tools=True  # Web search for verification
)

# Execute mission
result = orch.execute_mission(
    intent="Research production Kubernetes best practices",
    constraints="Focus on 2023-2024 releases, include real deployments",
    num_researchers=10,
    max_rounds=3,
    auto_stop=True  # Stop on HIGH consensus
)

# Check results
print(f"Consensus: {result['consensus_level']}")  # "HIGH"
print(f"Rounds completed: {result['rounds']}")    # 2 (stopped early)
print(f"Hallucination rate: {result['hallucination_rate']}")  # 3%
print(f"Verification rate: {result['verification_rate']}")    # 78%
```

---

## 🎓 Training Guide

### For Users (Swarmlords)
1. Start with `num_researchers=5, max_rounds=1` (fast feedback)
2. Increase to `num_researchers=10, max_rounds=3` for complex topics
3. Monitor `hallucination_rate` - if >10%, enable web search tools
4. Use `previous_digest` for iterative deep dives

### For Developers (HFO Contributors)
1. Each validation metric should have automated tests
2. Quorum thresholds (80%/60%) are tunable per domain
3. Temperature schedule can be customized for different tasks
4. Extend `QuorumResult` with domain-specific validations

---

**Status**: Ready for SysML v2 formalization and Python implementation

**Next**: Create `FOUR_HIERARCHICAL_LOOPS.md` detailing HIVE → GROWTH → SWARM → PREY composition
