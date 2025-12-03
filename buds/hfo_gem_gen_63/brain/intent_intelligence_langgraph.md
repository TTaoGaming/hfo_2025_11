# Intent: Intelligence Upgrade (LangGraph + Prey 1181)

## Context
The current `ResearchWorkflow` is a linear "Sense -> Act" loop.
The User wants to upgrade this to a **LangGraph** architecture, specifically implementing the **Prey 1181 Heartbeat** (1 Perceive -> 1 React -> 8 Execute -> 1 Yield).

## Goal
Implement `buds/hfo_gem_gen_63/07_navigator_brain/intelligence.py` using LangGraph.
Integrate this into the Temporal Workflow.

## The Prey 1181 Pattern
1.  **Perceive (1)**: Gather context from Memory (Bridger) and Web (MCP).
2.  **React (1)**: Analyze the context and generate a plan (List of tasks).
3.  **Execute (8)**: Execute the tasks in parallel (or up to 8 concurrent threads).
4.  **Yield (1)**: Synthesize the results into a final answer/state.

## Architecture
*   **Temporal**: Orchestrates the reliable execution.
*   **LangGraph**: Manages the cognitive state and loops within the "Thinking" phase.
*   **Activity**: The entire LangGraph run is encapsulated in a Temporal Activity `run_cognitive_cycle` to ensure non-determinism (LLM calls) is isolated.

## Scenario: The Heartbeat
```gherkin
Feature: Prey 1181 Cognitive Cycle

  Scenario: Run a full heartbeat
    Given a user query "Analyze the market"
    When the "Perceive" node runs
      Then it should fetch data from Memory and Web
    When the "React" node runs
      Then it should produce a Plan with multiple steps
    When the "Execute" node runs
      Then it should run the steps (simulating 8 parallel agents)
    When the "Yield" node runs
      Then it should summarize the execution into a final report
```
