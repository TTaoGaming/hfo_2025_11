---
holon:
  id: hfo-refined-bd-temporal-langgraph-2025-11-30
  type: artifact
  source: brain-dump-google-keep-2025-11-30.md
  topic: temporal-langgraph-implementation
  timestamp: 2025-11-30
---

# 🧠 Refined Brain Dump: Temporal & LangGraph Implementation

> **Source**: Extracted from `brain-dump-google-keep-2025-11-30.md`
> **Context**: Technical implementation strategy for the "Brain & Body" architecture.

## 🏗️ Executive Summary: The "Brain & Body" Analogy

To manage the complexity of this stack, treat tools as **Black Boxes**:

1.  **The Brain (LangGraph)**
    *   **Role**: Decision Logic.
    *   **Function**: Holds conversation history, remembers research, decides loops.
    *   **Weakness**: Brittle. No "save game" for hardware crashes.

2.  **The Body (Temporal)**
    *   **Role**: Life Support & Durability.
    *   **Function**: Wraps the brain. Guarantees survival. Restores memory after crashes.
    *   **The Black Box**: If you wrap a function in Temporal, it *will* eventually complete.

## 🪆 Architectural Overview: The "Russian Doll" Pattern

Use the **"Activity-Agent Pattern"**:

1.  **Layer 1 (Outer Shell): Temporal Workflow**
    *   The "Manager".
    *   Sets timers, wakes up, calls Activities.

2.  **Layer 2 (The Task): Temporal Activity**
    *   Standard Python function.
    *   **Crucially**: Contains the LangGraph agent.

3.  **Layer 3 (Inner Core): LangGraph Agent**
    *   Runs *inside* the Activity.
    *   Takes input -> Scatter-Gather Reasoning -> Returns Result.

**Visual Flow**:
`Temporal (Manager) -> triggers -> Activity (Worker) -> spins up -> LangGraph (Brain) -> returns result -> Temporal saves result -> Sleep.`

## 🤖 Master Prompts (For AI Generation)

### Phase 1: The "Brain" (LangGraph)
> "I need you to build a LangGraph agent that acts as a 'Black Box' reasoning unit.
> The Spec:
>  * Input State: Create a Pydantic model called AgentState with fields: research_topic (str), gathered_facts (list), is_complete (bool).
>  * The Graph:
>    * Node A (Researcher): Uses [Search Tool] to find info. Updates gathered_facts.
>    * Node B (Critic): Checks if facts are sufficient. If yes, set is_complete=True.
>    * Edge: If is_complete is False, loop back to Node A. If True, go to End.
>  * The Interface: Wrap this entire graph in a single synchronous function called run_research_agent(topic: str) -> dict.
> Constraint: Do not use any external memory persistence (like Checkpointers) yet. This function must simply take an input string and return the final state dictionary."

### Phase 2: The "Body" (Temporal)
> "Now I need to make run_research_agent durable using Temporal.io.
> The Spec:
>  * The Activity: Create a Temporal Activity named ResearchActivity. Inside this activity, import and call the run_research_agent function we just built.
>    * Constraint: Set a StartToCloseTimeout of 10 minutes.
>  * The Workflow: Create a Temporal Workflow named ResearchOrchestrator.
>    * It should accept a list of topics.
>    * It should loop through the topics and call ResearchActivity for each one.
>    * It should return a final aggregated report.
>  * The Worker: Write a run_worker.py script that connects to the Temporal server and registers both the Workflow and the Activity.
> Goal: I should be able to kill the run_worker.py script in the middle of a research task, restart it, and have it resume exactly where it left off."

## 🔍 The "Black Box" Cheat Sheet

| Component | File to Check | What to look for (The Interface) |
| :--- | :--- | :--- |
| **LangGraph** | `state.py` | Does `AgentState` have the fields you care about (facts, summary)? |
| **LangGraph** | `graph.py` | Look for `workflow.add_conditional_edges`. Is there a loop? |
| **Temporal** | `activities.py` | Look for `@activity.defn`. Does it simply call the LangGraph agent? |
| **Temporal** | `worker.py` | Does it register both the Workflow and the Activity? |
