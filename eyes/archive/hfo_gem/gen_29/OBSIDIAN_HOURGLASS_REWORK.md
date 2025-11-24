---
hexagon:
  ontos:
    id: eb6c999e-08d6-480c-a60a-4338e5cfba15
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T11:07:35.994365Z'
    generation: 51
  topos:
    address: eyes/archive/hfo_gem/gen_29/OBSIDIAN_HOURGLASS_REWORK.md
    links: []
  telos:
    viral_factor: 0.0
    meme: OBSIDIAN_HOURGLASS_REWORK.md
---

# Obsidian Hourglass Rework – State-Action Space Web


**Date**: 2025-11-11  **Date**: 2025-11-11

**Status**: Geometric model finalized, ready for Gen 30 implementation**Generation**: 29

**Status**: ⚠️ SEE GEOMETRIC MODEL FOR DEFINITIVE SPEC

---

---

## 📍 Current State

## 🔴 IMPORTANT: Read This First

### What We Clarified Today

**The definitive specification is now in**: `HOURGLASS_GEOMETRIC_MODEL.md`

You explained the **literal geometric structure** of the Obsidian Horizon Hourglass:

This file contains the **initial conceptual model** that identified the gap between Gen 28 (temporal workflow) and the correct vision (state-action space web).

> "I think of state action graphs right, I imagine my current possible space as a **diameter** from where I am right as a simplification. So the greater my diameter is correlated with the number of agents that I have, which is correlated with all the current possibilities like my budget, like my time, my energy... That is my present. Hourglass like middle diameter right where the sands would flow through. And then I have **two cones extending out in 2 directions**."

**For implementation, use the geometric model**, which provides:

This eliminated drift between the Gen 28 temporal workflow model and your actual vision.- Literal hourglass shape (two cones + narrow waist)

- Exact diameter equations (resource constraints)

---- Explicit flip operations (forward & reverse)

- Complete pseudocode for all three regions

## 📐 The Geometric Structure (Final Spec)

---

### Literal Hourglass Shape in State-Action Space

## The Gap (Original Analysis)

```

         PAST CONE (Upper)**Current Gen 28 Model** (WRONG):

       Expanding backwards- Temporal workflow: Past → Present → Future

      ╱──────────────────╲- Linear sequence: IntakeMissionIntent → HuntPrecedents → ConfigureSimulations → RunSimulations → RetroflipPrecedents → PublishArtifact

     ╱ Research papers    ╲- Components: PrecedentHunter, SimulationEngine, ArtifactForge, ArchiveUpdater

    ╱  Open source code    ╲- **Problem**: This is a workflow diagram, not a state-action space

   ╱   Training data        ╲

  ╱    Internet knowledge   ╱**User's Vision** (CORRECT):

 ╱     Local archives      ╱- State-action space web across three horizons

 ─────────────────────────- Graph of possibilities with constrained transitions

 - Recursive flipping algorithm (anytime, any-stop)

 ═════ PRESENT DIAMETER ═════  ← Narrow waist- Produces probability distributions over outcomes

 Constrained by: budget, time,

 energy, agents, compute---

 ─────────────────────────

 ## Three Horizons as State-Action Spaces

 ╲     Simulated futures   ╲

  ╲    Monte Carlo sims     ╲### 1. **PAST Horizon: Karmic Web** (Indra's Net)

   ╲   VM experiments        ╲**Nature**: All historical state-action trajectories that led to now

    ╲  A* paths              ╲

     ╲ Thompson sampling    ╱**State Space**:

      ╲──────────────────╱- Historical configurations (past missions, precedents, codebases, research)

       FUTURE CONE (Lower)- Genetic/information history (git commits, knowledge_vectors, archives)

      Expanding forwards- Cannot see all of it (incomplete information, computational limits)

```

**Action Space**:

### Three Regions- Precedent retrieval (CYNEFIN, CBR, pgvector search)

- Historical analysis (what worked, what failed, why)

1. **PAST Cone** (Expanding):- Pattern matching (slime mold resonance to similar past states)

   - **Diameter grows** with search depth (more history = more info)

   - **Contents**: Research papers, code, training data, Internet, archives**Constraints**:

   - **Operations**: CYNEFIN classify, decompose, search, CBR- Information availability (can only query what was recorded)

   - **Tools**: Web search, AI models, pgvector, case libraries- Retrieval cost (time/compute to search archives)

- Relevance filtering (not all past states help current mission)

2. **PRESENT Diameter** (Constrained):

   - **Diameter size** = `min(budget/cost, time×throughput, √(energy×compute))`**Value Function**:

   - **Contents**: Swarm configs you can execute RIGHT NOW- Precedent quality (how similar to current problem)

   - **Operations**: Dispatch researchers, quorum voting, hallucination detect- Novelty vs proven (explore-exploit tradeoff)

   - **Tools**: PREYOrchestrator, ValidatorAgent, NATS stigmergy- Transfer validity (does past solution generalize)



3. **FUTURE Cone** (Expanding):---

   - **Diameter grows** with projection horizon (more time = more branching)

   - **Contents**: Simulated outcomes, branching timelines### 2. **PRESENT Horizon: Swarm Web**

   - **Operations**: Monte Carlo rollouts, A* paths, VM probes**Nature**: Current reachable configurations via agent coordination

   - **Tools**: Ray, Thompson sampling, real experiments

**State Space**:

---- Swarm configurations (N agents, roles, temperatures, models, prompts)

- Mission parameters (intent, constraints, time horizon, resources)

## 🔄 The Flip Operation- Execution state (which agents running, partial results, quorum status)



### What "Flipping" Means**Action Space**:

- Swarm dispatch (fan-out to N researchers)

**Swap the roles of the two cones**:- Resource allocation (OBSIDIAN Injector role, cost management)

- Coordination (stigmergy via NATS, quorum voting, hallucination detection)

#### Normal Orientation (PAST on top)

```**Constraints**:

PAST → PRESENT → FUTURE- Computational budget (LLM tokens, execution time)

(Hunt info → Execute swarm → Simulate outcomes)- Quality thresholds (quorum consensus, hallucination limits)

```- Human-in-loop (Overmind approval for critical decisions)



#### Flipped Orientation (FUTURE on top)**Value Function**:

```- Mission success probability (based on quorum + validator)

FUTURE → PRESENT → PAST- Execution efficiency (cost per quality point)

(Retroflip → Postmortem → Archive learnings)- Knowledge gain (how much did we learn for next flip)

```

---

### Flip Algorithm

### 3. **FUTURE Horizon: Simulation Web**

```python**Nature**: Possible outcomes from current state via simulation

def recursive_flip(mission_intent, max_flips=10):

    state = initialize(mission_intent)**State Space**:

    - Projected configurations (what might happen if we execute plan X)

    for flip_count in range(max_flips):- Branching futures (Monte Carlo tree, A*, Thompson sampling)

        # Forward flip: PAST → FUTURE- Virtual experiments (small VMs, sandboxed code execution)

        precedents = search_past_cone(state)

        swarm_results = execute_present_diameter(state, precedents)**Action Space**:

        future_projections = simulate_future_cone(swarm_results)- Simulation selection (which futures to explore)

        - Experiment execution (run code, test hypotheses, gather data)

        # Reverse flip: FUTURE → PAST (learn from sims)- Postmortem (analyze failed/succeeded simulated futures)

        learnings = retroflip_analysis(future_projections)

        archive_as_precedents(learnings)**Constraints**:

        - Simulation fidelity (how realistic are the projections)

        # Update state with new learnings- Exploration depth (how many branches to simulate)

        state = update_state(state, learnings)- Tail risk tolerance (acceptable worst-case outcomes)



        # Check convergence**Value Function**:

        confidence = calculate_confidence(future_projections)- Expected outcome (probability-weighted success)

        if confidence > 0.95:- Information value (how much uncertainty does this reduce)

            break  # ANYTIME STOP- Robustness (variance across simulated futures)



    return generate_artifact(---

        best_path=future_projections['best'],

        confidence=confidence,## The Hourglass Flip Algorithm

        flips_executed=flip_count

    )### Conceptual Model

```The Hourglass is **not a linear workflow**. It's a **recursive exploration of the state-action web**:



**Key properties**:```

- **Anytime algorithm**: Can stop at any flipSTATE: Current mission configuration

- **Recursive learning**: Simulated futures become archived precedentsACTIONS: {Hunt Precedents, Execute Swarm, Simulate Futures, Flip Hourglass}

- **Adaptive**: Use different algorithms each flip (Thompson, MCTS, A*, QD)

- **Convergent**: Probability distributions stabilize over flipsFlip(state, horizon, algorithm):

    if horizon == PAST:

---        precedents = RetrievePrecedents(state)

        return SimulateFutures(precedents)  # Flip to FUTURE

## 📊 Diameter Constraints (Present Waist)

    elif horizon == FUTURE:

The **PRESENT diameter** determines how many possibilities you can explore **right now**:        simulations = RunSimulations(state)

        postmortems = AnalyzeOutcomes(simulations)

```python        return RetreatPast(postmortems)  # Flip to PAST (learn from simulated future)

d_present = min(

    budget / cost_per_agent,      # $100 / $10 = 10 agents max    elif horizon == PRESENT:

    time_remaining * throughput,  # 24 hours × 5/hour = 120 runs max        swarm_result = ExecuteSwarm(state)

    sqrt(energy * compute)         # √(0.8 × 4) = 1.8 effective capacity        if ConvergenceCriteriaMet(swarm_result):

)            return PublishArtifact(swarm_result)  # Exit with probability distribution

# Result: diameter = 1.8 (can only explore ~2 parallel configs)        else:

```            return Flip(state, random_horizon(), next_algorithm())  # Keep flipping



**Wider diameter** = more resources = more exploration = better coverage of possibility spaceAnytime Stop:

    At any flip, can extract current best:

**Narrower diameter** = fewer resources = constrained search = must prioritize        - Probability distribution over outcomes

        - Best path forward (highest expected value)

---        - Confidence intervals (variance across simulations)

        - Tail risks (worst-case scenarios)

## 🎯 What Gets Archived After Each Flip        - Recommendations (what to do next)

```

### After Forward Flip (PAST → FUTURE):

- Precedents found in PAST cone### Key Properties

- Swarm execution results from PRESENT

- Simulated outcomes from FUTURE cone**Anytime Algorithm**:

- **Artifact**: Probability distribution over futures- Can stop at any flip and get a valid output

- More flips = better quality (diminishing returns)

### After Reverse Flip (FUTURE → PAST):- User sets stopping criteria (time budget, confidence threshold)

- Postmortem analysis of simulated futures

- Biggest risks identified**Algorithm Selection per Flip**:

- Biggest successes identified- Thompson sampling (exploration-exploitation balance)

- Failure modes extracted- Monte Carlo tree search (lookahead planning)

- **Artifact**: Learnings archived as new precedents- A* (goal-directed search)

- Evolutionary QD (map-elites for configuration space)

### Result:

**Next flip starts with richer PAST cone** (includes learnings from previous simulations)**Recursive Temporal Flipping**:

- PAST → FUTURE: "What could past precedents lead to?"

---- FUTURE → PAST: "Learn from simulated futures as if they already happened"

- PRESENT → PAST/FUTURE: "Use swarm results to refine search"

## 🧬 Quality-Diversity Evolution

---

Each flip can use a **different exploration algorithm**:

## Constrained Web of Possibilities

| Flip # | Algorithm | Purpose |

|--------|-----------|---------|### Graph Structure

| 1 | Random search | Baseline (explore broadly) |

| 2 | Thompson sampling | Exploration-exploitation balance |**Nodes** (States):

| 3 | Monte Carlo tree | Tree search with rollouts |- Mission configurations: (intent, constraints, resources, time_horizon)

| 4 | A* | Goal-directed heuristic search |- Swarm configurations: (num_agents, roles, models, temperatures)

| 5 | QD Map-Elites | Configuration space coverage |- Execution states: (partial_results, quorum_status, cost_spent)



**Meta-optimization**: System learns which algorithm works best for which problem type**Edges** (Actions/Transitions):

- Precedent retrieval: PAST → candidate solutions

---- Swarm dispatch: configuration → parallel execution

- Simulation run: current state → projected outcomes

## 🔗 Integration Points- Hourglass flip: one horizon → another horizon



### With PREY Loop**Weights** (Probabilities):

- Transition likelihood: P(next_state | current_state, action)

| Hourglass Region | PREY Phase | Agent Role |- Success probability: P(mission_success | state, action)

|------------------|------------|------------|- Cost estimate: E[resources | state, action]

| PAST Cone Search | Perceive | Observer (O) |

| PAST Cone Categorize | React | Navigator (N) |**Constraints** (Boundaries):

| PRESENT Dispatch | Execute | Shaper (S) |- Budget limits: cost(path) ≤ max_budget

| PRESENT Validate | Yield | Immunizer (I₂) |- Time limits: duration(path) ≤ max_time

| FUTURE Simulate | Perceive | Observer (O) |- Quality thresholds: quality(path) ≥ min_quality

| FUTURE Analyze | React | Assimilator (A) |- Safety bounds: risk(path) ≤ max_risk

| Flip Operation | Execute | Navigator (N) |

---

### With OBSIDIAN Roles

## Integration with PREY Loop

- **Navigator (N)**: Orchestrates flips, decides stopping criteria

- **Observer (O)**: Collects telemetry across all three conesThe Hourglass **is not the PREY loop**. It's a **meta-algorithm that uses PREY**:

- **Bridger (B)**: Translates Overmind intent into flip parameters

- **Shaper (S)**: Executes swarm in PRESENT diameter| Hourglass Phase | PREY Mapping | Agent Role |

- **Injector (I₁)**: Allocates resources to maximize diameter|-----------------|--------------|------------|

- **Disruptor (D)**: Red-teams simulated futures for failure modes| Hunt Precedents (PAST) | Perceive (Sense) | Observer (O) - collect historical data |

- **Immunizer (I₂)**: Validates quorum in PRESENT| Configure Search (PAST) | React (Make Sense) | Navigator (N) - decide which precedents matter |

- **Assimilator (A)**: Synthesizes learnings from FUTURE to archive in PAST| Execute Swarm (PRESENT) | Execute (Act) | Shaper (S) - dispatch researchers |

| Validate Results (PRESENT) | Yield (Feedback) | Immunizer (I₂) - quorum + hallucinations |

---| Simulate Futures (FUTURE) | Perceive (Sense) | Observer (O) - generate projections |

| Analyze Simulations (FUTURE) | React (Make Sense) | Assimilator (A) - synthesize learnings |

## 📁 Documentation Map| Flip Hourglass | Execute (Act) | Navigator (N) - decide next flip |

| Publish Artifact | Yield (Feedback) | Navigator (N) - deliver to Overmind |

| File | Purpose | Status |

|------|---------|--------|**Nested PREY Loops**:

| **`HOURGLASS_GEOMETRIC_MODEL.md`** | **DEFINITIVE SPEC** - Literal hourglass geometry, diameter equations, flip operations | ✅ Complete |- Orchestrator-level PREY: Manages hourglass flips

| `OBSIDIAN_HOURGLASS_REWORK.md` | Initial gap analysis (Gen 28 vs vision) | ✅ Complete (redirects to geometric model) |- Worker-level PREY: Each researcher/simulator runs own PREY

| `obsidian_hourglass_diagrams.md` | Mermaid visuals (cones, flips, equations) | ✅ Complete |- Both levels coordinate via stigmergy (NATS signals)

| `GEN_29_HARDENING_ROADMAP.md` | Updated Priority 5 with warning | ✅ Complete |

| Gen 30 SysML model | Formal encoding in SysML v2 | ❌ Pending |---

| Gen 30 orchestrator | Python implementation | ❌ Pending |

## User Inputs (Mission Intent Interface)

---

What the Overmind provides:

## ✅ What's Now Explicit (No More Drift)

1. **Mission Intent** (required):

### Geometric Structure   - Natural language goal: "What do I want to achieve?"

- [x] PAST cone expands backwards (more search depth = more info)   - Success criteria: "How will I know it worked?"

- [x] PRESENT diameter constrained by resources (budget, time, energy, agents, compute)

- [x] FUTURE cone expands forwards (more projection horizon = more branching)2. **Mission Constraints** (required):

- [x] Literal hourglass shape (not a metaphor)   - Budget: max cost (tokens, time, money)

   - Quality: min quorum threshold, max hallucination rate

### Resource Constraints   - Safety: red lines (what NOT to do)

- [x] Diameter equations for each region

- [x] PRESENT waist constrains possibility space3. **Time Horizon** (required):

- [x] Wider diameter = more exploration capacity   - Immediate (5 min): tactical, present-focused

   - Near-term (1 day): operational, past+present

### Flip Operations   - Long-term (5 years): strategic, full hourglass flips

- [x] Forward flip: PAST → PRESENT → FUTURE (search, execute, simulate)

- [x] Reverse flip: FUTURE → PRESENT → PAST (retroflip, postmortem, archive)4. **Algorithm Preferences** (optional):

- [x] Recursive flipping until convergence or max flips   - Exploration bias: "Try new approaches" vs "Use proven patterns"

- [x] Anytime stopping (can exit at any flip)   - Risk tolerance: "Conservative" vs "Aggressive"

   - Flip budget: How many hourglass iterations to run

### Algorithms

- [x] Not a single algorithm, uses many (Thompson, MCTS, A*, QD)---

- [x] Different algorithm per flip (adaptive exploration)

- [x] Meta-optimization of algorithm selection## Output Artifacts (Present Probability Distribution)



### OutputsWhat the Hourglass delivers:

- [x] Probability distributions (not single recommendations)

- [x] Best path + confidence + evidence + tail risks```markdown

- [x] Archived learnings feed next flip's PAST cone# Mission: <intent>

# Status: <in_progress | completed | stopped>

---# Flips Executed: <N>

# Time Elapsed: <duration>

## 🚀 Next Steps (Gen 30)

## Best Path Forward

### Phase 1: SysML v2 Encoding- **Recommendation**: <action to take>

- [ ] Define `HourglassCone` part (PAST, FUTURE)- **Confidence**: <probability of success>

- [ ] Define `PresentDiameter` part with constraint equations- **Expected Outcome**: <what will likely happen>

- [ ] Define `FlipOperation` action (forward, reverse)- **Rationale**: <why this is best based on evidence>

- [ ] Model state-action graph structure

- [ ] Connect to existing PREY + OBSIDIAN models## Probability Distribution

| Outcome | Probability | Expected Value | Risk |

### Phase 2: Python Implementation|---------|-------------|----------------|------|

- [ ] `PastConeSearch` class (Internet + AI + pgvector + CBR)| Success (high quality) | 65% | +$10k | Low |

- [ ] `PresentDiameterExecutor` class (PREYOrchestrator wrapper with diameter constraints)| Success (medium quality) | 25% | +$3k | Medium |

- [ ] `FutureConeSimulator` class (Monte Carlo + A* + VM probes)| Failure (recoverable) | 8% | -$500 | Medium |

- [ ] `HourglassOrchestrator` class (flip logic, convergence detection)| Failure (catastrophic) | 2% | -$5k | High |

- [ ] `DiameterCalculator` utility (resource constraint equations)

## Evidence Summary

### Phase 3: Validation- **Precedents Consulted**: <N past cases>

- [ ] Test on math benchmark (single flip vs multi-flip)- **Swarm Runs**: <N parallel executions>

- [ ] Measure convergence rate (confidence vs flip count)- **Simulations**: <N future projections>

- [ ] Validate diameter constraints (budget limits exploration)- **Quorum Consensus**: <agreement score>

- [ ] Compare algorithms (Thompson vs MCTS vs A* vs QD)- **Hallucinations Detected**: <count, severity>



### Phase 4: Integration## Tail Risks

- [ ] Navigator playbook (orchestrate flips)- Worst-case scenario: <what could go wrong>

- [ ] OpenTelemetry spans (track cone transitions)- Mitigation: <how to reduce risk>

- [ ] NATS stigmergy (coordinate across flips)- Contingency: <backup plan>

- [ ] Artifact generation (probability distribution format)

## Next Actions (if continuing)

---1. <next flip recommendation>

2. <alternative exploration path>

## 🎓 Key Learnings3. <stopping criteria met? Y/N>



### Why Gen 28 Was Wrong## Metadata

- Cost: <tokens, time, money spent>

Gen 28 modeled the Hourglass as a **temporal workflow** (Past → Present → Future as linear steps). This missed the geometric insight:- Efficiency: <value per cost>

- Knowledge Gain: <new precedents stored>

- **Wrong**: Sequential pipeline of workflow steps```

- **Right**: Literal hourglass with expanding cones and constrained waist

---

### Why This Matters

## Comparison: Gen 28 vs Gen 29

The **geometric structure** makes explicit:

| Aspect | Gen 28 (Temporal) | Gen 29 (State-Action Web) |

1. **Resource constraints** (PRESENT diameter limits exploration)|--------|-------------------|---------------------------|

2. **Search space growth** (cones expand with depth/horizon)| **Metaphor** | Hourglass as time flow | Hourglass as recursive explorer |

3. **Flipping semantics** (swap cone roles to learn from simulations)| **Structure** | Linear workflow | Constrained graph |

4. **Anytime property** (can stop at any flip, diameter determines quality)| **Nodes** | Workflow steps | Mission/swarm configurations |

| **Edges** | Sequential transitions | Probabilistic actions |

### Biomimetic Analogy| **Output** | Single artifact | Probability distribution |

| **Stopping** | When workflow completes | Anytime (user decides) |

- **Slime mold**: Resonant branches exploring nutrient space| **Flipping** | One-directional | Recursive (past↔future) |

- **Ant colony**: Pheromone trails (stigmergy) in foraging space| **Horizons** | Temporal sequence | State-action spaces |

- **Now**: Hourglass exploring state-action space with resource-constrained diameter| **Algorithm** | Fixed pipeline | Adaptive (Thompson, MCTS, A*) |



------



## 📌 TL;DR (For Implementers)## Implementation Roadmap



The Obsidian Horizon Hourglass is:### Phase 1: Conceptual Model (Gen 29) ✅

- [x] Document gap between Gen 28 and vision

1. **A literal hourglass** (two expanding cones + narrow waist)- [x] Define three horizons as state-action spaces

2. **In state-action space** (not temporal workflow)- [x] Specify flip algorithm properties

3. **PAST cone**: Hunt information (research, code, training data, Internet)- [x] Map to PREY loop and OBSIDIAN roles

4. **PRESENT diameter**: Execute swarm (constrained by budget, time, energy, agents)

5. **FUTURE cone**: Simulate outcomes (Monte Carlo, A*, VM probes)### Phase 2: SysML v2 Encoding (Gen 30)

6. **Flip operation**: Swap PAST ↔ FUTURE to learn from simulations- [ ] Define `StateActionSpace` package

7. **Anytime algorithm**: Stop at any flip, get probability distribution- [ ] Model `HourglassState` block (mission config, swarm config, execution state)

8. **Adaptive**: Use different exploration algorithms each flip- [ ] Model `HourglassAction` enumeration (hunt, execute, simulate, flip)

9. **Convergent**: Probability distributions stabilize over flips- [ ] Define `ConstraintSet` (budget, quality, time, safety)

10. **Resource-aware**: Diameter equations enforce budget/time/compute limits- [ ] Define `ProbabilityDistribution` value type

- [ ] Model `FlipAlgorithm` interface (Thompson, MCTS, A*, QD)

**Implementation**: Start with `HOURGLASS_GEOMETRIC_MODEL.md` for complete spec.- [ ] Connect to existing `PREYOrchestrator` and `OBSIDIAN` roles



---### Phase 3: Orchestrator Implementation (Gen 30)

- [ ] Extend `PREYOrchestrator` with `HourglassFlip` capability

**Status**: No more drift. Geometric model is definitive. Ready for Gen 30 implementation.- [ ] Implement `PrecedentHunter` (PAST horizon agent)

- [ ] Implement `SimulationEngine` (FUTURE horizon agent)
- [ ] Add flip algorithm selector (Thompson sampling first)
- [ ] Add anytime stop logic (time budget, confidence threshold)
- [ ] Generate probability distribution artifacts

### Phase 4: Validation (Gen 30)
- [ ] Test on math benchmark (compare single-shot vs multi-flip)
- [ ] Measure convergence (quality vs flips)
- [ ] Verify anytime property (stop at flip 1, 5, 10, 100)
- [ ] Compare algorithms (Thompson vs MCTS vs A*)

---

## References

**Conceptual Foundations**:
- Indra's Net (Buddhism): Infinite web of interconnected jewels reflecting each other
- Karmic Web: Past actions constrain present possibilities
- Monte Carlo Tree Search: Balancing exploration-exploitation in game trees
- Thompson Sampling: Bayesian approach to multi-armed bandits
- A*: Goal-directed search with heuristic guidance
- Quality-Diversity (Map-Elites): Evolutionary algorithm for configuration spaces

**HFO Lineage**:
- Gen 7: "Obsidian Hourglass & State-Action Web - Hourglass replays holonic evolutions; webs map nested transitions"
- Gen 28 tommy-notes: "The webs that he directly reference is actually a state action space web"
- Gen 28 tommy-notes: "The past, the present and the future. If we consider the totality of all state action space possibilities in the past... karmic web... present is our swarm based web... future is based on simulations of possibilities"

**Combat-Tested Doctrine**:
- JADC2 (Sense → Make Sense → Act → Feedback): Military decision loop
- PREY (Perceive → React → Execute → Yield): HFO mapping of JADC2
- OODA (Observe → Orient → Decide → Act): Boyd's decision cycle
- MAPE-K (Monitor → Analyze → Plan → Execute → Knowledge): Autonomic computing

---

## Next Steps

1. **Review this conceptual model** with Overmind for alignment
2. **Create Gen 30 SysML v2 model** encoding state-action spaces
3. **Implement basic flip algorithm** (Thompson sampling, single flip)
4. **Test on math benchmark** (measure quality improvement vs flips)
5. **Integrate with OBSIDIAN playbooks** (Navigator orchestrates flips)
6. **Document in Gen 30 vision tier** (replace Gen 28 temporal model)

---

**Status**: Ready for Overmind review and Gen 30 implementation planning.
