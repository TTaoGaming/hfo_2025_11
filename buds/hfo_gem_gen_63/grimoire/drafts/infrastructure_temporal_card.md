---
card:
  id: 30b36407-3c84-41d7-9bc9-aa55ea247db4
  source: infrastructure_temporal.md
  type: Tool
---

# 🃏 ⏳ Temporal Orchestration Backbone

> **Intuition**: Temporal.io transmutes fragile, probabilistic LangGraph swarms into immortal, deterministic execution engines, conquering chaos through durable retries and stateful resurrection.

## 📜 The Incantation (Intent)
```gherkin
Feature: Durable Orchestration of Long-Running Swarm Missions

  Scenario: Execute Research Swarm with Failure Recovery
    Given a Temporal workflow is triggered with mission parameters
    And a worker is listening on "research-swarm-queue"
    When the workflow schedules the "run_research_swarm_activity"
    And the activity invokes LangGraph swarm via NATS JetStream
    And an exception occurs during LLM invocation or network blip
    Then Temporal retries the activity up to 3 times with backoff
    And the workflow timeouts after 5 minutes if hung
    And the final result is returned to the client asynchronously
```

## 🧪 The Catalyst (Code)
```python
# The Essence: Wrapper Workflow for Swarm Missions
import temporalio.workflow
from temporalio import activity, workflow
from temporalio.client import Client
from config import Config  # SSOT Config

@workflow.defn(name="swarm_workflow")
class SwarmWorkflow:
    @workflow.run
    async def run(self, mission_params: dict) -> dict:
        # Durable wrapper around LangGraph swarm
        result = await workflow.execute_activity(
            "run_research_swarm_activity",
            mission_params,
            start_to_close_timeout=temporalio.duration.Duration.from_minutes(5),
            retry_policy=workflow.ActivityRetryPolicy(
                initial_interval=temporalio.duration.Duration.from_seconds(10),
                maximum_attempts=3,
            ),
        )
        return result

# Activity: Idempotent Swarm Execution
@activity.defn
async def run_research_swarm_activity(mission_params: dict) -> dict:
    # Connect to NATS, invoke LangGraph, handle async LLM
    # (Idempotent: safe retry via checkpoints)
    from nats.aio.client import Client as NATS
    nats = NATS()
    await nats.connect()
    # ... Initialize & run LangGraph swarm ...
    return swarm_result
```

## ⚔️ Synergies
*   **LangGraph**: Wraps probabilistic swarm cycles (Perceive-React-Execute) in deterministic activities with heartbeats.
*   **NATS JetStream**: Provides durable messaging backbone for activity execution, retried on failure.
*   **Config SSOT**: Pulls `TEMPORAL_ADDRESS` for seamless worker/client connectivity.
*   **Hive Fleet Obsidian**: Powers long-running "missions" (hours/days) across workers, clients, and LLMs.
*   **Workers/Queues**: Scalable compute via `research-swarm-queue` for high-throughput, replaceable stages.