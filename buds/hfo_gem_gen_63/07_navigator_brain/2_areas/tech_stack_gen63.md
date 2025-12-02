---
holon:
  id: hfo-tech-stack-gen63
  type: architecture
  status: active
  generation: 63
  author: Swarmlord
  theme: The Hydra Platform (Consolidated)
---

# 🛠️ HFO Gen 63: The Hydra Platform

> **Goal**: A consolidated, minimal, high-performance stack.

## 1. The Core (The Hydra Head)
*   **Language**: Python 3.10+
*   **Configuration**: `pydantic-settings` (Strict Environment Management).
*   **Logging**: `structlog` (JSON logs for observability).

## 2. The Brain (Intelligence)
*   **Provider**: **OpenRouter** (Unified API for GPT-4, Claude 3, Llama 3).
*   **Agent Framework**: **OpenAI Swarm** (Lightweight, stateless agent orchestration) + **LangGraph** (Stateful flows where needed).
*   **Structured Output**: **Instructor** (Pydantic-based LLM responses).

## 3. The Nervous System (Communication)
*   **Event Bus**: **NATS JetStream** (The spinal cord).
    *   Subject: `hfo.gen63.>`
*   **RPC**: NATS Request-Reply (Low latency internal comms).

## 4. The Memory (Storage)
*   **Vector Store**: **LanceDB** (Embedded, fast, disk-based).
*   **Relational**: **SQLite3** (Local, simple, ACID).
*   **Graph**: **NetworkX** (In-memory graph for immediate reasoning) -> **Neo4j** (Optional, if scale needed).

## 5. The Muscle (Execution)
*   **Orchestration**: **Temporal** (Durable workflows, retries, sagas).
*   **Compute**: **Ray** (Parallel execution of heavy tasks).

## 6. The Tools (Effectors)
*   **Web Search**: DuckDuckGo / Google Custom Search.
*   **File System**: Local FS (Sandboxed).
*   **Code Execution**: E2B (Sandboxed Python) or Local Docker.

## 7. The Consolidation Plan
1.  **Migrate** useful logic from `buds/hfo_gem_gen_61`.
2.  **Refactor** into `buds/hfo_gem_gen_63/src`.
3.  **Verify** with `pytest`.
