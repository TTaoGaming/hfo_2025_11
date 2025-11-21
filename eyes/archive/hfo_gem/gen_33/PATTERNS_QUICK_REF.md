# Gen 33 Architecture Patterns - Quick Reference

**Created**: 2025-11-17
**Purpose**: Quick lookup for all 10 formalized patterns + 4 nested loops

---

## 10 Architecture Patterns

| # | Pattern | Use Case | Key Components |
|---|---------|----------|----------------|
| 1 | **Temporal Activity + LangGraph Agent** | Single researcher with tool access | Temporal wraps LangGraph state machine |
| 2 | **Supervisor** | Meta-agent coordinates sub-agents | Swarmlord routes to specialized agents |
| 3 | **Map-Reduce-Filter** | Parallel → aggregate → quality filter | Scatter → cluster → filter hallucinations |
| 4 | **Scatter-Gather** | Byzantine quorum (10 models → consensus) | Disperse to diverse models → converge to 7/10 |
| 5 | **Hub-and-Spokes** | Central coordinator delegates to specialists | Supervisor routes to Observer/Bridger/Shaper/Assimilator |
| 6 | **Hierarchical Swarm** | L2/L3 scaling with nested supervisors | Fractal: L2 supervisor → 10 L1 supervisors → 100 L0 workers |
| 7 | **Network Stigmergy** | Decentralized NATS coordination | Agents publish signals (heartbeat/confidence/citation) with TTL decay |
| 8 | **Reflexion** | Self-critique loop | Generate → Critique → Refine → loop until quality > 0.8 |
| 9 | **PREY Loop** | Single-agent execution | Perceive → React → Execute → Yield (Observer/Bridger/Shaper/Assimilator) |
| 10 | **SWARM Loop (D3A+M)** | Multi-agent tactical coordination | Set → Watch → Act → Review → Mutate |

---

## 4 Nested Control Loops

| Loop | Level | Duration | Pattern | Roles |
|------|-------|----------|---------|-------|
| **PREY** | Agent | Seconds | Perceive → React → Execute → Yield | Observer, Bridger, Shaper, Assimilator |
| **SWARM** | Tactical | Minutes | Set → Watch → Act → Review → Mutate (D3A+M) | All 8 OBSIDIAN roles |
| **GROWTH** | Strategic | Hours | Plan → Execute → Validate → Synthesize | Navigator leads, all 8 |
| **HIVE** | Apex | Days/Weeks | Evolve → Integrate → Verify → Deploy | All 8 + Human oversight |

**Nesting**: HIVE contains GROWTH contains SWARM contains PREY
**Feedback**: Bottom-up (PREY yields → SWARM review → GROWTH validate → HIVE verify)
**Constraints**: Top-down (HIVE architecture → GROWTH plans → SWARM params → PREY context)

---

## PREY Loop (Agent Level)

**Pattern**: Perceive → React → Execute → Yield

```python
# Observer: Perceive
observations = {
    "files": list_files(workspace),
    "precedents": query_pgvector(intent),
    "signals": fetch_nats_signals(run_id)
}

# Bridger: React
actions = plan_actions(observations, intent)

# Shaper: Execute
results = [execute_tool(action) for action in actions]

# Assimilator: Yield
feedback = synthesize_feedback(actions, results)
store_to_pgvector(feedback)
```

**Duration**: 1-30 seconds
**Scope**: Single agent
**Validation**: Self-check (reflexion)

---

## SWARM Loop (Tactical Level)

**Pattern**: Set → Watch → Act → Review → Mutate (D3A + M)

### 1. SET (Define)
- Navigator defines mission parameters
- Sets: num_agents, model_roster, timeout, quality_threshold
- Initializes NATS stigmergy stream

### 2. WATCH (Detect)
- Observer monitors real-time NATS signals (heartbeat, confidence, citation)
- Immunizer detects anomalies (low confidence quorum, missing heartbeats)
- Query pgvector for historical precedents

### 3. ACT (Decide + Execute)
- Injector provisions agents (spawn 10-100-1000 workers)
- Shaper executes map-reduce-filter
  - Map: Scatter to N agents in parallel
  - Reduce: Cluster responses by similarity
  - Filter: Remove hallucinations, low confidence

### 4. REVIEW (Assess)
- Disruptor challenges consensus (red team)
- Immunizer validates quality (blue team)
  - Byzantine consensus (CP-WBFT weighted voting)
  - Precedent alignment (pgvector similarity)
  - Hallucination detection (citation validation)
  - Quality score = consensus * 0.4 + (1-hallucination_rate) * 0.3 + citations * 0.2 + precedents * 0.1

### 5. MUTATE (Optimize)
- Assimilator learns from results, updates MAP-Elites archive
- Navigator selects next config via hyper-heuristic
  - DSPy: Optimize prompts (few-shot learning)
  - Bayesian: Optimize hyperparams (temperature, num_agents)
  - Genetic: Optimize model selection
  - Quality-diversity focus: Diverse high-quality configs, not just best

**Duration**: 30-300 seconds
**Scope**: Multi-agent (10-100-1000)
**Validation**: Byzantine quorum (7/10 consensus)

---

## D3A + Mutate vs OODA

| Dimension | OODA (Individual) | D3A + Mutate (Swarm) |
|-----------|-------------------|----------------------|
| Observe | Agent senses | WATCH: Telemetry + stigmergy |
| Orient | Agent interprets | SET: Supervisor defines params |
| Decide | Agent chooses | ACT: Map-reduce-filter |
| Act | Agent executes | ACT: Parallel swarm |
| (NEW) | — | REVIEW: Byzantine consensus |
| (NEW) | — | MUTATE: Evolutionary optimization |
| Scope | 1 agent | 10-1000 agents |
| Validation | Self-check | 7/10 quorum |
| Learning | Reactive | Evolutionary (archive) |

---

## OBSIDIAN 8 Roles

| Role | Function | Primary Use |
|------|----------|-------------|
| **Observer** | Sense/Perceive | PREY Perceive, SWARM Watch |
| **Bridger** | Translate/Interpret | PREY React, SWARM Review (synthesize) |
| **Shaper** | Execute/Transform | PREY Execute, SWARM Act |
| **Injector** | Resource Provision | SWARM Act (spawn agents) |
| **Disruptor** | Red Team | SWARM Review (challenge) |
| **Immunizer** | Blue Team | SWARM Review (validate) |
| **Assimilator** | Learn/Integrate | PREY Yield, SWARM Mutate |
| **Navigator** | Strategy/Coordinate | SWARM Set, GROWTH, HIVE |

**Key Principle**: Roles are fractal (same definition at different scales)

---

## Network Stigmergy (NATS)

**Signal Types**:

| Signal | TTL | Purpose |
|--------|-----|---------|
| Heartbeat | 30s | Agent liveness (active/blocked/complete) |
| Confidence | 60s | Self-assessment (0.0-1.0 confidence score) |
| Citation | 300s | File references for cross-validation |
| Alert | No TTL | Quorum failures, hallucinations, critical issues |

**Subjects**:
```
hfo.stigmergy.{run_id}.heartbeat.{agent_id}
hfo.stigmergy.{run_id}.confidence.{agent_id}
hfo.stigmergy.{run_id}.citations.{agent_id}
hfo.stigmergy.{run_id}.alerts
hfo.stigmergy.{run_id}.quorum
```

**Why Stigmergy**:
- Decentralized (no bottleneck)
- Temporal decay (TTL auto-expires old signals)
- Indirect coordination (agents read environment, not each other)
- Scales to 1000+ agents

---

## Pattern Selection Guide

**When to use**:

- **Temporal Activity + LangGraph**: Single researcher with tool reasoning
- **Supervisor**: Need to route between specialized sub-agents
- **Map-Reduce-Filter**: Parallel execution with quality filtering
- **Scatter-Gather**: Byzantine consensus across diverse models
- **Hub-and-Spokes**: Central coordinator delegates to 4-8 specialists
- **Hierarchical Swarm**: L2+ scale (100-1000 agents)
- **Network Stigmergy**: Decentralized coordination, detect quorum failures
- **Reflexion**: Agent self-critique, iterative quality improvement
- **PREY Loop**: Single-agent tactical execution
- **SWARM Loop**: Multi-agent tactical coordination with optimization

**Pattern Composition**:
- PREY uses Reflexion (self-critique) + Temporal Activity (tool access)
- SWARM uses Scatter-Gather (quorum) + Map-Reduce-Filter (parallel) + Network Stigmergy (coordination)
- Hierarchical Swarm uses Hub-and-Spokes (each level) + Supervisor (routing)

---

## Quick Start Commands

```bash
# Read full patterns doc
cat hfo_gem/gen_33/README.md

# Pattern details
ls hfo_gem/gen_33/patterns/

# Loop details
ls hfo_gem/gen_33/loops/

# Tech stack
grep "^### [0-9]" hfo_gem/gen_33/README.md
```

---

**Status**: All 10 patterns formalized ✅
**Next**: Implement Pattern 9 (PREY) + Pattern 10 (SWARM) in LangGraph
