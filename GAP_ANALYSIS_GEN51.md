---
# ==================================================================
# 🤖 THE HEXAGON (System Generated)
# ==================================================================
hexagon:
  ontos:
    id: d1e2fa22-33e8-43e7-86b7-b2b1128caf9e
    type: md
    owner: Swarmlord
  chronos:
    status: active
    urgency: 0.5
    decay: 0.5
    created: '2025-11-23T10:20:43.116674+00:00'
  topos:
    address: GAP_ANALYSIS_GEN51.md
    links: []
  telos:
    viral_factor: 0.0
    meme: GAP_ANALYSIS_GEN51.md
---

# 🦅 Hive Fleet Obsidian: Generation 51 Gap Analysis
> **Date**: November 22, 2025
> **Status**: CRITICAL REGRESSION
> **Focus**: Infrastructure, Stability, and Observability

## 🚨 Executive Summary
We are currently in a state of **Regression**. While the "MOBS" (AGENTS.md) indicates that Stigmergy and Swarm logic were verified in Gen 50, the transition to Gen 51 has introduced configuration drift and instability.

**Key Finding**: The "Hybrid Stability Protocol" (Docker Infra + Host Agents) is fragile due to port mapping inconsistencies (4222 vs 4225) and lack of robust service discovery.

---

## 📉 The Gap: Intent vs. Reality

| Feature | Intent (Brain) | Reality (Body) | Status |
| :--- | :--- | :--- | :--- |
| **Stigmergy** | Agents communicate via NATS JetStream on port `4225`. | Agents are defaulting to `4222` and crashing. | 🔴 **BROKEN** |
| **Execution** | Asynchronous, non-blocking background swarms. | Terminal freezes; `nohup` is a fragile workaround. | 🟡 **FRAGILE** |
| **Observability** | "Watch" step provides real-time metrics & dashboards. | We are `tail -f`ing a log file. | 🟠 **PRIMITIVE** |
| **Configuration** | Single Source of Truth (SSOT) via `.env` & `yaml`. | Hardcoded defaults in Python files are overriding config. | 🔴 **DRIFT** |
| **Resilience** | Durable execution via Temporal. | Script crashes on first network error. | 🔴 **MISSING** |

---

## 🔍 Root Cause Analysis (The "Why")

### 1. Configuration Drift (The Port 4222/4225 Schism)
*   **Docker**: Maps NATS to `4225` (Host) -> `4222` (Container).
*   **Code**: Multiple files (`research_swarm.py`, `prey_agent.py`, `stigmergy.py`) had hardcoded defaults of `4222`.
*   **Fix Attempted**: We patched the defaults to `4225`, but the runtime is still picking up `4222` in some paths, likely due to `CONFIG` loading precedence or `load_dotenv` issues in the `nohup` context.

### 2. The "Script" Trap
*   We are running `research_swarm.py` as a standalone script.
*   **Consequence**: It has no supervisor. If it crashes (e.g., NATS unavailable), it dies.
*   **Solution**: We need the **Temporal Workflow** (`body/temporal/swarm_workflow.py`) to manage the lifecycle and retries.

### 3. Blind Observability
*   We are flying blind. We rely on `print` statements and log files.
*   **Need**: A simple "Mission Control" dashboard (even a static HTML file that polls an endpoint) or integration with LangSmith for real-time tracing.

---

## 🛠️ Remediation Plan (The "How")

### Phase 1: Stabilize (Immediate)
1.  **Enforce Config**: Remove ALL default values from Python code. Force failure if `NATS_URL` is missing.
2.  **Verify Env**: Ensure `nohup` inherits the correct environment variables.
3.  **Retry Logic**: Add `tenacity` retry decorators to NATS connection logic.

### Phase 2: Orchestrate (Next Session)
1.  **Temporal Integration**: Wrap `research_swarm.py` in a Temporal Activity.
2.  **Dockerize Agents**: Move the agents into a Docker container that shares the network with NATS (eliminating the port mapping confusion).

### Phase 3: Observe
1.  **Stigmergy Dashboard**: Create a simple TUI or Web UI that subscribes to `swarm.>` subjects and displays status.

---

## 📋 Action Items for User
1.  **Stop** trying to run the swarm blindly.
2.  **Review** this Gap Analysis.
3.  **Authorize** the "Stabilize" phase: Refactor code to strictly use `os.getenv` without hardcoded fallbacks, ensuring we fail fast if config is wrong.
