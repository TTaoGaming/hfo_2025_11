# 💓 Obsidian Heart: The Atomic Heartbeat Protocol

> **Status**: Design (Gen 55)
> **Context**: Chromebook Plus (8GB RAM) Optimization
> **Goal**: A steady, rhythmic, variable heartbeat powered by a **Single Atomic Agent (1-1-1-1)** running 24/7.

## 1. The Diagnosis: Architectural Violation

You are correct. The system is crashing because the AI implementation drifted from the **Fractal Holarchy** architecture.

*   **The Intent**:
    *   **Level 0 (Atomic)**: `1-1-1-1` = **1 Agent**, 1 Loop, 1 Thread. This is the "Heart". It should never crash.
    *   **Level 1 (Squad)**: `8-8-8-8` = **8 Agents**. This is the "Muscle". It requires heavy resources.
*   **The Reality (Ad Hoc)**:
    *   The file `cleanroom_prey_1111.py` (which should be Atomic) was "hacked" to launch **8 concurrent agents**.
    *   This created a "Thundering Herd" of 8 infinite loops on your 8GB RAM machine.
    *   **Result**: OOM (Out of Memory) and System Freeze.

## 2. The Solution: Restore the Holarchy

We must strictly separate the **Heart (1)** from the **Swarm (8)**.

### 2.1. The Atomic Heart (`body/hands/atomic_heart.py`)
*   **Concurrency**: **1** (Strictly Single Threaded).
*   **Role**: The "Always On" background process.
*   **Model**: `gemma3:270m` (Lightweight).
*   **Loop**:
    1.  **Perceive**: Check System Health (RAM), Check NATS for Signals.
    2.  **React**: Decide if a "Swarm" is needed.
    3.  **Execute**: Perform *light* maintenance or *spawn* a task.
    4.  **Yield**: Emit a Heartbeat Signal (`hfo.heartbeat`).
*   **Frequency**: Variable (Variable Heart Rate).
    *   *Resting*: Every 60s.
    *   *Active*: Every 10s.

### 2.2. The Fractal Squad (`body/hands/fractal_squad.py`)
*   **Concurrency**: **Up to 8** (Dynamic).
*   **Role**: The "Heavy Lifter". Only runs when summoned by the Heart.
*   **Gating**:
    *   The Heart *only* summons the Squad if RAM > 4GB.
    *   If RAM is low, the Heart does the work itself (slowly) or queues it.

## 3. The "Rhythmic Beating" Architecture

We will implement a **Systolic/Diastolic** rhythm.

| Phase | Component | Action | Resource Usage |
| :--- | :--- | :--- | :--- |
| **Diastole** (Rest) | **Atomic Heart** | Wakes up, checks NATS, checks RAM. | ~300MB (Model) + ~50MB (Python) |
| **Systole** (Beat) | **Atomic Heart** | Runs 1 Inference Cycle (PREY). | ~500MB (Peak) |
| **Pulse** (Signal) | **NATS** | Publishes `hfo.heartbeat`. | Negligible |
| **Surge** (Optional) | **Fractal Squad** | *Only if summoned*: Spawns 4-8 agents. | ~2GB - 4GB |

## 4. What is Possible on Chromebook Plus?

With `gemma3:270m` (~300MB VRAM) and 8GB System RAM:

*   **1 Agent (Atomic)**: **100% Safe**. Can run 24/7. Will consume <1GB total.
*   **4 Agents (Half Squad)**: **Safe**. Will consume ~2-3GB. Good for "Burst" work.
*   **8 Agents (Full Squad)**: **Risky**. 8 concurrent Python interpreters + Ollama overhead + VS Code + OS will push memory to >90%, causing swap thrashing and freezes.

## 5. The Plan (Design Only)

1.  **Purge the Ad Hoc**: Delete the "8-agent loop" from `cleanroom_prey_1111.py`.
2.  **Consecrate the Atom**: Rewrite `cleanroom_prey_1111.py` to be strictly **Single Agent**.
3.  **Create the Squad**: Create a new `cleanroom_prey_8888.py` for the multi-agent logic, but *gated* by the Heart.
4.  **Connect the Nerves**: Ensure the Heartbeat writes to NATS, so you can see the "Pulse" in your dashboard without crashing the machine.

## 6. The Blast Shield (Safe Testing)

To verify "what is possible" without crashing the host, we use a **Docker Blast Shield**.

*   **Tool**: `sandbox/crash_test/run_safe.sh`
*   **Mechanism**: Runs the swarm in a container with **Hard Limits** (2GB RAM, 2 CPUs).
*   **Outcome**: If the swarm exceeds limits, the *container* dies. The Chromebook remains stable.
*   **Usage**: `bash sandbox/crash_test/run_safe.sh`

This restores the **Fractal Holarchy**. The Heart (1) beats forever. The Hands (8) only work when the Heart is strong.
