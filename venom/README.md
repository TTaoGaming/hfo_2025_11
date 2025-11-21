# 🧪 The Venom (Disruptor)

> **Role**: Disruptor / Red Team
> **JADC2 Mapping**: Red Team
> **Gherkin Source**: `brain/swarm_workflow.feature` (Step: Mutate/Test)

## 🧬 Biological Function
The **Venom** is the agent of **Stress** and **Evolution**. It runs tests, injects faults, and challenges the system to ensure it is robust. It is the "immune system trainer" that makes the Hive anti-fragile.

## 📂 Contents
*   **Smoke Tests**: Quick verification scripts (`smoke/`).
*   **Unit Tests**: Detailed code verification (`test_*.py`).
*   **Chaos Monkey**: Scripts that intentionally break things.

## 🤖 Agent Instructions
*   **Attack**: Try to break the system (in a controlled way).
*   **Verify**: Ensure fixes actually work.

## 🚀 How to Run Tests

The preferred method is using the **Genesis Protocol**:

```bash
# Run all smoke tests
python genesis.py --venom
```

Alternatively, run specific tests with `pytest`:

```bash
# Run infrastructure tests
pytest venom/test_infrastructure.py
```
