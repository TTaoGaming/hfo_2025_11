---
hexagon:
  ontos:
    id: 59d2f39d-cd55-4ef8-a9b9-30efdc8a4242
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.989327Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_29/HOURGLASS_GEOMETRIC_MODEL.md
    links: []
  telos:
    viral_factor: 0.0
    meme: HOURGLASS_GEOMETRIC_MODEL.md
---
# Obsidian Horizon Hourglass – Geometric Model

**Date**: 2025-11-11
**Author**: Overmind (TTao)
**Status**: Definitive geometric specification

---

## The Core Insight: It's Literally an Hourglass Shape

The Obsidian Horizon Hourglass is **not a metaphor**. It's a **geometric structure in state-action space** with three regions:

1. **PAST Cone** (expanding backwards): All information that has been done
2. **PRESENT Diameter** (narrow waist): Current possibility space constrained by resources
3. **FUTURE Cone** (expanding forwards): Simulated projections of possibilities

```
            PAST CONE
           (Information)
              ╱│╲
             ╱ │ ╲
            ╱  │  ╲         ← Expanding: More information available
           ╱   │   ╲           (research papers, training data, precedents)
          ╱    │    ╲
         ╱     │     ╲
        ╱      │      ╲
       ╱       │       ╲
      ╱        │        ╲
     ╱─────────┼─────────╲

    ═══════════════════════  ← PRESENT DIAMETER (Narrow Waist)
                              Constrained by: budget, time, energy, agents

     ╲─────────┼─────────╱
      ╲        │        ╱
       ╲       │       ╱
        ╲      │      ╱
         ╲     │     ╱
          ╲    │    ╱
           ╲   │   ╱
            ╲  │  ╱         ← Expanding: More futures simulated
             ╲ │ ╱             (Monte Carlo, swarm probes, VM experiments)
              ╲│╱
         FUTURE CONE
        (Simulations)
```

---

## Region 1: PAST Cone (Upper Cone)

**Shape**: Expanding cone going backwards in time/information space

**Diameter grows because**: The further back we look, the more information exists
- Research papers spanning decades
- Open source codebases
- Training data from billions of documents
- Historical precedents from pgvector archive
- Internet knowledge (web search, documentation)

**Contents** (State-Action Pairs):
- **States**: Historical problem configurations that were solved
- **Actions**: Solutions that were applied (what worked, what failed)
- **Transitions**: How problems evolved over time

**Operations** (Hunt for Information):
```python
def search_past_cone(problem_intent: str):
    """
    CYNEFIN categorization + break down problem into pieces
    """
    # 1. Categorize problem (clear/complicated/complex/chaotic)
    category = cynefin_classify(problem_intent)

    # 2. Break into sub-problems
    decomposed = decompose_problem(problem_intent, category)

    # 3. Search for each piece
    precedents = []
    for sub_problem in decomposed:
        # Internet search (research papers, docs, Stack Overflow)
        web_results = internet_search(sub_problem)

        # AI model knowledge (vast training data)
        llm_knowledge = query_llm_knowledge(sub_problem)

        # Local precedents (pgvector archive)
        local_precedents = pgvector_search(sub_problem)

        # Case-based reasoning (similar past cases)
        cbr_cases = case_based_reasoning(sub_problem)

        precedents.extend([web_results, llm_knowledge, local_precedents, cbr_cases])

    return precedents  # Rich information from expanding past cone
```

**Key Properties**:
- **Unbounded exploration**: Can search as deeply as needed (limited only by time/cost)
- **Multiple sources**: Internet, AI models, local archives, case libraries
- **Decomposition**: Break complex problems into searchable pieces
- **Evidence gathering**: Collect what has been done before

---

## Region 2: PRESENT Diameter (Narrow Waist)

**Shape**: Narrow circular cross-section (the "bottleneck" where sand flows through)

**Diameter size = Current possibility space**:
```
diameter ∝ f(budget, time, energy, num_agents, compute)
```

The more resources you have RIGHT NOW, the wider the diameter (more possibilities reachable).

**Constraints that narrow the waist**:
- **Budget**: How much $ can you spend on LLM calls, compute, agents
- **Time**: How long until deadline (5 min vs 5 years changes diameter)
- **Energy**: Your cognitive bandwidth, team capacity
- **Agents**: Number of AI workers you can dispatch (10 vs 100)
- **Compute**: VM resources, Ray cluster size, GPU availability

**Contents** (Current Reachable States):
- **Swarm configurations**: Valid combinations of (N agents, roles, models, temps, prompts)
- **Execution states**: What you can do RIGHT NOW given constraints
- **Mission parameters**: Feasible goals within budget/time/quality bounds

**Operations** (Execute in Present):
```python
def execute_present_diameter(mission_intent: str, precedents: list, constraints: dict):
    """
    Dispatch swarm within current resource constraints
    """
    # Calculate diameter (how many possibilities can we explore?)
    max_agents = constraints['budget'] / cost_per_agent
    max_time = constraints['deadline'] - time.now()

    diameter = min(max_agents, max_time * throughput)

    # Dispatch swarm (fan-out within diameter)
    swarm_config = {
        'num_researchers': int(diameter * 0.8),  # Most resources to research
        'num_validators': int(diameter * 0.1),   # Some to validation
        'num_synthesizers': int(diameter * 0.1)  # Some to synthesis
    }

    # Execute PREY loop
    results = prey_orchestrator.execute(
        intent=mission_intent,
        precedents=precedents,
        config=swarm_config
    )

    return results  # Constrained by present diameter
```

**Key Properties**:
- **Constrained**: Cannot explore all possibilities, only what fits in diameter
- **Resource-bound**: Bigger budget/time = wider diameter = more exploration
- **Trade-offs**: Must choose which possibilities to explore (can't do everything)
- **Execution layer**: This is where actual work happens (swarm dispatch, quorum, artifacts)

---

## Region 3: FUTURE Cone (Lower Cone)

**Shape**: Expanding cone going forwards in simulation space

**Diameter grows because**: The further forward we project, the more possible futures branch

**Contents** (Simulated Futures):
- **States**: Projected outcomes from present actions
- **Actions**: Hypothetical moves we could make
- **Transitions**: Branching timelines (Monte Carlo tree, A* paths)
- **Experiments**: Real little futures (swarm probes in VMs, code execution)

**Operations** (Simulate Futures):
```python
def simulate_future_cone(current_state: dict, precedents: list, num_simulations: int = 100):
    """
    Project probabilities into future using past information
    """
    # 1. Use past precedents to build probability models
    success_rates = calculate_success_rates(precedents)
    risk_factors = extract_risk_factors(precedents)

    # 2. Run simulations (expanding cone of possibilities)
    futures = []
    for i in range(num_simulations):
        # Monte Carlo rollout
        trajectory = monte_carlo_rollout(
            start_state=current_state,
            success_probs=success_rates,
            risks=risk_factors
        )

        # OR: Real VM experiments (swarm probes)
        if can_run_vm_experiment(current_state):
            trajectory = vm_probe_experiment(current_state)

        futures.append(trajectory)

    # 3. Analyze outcomes
    probability_dist = aggregate_futures(futures)

    return {
        'best_outcome': max(futures, key=lambda f: f.expected_value),
        'worst_outcome': min(futures, key=lambda f: f.expected_value),
        'probability_distribution': probability_dist,
        'tail_risks': identify_tail_risks(futures),
        'high_leverage': identify_high_leverage(futures)
    }
```

**Key Properties**:
- **Expanding exploration**: More simulations = wider cone = better coverage
- **Real experiments**: Can run actual code in VMs (swarm probes testing futures)
- **Probabilistic**: Use past information to weight future trajectories
- **Branching**: Each action creates multiple possible outcome paths

---

## The Flip Operation

### What "Flipping the Hourglass" Means

When you **flip the hourglass**, you **swap the roles of the two cones**:

#### State 1: Normal Orientation (Past on Top)
```
        PAST
       (Hunt)
         │
    ═══PRESENT═══
         │
      FUTURE
    (Simulate)
```

**Flow**: Past information → Present execution → Future simulations

#### State 2: Flipped Orientation (Future on Top)
```
      FUTURE
    (Retroflip)
         │
    ═══PRESENT═══
         │
        PAST
     (Archive)
```

**Flow**: Simulated futures → Present analysis → Past archive (learn from futures as if they already happened)

---

## Flip Algorithm (Explicit Steps)

### Flip Type 1: PAST → FUTURE (Forward Flip)

**Input**: Mission intent at PRESENT diameter
**Output**: Probability distribution over FUTURE cone

```python
def forward_flip(mission_intent: str, constraints: dict):
    """
    Past precedents → Present execution → Future simulations
    """
    # 1. PAST CONE: Search for information
    precedents = search_past_cone(mission_intent)

    # 2. PRESENT DIAMETER: Execute swarm with precedents
    swarm_results = execute_present_diameter(
        mission_intent=mission_intent,
        precedents=precedents,
        constraints=constraints
    )

    # 3. FUTURE CONE: Simulate outcomes
    future_projections = simulate_future_cone(
        current_state=swarm_results,
        precedents=precedents,
        num_simulations=100
    )

    return future_projections
```

### Flip Type 2: FUTURE → PAST (Reverse Flip / Retroflip)

**Input**: Simulated futures from FUTURE cone
**Output**: Learnings archived in PAST cone

```python
def reverse_flip(simulated_futures: list):
    """
    Simulated futures → Present postmortem → Past archive (learn from sims)
    """
    # 1. FUTURE CONE (now on top after flip): Analyze simulations
    for future in simulated_futures:
        # Treat simulation as if it already happened
        postmortem = retrospective_analysis(future)

        # Extract learnings
        learnings = {
            'biggest_risks': identify_risks(postmortem),
            'biggest_successes': identify_successes(postmortem),
            'attention_points': extract_attention_points(postmortem),
            'failure_modes': extract_failures(postmortem)
        }

        # 2. PRESENT DIAMETER: Process learnings
        actionable_insights = synthesize_insights(learnings)

        # 3. PAST CONE (now on bottom after flip): Archive as precedents
        archive_as_precedent(
            source='simulated_future',
            outcome=future.outcome,
            learnings=actionable_insights,
            confidence=future.probability
        )

    return archived_learnings
```

### Flip Type 3: Continuous Flipping (Recursive Exploration)

**Input**: Mission intent + stopping criteria
**Output**: Converged probability distribution

```python
def recursive_flip(mission_intent: str, max_flips: int = 10, convergence_threshold: float = 0.95):
    """
    Keep flipping until convergence or max flips reached (anytime algorithm)
    """
    state = initialize_state(mission_intent)
    flip_count = 0
    confidence = 0.0

    while flip_count < max_flips and confidence < convergence_threshold:
        # Forward flip: PAST → FUTURE
        future_projections = forward_flip(state['mission'], state['constraints'])

        # Reverse flip: FUTURE → PAST (learn from simulations)
        learnings = reverse_flip(future_projections['trajectories'])

        # Update state with new learnings
        state = update_state_with_learnings(state, learnings)

        # Check convergence (are predictions stabilizing?)
        confidence = calculate_confidence(future_projections['probability_distribution'])

        flip_count += 1

        # ANYTIME STOP: Can exit here and get valid artifact
        if user_requests_stop():
            break

    # Generate final artifact
    return generate_probability_distribution_artifact(
        best_path=future_projections['best_outcome'],
        confidence=confidence,
        flips_executed=flip_count,
        evidence_summary={
            'precedents': len(state['precedents']),
            'simulations': len(future_projections['trajectories']),
            'learnings': len(learnings)
        }
    )
```

---

## Quality-Diversity (QD) Evolution Through Flips

Each flip can **evolve the search strategy** using different algorithms:

```python
flip_algorithms = [
    'thompson_sampling',    # Bayesian multi-armed bandit (exploration-exploitation)
    'monte_carlo_tree',     # Tree search with rollouts
    'a_star',               # Goal-directed heuristic search
    'evolutionary_qd',      # Map-elites for configuration space
    'random_search',        # Baseline (random exploration)
]

def evolve_flip_strategy(flip_history: list, current_performance: dict):
    """
    Meta-optimize which flip algorithm to use based on performance
    """
    # QD map-elites: Explore algorithm × parameter space
    best_algorithm = map_elites(
        search_space=flip_algorithms,
        fitness_function=lambda algo: measure_convergence_rate(algo, flip_history),
        diversity_metrics=['exploration_breadth', 'exploitation_depth']
    )

    return best_algorithm
```

---

## Geometric Constraints

### Diameter Equations

**PRESENT Diameter**:
```
d_present = min(
    budget / cost_per_agent,
    time_remaining * throughput,
    sqrt(energy * compute)
)
```

**PAST Cone Radius** (at depth t):
```
r_past(t) = base_radius + expansion_rate * t

where:
  t = search depth (hours, days, years back)
  expansion_rate = information growth rate
  base_radius = minimum search scope
```

**FUTURE Cone Radius** (at projection distance h):
```
r_future(h) = base_radius + branching_factor^h

where:
  h = projection horizon (minutes, hours, days ahead)
  branching_factor = average number of outcomes per action
  base_radius = minimum simulation set
```

---

## Visual Example: Math Benchmark Mission

### Initial State (No Flips Yet)
```
         PAST CONE
    ╱─────────────╲
   │ Math textbooks │
   │ Research papers│
   │ Stack Overflow │
   │ Training data  │
    ╲─────────────╱

    ═══PRESENT═══
    Budget: $100
    Time: 1 day
    Agents: 10

    ╱─────────────╲
   │ Simulate GPT-4│
   │ Simulate GPT-3│
   │ Simulate CoT  │
   │ Simulate fine-│
   │ tuning        │
    ╲─────────────╱
      FUTURE CONE
```

### After Flip 1 (PAST → FUTURE)
- Searched past: Found 20 precedents on math problem solving
- Executed present: Dispatched 10 researchers with CoT prompts
- Simulated future: 100 Monte Carlo runs → 75% confidence GPT-4 + CoT works best

### After Flip 2 (FUTURE → PAST)
- Retroflipped: Analyzed failed simulations (25% failure cases)
- Post-mortem: Identified hallucination patterns in word problems
- Archived learning: "Word problems need explicit step labels to prevent hallucinations"

### After Flip 3 (PAST → FUTURE, with new learnings)
- Searched past: Now includes archived simulation learnings
- Executed present: Updated prompts with step labels
- Simulated future: 100 new runs → 85% confidence (improved!)

**Convergence**: After 3 flips, confidence stabilized at 85%. STOP and deliver artifact.

---

## Integration with PREY Loop

Each region of the hourglass maps to PREY phases:

| Hourglass Region | PREY Phase | Action |
|------------------|------------|--------|
| **PAST Cone Search** | Perceive (Sense) | Hunt for information, gather precedents |
| **PAST Cone Categorization** | React (Make Sense) | CYNEFIN classify, decompose, CBR |
| **PRESENT Diameter Dispatch** | Execute (Act) | Launch swarm, run experiments |
| **PRESENT Diameter Validation** | Yield (Feedback) | Quorum check, hallucination detect |
| **FUTURE Cone Simulation** | Perceive (Sense) | Generate projections, run VMs |
| **FUTURE Cone Analysis** | React (Make Sense) | Calculate probabilities, identify risks |
| **Flip Operation** | Execute (Act) | Swap cones, archive learnings |
| **Artifact Publication** | Yield (Feedback) | Deliver probability distribution |

---

## Key Clarifications (Addressing Drift)

### ❌ What the Hourglass is NOT:
1. **Not a workflow diagram**: It's a geometric structure in state-action space
2. **Not a single algorithm**: It's a framework that uses many algorithms (Thompson, MCTS, A*, QD)
3. **Not a metaphor**: It literally has two cones and a narrow waist with specific meanings

### ✅ What the Hourglass IS:
1. **Geometric structure**: Two expanding cones (PAST, FUTURE) connected by narrow waist (PRESENT)
2. **State-action space**: Each point in the cones is a (state, action) configuration
3. **Resource-constrained**: PRESENT diameter limited by budget, time, energy, agents, compute
4. **Flippable**: Can swap PAST ↔ FUTURE to learn from simulations as if they were history
5. **Anytime algorithm**: Can stop at any flip and get valid probability distribution output

---

## Implementation Checklist

- [ ] **Past Cone Search**: Internet + AI models + pgvector + CBR
- [ ] **Present Diameter Execution**: PREYOrchestrator with resource constraints
- [ ] **Future Cone Simulation**: Monte Carlo + A* + VM probes
- [ ] **Flip Mechanism**: Forward flip (PAST→FUTURE) + Reverse flip (FUTURE→PAST)
- [ ] **Convergence Detection**: Measure when probability distribution stabilizes
- [ ] **QD Evolution**: Meta-optimize flip algorithm selection
- [ ] **Geometric Constraints**: Calculate diameters based on budget/time/compute
- [ ] **Artifact Generation**: Probability distribution + evidence + tail risks

---

**Status**: Definitive geometric model complete. No more drift. This is the spec.
