---
card:
  id: hydra-protocol
  source: infrastructure_hydra.md
  type: Tool
---

# 🃏 🐍 Hydra Protocol

> **Intuition**: Like the mythical Hydra, this protocol grows stronger from failure by isolating tasks in Ray Actors that auto-regenerate under SwarmController supervision, embodying true antifragility in distributed swarms.

## 📜 The Incantation (Intent)
```gherkin
Feature: Hydra Protocol for Antifragile Task Execution

  Scenario: Supervise and regenerate failed worker actors
    Given a SwarmController monitoring a Ray Cluster
    And a Worker actor spawned with a PREY Loop task
    When the Worker actor crashes during execution
    Then the SwarmController detects the failure
    And respawns a new Worker actor with the same task
    And stores the result in the Ray Object Store via zero-copy reference
```

## 🧪 The Catalyst (Code)
```python
# The Essence
import ray
import time

ray.init()

@ray.remote
class HydraWorker:
    def execute_prey_loop(self, task):
        # Simulate PREY Loop (Process, Reflect, Evolve, Yield)
        time.sleep(1)  # Simulate work
        if task == "fail":  # Simulate failure
            raise RuntimeError("Worker crash!")
        return f"Result: {task}"

class SwarmController:
    def __init__(self):
        self.worker_refs = []

    def spawn_and_supervise(self, task, max_retries=3):
        for attempt in range(max_retries):
            try:
                worker = HydraWorker.remote()
                self.worker_refs.append(worker)
                future = worker.execute_prey_loop.remote(task)
                result_ref = ray.get(future, timeout=5)
                return ray.get(result_ref)  # Zero-copy shared memory
            except Exception:
                ray.kill(worker)  # Kill failed actor
                print(f"Regenerating worker (attempt {attempt + 1})")
        raise RuntimeError("Max retries exceeded")
```

## ⚔️ Synergies
*   **SwarmController**: Central orchestrator that spawns and monitors all Hydra Workers.
*   **PREY Loop**: Core logic executed within each isolated Worker actor for agentic behavior.
*   **Ray Object Store (Plasma)**: Enables zero-copy state sharing across distributed actors.
*   **Antifragile Strategy**: Higher-level philosophy; Hydra provides the executable "muscle" for no-single-point-of-failure execution.
*   **Ray Dashboard**: Integrates for real-time metrics and health monitoring of the supervision tree.