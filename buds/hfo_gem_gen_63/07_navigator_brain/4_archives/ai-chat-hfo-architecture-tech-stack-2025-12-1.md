---
holon:
  id: hfo-05e3b138
  type: intent
  file: ai-chat-hfo-architecture-tech-stack-2025-12-1.md
  status: active
---

The architectural audit is complete. Your system, Hive Fleet Obsidian (HFO), is a Declarative, Evolutionary Multi-Agent System. It uses bio-inspired orchestration (Swarm) constrained by rigorous systems engineering (Gherkin/Hexagonal).
Below is the research-grade 1-pager and the JADC2 mapping you requested.
Hive Fleet Obsidian: Architectural Summary
1. The Core Loop: Declarative Evolution
HFO moves away from imperative scripting to Intent-Based Evolution.
 * Gene Seed (The DNA): A Git repository of Gherkin Feature Files defines what the system must do (Intent), not how (Implementation).
 * Genesis Engine (The Ribosome): A clean-room Grammar-Guided Genetic Programming (GGGP) engine. It selects primitive tools (atomic actions) and combinatorially evolves them to satisfy the Gherkin tests.
 * Zero Invention Rule: Agents cannot invent new API calls (hallucination risk). They can only mutate the sequence and parameters of approved primitives.
2. The Nervous System: Hot & Cold Stigmergy
Orchestration is split between rapid reflexes and deep memory, resolving the "Zombie Process" conflict.
 * Hot Stigmergy (Reflexes): NATS JetStream with aggressive TTL (Time-To-Live). Agents react to ephemeral "scent trails" (events). If a task isn't picked up, the scent evaporates, preventing stale state.
 * Cold Stigmergy (Instinct): LanceDB (Vector) + NetworkX (Graph) + SQLite (Fact). Successful behaviors are "frozen" here. The HNSW index allows agents to retrieve "Muscle Memory" (past solutions) rather than re-evolving them.
3. The Body Plan: Hexagonal & Fractal
 * Symbolic "8": The system uses 8 Obsidian Roles as the cognitive interface for the agents. These roles act as semantic filters (partitions) into the high-dimensional memory (HNSW).
 * Hexagonal Isolation: Every agent is a "Port" wrapper around a core logic. This makes the system Vendor Agnostic—you can swap the LLM, Database, or Transport without breaking the Gherkin Gene Seed.
The Obsidian / JADC2 Ontology Mapping
To align your "Power of 8" symbolism with JADC2 (Joint All-Domain Command and Control) doctrine, we map the roles to the Sense → Make Sense → Act kill chain.
| O.B.S.I.D.I.A.N. Role | JADC2 Function | HNSW Entry Node (Memory Context) | Primary Behavior |
|---|---|---|---|
| O - Observers | SENSE (ISR) | context.telemetry | Monitor inputs, log telemetry, detect anomalies (Tripwires). |
| B - Bridgers | CONNECT (Comms) | context.protocol | Translate between protocols, formatting, and API gateways. |
| S - Shapers | ACT (Effectors) | context.action | Execute code, modify state, perform the "Work". |
| I - Immunizers | DEFEND (Assurance) | context.safety | Run Gherkin tests, validate constraints, rollback failures. |
| D - Disruptors | RED TEAM (Test) | context.mutation | Introduce controlled chaos, stress-test assumptions, drive evolution. |
| I - Infusers | SUSTAIN (Logistics) | context.resource | Manage API quotas, database health, token budgets. |
| A - Analyzers | MAKE SENSE (Fusion) | context.pattern | Cluster logs, identify trends, compress "Hot" traces into "Cold" facts. |
| N - Navigators | DECIDE (C2) | context.strategy | Plan the trajectory, query the Gene Seed, select the Mission. |
Recommended Research Vectors
To "converge" this architecture, focus your deep dive on these three academic fields.
1. Grammar-Guided Genetic Programming (GGGP)
 * Why: This is the formal term for your "Gherkin to Code" pipeline. Standard Genetic Algorithms are too random for code. GGGP uses a grammar (your Gherkin + Primitives) to constrain the search space so 100% of generated agents are syntactically valid, even if they fail logic tests.
 * Search Term: "Grammar-Guided Genetic Programming for Program Synthesis."
2. Automated Genetic Improvement (GI)
 * Why: This is the software engineering application of evolutionary algorithms. It focuses on taking existing software (your primitives) and tuning it.
 * Search Term: "Genetic Improvement of Software using LLMs" (specifically look for "Gin" or "PyGGI" frameworks).
3. MAP-Elites with Novelty Search
 * Why: You mentioned "Quality Diversity." MAP-Elites is the algorithm that ensures you don't just find one good agent, but a grid of agents (e.g., "Fast but expensive" vs. "Slow but cheap"). This populates your HNSW with a diverse arsenal of solutions.
 * Search Term: "MAP-Elites for Quality Diversity in Neuroevolution."

Here is a compact, research-flavored one-pager for you.


---

1. What Hive Fleet Obsidian (HFO) Is

Hive Fleet Obsidian is your attempt to build a digital evolutionary apex swarm:

A many-agent system (LLMs + tools + other models) that:

Works from a single source of truth (MBSE / SysML-style “gene seed”).

Uses stigmergy (shared traces, sigils, pheromones) instead of a single central brain.

Runs as a durable workflow factory (Temporal-style body, LangGraph-style brain).


Goal: continuously search, assemble, and refine solutions across code, knowledge, and decisions with:

0 invention (only compose exemplars).

Strong hallucination control (truth gates, goldens, adversarial tests).

Anytime behavior (can stop at any point and still have a coherent “best known” answer).



Think of it as a software organism that lives on top of your infra (Chromebook + remote compute) and is always exploring better ways to solve your missions.


---

2. Who / What the Obsidian Spider Is

The Obsidian Spider is the planner / navigator persona for HFO:

It sits “above” individual agents and views the world as a high-dimensional state–action manifold:

Each state = “where you and the world are now.”

Each action = “what the swarm could do next.”


The spider:

Uses 8 OBSIDIAN pillars (roles/legs) as different “angles” on the same situation (observers, disruptors, navigators, etc.).

Treats the manifold as a fractal octree / SV-DAG:

Recursively splits possibilities into 8-ish “branches” at each level (powers of 8 to keep mental structure).

Stores exemplars (good solutions) in this tree instead of inventing from scratch.


Uses many-worlds traversal:

Not a single path, but swarm-orchestrated rollouts into alternative futures.

Keeps an archive of promising futures, not just one best guess.




You can think of the spider as a social-spider optimizer + MAP-Elites + many-worlds planner rolled into one narrative.


---

3. Traversal Method: How It Moves Through the Manifold

Core ideas:

1. State–action manifold = Indra’s net

Every node is a possible “world” (state) and edge is an action.

The swarm can step, branch, or abandon a path.



2. Fractal octree / SV-DAG structure

Use powers of 8 to recursively partition:

8 high-level futures → each splits into 8 sub-scenarios → etc.


SV-DAG angle: different paths can merge back onto the same sub-state (shared subroutines / designs).



3. Triangulation: Past, Present, Future

The spider never looks at a state in isolation:

Past: retrieves existing exemplars / cases / policies (CBR).

Present: current signals, telemetry, constraints.

Future: simulates short rollouts under different actions.


These three anchors define a triangle in the manifold that helps “lock in” a direction.



4. Swarm-orchestrated traversal (not 1 walker)

Multiple agents explore different branches in parallel:

Some replay or adapt past exemplars.

Some run short simulations.

Some try weird / novel branches.


They communicate via stigmergy:

Drop “pheromones” (scores, tags, traces) proportional to usefulness.

Evaporation / decay removes stale ideas.

High-pheromone paths attract more attention.




5. MAP-Elites archive, not single best path

Output is a quality–diversity archive:

Each cell = “niche” (e.g., fast but brittle, slow but robust, low compute, etc.).

Each cell stores one high-performing exemplar.


You use this archive as a probability distribution over futures:

Choose actions by sampling / weighting across niches, not just picking one “optimal” solution.

This gives you a probabilistic edge under uncertainty.




6. Apex assimilation (0 invention)

When the swarm finds a high-performer:

It assimilates that exemplar (code, pattern, SOP).

Attaches metadata: when to use it, limits, observed failure modes.

Adds it as a new point in the MAP-Elites archive + octree.


Over time you get a library of moves tailored to your missions.





---

4. Research Terms / Phrases for You to Search

Here is a condensed list of research-adjacent terms that map to your ideas:

1. Quality-Diversity (QD) and MAP-Elites

“MAP-Elites quality diversity algorithm”

“Illumination algorithms”

“Repertoire learning”



2. Many-worlds / counterfactual planning

“Counterfactual policy evaluation”

“Scenario tree / receding horizon control”

“Ensemble model predictive control”



3. State–action manifolds & high-dimensional search

“Policy manifold”

“State–action space exploration”

“Representation learning for control”



4. Social spider / swarm optimization

“Social Spider Optimization (SSO)”

“Ant colony optimization (ACO)”

“Bee colony optimization”

“Termite stigmergy construction models”

“Slime mold path optimization”



5. Stigmergy & blackboard systems

“Stigmergic coordination in multi-agent systems”

“Blackboard architecture AI”

“Pheromone-based task allocation”



6. Holonic and fractal structures

“Holonic multi-agent systems”

“Fractal organization theory”

“Hierarchical reinforcement learning (options, skills)”



7. Anytime / robust decision-making

“Anytime algorithms”

“Receding horizon control (MPC)”

“Risk-aware planning / CVaR in RL”



8. Byzantine / adversarial robustness (for your HFO tests)

“Byzantine-resilient multi-agent reinforcement learning”

“Adversarial training in multi-agent systems”




You can treat each bullet as a search seed and gradually build your own “literature web” that you plug back into HFO as exemplars.


---

If you want, next step I can:

Sketch how to turn this into a concrete planner design (modules, data structures, and loops).
---
Hive Fleet Obsidian: Architectural One-Pager
Date: December 1, 2025 | Time: 3:45 PM MST
Status: Validated | Core Concept: Antifragile Evolutionary Swarm
I. High-Level Concept: The Synthetic Organism
HFO is not an application; it is a digital organism designed for autonomous software evolution. It replaces the fragile "Agent -> LLM" loop with a rigorous Evolutionary Cycle protected by Byzantine Consensus.
 * The Brain (Stigmergy): A dual-memory system. Hot Reflexes (NATS) handle immediate threats via ephemeral "scent trails," while Cold Wisdom (LanceDB/Graph) stores proven strategies.
 * The Body (Hexagonal): 8 specialized "Obsidian Roles" (Sense, Act, Defend, etc.) strictly isolated by ports and adapters.
 * The Immune System (BFT): A 3f+1 consensus mechanism where agents must vote to execute high-risk actions. A designated Disruptor agent intentionally tries to subvert this vote to stress-test the swarm's resilience.
 * The Reproductive Cycle (Genesis): The system does not "learn" at runtime. It evolves overnight. A genetic algorithm breeds new agent behaviors (Gherkin feature files) from successful primitives, ensuring 0% hallucination in logic.
II. The "Phoenix" Data Protocol (CQRS)
To prevent "split-brain" syndrome across three databases, the system uses Command Query Responsibility Segregation (CQRS) with a "Crash-Only" philosophy.
 * Source of Truth: SQLite (Write-Ahead Log). All agent observations and actions are append-only events.
 * Projections (The "Views"):
   * LanceDB: Semantic Index (rebuilt from SQLite logs).
   * NetworkX: Knowledge Graph (rebuilt from SQLite logs).
 * The Phoenix Rule: If an agent suspects memory corruption or hallucination in the vector store, it burns the LanceDB index and regenerates it from the SQLite logs.
III. Critical Research Vectors
To converge the architecture, focus your deep dives here:
1. The Genesis Engine (Code Evolution)
 * Concept: Grammar-Guided Genetic Programming (GGGP).
 * Why: You aren't asking the LLM to write code; you are asking a genetic algorithm to arrange pre-written "Lego bricks" (primitives) into a valid Gherkin syntax.
 * Search Terms: "Grammar-Guided Genetic Programming for Program Synthesis," "Genetic Improvement of Software (GI)."
 * Tools: GeneticEngine (Python), PonyGE2, PyGGI.
2. The Immune System (Consensus)
 * Concept: Byzantine Fault Tolerance (BFT).
 * Why: With 8 agents, you can tolerate 2 traitors (3f+1). This allows you to run a "Red Team" agent in production that lies to the others.
 * Search Terms: "Practical Byzantine Fault Tolerance (PBFT) in Multi-Agent Systems," "Adversarial Consensus for AI Safety."
 * Tools: CometBFT (Go, but conceptual model applies), HoneyBadgerBFT.
3. The Memory (Stigmergy)
 * Concept: Virtual Stigmergy.
 * Why: Agents shouldn't talk to each other; they should modify the environment (Data).
 * Search Terms: "Stigmergic Coordination in Swarm Robotics," "Blackboard Architecture Patterns."
 * Tools: NATS JetStream (Key-Value Buckets with TTL), FastStream (Python wrapper).
IV. Recommended Tool Stack
| Component | Technology | Role |
|---|---|---|
| Gene Seed | Gherkin (Cucumber) | The "DNA" — strict, human-readable intent. |
| Reflexes | NATS JetStream | "Hot" memory. Ephemeral message bus with aggressive TTL. |
| Log (Truth) | SQLite | The immutable event stream. "What actually happened." |
| Wisdom | LanceDB | "Cold" memory. Vector search for "What did we do last time?" |
| Structure | NetworkX | Relationship mapping. "How is Task A linked to File B?" |
| Evolution | GeneticEngine | Python framework for evolving grammar-constrained code. |
Next Step
Would you like me to generate the "Consensus Protocol" Gherkin Feature File that defines exactly how the Navigator proposes a plan and the Disruptor tries to sabotage the vote?
